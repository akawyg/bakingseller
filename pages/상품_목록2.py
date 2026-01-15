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

product = st.session_state.get("selected_product")

if product is None:
    st.warning("상품을 먼저 선택해주세요.")
    st.stop()

st.title(product["name"])

col1, col2 = st.columns([2, 1])

with col1:
    st.image(product["image"], use_container_width=True)
    st.image(product["image"], use_container_width=True)

with col2:
    st.subheader("상품 설명")
    st.write("""
    이 상품은 예시 상품입니다.  
    실제 설명은 나중에 자유롭게 수정하세요.
    """)

    option = st.selectbox(
        "옵션 선택",
        ["옵션 A", "옵션 B", "옵션 C"]
    )

    quantity = st.number_input(
        "수량",
        min_value=1,
        value=1
    )

    st.markdown(f"### 가격: {product['price']}")

    if st.button("🛍️ 주문하기"):
        st.success("주문이 완료되었습니다! (실제 결제는 미구현)")

