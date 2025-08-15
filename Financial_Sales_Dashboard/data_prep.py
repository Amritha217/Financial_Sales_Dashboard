import pandas as pd

# Load raw data
df = pd.read_csv("raw_data/Financials.csv")

# Clean nulls
df = df.dropna(subset=["Sales", "Profit", "Units Sold"])


df.rename(columns={"COGS": "Cost_of_Goods_Sold"}, inplace=True)

# Create calculated column
df["Profit_Margin"] = df["Profit"] / df["Sales"]

# Export cleaned data
df.to_csv("processed_data/Financials_cleaned.csv", index=False)

print("Data prep complete! Processed CSV is ready for Power BI.")
