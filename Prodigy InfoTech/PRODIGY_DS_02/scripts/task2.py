import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/train.csv")

# -----------------------------
# Data Cleaning
# -----------------------------
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df.drop("Cabin", axis=1, inplace=True)

# -----------------------------
# EDA Visualizations
# -----------------------------

# Survival Count
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Count")
plt.savefig("../outputs/survival.png")
plt.clf()

# Survival by Gender
df.groupby("Sex")["Survived"].mean().plot(kind="bar")
plt.title("Survival Rate by Gender")
plt.savefig("../outputs/gender.png")
plt.clf()

# Survival by Class
df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.title("Survival Rate by Class")
plt.savefig("../outputs/class.png")
plt.clf()

# Age Distribution
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.savefig("../outputs/age.png")
plt.clf()

# Fare Distribution
plt.hist(df["Fare"], bins=20)
plt.title("Fare Distribution")
plt.savefig("../outputs/fare.png")
plt.clf()

print("Task 02 completed successfully!")s