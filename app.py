import streamlit as st

st.set_page_config(
    page_title="My Shop",
    layout="wide"
)

st.title("🛍️ My Online Shop")

st.markdown("""
### 여기에 홍보 문구를 작성하세요  
이 문장은 **나중에 직접 수정하기 쉬우라고 임시 텍스트**입니다.

- 최고의 품질
- 합리적인 가격
- 빠른 배송

지금 바로 상품을 확인해 보세요!
""")

st.markdown("---")

st.subheader("📌 페이지 안내")
st.write("""
왼쪽 상단 메뉴를 통해  
- **상품 목록**
- **상품 상세**
페이지로 이동할 수 있습니다.
""")
