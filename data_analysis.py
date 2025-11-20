import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load the CSV file
# -------------------------------
df = pd.read_csv("sales.csv")

print("\n--- FIRST 5 ROWS ---")
print(df.head())

# -------------------------------
# 2. Create a Total column
# -------------------------------
df["Total"] = df["Quantity"] * df["Price"]

print("\n--- DATA WITH TOTAL COLUMN ---")
print(df.head())

# -------------------------------
# 3. Basic total sales
# -------------------------------
total_sales = df["Total"].sum()
print("\nTotal Sales Amount:", total_sales)

# -------------------------------
# 4. Sales by Category
# -------------------------------
category_sales = df.groupby("Category")["Total"].sum()
print("\n--- SALES BY CATEGORY ---")
print(category_sales)

# -------------------------------
# 5. Sales by Product
# -------------------------------
product_sales = df.groupby("Product")["Total"].sum().sort_values(ascending=False)
print("\n--- SALES BY PRODUCT ---")
print(product_sales)

# -------------------------------
# 6. Monthly Sales Trend
# -------------------------------
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Total"].sum()
print("\n--- MONTHLY SALES ---")
print(monthly_sales)

# -------------------------------
# 7. Charts
# -------------------------------

# Chart 1: Category Sales
plt.figure(figsize=(8,5))
category_sales.plot(kind="bar", title="Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Chart 2: Monthly Sales Trend
plt.figure(figsize=(8,5))
monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
# Chart 3: Category Sales Pie Chart
plt.figure(figsize=(7,7))
plt.pie(category_sales, labels=category_sales.index, autopct="%1.1f%%", startangle=140)
plt.title("Category Sales Distribution")
plt.tight_layout()
plt.show()
