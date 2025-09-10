import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# ==============================
# CONFIG
# ==============================
st.set_page_config(page_title="Uber Data Analytics", page_icon="🚖", layout="wide")

# ==============================
# LOAD DATA (LOCAL ONLY)
# ==============================
@st.cache_data
def load_data():
    df = pd.read_csv("ncr_ride_bookings.csv")  # Must be in same repo as app.py
    df['Date'] = pd.to_datetime(df['Date'])
    df['Time'] = pd.to_datetime(df['Time'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day_name()
    df['Hour'] = df['Time'].dt.hour
    df['Payment Method'] = df['Payment Method'].fillna("Unknown")
    df["Avg VTAT"] = df["Avg VTAT"].fillna(df["Avg VTAT"].mean())
    df["Avg CTAT"] = df["Avg CTAT"].fillna(df["Avg CTAT"].mean())
    return df

df = load_data()

# ==============================
# SIDEBAR FILTERS
# ==============================
st.sidebar.header("🔍 Filters")
min_date, max_date = df['Date'].min(), df['Date'].max()
date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date])
vehicles = st.sidebar.multiselect("Vehicle Types", df['Vehicle Type'].unique(), default=df['Vehicle Type'].unique())
payments = st.sidebar.multiselect("Payment Methods", df['Payment Method'].unique(), default=df['Payment Method'].unique())
statuses = st.sidebar.multiselect("Booking Status", df['Booking Status'].unique(), default=df['Booking Status'].unique())

# Apply filters
df_filtered = df[
    (df['Date'].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1]))) &
    (df['Vehicle Type'].isin(vehicles)) &
    (df['Payment Method'].isin(payments)) &
    (df['Booking Status'].isin(statuses))
]

# ==============================
# KPIs
# ==============================
st.title("🚖 Uber Data Analytics Dashboard")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Rides", f"{len(df_filtered):,}")
col2.metric("Completed", df_filtered[df_filtered["Booking Status"] == "Completed"].shape[0])
col3.metric("Cancelled", df_filtered[df_filtered["Booking Status"].str.contains("Cancel")].shape[0])
col4.metric("Avg CTAT", f"{df_filtered['Avg CTAT'].mean():.2f} mins")

# ==============================
# VISUALIZATIONS
# ==============================
st.markdown("## 📈 Trends & Patterns")

# --- Monthly rides
st.subheader("Rides per Month")
months = df_filtered.groupby('Month').size()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=months.index, y=months.values, marker='o', ax=ax)
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
st.pyplot(fig)

# --- Daily rides
st.subheader("Rides by Day of Week")
days = df_filtered.groupby('Day').size().reindex(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=days.index, y=days.values, palette='viridis', ax=ax)
st.pyplot(fig)

# --- Hourly rides
st.subheader("Rides by Hour of Day")
hours = df_filtered.groupby('Hour').size()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hours.index, y=hours.values, marker='o', ax=ax)
ax.set_xticks(range(0, 24))
st.pyplot(fig)

# --- Vehicle Type
st.subheader("Rides per Vehicle Type")
vehicle = df_filtered['Vehicle Type'].value_counts()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=vehicle.values, y=vehicle.index, palette='Blues_r', ax=ax)
st.pyplot(fig)

# --- Pickup & Drop Locations
st.subheader("Top Pickup & Drop Locations")
col1, col2 = st.columns(2)
with col1:
    st.bar_chart(df_filtered['Pickup Location'].value_counts().head(5))
with col2:
    st.bar_chart(df_filtered['Drop Location'].value_counts().head(5))

# --- Booking Status
st.subheader("Booking Status Distribution")
fig, ax = plt.subplots()
booking = df_filtered['Booking Status'].value_counts()
ax.pie(booking.values, labels=booking.index, autopct='%1.1f%%', startangle=140, shadow=True)
st.pyplot(fig)

# --- Cancellation Reasons
st.subheader("Cancellation Reasons")
cols = ["Reason for cancelling by Customer", "Driver Cancellation Reason", "Incomplete Rides Reason"]
titles = ["By Customer", "By Driver", "Incomplete Rides"]
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
for i, (col, title) in enumerate(zip(cols, titles)):
    counts = df_filtered[col].value_counts().head(5)
    axes[i].pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    axes[i].set_title(title)
st.pyplot(fig)

# ==============================
# RAW DATA EXPLORER
# ==============================
st.markdown("## 🔎 Explore Raw Data")
st.dataframe(df_filtered)

csv = df_filtered.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download Filtered Data", data=csv, file_name="uber_filtered.csv", mime="text/csv")

