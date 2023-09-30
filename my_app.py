import matplotlib.pyplot as plt
import streamlit as st
from dabl import plot
from sklearn.datasets import fetch_openml

st.set_page_config(
    page_title="dk - Dabl data analysis baseline library",
    layout="wide",
    initial_sidebar_state="expanded",
)

X, y = fetch_openml('diamonds', as_frame=True, return_X_y=True)

st.pyplot(X, y)

# plot(X, y)
# plt.show()
