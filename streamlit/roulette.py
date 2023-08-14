import streamlit as st
import random
import time

# ルーレットの項目を入力する
r_name = st.sidebar.text_input('タイトルを入力してください')
r_f_str = st.sidebar.text_input('前の文章')
r_e_str = st.sidebar.text_input('後の文章')
items = st.sidebar.text_input("ルーレットの項目をカンマで区切って入力してください(例：AAA,BBB,CCC)")


st.title(r_name)
ret = ''

placeHolder = st.empty() # placeHolderオブジェクトを作成
placeHolder.text(f'{r_f_str}「{ret}」{r_e_str}') 

left_column, right_column = st.columns(2)

#if items:
items = items.split(",")

if items:
    l_button = left_column.button("ルーレットを回す")
    r_button = right_column.button("ルーレットを止める")
    while l_button:
        ret = random.choice(items)
        placeHolder.text(f'{r_f_str}「{ret}」{r_e_str}') 
            
        if r_button:
            break

        time.sleep(0.05)
            
else:
        # リストが空ならエラーを表示する
    st.error("項目を入力してください")

placeHolder.text(f'{r_f_str}「{ret}」{r_e_str}') 

