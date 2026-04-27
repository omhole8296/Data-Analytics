import pandas as pd
import matplotlib.pyplot as plt
import os

# Create outputs folder
os.makedirs("../outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("../data/US_Accidents_sample.csv")

# -----------------------------
# Select columns
# -----------------------------
df = df[
    [
        "Severity",
        "Start_Time",
        "Weather_Condition",
        "State",
        "Start_Lat",
        "Start_Lng",
        "Sunrise_Sunset",
    ]
]

# -----------------------------
# Data Cleaning
# -----------------------------
df.dropna(inplace=True)

# Convert time
df["Start_Time"] = pd.to_datetime(df["Start_Time"])
df["Hour"] = df["Start_Time"].dt.hour

# -----------------------------
# Accidents by Hour
# -----------------------------
df["Hour"].value_counts().sort_index().plot(
    kind="bar", figsize=(10, 5)
)
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.savefig("../outputs/hourly_accidents.png")
plt.clf()

# -----------------------------
# Weather Conditions
# -----------------------------
df["Weather_Condition"].value_counts().head(10).plot(
    kind="bar", figsize=(10, 5)
)
plt.title("Top Weather Conditions During Accidents")
plt.xlabel("Weather")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../outputs/weather_conditions.png")
plt.clf()

# -----------------------------
# Severity Distribution
# -----------------------------
df["Severity"].value_counts().sort_index().plot(kind="bar")
plt.title("Accident Severity Distribution")
plt.xlabel("Severity")
plt.ylabel("Count")
plt.savefig("../outputs/severity.png")
plt.clf()

# -----------------------------
# Top States
# -----------------------------
df["State"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 States with Most Accidents")
plt.xlabel("State")
plt.ylabel("Count")
plt.savefig("../outputs/top_states.png")
plt.clf()

# -----------------------------
# Day vs Night
# -----------------------------
df["Sunrise_Sunset"].value_counts().plot(kind="bar")
plt.title("Day vs Night Accidents")
plt.xlabel("Time")
plt.ylabel("Count")
plt.savefig("../outputs/day_night.png")
plt.clf()

# -----------------------------
# Hotspots
# -----------------------------
plt.figure(figsize=(10, 6))
plt.scatter(
    df["Start_Lng"],
    df["Start_Lat"],
    s=1,
    alpha=0.3
)
plt.title("Accident Hotspots")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("../outputs/hotspots.png")
plt.clf()

print("Task 05 completed successfully!")