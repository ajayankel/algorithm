import pandas as pd

def load_products(filepath):
    return pd.read_csv(filepath)

def recommend_products(df, product_name, n=3):
    product = df[df['name'].str.lower() == product_name.lower()]
    if product.empty:
        print(f"Product '{product_name}' not found.")
        return pd.DataFrame()
    
    category = product.iloc[0]['category']
    recommendations = df[(df['category'] == category) & (df['name'].str.lower() != product_name.lower())]
    
    if len(recommendations) > n:
        recommendations = recommendations.sample(n)
    
    return recommendations

if __name__ == "__main__":
    df = load_products("data/products.csv")
    product_to_search = "Red Shoes"
    recs = recommend_products(df, product_to_search)
    print(f"Recommendations based on category for '{product_to_search}':")
    print(recs)
