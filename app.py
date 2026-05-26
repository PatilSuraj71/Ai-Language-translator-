# import streamlit as st
# from googletrans import Translator
# from gtts import gTTS
# import tempfile


# st.set_page_config(
#     page_title="AI Translator",
#     page_icon="🌍",
#     layout="wide"
# )


# st.markdown("""
# <style>

# .stApp {
#     background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
#     color: white;
# }

# .title {
#     text-align: center;
#     font-size: 50px;
#     font-weight: bold;
#     color: cyan;
# }

# .box {
#     background: rgba(255,255,255,0.1);
#     padding: 20px;
#     border-radius: 20px;
#     backdrop-filter: blur(10px);
# }

# textarea {
#     font-size: 22px !important;
# }

# </style>
# """, unsafe_allow_html=True)


# st.markdown(
#     '<p class="title">🌍 AI Voice Translator</p>',
#     unsafe_allow_html=True
# )



# languages = {
#     "English": "en",
#     "Hindi": "hi",
#     "Japanese": "ja",
#     "French": "fr",
#     "German": "de",
#     "Spanish": "es",
#     "Korean": "ko",
#     "Chinese": "zh-cn",
#     "Russian": "ru",
#     "Arabic": "ar",
#     "Marathi": "mr"
# }



# selected_language = st.selectbox(
#     "🌐 Select Target Language",
#     list(languages.keys())
# )


# col1, col2 = st.columns(2)

# translator = Translator()


# with col1:

#     st.subheader("⌨️ Enter Text")

#     user_text = st.text_area(
#         "",
#         height=300,
#         placeholder="Type something..."
#     )



# with col2:

#     st.subheader("🔄 Translation")

#     if user_text:

#         translated = translator.translate(
#             user_text,
#             dest=languages[selected_language]
#         )

#         translated_text = translated.text

#         st.text_area(
#             "",
#             value=translated_text,
#             height=300
#         )

#         # ================= TEXT TO SPEECH ================= #

#         tts = gTTS(
#             text=translated_text,
#             lang=languages[selected_language]
#         )

#         temp_audio = tempfile.NamedTemporaryFile(
#             delete=False,
#             suffix=".mp3"
#         )

#         tts.save(temp_audio.name)

#         st.subheader("🔊 AI Voice Assistant")

#         st.audio(temp_audio.name)

#         # ================= DOWNLOAD AUDIO ================= #

#         with open(temp_audio.name, "rb") as file:

#             st.download_button(
#                 label="⬇️ Download Voice",
#                 data=file,
#                 file_name="translated_voice.mp3",
#                 mime="audio/mp3"
#             )

# # ================= FOOTER ================= #

# st.markdown("""
# <hr>
# <center>
# <h4>Made by Suraj Patil ❤️</h4>
# </center>
# """, unsafe_allow_html=True)


import streamlit as st
from googletrans import Translator
from gtts import gTTS
import tempfile
import speech_recognition as sr   # NEW


st.set_page_config(
    page_title="AI Translator",
    page_icon="🌍",
    layout="wide"
)


st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}

.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: cyan;
}

.box {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
}

textarea {
    font-size: 22px !important;
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    '<p class="title">🌍 AI Voice Translator</p>',
    unsafe_allow_html=True
)



languages = {
    "English": "en",
    "Hindi": "hi",
    "Japanese": "ja",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Korean": "ko",
    "Chinese": "zh-cn",
    "Russian": "ru",
    "Arabic": "ar",
    "Marathi": "mr"
}



selected_language = st.selectbox(
    "🌐 Select Target Language",
    list(languages.keys())
)


# ================= VOICE INPUT FUNCTION ================= #

recognizer = sr.Recognizer()

def voice_input():

    with sr.Microphone() as source:

        st.info("🎤 Listening... Speak Now")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        st.success("✅ Voice Recognized")

        return text

    except:

        st.error("❌ Could not recognize voice")

        return ""


# ================= BUTTON ================= #

voice_text = ""

if st.button("🎙️ Start Voice Input"):

    voice_text = voice_input()



col1, col2 = st.columns(2)

translator = Translator()


with col1:

    st.subheader("⌨️ Enter Text")

    user_text = st.text_area(
        "",
        value=voice_text,   # NEW
        height=300,
        placeholder="Type something..."
    )



with col2:

    st.subheader("🔄 Translation")

    if user_text:

        translated = translator.translate(
            user_text,
            dest=languages[selected_language]
        )

        translated_text = translated.text

        st.text_area(
            "",
            value=translated_text,
            height=300
        )

        # ================= TEXT TO SPEECH ================= #

        tts = gTTS(
            text=translated_text,
            lang=languages[selected_language]
        )

        temp_audio = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        tts.save(temp_audio.name)

        st.subheader("🔊 AI Voice Assistant")

        st.audio(temp_audio.name)

        # ================= DOWNLOAD AUDIO ================= #

        with open(temp_audio.name, "rb") as file:

            st.download_button(
                label="⬇️ Download Voice",
                data=file,
                file_name="translated_voice.mp3",
                mime="audio/mp3"
            )

# ================= FOOTER ================= #

st.markdown("""
<hr>
<center>
<h4>Made by Suraj Patil ❤️</h4>
</center>
""", unsafe_allow_html=True)