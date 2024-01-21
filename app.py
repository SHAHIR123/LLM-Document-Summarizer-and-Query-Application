import streamlit as st 
import urllib
import base64
import os
from llama_index import ServiceContext
from llama_index import set_global_service_context
import torch
from rag import semantic_search, summarize

#function to save a file
def save_uploadedfile(uploadedfile):
    for filename in os.listdir("data"):
        file_path = os.path.join("data", filename)
        os.remove(file_path)
    with open(os.path.join("data",uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to directory".format(uploadedfile.name))

# @st.cache_data
#function to display the PDF of a given file 
def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    # pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
    

#streamlit application
st. set_page_config(layout='wide')
# st.image("sample.png")
# st.title(':violet[ LLM SUMMARIZATION]')
st.header('Semantic Search Application', divider='rainbow')

uploaded_pdf = st.file_uploader("Upload your PDF", type=['pdf'])

if uploaded_pdf is not None:
    col1, col2, col3 = st.columns([2,1,1])
    with col1:
        input_file = save_uploadedfile(uploaded_pdf)
        pdf_file = "data/"+uploaded_pdf.name
        pdf_view = displayPDF(pdf_file)
    with col2:
        st.success("Search Area")
        query_search = st.text_area("Search your query")
        if st.checkbox("search"):
            st.info("Your query: "+query_search)

            result = semantic_search(query_search)
            st.write(result)
    with col3:
        st.success("Automated Summarization")
        summary_result = summarize(pdf_file)
        st.write(summary_result)     
         
            