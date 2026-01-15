import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

BASE_DIR = Path(__file__).resolve().parent.parent

product = {
    "name": "상품 2",
    "price": "20,000원",
    "image": BASE_DIR / "images" / "product2_1.jpg",
    "description": "인기 많은 상품 2입니다."
}

# 🔝 상단 버튼
top_col1, top_col2, top_col3 = st.columns([1, 6, 1])
with top_col3:
    if st.button("← 목록으로"):
        st.switch_page("app.py")

st.image(str(product["image"]), use_container_width=True)
st.title(product["name"])
st.write(product["price"])
st.write(product["description"])
