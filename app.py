import streamlit as st
import utils

st.title(':llama: This is Offline Chatbot Project')

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role':'assistant', 
                                     'content':'How can I Help You'}]
    
st.chat_message('assistant').write('How can I Help You') 
## for msg in ...
for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])
    
model = 'qwen2.5-coder:7b'
prompt =  st.chat_input('Enter Your Question: ')
if prompt:
    
    st.chat_message('user').write(prompt)
    st.session_state['messages'].append({'role':'user', 'content':prompt})
        
    if 'password' in prompt:
        st.chat_message("ai").write('I can not answer to these topics')
        st.session_state['messages'].append({'role':'ai', 'content':'I can not answer to this queston'})   
    else:
        prompt2 = 'explain ypur anwer using several examples' + prompt
        with st.spinner('Wait for generate response...'):
            result = utils.call_ollama_model(model, prompt)

        st.chat_message('assistant').write(result)
        st.session_state['messages'].append({'role':'ai', 'content':result})