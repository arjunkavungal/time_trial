import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
X = [[1, 1], [1, 2], [2, 2], [2, 3],[3,4]]
y = [0,1,2,3,4]
reg = LinearRegression().fit(X, y)
title = st.text_input('Movie title', '')
title2 = st.text_input('a', '')
st.write('The current movie title is', reg.predict([[int(title), int(title2)]]))
