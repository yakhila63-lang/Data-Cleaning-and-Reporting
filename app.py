import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Cleaning Report", layout="wide")
st.title("📊 Sales Data Cleaning & Reporting Dashboard")

uploaded_file = st.file_uploader("Upload your raw.csv file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("1. Raw Data")
    st.dataframe(df)

    # Cleaning Logic
    df_clean = df.copy()
    df_clean.drop_duplicates(subset=['OrderID'], keep='first', inplace=True)
    df_clean['Product'] = df_clean['Product'].fillna('Unknown')
    df_clean['Sales'] = pd.to_numeric(df_clean['Sales'], errors='coerce').fillna(0)
    df_clean['Quantity'] = df_clean['Quantity'].fillna(1)
    df_clean['CustomerName'] = df_clean['CustomerName'].fillna('Unknown Customer')
    df_clean['Region'] = df_clean['Region'].replace('Nrth', 'North')

    st.subheader("2. Cleaned Data ✅")
    st.dataframe(df_clean)
    st.write(f"Original rows: {len(df)} | Cleaned rows: {len(df_clean)}")

    # Report Generation
    st.subheader("3. Sales Summary by Region")
    summary = df_clean.groupby('Region')['Sales'].sum().reset_index()
    summary.columns = ['Region', 'Total Sales']
    st.dataframe(summary)

    # Charts Section
    st.subheader("4. Visualizations")
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Bar Chart**")
        fig1, ax1 = plt.subplots()
        ax1.bar(summary['Region'], summary['Total Sales'], color='#2E86AB')
        ax1.set_title('Total Sales by Region')
        ax1.set_xlabel('Region')
        ax1.set_ylabel('Total Sales')
        plt.xticks(rotation=45)
        st.pyplot(fig1)

    with col2:
        st.write("**Pie Chart**")
        fig2, ax2 = plt.subplots()
        ax2.pie(summary['Total Sales'], labels=summary['Region'], autopct='%1.1f%%', startangle=90)
        ax2.set_title('Sales Distribution by Region')
        st.pyplot(fig2)

    st.success("Report generated successfully!")
    
    # Download Excel
    with pd.ExcelWriter('automated_report.xlsx', engine='openpyxl') as writer:
        df_clean.to_excel(writer, sheet_name='Cleaned_Data', index=False)
        summary.to_excel(writer, sheet_name='Sales_Summary', index=False)
    
    with open("automated_report.xlsx", "rb") as file:
        st.download_button(
            label="Download Excel Report",
            data=file,
            file_name="automated_report.xlsx"
        )
else:
    st.info("Please upload raw.csv to start cleaning")