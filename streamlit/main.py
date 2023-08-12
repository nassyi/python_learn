import streamlit as st
import time

st.title('streamlit 入門')

st.write('プログレスバーの表示')
'start'
latest_iteration=st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button('左カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

exp = st.expander('問い合わせ')
exp.write('問い合わせ内容を書く')

option = st.text_input('趣味を教えて')
'あなたの好きな趣味は、', option, 'です'

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition

#if st.checkbox('show image'):
#    img = Image.open('download.png')
#    st.image(img, caption='google', use_column_width=True)

