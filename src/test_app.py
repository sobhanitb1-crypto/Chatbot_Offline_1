import streamlit as st
import time

prompt = st.chat_input("Enter your question? ")
if prompt:
    st.write(f"OK : Your question is: {prompt}")
    
message = st.chat_message("ai").write("How can i help you")
message_user = st.chat_message("user").write("who is Ronaldo")
"""
with st.spinner("wait for answer..."):
    time.sleep(6)
    
st.write("Done")
"""
#Counter = 0

#if st.button("ADD"):
#    Counter += 1
#    st.write(f"counter: {Counter}")
st.write(f"session-state: {st.session_state}")

if "counter" not in st.session_state:
    st.session_state["counter"] = 0
    
if st.button("ADD"):
    st.session_state["counter"] +=1
    st.write(f"counter: {st.session_state["counter"]}")
