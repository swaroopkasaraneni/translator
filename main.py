import IPython.display as ipd
import TextExtractor
import AudioConvertor
import LLMExecuter
from CustomError import CustomError
import streamlit as st

language_dict = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it"
}

def alertMessageHtml(msg):
  return f"""
    <div style="
        color: red; 
        font-family: 'Courier New', monospace; 
        font-size: 20px; 
        font-weight: bold;
    ">
       {msg} 
    </div>
    """

st.title("Translation Application")

col1, col2 = st.columns([2, 2])  # Adjust column width proportions if needed
with col1:
    selected_language = st.selectbox("Select language", list(language_dict.keys()))

with col2:
    slow_speech = st.checkbox("Slow speech")

text = st.text_input("Text: ")
uploaded_file  = st.file_uploader("Upload a file and supporting format:pdf,docx,txt,csv,xlsx:")

if uploaded_file is not None:
  doc_name = uploaded_file.name
  if doc_name.endswith(".pdf"):
    text = TextExtractor.from_pdf(uploaded_file)
  elif doc_name.endswith(".docx"):
    text = TextExtractor.from_docx(uploaded_file)
  elif doc_name.endswith(".txt"):
    text = TextExtractor.from_txt(uploaded_file)
  elif doc_name.endswith(".csv"):
    text = TextExtractor.from_csv(uploaded_file)
  elif doc_name.endswith(".xlsx"):
    text = TextExtractor.from_excel(uploaded_file)
  else:
    st.markdown(alertMessageHtml("file is not supported"), unsafe_allow_html=True)


# Display the corresponding value (language code)
st.write(f"You selected: {selected_language} ({language_dict[selected_language]})")

try:
  if text:
      st.write("Translation:")
      tran_text = LLMExecuter.executeGooglePalm(text,"English",selected_language)
      st.write(tran_text)
      audio_file = AudioConvertor.textToSpeech(tran_text,language_dict[selected_language],slow_speech)
      # Display audio player in Streamlit
      st.audio(audio_file, format="audio/mp3")
      # Play the audio
      st.write("Playing your text as speech...")
      ipd.display(ipd.Audio(audio_file))
  else:
    st.markdown(alertMessageHtml('provide the Data for Translation'), unsafe_allow_html=True)    
except CustomError as e:
    st.markdown(alertMessageHtml(e.message+", please try later"), unsafe_allow_html=True)







