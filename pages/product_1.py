import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔝 상단 가짜 메뉴
menu_l, menu_c, menu_r = st.columns([1, 6, 1])
with menu_l:
    if st.button("← 목록"):
        st.switch_page("app.py")

st.title("상품 1")

st.image(
    str(BASE_DIR / "images" / "product1_1.jpg"),
    use_container_width=True
)

st.write("💰 가격: 10,000원")
st.write("🍰 설명: 맛있는 상품 1입니다.")
