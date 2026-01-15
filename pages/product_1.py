import streamlit as st

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("🏠 메인"):
        st.switch_page("app.py")

with col2:
    if st.button("🛒 상품"):
        st.switch_page("pages/product_1.py")

with col3:
    if st.button("📦 주문"):
        st.switch_page("pages/product_2.py")

import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
section[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)
import streamlit as st

st.title("🛒 상품 목록")

products = [
    {
        "id": 1,
        "name": "상품 1",
        "price": "10,000원",
        "image": "../images/product1_1.jpg"
    },
    {
        "id": 2,
        "name": "상품 2",
        "price": "20,000원",
        "image": "../images/product2_1.jpg"
    }
]

cols = st.columns(2)

for idx, product in enumerate(products):
    with cols[idx % 2]:
        st.image(product["image"], use_container_width=True)
        st.subheader(product["name"])
        st.write(product["price"])

        if st.button(f"{product['name']} 구매하기", key=product["id"]):
            st.session_state["selected_product"] = product
            st.switch_page("pages/2_상품_상세.py")

