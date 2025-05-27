from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

def load_products():
    return pd.read_csv("data/products.csv")

def recommend_products(df, product_name, n=3):
    product = df[df['name'].str.lower() == product_name.lower()]
    if product.empty:
        return None
    category = product.iloc[0]['category']
    recommendations = df[(df['category'] == category) & (df['name'].str.lower() != product_name.lower())]
    if len(recommendations) > n:
        recommendations = recommendations.sample(n)
    return recommendations

@app.route("/", methods=["GET", "POST"])
def home():
    df = load_products()
    recommendations = None
    error = None
    product_name = ""
    if request.method == "POST":
        product_name = request.form.get("product_name")
        recs = recommend_products(df, product_name)
        if recs is None:
            error = f"Product '{product_name}' not found."
        else:
            recommendations = recs.to_dict(orient="records")
    return render_template("index.html", recommendations=recommendations, error=error, product_name=product_name)

if __name__ == "__main__":
    app.run(debug=True)
