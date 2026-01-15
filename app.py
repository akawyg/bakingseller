import streamlit as st

st.set_page_config(
    page_title="베이킹 셀러",
    layout="wide"
)

# 🔝 상단 메뉴
menu_l, menu_c, menu_r = st.columns([1, 6, 1])

with menu_l:
    st.markdown("### 🏠 홈")

with menu_r:
    if st.button("상품 보기"):
        st.switch_page("pages/1_products.py")

# 🧁 소개 문구
st.title("🍞 베이킹 셀러")

st.write("""
이 사이트는 수제로 만든 베이킹 상품을 판매하는 공간입니다.  
신선한 재료와 정성으로 만든 상품들을 만나보세요.

(이 문구는 자유롭게 수정하셔도 됩니다)
""")

st.image(
    "https://images.unsplash.com/photo-1509440159598-0249088772ff",
    use_container_width=True
)


