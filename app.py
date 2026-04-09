import streamlit as st
import time
import random

st.set_page_config(
    page_title="AI Study Chat",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
/* App background */
.stApp {
    background-color: #343541;
    color: #ECECF1;
}

/* Main content area */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 900px;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 800;
    color: #ECECF1;
    margin-bottom: 0.25rem;
}

.sub-title {
    text-align: center;
    font-size: 1.1rem;
    color: #B4B7C5;
    margin-bottom: 2rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #202123;
}

section[data-testid="stSidebar"] * {
    color: #ECECF1 !important;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    border: 1px solid #565869;
    background-color: #40414F;
    color: #ECECF1;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #4b4d5c;
    border-color: #6b6d7a;
}

/* Chat message containers */
[data-testid="stChatMessage"] {
    border-radius: 16px;
    padding: 0.8rem 1rem;
    margin-bottom: 1rem;
}

/* User message */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background-color: #444654;
    border: 1px solid #565869;
}

/* Assistant message */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background-color: #3a3b47;
    border: 1px solid #4e5160;
}

/* Input box */
[data-testid="stChatInput"] {
    position: sticky;
    bottom: 0;
    background-color: #343541;
    padding-top: 0.75rem;
}

/* Divider text */
.small-note {
    font-size: 0.9rem;
    color: #B4B7C5;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🤖 AI Study Chat</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">A ChatGPT-style study assistant built with Streamlit</div>',
    unsafe_allow_html=True
)

with st.sidebar:
    st.markdown("## ⚙️ Options")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.last_topic = None
        st.rerun()

    st.markdown("---")
    st.markdown("### 💡 Try asking:")
    st.markdown("- What is food?")
    st.markdown("- What are nutrients?")
    st.markdown("- What is Python?")
    st.markdown("- What is AI?")
    st.markdown("- What is machine learning?")
    st.markdown("- What is data science?")
    st.markdown("- Give me study tips")
    st.markdown("- Tell me more")
    st.markdown("- Explain")
    st.markdown("---")
    st.caption("Built by Siya 🚀")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_topic" not in st.session_state:
    st.session_state.last_topic = None


def get_topic_response(topic, mode="basic"):
    data = {
        "ai": {
            "basic": "AI allows machines to learn, think, and make decisions like humans.",
            "more": "AI includes areas like machine learning, natural language processing, robotics, and computer vision.",
            "explain": "Artificial intelligence means making computers perform tasks that usually require human intelligence, such as understanding language, recognizing images, and solving problems."
        },
        "python": {
            "basic": "Python is a programming language used for web development, automation, AI, and data science.",
            "more": "Python is popular because it is easy to read and has powerful libraries like NumPy, Pandas, and TensorFlow.",
            "explain": "Python is a language used to give instructions to a computer. It is beginner-friendly and widely used in software development and artificial intelligence."
        },
        "machine learning": {
            "basic": "Machine learning is a branch of AI that helps computers learn from data.",
            "more": "It is used in spam filters, fraud detection, recommendation systems, and image recognition.",
            "explain": "Machine learning teaches computers to find patterns in data so they can make predictions or decisions without being manually programmed for every case."
        },
        "data science": {
            "basic": "Data science is the study of data to find useful patterns and insights.",
            "more": "It combines programming, statistics, and visualization to solve real-world problems.",
            "explain": "Data science involves collecting, analyzing, and interpreting data to help people make better decisions."
        },
        "food": {
            "basic": "Food is any substance eaten to provide energy and nourishment.",
            "more": "Food gives the body energy, helps growth, and keeps the body healthy.",
            "explain": "Food is what living things eat to survive, grow, and stay healthy. It contains nutrients the body needs to function properly."
        },
        "nutrients": {
            "basic": "Nutrients are substances in food that the body needs.",
            "more": "These include carbohydrates, proteins, fats, vitamins, minerals, and water.",
            "explain": "Nutrients are important components in food that help the body grow, repair itself, and maintain proper health."
        },
        "study": {
            "basic": "Good study habits include planning, practicing, and taking breaks.",
            "more": "Use active recall, spaced repetition, and practice questions to improve memory.",
            "explain": "Studying effectively means understanding concepts, testing yourself, and reviewing regularly instead of only rereading notes."
        }
    }

    return data.get(topic, {}).get(mode, "I'm not sure about that yet.")


def detect_topic(question):
    q = question.lower().strip()

    if "machine learning" in q:
        return "machine learning"
    if "data science" in q:
        return "data science"
    if "python" in q:
        return "python"
    if "artificial intelligence" in q or q == "ai" or "what is ai" in q:
        return "ai"
    if "food" in q or "nutrition" in q or "eat" in q:
        return "food"
    if "nutrient" in q:
        return "nutrients"
    if "study" in q or "exam" in q or "revise" in q or "revision" in q:
        return "study"
    return None


def get_response(user_input):
    question = user_input.lower().strip()

    if any(word in question for word in ["hi", "hello", "hey"]):
        return "Hello 👋 I’m your AI Study Chat assistant. Ask me about Python, AI, food, nutrients, machine learning, data science, or study tips."

    topic = detect_topic(question)

    if topic:
        st.session_state.last_topic = topic
        return get_topic_response(topic, "basic")

    if any(phrase in question for phrase in ["tell me more", "give me more", "more", "go on"]):
        if st.session_state.last_topic:
            return get_topic_response(st.session_state.last_topic, "more")
        return "Tell me the topic you want more about 😊"

    if any(word in question for word in ["explain", "why", "how"]):
        if st.session_state.last_topic:
            return get_topic_response(st.session_state.last_topic, "explain")
        return "Please tell me what you want explained 😊"

    if any(word in question for word in ["add", "subtract", "multiply", "divide"]):
        return "It sounds like you’re asking about math. Give me a specific example like 12 + 8."

    if "who are you" in question:
        return "I am a simple AI-style study assistant built with Python and Streamlit."

    fallback_responses = [
        f"I’m not fully trained on '{user_input}' yet 🤖 Try asking about AI, Python, food, machine learning, data science, or study tips.",
        "That’s interesting 👀 I can help better with science, technology, and study questions.",
        "I’m still learning that topic 😅 Try asking about Python, AI, nutrients, or exams."
    ]
    return random.choice(fallback_responses)


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_input = st.chat_input("Message AI Study Chat...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_response(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""

        for char in response:
            full_response += char
            placeholder.markdown(full_response + "▌")
            time.sleep(0.008)

        placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": response})