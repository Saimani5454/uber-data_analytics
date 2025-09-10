🚖 Uber Data Analytics Dashboard

This repository hosts an advanced Streamlit web app for exploring Uber ride bookings. It features:

Local file loading (with upload fallback).

KPI summaries: Total Rides, Completed, Canceled, Average CTAT.

Interactive visualizations: Trends by month, day, hour; vehicle types; booking status; cancellation reasons; pickup/drop locations.

Auto-generated PDF report with key insights from your data.

Embedded Power BI report (Uber.pdf), displayed and downloadable from within the app.

Live Demo

Check it out live here:
Uber Data Analytics Dashboard
 
uberdataanalysis-box3mi59jqezzxefndbxzn.streamlit.app

Project Structure
uber-data-analytics/
├── app.py                   # Streamlit application
├── requirements.txt         # Dependencies
├── ncr_ride_bookings.csv    # Dataset (local or upload)
├── Uber.pdf                 # Embedded Power BI visualization
└── README.md                # This documentation

Getting Started
Run Locally

Clone the repository:

git clone https://github.com/<your-username>/uber-data-analytics.git
cd uber-data-analytics


Install dependencies:

pip install -r requirements.txt


Launch the app:

streamlit run app.py


The app will open at http://localhost:8501
.

Deploy to Streamlit Cloud

Push your repo to GitHub.

Navigate to Streamlit Community Cloud
.

Deploy the repo → your app will be hosted at something like:

https://<your-username>-uber-data-analytics.streamlit.app

Features Overview

Filters: Date range, vehicle type, payment method, booking status.

KPIs: Quickly view key metrics.

Visual analytics: Line charts, bar charts, pie charts for multiple dimensions of your data.

Raw Data Explorer: View and download filtered data.

PDF Reports:

Auto-generated from filtered dataset.

Embedded Power BI export (Uber.pdf).

Requirements
streamlit
pandas
numpy
matplotlib
seaborn
reportlab


base64, os, and warnings are part of Python's standard library—no need to list them.

License

This project is provided for educational and analytical purposes only.
