# ============================================================
# PROJECT 1: Rule-Based AI Chatbot (Streamlit Enhanced Version)
# Internship: DecodeLabs AI Track | Batch 2026
# Developer: Muhammad Yasin
# ============================================================

import streamlit as st
import random
import time
from datetime import datetime

# ------------------------------------------------------------
# KNOWLEDGE BASE — Dictionary of rules
# ------------------------------------------------------------
responses = {
    "hello": ["Hello! How can I help you today?",
              "Hey there! What's on your mind?",
              "Hi! Great to see you."],
    "hi": ["Hi! How are you doing?",
           "Hello! What can I do for you?"],
    "hey": ["Hey! How can I assist you?"],

    "what is your name": ["My name is DecoBot — your rule-based AI assistant!"],
    "who are you": ["I'm DecoBot, built by Muhammad Yasin at DecodeLabs."],
    "who made you": ["I was built by Muhammad Yasin as part of the DecodeLabs AI Internship."],

    "how are you": ["I'm just code, but I'm running perfectly — thanks for asking!",
                    "All systems operational! How about you?"],

    "what is ai": ["AI stands for Artificial Intelligence — it means teaching machines to simulate human thinking."],
    "what is python": ["Python is a beginner-friendly programming language widely used in AI and data science."],
    "what is a chatbot": ["A chatbot is a program that simulates conversation with humans using rules or AI models."],

    "what is decodelabs": ["DecodeLabs is an AI training organization that helps students build real-world AI projects."],
    "tell me about this project": ["This is Project 1 of the DecodeLabs AI Internship — a Rule-Based Chatbot built with pure Python logic!"],

    "tell me a joke": ["Why do programmers prefer dark mode? Because light attracts bugs! 😄",
                       "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads. 😂"],
    "what can you do": ["I can answer questions, tell jokes, and have simple conversations — all with pure Python logic!"],
    "are you smart": ["I follow rules very precisely — which is a kind of intelligence!"],

    "motivate me": ["Every expert was once a beginner. Keep building, Yasin!",
                    "The best time to start was yesterday. The second best time is now. Code on!"],

    "bye": ["Goodbye! Keep coding and stay awesome!"],
    "goodbye": ["See you later! All the best with your internship!"],
    "see you": ["Take care! Come back anytime."],
}

EXIT_COMMANDS = ["exit", "quit", "close", "bye", "goodbye", "stop"]

# ------------------------------------------------------------
# Helper Functions
# ------------------------------------------------------------
def get_time_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "🌅 Good morning"
    elif hour < 17:
        return "☀️ Good afternoon"
    elif hour < 21:
        return "🌆 Good evening"
    else:
        return "🌙 Good night"

def sanitize(text):
    return text.lower().strip().rstrip("!?.,")

def get_response(user_input):
    matched_responses = responses.get(user_input, None)
    if matched_responses:
        return random.choice(matched_responses)
    else:
        fallbacks = [
            "I'm not sure about that yet. Try asking something else!",
            "Hmm, I don't have a rule for that. Can you rephrase?",
            "That's beyond my current knowledge base. I'm still learning!",
        ]
        return random.choice(fallbacks)

# Chat bubble styling
def chat_bubble(message, role="assistant"):
    if role == "user":
        st.markdown(
            f"<div style='background:#2E86C1; padding:10px; border-radius:10px; color:white; margin:5px 0;'>{message}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='background:#27AE60; padding:10px; border-radius:10px; color:white; margin:5px 0;'>{message}</div>",
            unsafe_allow_html=True
        )

# Typing effect for bot replies
def typing_effect(text):
    placeholder = st.empty()
    displayed = ""
    for char in text:
        displayed += char
        placeholder.markdown(
            f"<div style='background:#27AE60; padding:10px; border-radius:10px; color:white;'>{displayed}</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.02)

# ------------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------------
st.set_page_config(page_title="DecoBot Chatbot", page_icon="🤖")

# Custom header
st.markdown("<h1 style='text-align:center; color:#FF4B4B;'>🤖 DecoBot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Rule-Based AI Chatbot | DecodeLabs Internship 2026</p>", unsafe_allow_html=True)

# Sidebar info
st.sidebar.title("About DecoBot")
st.sidebar.info("Built by Muhammad Yasin during DecodeLabs AI Internship 2026.")
st.sidebar.success("Tip: Try asking me about AI, Python, or tell me to motivate you!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add greeting at start
    greeting = get_time_greeting()
    st.session_state.messages.append({"role": "assistant", "content": f"{greeting}! I'm DecoBot. Type 'exit' to quit."})

# Display chat history
for msg in st.session_state.messages:
    chat_bubble(msg["content"], role=msg["role"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    # Show user message
    chat_bubble(prompt, role="user")
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Process input
    clean = sanitize(prompt)

    if clean in EXIT_COMMANDS:
        reply = "Goodbye! It was great chatting with you. Keep coding! 🚀"
        typing_effect(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
    else:
        reply = get_response(clean)
        typing_effect(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
