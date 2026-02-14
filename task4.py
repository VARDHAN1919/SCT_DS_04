import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATASET
# -----------------------------
df = pd.read_csv("US_Accidents_March23.csv")

# Convert Start_Time to datetime
df["Start_Time"] = pd.to_datetime(df["Start_Time"])

# Extract hour from time
df["Hour"] = df["Start_Time"].dt.hour

# -----------------------------
# BAR GRAPH — Accidents by Hour
# -----------------------------
plt.figure()
df["Hour"].value_counts().sort_index().plot(kind="bar")

plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.show()

# -----------------------------
# 3D PIE CHART — Weather
# -----------------------------
plt.figure()

weather_counts = df["Weather_Condition"].value_counts()
explode = [0.05] * len(weather_counts)

plt.pie(
    weather_counts,
    labels=weather_counts.index,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode
)

plt.title("3D Pie Chart of Weather Conditions in Accidents")
plt.show()

# -----------------------------
# LINE GRAPH — Severity Trend
# -----------------------------
plt.figure()
df["Severity"].value_counts().sort_index().plot(
    kind="line",
    marker="o"
)

plt.title("Accident Severity Distribution")
plt.xlabel("Severity Level")
plt.ylabel("Number of Accidents")
plt.show()

print("All graphs generated successfully!")
