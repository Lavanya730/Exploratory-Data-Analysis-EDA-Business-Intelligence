import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("Sales_Dataset.csv")

# Remove extra spaces if any
df.columns = df.columns.str.strip()

# Convert date
df["Order_Date"] = pd.to_datetime(df["Order_Date"], format="%d-%m-%Y")

# Create Month column
df["Month"] = df["Order_Date"].dt.month

# -----------------------------
# Basic KPIs
# -----------------------------
print("Total Revenue:", df["Revenue"].sum())
print("Total Orders:", df["Order_ID"].nunique())
print("Total Customers:", df["Customer_ID"].nunique())

# -----------------------------
# 1️⃣ Monthly Revenue Trend
# -----------------------------
monthly_sales = df.groupby("Month")["Revenue"].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# -----------------------------
# 2️⃣ Top 5 Products
# -----------------------------
top_products = df.groupby("Product_Name")["Revenue"].sum().sort_values(ascending=False).head(5)

plt.figure()
top_products.plot(kind="bar")
plt.title("Top 5 Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# 3️⃣ Region-wise Revenue
# -----------------------------
region_sales = df.groupby("Region")["Revenue"].sum()

plt.figure()
region_sales.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()

# -----------------------------
# 4️⃣ Payment Method Distribution
# -----------------------------
payment_sales = df.groupby("Payment_Method")["Revenue"].sum()

plt.figure()
payment_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Payment Method Revenue Share")
plt.ylabel("")
plt.show()