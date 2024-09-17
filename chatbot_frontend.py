# Source:Below code is provided by Streamlit and AWS 

#1 import streamlit and chatbot file
import streamlit as st 
import  chatbot_backend as demo  #**Import your Chatbot file as demo


st.title("Hi, This is Chatbot Mitch :sunglasses:") # **Modify this based on the title you want in want

#https://docs.streamlit.io/library/api-reference/session-state
if 'memory' not in st.session_state: 
    st.session_state.memory = demo.demo_memory() #** Modify the import and memory function() attributes initialize the memory

#https://docs.streamlit.io/library/api-reference/session-state
if 'chat_history' not in st.session_state: #see if the chat history hasn't been created yet
    st.session_state.chat_history = [] #initialize the chat history

# basically for streamlit, the history only keeps track of the data, not the ui elements
# so we have to regenerate ui elements every render
for message in st.session_state.chat_history: 
    with st.chat_message(message["role"]): 
        st.markdown(message["text"]) 
     
input_text = st.chat_input("Powered by Bedrock and Claude") # **display a chat input box
if input_text: 
    
    with st.chat_message("user"): 
        st.markdown(input_text) 
    
    st.session_state.chat_history.append({"role":"user", "text":input_text}) 

    chat_response = demo.demo_conversation(input_text=input_text, memory=st.session_state.memory) #** replace with ConversationChain Method name - call the model through the supporting library
    
    with st.chat_message("assistant"): 
        st.markdown(chat_response) 
    
    st.session_state.chat_history.append({"role":"assistant", "text":chat_response}) 