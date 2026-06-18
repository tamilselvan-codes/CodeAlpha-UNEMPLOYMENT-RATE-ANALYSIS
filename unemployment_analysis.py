import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"D:\Unemployment Rate Analysis\Unemployment in India.csv")

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Print column names
print("Columns in dataset:")
print(df.columns)

# Find date column automatically
date_col = None

for col in df.columns:
    if "date" in col.lower():
        date_col = col
        break

if date_col is None:
    print("\nNo Date column found.")
    print("Please check the column names printed above.")
    exit()

# Convert date column
df[date_col] = pd.to_datetime(df[date_col])

# Extract year and month
df["Year"] = df[date_col].dt.year
df["Month"] = df[date_col].dt.month

# Find unemployment rate column automatically
rate_col = None

for col in df.columns:
    if "unemployment rate" in col.lower():
        rate_col = col
        break

if rate_col is None:
    print("\nNo unemployment rate column found.")
    print("Columns available:")
    print(df.columns)
    exit()

# Show first rows
print("\nFirst 5 rows:")
print(df.head())

# Statistics
print("\nSummary:")
print(df[rate_col].describe())

# Yearly average unemployment rate
yearly_rate = df.groupby("Year")[rate_col].mean()

# Plot yearly trend
plt.figure(figsize=(10,6))
plt.plot(yearly_rate.index, yearly_rate.values, marker='o')
plt.title("Average Unemployment Rate by Year")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.show()

# Monthly trend
monthly_rate = df.groupby("Month")[rate_col].mean()

plt.figure(figsize=(10,6))
plt.plot(monthly_rate.index, monthly_rate.values, marker='o')
plt.title("Monthly Unemployment Trend")
plt.xlabel("Month")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.show()

# COVID impact analysis
df["Period"] = df["Year"].apply(
    lambda x: "Before COVID" if x < 2020 else "During COVID"
)

plt.figure(figsize=(8,6))
sns.boxplot(
    x="Period",
    y=rate_col,
    data=df
)

plt.title("Impact of COVID-19 on Unemployment")
plt.show()

print("\nAnalysis Completed Successfully.")
df['Month'] = df['Date'].dt.month

monthly_rate = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(10,5))
monthly_rate.plot(marker='o')
plt.title('Monthly Unemployment Trend')
plt.xlabel('Month')
plt.ylabel('Rate (%)')
plt.show()
df['Period'] = df['Year'].apply(
    lambda x: 'Before COVID' if x < 2020 else 'During COVID'
)

sns.boxplot(
    x='Period',
    y='Estimated Unemployment Rate (%)',
    data=df
)

plt.title('COVID-19 Impact on Unemployment')
plt.show()