# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Loading and Inspection
# Load the CSV file into a pandas DataFrame
df = pd.read_csv("retail_data.csv")

print("--- Initial Data Inspection ---")
print(df.head())
print("\n")

# 2. Data Cleaning and Transformation
# Convert 'Date' column to datetime objects
df["Date"] = pd.to_datetime(df["Date"])

# Create a new column for 'Month'
df["Month"] = df["Date"].dt.to_period("M")

# 3. Exploratory Data Analysis (EDA)
print("--- Sales Metrics ---")
total_sales = df["Total_Sales"].sum()
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Average Transaction Value: ${df['Total_Sales'].mean():,.2f}")
print("\n")

# Top Product Categories by Sales
category_sales = (
    df.groupby("Product_Category")["Total_Sales"].sum().sort_values(ascending=False)
)
print("--- Sales by Product Category ---")
print(category_sales)
print("\n")

# Sales Trend over Time (Monthly)
monthly_sales = df.groupby("Month")["Total_Sales"].sum()
print("--- Monthly Sales Trend ---")
print(monthly_sales)
print("\n")

# 4. Visualization (Requires Matplotlib/Seaborn to display in a notebook environment)
# Sales by Product Category Bar Chart
plt.figure(figsize=(10, 6))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title("Total Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales ($)")
plt.show()


# Sales by Region Pie Chart
region_sales = df.groupby("Region")["Total_Sales"].sum()
plt.figure(figsize=(8, 8))
plt.pie(
    region_sales,
    labels=region_sales.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=sns.color_palette("pastel"),
)
plt.title("Sales Distribution by Region")
plt.show()
