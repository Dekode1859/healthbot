import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import time

def get_response(model, query):
    prompt_template = PromptTemplate(
            template="I have a question about my health. {user_question}",
            input_variables=["user_question"]
        )
    # get the response
    memory = ConversationBufferMemory(memory_key="messages", return_messages=True)
    print(memory)
    conversation_chain = LLMChain(
        llm=model,
        prompt=prompt_template,
        # retriever=vectorstore.as_retriever(),
        memory=memory)
    response = conversation_chain.invoke(query)
    answer = response["text"]
    if "\n\n" in answer:
        answer = answer.split("\n\n", 1)[1]
    return answer

def main():
    st.title("Health Chatbot")
    # load the environment variables    
    load_dotenv()
    print("Loading LLM from HuggingFace")
    with st.spinner('Loading LLM from HuggingFace...'):
        llm = HuggingFaceHub(repo_id="HuggingFaceH4/zephyr-7b-beta", model_kwargs={"temperature":0.7, "max_new_tokens":1028, "top_p":0.95})

        # llm = HuggingFaceHub(repo_id="ajdev/falcon_medical", model_kwargs={"temperature":0.7, "max_new_tokens":250, "top_p":0.95})
    
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
        
    if st.button("Clear Chat"):
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.chat_message("user").markdown(message["content"])
        else:
            st.chat_message("bot").markdown(message["content"])
    
    user_prompt = st.chat_input("ask a question", key="user")
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})
        with st.spinner('Thinking...'):
            start_time = time.time()
            response = get_response(llm, user_prompt)
            st.write("Response Time: ", time.time() - start_time)
        st.chat_message("bot").markdown(response)
        st.session_state.messages.append({"role": "bot", "content": response})
        
if __name__ == "__main__":
    main()