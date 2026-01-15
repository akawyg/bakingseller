import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="베이킹 셀러",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent

st.title("🍞 베이킹 상품 목록")
st.write("원하시는 상품을 선택하세요.")

products = [
    {
        "id": 1,
        "name": "상품 1",
        "price": "10,000원",
        "image": BASE_DIR / "images" / "product1_1.jpg",
        "page": "pages/1_product_1.py"
    },
    {
        "id": 2,
        "name": "상품 2",
        "price": "20,000원",
        "image": BASE_DIR / "images" / "product2_1.jpg",
        "page": "pages/2_product_2.py"
    }
]

cols = st.columns(len(products))

for col, product in zip(cols, products):
    with col:
        st.image(str(product["image"]), use_container_width=True)
        st.subheader(product["name"])
        st.write(product["price"])
        if st.button("자세히 보기", key=product["id"]):
            st.switch_page(product["page"])
