# ===============================
# CRIME DATA ANALYSIS PROJECT
# ===============================

# ===============================
# 1. IMPORT LIBRARIES
# ===============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


# ===============================
# 2. LOAD DATASET
# ===============================
# Make sure your dataset is inside /data folder
file_path = "data/crime_dataset.xlsx"

df = pd.read_excel(r"C:\Users\vaibh\OneDrive\Desktop\numpy project\crime dataset.xlsx")

print("First 5 rows:\n")
print(df.head())

print("\nDataset Info:\n")
print(df.info())


# ===============================
# 3. DATA CLEANING
# ===============================
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

print("\nCleaned Data Shape:", df.shape)


# ===============================
# 4. FEATURE ENGINEERING
# ===============================
# Create Status Column (Solved / Unsolved)
df['Status'] = df['Arrests'].apply(lambda x: 'Solved' if x > 0 else 'Unsolved')


# ===============================
# 5. EXPLORATORY DATA ANALYSIS
# ===============================

# ---------- 5.1 Most Frequent Crime Type ----------
crime_type = df.groupby('Crime_Type')['Cases'].sum().sort_values(ascending=False)

plt.figure()
crime_type.plot(kind='bar')
plt.title("Top Crime Types")
plt.xlabel("Crime Type")
plt.ylabel("Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ---------- 5.2 Crime by State ----------
state = df.groupby('State')['Cases'].sum().sort_values(ascending=False)

plt.figure()
state.plot(kind='bar')
plt.title("Crime by State")
plt.xlabel("State")
plt.ylabel("Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ---------- 5.3 Crime Trend Over Years ----------
yearly = df.groupby('Year')['Cases'].sum()

plt.figure()
yearly.plot(marker='o')
plt.title("Crime Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Cases")
plt.grid(True)
plt.tight_layout()
plt.show()


# ---------- 5.4 Gender-wise Crime ----------
gender = df.groupby('Victim_Gender')['Cases'].sum()

plt.figure()
gender.plot(kind='pie', autopct='%1.1f%%')
plt.title("Crime by Gender")
plt.ylabel("")
plt.tight_layout()
plt.show()


# ---------- 5.5 Solved vs Unsolved ----------
status = df.groupby('Status')['Cases'].sum()

plt.figure()
status.plot(kind='pie', autopct='%1.1f%%')
plt.title("Solved vs Unsolved Cases")
plt.ylabel("")
plt.tight_layout()
plt.show()


# ===============================
# 6. ADVANCED ANALYSIS
# ===============================

# ---------- 6.1 Correlation Heatmap ----------
corr = df.corr(numeric_only=True)

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


# ---------- 6.2 Outlier Detection ----------
plt.figure()
sns.boxplot(x=df['Cases'])
plt.title("Outlier Detection (Cases)")
plt.tight_layout()
plt.show()


# ===============================
# 7. SAVE RESULTS (OPTIONAL)
# ===============================

# Save grouped data
crime_type.to_csv("outputs/crime_type.csv")
state.to_csv("outputs/state_crime.csv")
yearly.to_csv("outputs/yearly_trend.csv")


# ===============================
# 8. DONE
# ===============================
print("\nAnalysis Completed Successfully ✅")