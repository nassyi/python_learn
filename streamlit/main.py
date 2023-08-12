import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 入門')

st.write('インタラクティブウィジェット')

option = st.text_input('趣味を教えて')


'あなたの好きな趣味は、', option, 'です'

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition

#if st.checkbox('show image'):
#    img = Image.open('download.png')
#    st.image(img, caption='google', use_column_width=True)

