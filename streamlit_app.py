import streamlit as st
import json

# ===== Load Knowledge Base =====
with open("knowledge_base.json") as f:
    KB = json.load(f)

# ===== Session State =====
if "messages" not in st.session_state:
    st.session_state.messages = []

if "lead_stage" not in st.session_state:
    st.session_state.lead_stage = None

if "lead_data" not in st.session_state:
    st.session_state.lead_data = {}

# ===== Tool =====
def mock_lead_capture(name, email, platform):
    return f"✅ Lead captured: {name}, {email}, {platform}"

# ===== Intent Detection =====
def detect_intent(text):
    text = text.lower()
    if any(x in text for x in ["hi", "hello", "hey"]):
        return "greeting"
    if any(x in text for x in ["price", "pricing", "plan", "cost"]):
        return "pricing"
    if any(x in text for x in ["buy", "subscribe", "try", "want", "start"]):
        return "high_intent"
    return "general"

# ===== RAG =====
def get_pricing():
    basic = KB["pricing"]["basic"]
    pro = KB["pricing"]["pro"]

    return (
        f"📦 **Pricing**\n\n"
        f"**Basic**: {basic['price']} → {', '.join(basic['features'])}\n\n"
        f"**Pro**: {pro['price']} → {', '.join(pro['features'])}"
    )

# ===== Lead Flow =====
def handle_lead_flow(user_input):
    if st.session_state.lead_stage == "name":
        st.session_state.lead_data["name"] = user_input
        st.session_state.lead_stage = "email"
        return "What's your email?"

    elif st.session_state.lead_stage == "email":
        st.session_state.lead_data["email"] = user_input
        st.session_state.lead_stage = "platform"
        return "Which platform? (YouTube/Instagram)"

    elif st.session_state.lead_stage == "platform":
        st.session_state.lead_data["platform"] = user_input

        data = st.session_state.lead_data
        result = mock_lead_capture(data["name"], data["email"], data["platform"])

        # Reset
        st.session_state.lead_stage = None
        st.session_state.lead_data = {}

        return result

# ===== UI =====
st.set_page_config(page_title="AutoStream AI", layout="centered")

st.title("🎬 AutoStream AI Agent")
st.caption("Convert conversations into leads")

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
user_input = st.chat_input("Ask about pricing, plans, etc...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Handle lead flow first
    if st.session_state.lead_stage:
        response = handle_lead_flow(user_input)

    else:
        intent = detect_intent(user_input)

        if intent == "greeting":
            response = "Hey. Ask me something useful."

        elif intent == "pricing":
            response = get_pricing()

        elif intent == "high_intent":
            st.session_state.lead_stage = "name"
            response = "Nice. Let's get you started.\n\nWhat's your name?"

        else:
            response = "Ask about pricing or plans."

    # Show response
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)