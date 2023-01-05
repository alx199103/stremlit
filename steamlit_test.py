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

st.dataframe(df.style.highlight_max(axis=0),width=300,height=200)
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import pandas
```
"""

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df2)


st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('20210326-131146-046.jpg')
    st.image(img,caption='Takayuki Nakagawa',use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))
)

'あなたの好きな数字は、', option , 'です。'

st.sidebar.write('Interactive Widgets')

text = st.sidebar.text_input('あなたの趣味を教えてください。')
condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

'あなたの好きな趣味は、', text , 'です。'


'あなたの好きなコンデションは、', condition , 'です。'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問合せ')
expander.write('問合せ内容を書く')
expander.write('問合せ内容を書く')
expander.write('問合せ内容を書く')
expander.write('問合せ内容を書く')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'