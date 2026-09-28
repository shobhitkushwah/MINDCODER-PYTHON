import streamlit as st
import time

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="My AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background-color: #212121;
}

section[data-testid="stSidebar"] {
    background-color: #171717;
}

.chat-container {
    max-width: 850px;
    margin: auto;
}

.user-message {
    background-color: #2f2f2f;
    padding: 15px 20px;
    border-radius: 18px;
    margin: 15px 0;
}

.ai-message {
    padding: 15px 20px;
    margin: 15px 0;
}

.avatar {
    font-size: 25px;
    margin-right: 12px;
}

.title {
    text-align: center;
    font-size: 32px;
    font-weight: 600;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# SESSION STATE
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# SIDEBAR
# -----------------------------

with st.sidebar:

    st.title("🤖 My AI")

    if st.button(
        "＋ New Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.subheader("Chats")

    st.button(
        "💬 Python Project",
        use_container_width=True
    )

    st.button(
        "💬 ML Roadmap",
        use_container_width=True
    )

    st.button(
        "💬 Pandas Help",
        use_container_width=True
    )

    st.divider()

    model = st.selectbox(
        "Model",
        [
            "My AI Model",
            "Llama",
            "Mistral",
            "Gemma"
        ]
    )

    temperature = st.slider(
        "Temperature",
        0.0,
        2.0,
        0.7
    )

    uploaded_file = st.file_uploader(
        "Upload file",
        type=[
            "pdf",
            "txt",
            "csv",
            "docx"
        ]
    )


# -----------------------------
# MAIN CHAT AREA
# -----------------------------

st.markdown(
    '<div class="chat-container">',
    unsafe_allow_html=True
)

if len(st.session_state.messages) == 0:

    st.markdown(
        '<div class="title">How can I help you?</div>',
        unsafe_allow_html=True
    )

else:

    for message in st.session_state.messages:

        role = message["role"]
        content = message["content"]

        if role == "user":

            st.markdown(
                f"""
                <div class="user-message">
                    <span class="avatar">👤</span>
                    {content}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
                <div class="ai-message">
                    <span class="avatar">🤖</span>
                    {content}
                </div>
                """,
                unsafe_allow_html=True
            )


# -----------------------------
# CHAT INPUT
# -----------------------------

prompt = st.chat_input(
    "Message My AI..."
)

if prompt:

    # Store user message

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    st.rerun()


st.markdown(
    "</div>",
    unsafe_allow_html=True
)