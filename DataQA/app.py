import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')
st.title("Talk to your data file...")

col1, col2 = st.columns([0.3,0.7])
data = pd.DataFrame()
with col1:
    upload_file = st.file_uploader("Upload a CSV file")

    if upload_file is not None:
        data = pd.read_csv(upload_file)
        st.write(data.head())
with col2:
    prompt = st.text_area('Enter your Prompt....')
    # from pandasai.llm.local_llm import LocalLLM
    # model = LocalLLM(api_base = 'http://localhost:11434/v1', model='llama3')

    from pandasai.llm.openai import OpenAI
    model = OpenAI(api_token='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')

    # from pandasai.llm.llama3 import llama3
    # model = OpenAI(api_token='LL-xt5kWtIsM2Ur3j4a7UKQ5cFBj1RY6tjJKljNdRmPURZjiKCIOMyEyvL7CPlDGaZR')

    from pandasai import SmartDataframe
    df = SmartDataframe(data, config={'llm':model})

    if st.button('Generate'):
        if prompt:
            with st.spinner('Generating response.....'):
                st.write(df.chat(prompt))