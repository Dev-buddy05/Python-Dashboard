import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

st.title("Student Data Analysis")

st.subheader("Data Info")
df=pd.read_csv("StudentsPerformance.csv")
st.dataframe(df)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Gender Count")
df_gender = df["gender"].value_counts().rename_axis("Gender").reset_index(name="Count")
st.dataframe(df_gender)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

fig, ax = plt.subplots(1, 1)
_, _, per_labels = ax.pie(x=df_gender["Count"], labels=df_gender["Gender"], autopct="%1.0f%%")
for i in range(len(per_labels)):
  per_labels[i].set_color("white")
st.pyplot(fig)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Education vs Math Score")
df_edu = df.groupby("parental level of education")[["parental level of education", "math score"]].agg("sum").sort_values(by="math score", ascending=False).reset_index()
df_edu

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

fig, ax = plt.subplots(1, 1)
ax.bar(df_edu["parental level of education"], df_edu["math score"])
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Education vs Reading Score")
df_edu = df.groupby("parental level of education")[["parental level of education", "reading score"]].agg("sum").sort_values(by="reading score", ascending=False).reset_index()
df_edu

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

fig, ax = plt.subplots(1, 1)
ax.scatter(df_edu["parental level of education"], df_edu["reading score"])
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

st.subheader("Education vs Writing Score")
df_edu = df.groupby("parental level of education")[["parental level of education", "writing score"]].agg("sum").sort_values(by="writing score", ascending=True).reset_index()
df_edu

st.markdown("""<hr style="height:5px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

fig, ax = plt.subplots(1, 1)
ax.plot(df_edu["parental level of education"], df_edu["writing score"])
plt.xticks(rotation=45)
st.pyplot(fig)