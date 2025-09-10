import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import io

warnings.filterwarnings('ignore')


st.title("🚖 Uber Exploratory Data Analysis (EDA)")
st.markdown("This app provides insights into Uber ride bookings data.")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("ncr_ride_bookings.csv")
    return df

df1 = load_data()

st.subheader("📊 Raw Data Preview")
st.write(df1.head())

# --- Missing Values ---
st.subheader("🧹 Missing Values")
st.write(df1.isnull().sum())

# --- Data Info ---
st.subheader("ℹ️ Dataset Info")
buffer = io.StringIO()
df1.info(buf=buffer)
st.text(buffer.getvalue())

# --- Duplicate Records ---
st.write("Number of duplicate records:", df1.duplicated().sum())
st.write("Shape of dataset:", df1.shape)

# --- Data Cleaning ---
df1['Payment Method'] = df1['Payment Method'].fillna("Unknown")
df1["Avg VTAT"] = df1["Avg VTAT"].fillna(df1["Avg VTAT"].mean())
df1["Avg CTAT"] = df1["Avg CTAT"].fillna(df1["Avg CTAT"].mean())

df1['Date'] = pd.to_datetime(df1['Date'])
df1['Time'] = pd.to_datetime(df1['Time'])

df1['Year'] = df1['Date'].dt.year
df1['Month'] = df1['Date'].dt.month
df1['Day'] = df1['Date'].dt.day_name()

# --- Visualizations ---
st.subheader("📈 Number of Rides per Month")
months = df1.groupby('Month').size()
fig, ax = plt.subplots(figsize=(13, 5))
sns.lineplot(x=months.index, y=months.values, marker='o', ax=ax)
ax.set_title('Number of Rides per Month')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Rides')
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['January','February','March','April','May','June',
                    'July','August','September','October','November','December'],
                   rotation=45)
st.pyplot(fig)

st.subheader("📅 Number of Rides per Day")
days = df1.groupby('Day').size().reindex(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
fig, ax = plt.subplots(figsize=(13, 5))
sns.barplot(x=days.index, y=days.values, palette='viridis', ax=ax)
ax.set_title('Number of Rides per Day')
ax.set_xlabel('Day')
ax.set_ylabel('Number of Rides')
for x, y in enumerate(days.values):
    ax.text(x, y + 10, str(y), ha='center')
st.pyplot(fig)

st.subheader("⏰ Booking by Hours of Day")
hours = df1.groupby(df1['Time'].dt.hour).size()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hours.index, y=hours.values, marker='o', ax=ax)
ax.set_title('Booking by Hours of Day')
ax.set_xlabel('Hour')
ax.set_ylabel('Number of Bookings')
for i, j in enumerate(hours.values):
    ax.text(i, j + 10, str(j), ha='center', fontsize=8)
st.pyplot(fig)

st.subheader("🚗 Number of Rides per Vehicle Type")
vehicle = df1['Vehicle Type'].value_counts()
fig, ax = plt.subplots(figsize=(13, 5))
sns.barplot(x=vehicle.values, y=vehicle.index, palette='viridis', ax=ax)
ax.set_title('Number of Rides per Vehicle Type')
ax.set_xlabel('Number of Rides')
ax.set_ylabel('Vehicle Type')
st.pyplot(fig)

st.subheader("📍 Top Pickup & Drop Locations")
location_pick = df1['Pickup Location'].value_counts().head(5)
location_drop = df1['Drop Location'].value_counts().head(5)
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
sns.barplot(x=location_pick.index, y=location_pick.values, ax=axes[0], palette="Blues_r")
axes[0].set_title('Top 5 Pickup Locations')
sns.barplot(x=location_drop.index, y=location_drop.values, ax=axes[1], palette="Greens_r")
axes[1].set_title('Top 5 Drop Locations')
plt.tight_layout()
st.pyplot(fig)

st.subheader("❌ Booking Status Distribution")
booking = df1['Booking Status'].value_counts()
explode = [0.1 if (v / booking.sum()) >= 0.15 else 0.05 for v in booking.values]
plt.pie(booking.values, labels=booking.index, autopct='%1.1f%%', explode=explode,
        startangle=140, colors=sns.color_palette("deep"), shadow=True,
        wedgeprops={'edgecolor': 'black'})
st.pyplot()

st.subheader("🚫 Cancellation Reasons")
cols = ["Reason for cancelling by Customer", "Driver Cancellation Reason", "Incomplete Rides Reason"]
titles = ["Canceling by Customer", "Canceling by Driver", "Incomplete Rides"]
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
axes = axes.flatten()
for i, (col, title) in enumerate(zip(cols, titles)):
    counts = df1[col].value_counts(dropna=True)
    total = counts.sum()
    explode = [0.1 if v/total >= 0.15 else 0.05 for v in counts.values]
    wedges, texts, autotexts = axes[i].pie(
        counts,
        labels=counts.index,
        autopct='%1.1f%%',
        startangle=140,
        shadow=True,
        explode=explode,
        wedgeprops={'edgecolor': 'black'},
        colors=sns.color_palette("deep"),
    )
    axes[i].set_title(title, fontsize=14)
fig.delaxes(axes[3])  # remove empty subplot
plt.tight_layout()
st.pyplot(fig)
