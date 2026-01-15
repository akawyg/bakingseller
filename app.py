import streamlit as st

st.set_page_config(
    page_title="베이킹 셀러",
    layout="wide"
)

# 🔝 상단 메뉴 (가짜 네비게이션)
menu_l, menu_c, menu_r = st.columns([1, 6, 1])

with menu_l:
    st.markdown("### 🏠 홈")

with menu_r:
    if st.button("상품 보기"):
        st.switch_page("pages/1_products.py")

# 🧁 메인 소개
st.title("🍞 베이킹 셀러에 오신 것을 환영합니다")

st.write("""
이 사이트는 맛있는 베이킹 상품을 판매하는 쇼핑몰입니다.  
신선한 재료와 정성으로 만든 다양한 상품을 만나보세요.

(이 문구는 나중에 자유롭게 수정하셔도 됩니다)
""")

st.image(
    "https://images.unsplash.com/photo-1542826438-6f7f8f2c2d3b",
    use_container_width=True
)

