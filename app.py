import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="GA11 VOC", page_icon=":squid:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_cat = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_OT15QW.json")

# ----header section ---
with st.container():
    st.subheader("Hallo, ich bin LIVID")
    st.title("und wer bist du?")
    st.write("hehehe hahaha tttt")
    st.write("[My Github >](https://github.com/ilivid)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("what's this")
        st.write("##")
        st.write("sssss")
    with right_column:
        st_lottie(lottie_cat, height=300, key='cat')