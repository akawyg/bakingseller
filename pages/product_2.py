import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

BASE_DIR = Path(__file__).resolve().parent.parent

menu_l, menu_c, menu_r = st.columns([1, 6, 1])
with menu_l:
    if st.button("← 목록"):
        st.switch_page("app.py")

st.title("상품 2")

st.image(
    str(BASE_DIR / "images" / "product2_1.jpg"),
    use_container_width=True
)

st.write("💰 가격: 20,000원")
st.write("🍰 설명: 인기 많은 상품 2입니다.")
