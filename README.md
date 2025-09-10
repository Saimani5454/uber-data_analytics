# 🚖 Uber Data Analytics Dashboard

![Dashboard Preview](images/dashboard_preview.png)

This repository hosts a fully interactive **Streamlit web app** for analyzing Uber ride data.  
The dashboard includes:

- **Dynamic data filtering** by date, vehicle type, payment method, and booking status  
- **Key Performance Indicators (KPIs)**: total rides, completed rides, cancelled rides, average CTAT  
- **Visual insights**: monthly, daily, and hourly ride trends; vehicle type distribution; booking status breakdown; cancellation reasons; top pickup/drop locations  
- **Raw data explorer** with CSV download option  
- **Auto-generated PDF report** summarizing key metrics  
- **Embedded Power BI PDF** (`Uber.pdf`) for additional visualization  

👉 **Live Demo**: [Open the Streamlit App](https://uber-dataanalytics-sai403da.streamlit.app/)

---

## 📂 Repository Structure

uber-data-analytics/
├── app.py # Streamlit dashboard with analytics & PDF features
├── requirements.txt # Dependencies for deployment
├── ncr_ride_bookings.csv # Dataset (for analytics)
├── Uber.pdf # Power BI report (embedded in dashboard)
├── images/ # Screenshots for README
└── README.md # Project documentation

yaml
Copy code

---

## 🚀 Run Locally

1. Clone the repo:  
   ```bash
   git clone https://github.com/<your-username>/uber-data-analytics.git
   cd uber-data-analytics
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Launch the app:

bash
Copy code
streamlit run app.py
Open http://localhost:8501 in your browser 🎉

🌐 Deploy on Streamlit Cloud
Your app is already live at:
👉 https://uber-dataanalytics-sai403da.streamlit.app/

To update:

Push changes to this repo.

Streamlit Cloud will automatically redeploy the latest version.

📊 Features Overview
🔍 Filters

Select date range, vehicle type, payment method, and booking status.

📌 KPIs

Quick summary metrics for total rides, completed, cancelled, and avg CTAT.

📈 Visualizations

Rides by month, day, and hour

Vehicle type distribution

Booking status pie chart

Cancellation reason breakdown

Top pickup & drop locations

📄 Reports

Auto-generated PDF report from dataset

Embedded Power BI report (Uber.pdf) inside the app

🛠 Requirements
Dependencies listed in requirements.txt:

txt
Copy code
streamlit
pandas
numpy
matplotlib
seaborn
reportlab
📄 License
This project is for educational and analytical purposes only.
