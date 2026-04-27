# 🚗 Task 05 – Traffic Accident Data Analysis

**Prodigy InfoTech Data Science Internship**

---

## 🚀 Objective

The objective of this task is to analyze traffic accident data to identify patterns related to road conditions, weather, and time of day. The project also visualizes accident hotspots and contributing factors.

---

## 📁 Dataset

* Dataset used: **US Accidents Dataset**
* Source: Kaggle
* File used in project: `US_Accidents_sample.csv`
* Note: A sampled subset of the original dataset was used due to the large file size.

---

## 📊 Features Used

* Severity
* Start_Time
* Weather_Condition
* State
* Start_Lat
* Start_Lng
* Sunrise_Sunset

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

* Selected relevant columns
* Removed rows with missing values
* Converted `Start_Time` to datetime format
* Extracted accident hour for time-based analysis

---

## 📈 Exploratory Data Analysis

### 📌 Accidents by Hour of Day

Shows peak accident hours and time-of-day patterns.

![Accidents by Hour](outputs/hourly_accidents.png)

---

### 📌 Top Weather Conditions During Accidents

Displays weather conditions most commonly associated with accidents.

![Weather Conditions](outputs/weather_conditions.png)

---

### 📌 Accident Severity Distribution

Shows the frequency of severity levels.

![Severity Distribution](outputs/severity.png)

---

### 📌 Top 10 States with Most Accidents

Highlights states with highest accident counts.

![Top States](outputs/top_states.png)

---

### 📌 Day vs Night Accidents

Compares accident occurrence during day and night.

![Day vs Night](outputs/day_night.png)

---

### 📌 Accident Hotspots

Scatter plot of accident locations using latitude and longitude.

![Hotspots](outputs/hotspots.png)

---

## 🧠 Key Insights

* Accidents are more frequent during commuting hours
* Clear and cloudy weather still show many accidents due to high traffic volume
* Certain states report significantly higher accident counts
* Accident hotspots are concentrated in urban and high-traffic regions
* Both daytime and nighttime conditions contribute to accidents

---

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib

---

## 📁 Project Structure

```text
Prodigy-DataScience-Task5/
│
├── data/
│   └── US_Accidents_sample.csv
│
├── notebooks/
│   └── Prodigy InfoTech task 5.ipynb
│
├── scripts/
│   └── task5.py
│
├── outputs/
│   ├── Accident Hotspots.png
│   ├── Accident Severity Distribution.png
│   ├── Accidents by Hour of Day.png
│   ├── Day vs Night Accidents.png
│   ├── Top 10 States with Most Accidents.png
│   └── Top Weather Conditions During Accidents.png
│
├── README.md
└── requirements.txt
```

---

## 🔗 Conclusion

This task provided practical experience in analyzing large real-world datasets, identifying accident trends, and using data visualization to uncover meaningful traffic safety insights.

---

## 🙌 Acknowledgement

Thanks to Prodigy InfoTech for providing this opportunity to work on real-world data science projects.

---
