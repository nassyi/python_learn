import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 入門')

st.write('Display image')
img = Image.open('download.png')
st.image(img, caption='google', use_column_width=True)

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
st.map(df)


#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0))
#st.table(df.style.highlight_max(axis=0))

