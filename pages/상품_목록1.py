import streamlit as st

st.title("🛒 상품 목록")

products = [
    {
        "id": 1,
        "name": "상품 1",
        "price": "10,000원",
        "image": "images/product1_1.jpg"
    },
    {
        "id": 2,
        "name": "상품 2",
        "price": "20,000원",
        "image": "images/product2_1.jpg"
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

