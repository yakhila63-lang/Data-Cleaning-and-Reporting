# Data Cleaning and Reporting Dashboard 📊

Automated Data Cleaning & Reporting Dashboard using Streamlit + Pandas.

## ✨ Features
- **Upload CSV**: Any sales/order data with OrderID, Product, Sales, Region
- **Auto Clean**: 
    - Remove duplicates based on OrderID
    - Fill missing Sales → 0, Product → Unknown, Quantity → 1  
    - Fix typos: Nrth → North
- **Visualize**: Bar Chart + Pie Chart for region-wise sales
- **Export**: Download Excel report with 2 sheets: `Cleaned_Data` + `Sales_Summary`

## 🛠️ Tech Stack
Python, Pandas, Matplotlib, Streamlit, XlsxWriter

## ⚡ Quick Start - Run Locally
```bash
# 1. Clone repo
git clone https://github.com/yakhila83-lang/Data-Cleaning-and-Reporting.git

# 2. Install packages
pip install -r requirements.txt

# 3. Run app
streamlit run app.py
