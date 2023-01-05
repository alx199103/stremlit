import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrames')

df = pd.DataFrame({
    '1列名':[1,2,3,4],
    '2列名':[10,20,30,40],
})