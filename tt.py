import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
X = [[1, 1], [1, 2], [2, 2], [2, 3]]
y = [0,1,2,3]
reg = LinearRegression().fit(X, y)
reg.predict(np.array([[3, 5]]))
title = st.text_input('Movie title', '')
title2 = st.text_input('Movie title', '')
reg.predict([[int(title), int(title2)]])
st.write('The current movie title is', title)