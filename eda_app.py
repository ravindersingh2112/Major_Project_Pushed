import pandas as pd
from PIL import Image
import streamlit as st

def run_eda_app():
	st.subheader("Real Estate : Data Analysis")

	submenu = st.sidebar.selectbox("Submenu", ["Descriptive"])
	df = pd.read_csv("Final_Project.csv")

	if submenu == "Descriptive":
		img1 = Image.open("Real_Estate.jpg")
		st.image(img1)
		
		with st.expander("Dataset"):
			st.dataframe(df)

		with st.expander("Data Types"):
			st.dataframe(df.dtypes)

		with st.expander("Data Summary"):
			st.dataframe(df.describe())

		with st.expander("Location Distribution"):
			st.dataframe(df["Region"].value_counts().head(30))