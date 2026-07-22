import streamlit as st
import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Language Translation Tool")
st.write("Translate text between multiple languages.")

languages = GoogleTranslator().get_supported_languages()

source_lang = st.selectbox(
    "Select Source Language",
    languages,
    index=languages.index("english")
)

target_lang = st.selectbox(
    "Select Target Language",
    languages,
    index=languages.index("hindi")
)

text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type something here..."
)

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        translated = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

        st.success("Translation Complete!")

        st.text_area(
            "Translated Text",
            translated,
            height=180
        )