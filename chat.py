import streamlit as st

from dotenv import load_dotenv

from llm import get_ai_response
    
st.set_page_config(page_title="형법 챗봇", page_icon="🤖")

st.title("🤖 형법 챗봇")
st.caption("여러분의 궁금증을 언제든지 물어보세요. 범죄와 처벌, 자기 방어, 개인 권리와 보호에 관해 알려드립니다.")

load_dotenv()

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

for message in st.session_state.message_list:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_question := st.chat_input(placeholder="다양한 범죄와 그에 따른 처벌, 자기 방어, 개인의 권리와 보호에 관련된 궁금한 내용들을 말씀해주세요!"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({"role": "user", "content": user_question})

    with st.spinner("답변을 생성하는 중입니다"):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)
        st.session_state.message_list.append({"role": "ai", "content": ai_message})
