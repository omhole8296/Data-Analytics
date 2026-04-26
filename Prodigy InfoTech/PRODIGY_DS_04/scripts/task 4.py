import pandas as pd
import matplotlib.pyplot as plt
import os

# Create outputs folder
os.makedirs("../outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("../data/twitter_training.csv")

# -----------------------------
# Data Cleaning
# -----------------------------
df.dropna(inplace=True)
df["Tweet"] = df["Tweet"].astype(str)

# -----------------------------
# Overall Sentiment Distribution
# -----------------------------
df["Sentiment"].value_counts().plot(kind="bar")
plt.title("Overall Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.savefig("../outputs/sentiment.png")
plt.clf()

# -----------------------------
# Top 10 Topics
# -----------------------------
df["Topic"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Topics")
plt.xlabel("Topic")
plt.ylabel("Mentions")
plt.xticks(rotation=45)
plt.savefig("../outputs/topics.png")
plt.clf()

# -----------------------------
# Sentiment by Topic
# -----------------------------
pd.crosstab(df["Topic"], df["Sentiment"]).head(10).plot(
    kind="bar",
    figsize=(12,6)
)

plt.title("Sentiment by Topic")
plt.xlabel("Topic")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig("../outputs/topic_sentiment.png")
plt.clf()

# -----------------------------
# Tweet Length Distribution
# -----------------------------
df["Tweet_Length"] = df["Tweet"].apply(len)

plt.hist(df["Tweet_Length"], bins=30)
plt.title("Tweet Length Distribution")
plt.xlabel("Characters")
plt.ylabel("Count")
plt.savefig("../outputs/tweet_length.png")
plt.clf()

print("Task 04 completed successfully!")