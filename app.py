
import streamlit as st # 확장자가 길어서 st 로 줄임

# 앱의 메인 타이틀을 출력
st.title('튜토리얼1 : 텍스트 출력')


# 큰 제목을 출력
st.header(" 기본 텍스트 출력")

# 일반적인 문자열을 그대로 출력
st.text('기본 텍스트를 출력합니다.')

# 중간 제목을 출력
st.subheader("마크다운 활용")

# 마크다운 문법을 활용하여 서식을 적용한 텍스트를 출력
st.markdown("**굵게**,_기울임_, [링크](https://streamlit.io)")

# # 코드 설명 섹션을 출력
# st.subheader("코드 출력")
# 
#  # 코드 블록을 출력(하이라이팅 포함)
# st.code("print('Hello, Streamlit!)", language="python")

st.divider # 뭐야 뭐가 움직여

# 코드 설명 섹션을 출력
st.subheader("코드 출력")

# 코드 블록을 출력 (하이라이팅 포함)
st.code("print('Hello, Streamlit!')", language="python")

st.divider
