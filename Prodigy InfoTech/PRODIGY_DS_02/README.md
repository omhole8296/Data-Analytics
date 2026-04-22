📊 Task 02 – Data Cleaning & Exploratory Data Analysis (EDA)

Prodigy InfoTech Data Science Internship

🚀 Objective

The goal of this task is to perform data cleaning and exploratory data analysis (EDA) on a dataset to identify patterns, relationships, and trends.

📁 Dataset
Dataset used: Titanic Dataset (train.csv)
Contains information about passengers such as age, gender, class, fare, and survival status.
🧹 Data Cleaning

The dataset contained missing values and irrelevant columns. The following steps were performed:

Filled missing values in Age using median
Filled missing values in Embarked using mode
Dropped Cabin column due to excessive missing values
🔍 Exploratory Data Analysis (EDA)
📌 Survival Distribution
Majority of passengers did not survive
📌 Survival by Gender
Females had a significantly higher survival rate than males
📌 Survival by Passenger Class
Passengers in 1st class had the highest survival rate
3rd class passengers had the lowest survival rate
📌 Age Distribution
Most passengers were young adults
📌 Fare Distribution
Fare data is right-skewed, indicating a few passengers paid very high fares
📊 Visualizations

(Add your images in outputs/ folder)

![Survival Count](outputs/survival.png)
![Gender Survival](outputs/gender.png)
![Class Survival](outputs/class.png)
![Age Distribution](outputs/age.png)
![Fare Distribution](outputs/fare.png)
🛠️ Technologies Used
Python
Pandas
Matplotlib
📌 Key Insights
Gender plays a major role in survival probability
Socio-economic status (class) affects survival chances
Younger passengers had slightly better survival trends
Data cleaning is essential before analysis
🔗 Conclusion

This task helped in understanding how to clean real-world data and extract meaningful insights using exploratory data analysis techniques.

🙌 Acknowledgement

Thanks to Prodigy InfoTech for providing this opportunity to apply data science concepts on real-world datasets.
