import streamlit as st

with st.form(key='profile_form'):
    #テクストボックス
    name=st.text_input('名前')
    address=st.text_input('住所')
    
    #セレクトボックス
    age_category=st.radio(
        '年齢層',
        ('子ども(18才未満)','大人(18才以上)'))
    
    submit_btn=st.form_submit_button('送信')
    cancel_btn=st.form_submit_button('キャンセル')
    
    if submit_btn:
        st.text(f'ようこそ！{name}さん！{address}に郵送しました！')
        st.text(f'年齢層:{age_category}')
        st.text(f'趣味：{",".join(hobby)}')