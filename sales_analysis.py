import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Initial Data:")
print(df)

print("\nShape of data:", df.shape)
print("\nColumn Info:")
print(df.info())

df['Quantity'] = df['Quantity'].fillna(0)

df['Total_Sales'] = df['Total_Sales'].fillna(df['Quantity'] * df['Price'])

# Remove duplicates if any
df = df.drop_duplicates()

print("\nCleaned Data:")
print(df)

total_revenue = df['Total_Sales'].sum()

best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()

average_sale = df['Total_Sales'].mean()

print("\n--- Sales Metrics ---")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best Selling Product: {best_product}")
print(f"Average Order Value: ₹{average_sale:,.2f}")

summary = pd.DataFrame({
    "Metric": ["Total Revenue", "Best Selling Product", "Average Order Value"],
    "Value": [total_revenue, best_product, average_sale]
})

summary.to_csv("summary.csv", index=False)

print("\nReport generated successfully!")
