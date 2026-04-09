import streamlit as st
import time
import random

st.set_page_config(page_title="AI Study Chat", page_icon="🤖", layout="centered")

st.title("🤖 AI Study Chat")
st.caption("A smarter AI-style study assistant built with Streamlit")

with st.sidebar:
    st.header("⚙️ Options")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.last_topic = None
        st.rerun()

    st.markdown("### 💡 Try asking:")
    st.markdown("- What is food?")
    st.markdown("- What are nutrients?")
    st.markdown("- What is Python?")
    st.markdown("- What is AI?")
    st.markdown("- What is machine learning?")
    st.markdown("- What is data science?")
    st.markdown("- Give me study tips")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "last_topic" not in st.session_state:
    st.session_state.last_topic = None


def get_topic_response(topic, mode="basic"):
    if topic == "ai":
        if mode == "more":
            return "AI includes areas like machine learning, natural language processing, robotics, and computer vision."
        elif mode == "explain":
            return "Artificial intelligence means making computers do tasks that usually need human thinking, like understanding language, recognizing images, or making decisions."
        return "AI allows machines to learn, think, and make decisions like humans."

    elif topic == "python":
        if mode == "more":
            return "Python is popular because it is simple to read and has powerful libraries for web development, automation, data science, and AI."
        elif mode == "explain":
            return "Python is a computer language people use to write programs. It is beginner-friendly and very useful in many fields."
        return "Python is a programming language used for web development, automation, AI, and data science."

    elif topic == "machine learning":
        if mode == "more":
            return "Machine learning is used in spam filters, recommendation systems, fraud detection, and image recognition."
        elif mode == "explain":
            return "Machine learning teaches computers to learn patterns from data so they can make predictions or decisions without being manually programmed for every case."
        return "Machine learning is a branch of AI that helps computers learn from data."

    elif topic == "data science":
        if mode == "more":
            return "Data science combines programming, statistics, and visualization to analyze data and discover useful insights."
        elif mode == "explain":
            return "Data science is the process of collecting and studying data to answer questions and solve problems."
        return "Data science is the study of data to find useful patterns and insights."

    elif topic == "food":
        if mode == "more":
            return "Food gives the body energy and nutrients needed for growth, repair, and health."
        elif mode == "explain":
            return "Food is what living things eat to stay alive, grow, and get energy."
        return "Food is any substance eaten to give the body energy and nourishment."

    elif topic == "nutrients":
        if mode == "more":
            return "Main nutrients include carbohydrates, proteins, fats, vitamins, minerals, and water. Each has a different job in the body."
        elif mode == "explain":
            return "Nutrients are useful substances in food that help your body grow, stay healthy, and work properly."
        return "Nutrients are substances in food that the body needs for energy, growth, and repair."

    elif topic == "study":
        if mode == "more":
            return "You can improve studying by using active recall, spaced repetition, practicing past questions, and avoiding distractions."
        elif mode == "explain":
            return "Good study habits mean learning in a focused way, reviewing often, and testing yourself instead of only rereading notes."
        return "Good study habits include using a timetable, studying in short focused sessions, practicing questions, taking breaks, and reviewing regularly."

    return "I'm not sure about that yet."


def detect_topic(question):
    q = question.lower().strip()

    if "machine learning" in q:
        return "machine learning"
    if "data science" in q:
        return "data science"
    if "python" in q:
        return "python"
    if "artificial intelligence" in q or q == "ai" or "what is ai" in q or "what is artificial intelligence" in q:
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

user_input = st.chat_input("Ask me something...")

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
            time.sleep(0.01)

        placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": response})