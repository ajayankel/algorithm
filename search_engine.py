import pandas as pd

def load_products(file_path):
    return pd.read_csv(file_path)

def search_products(query, df):
    query = query.lower()
    return df[df['name'].str.lower().str.contains(query)]

if __name__ == "__main__":
    df = load_products("data/products.csv")
    result = search_products("shoes", df)
    print("Search Results for 'shoes':")
    print(result)
