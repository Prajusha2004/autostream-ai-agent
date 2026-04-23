import json

# ===== Load Knowledge Base =====
with open("knowledge_base.json") as f:
    KB = json.load(f)

# ===== State =====
state = {
    "intent": None,
    "lead_stage": None,  # None, collecting_name, collecting_email, collecting_platform
    "lead_data": {}
}

# ===== Tool =====
def mock_lead_capture(name, email, platform):
    print(f"\n✅ Lead captured successfully: {name}, {email}, {platform}\n")

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
        f"\n📦 Pricing:\n"
        f"- Basic: {basic['price']} → {', '.join(basic['features'])}\n"
        f"- Pro: {pro['price']} → {', '.join(pro['features'])}\n"
    )

# ===== Lead Flow Handler =====
def handle_lead_flow(user_input):
    if state["lead_stage"] == "collect_name":
        state["lead_data"]["name"] = user_input
        state["lead_stage"] = "collect_email"
        return "Got it. What's your email?"

    elif state["lead_stage"] == "collect_email":
        state["lead_data"]["email"] = user_input
        state["lead_stage"] = "collect_platform"
        return "Nice. Which platform do you create content on? (YouTube/Instagram)"

    elif state["lead_stage"] == "collect_platform":
        state["lead_data"]["platform"] = user_input

        data = state["lead_data"]

        # TOOL EXECUTION (only here, not before)
        mock_lead_capture(data["name"], data["email"], data["platform"])

        # Reset
        state["lead_stage"] = None
        state["lead_data"] = {}

        return "You're all set. We'll reach out shortly 🚀"

    return None

# ===== Main Chat =====
def chat():
    print("🤖 AutoStream Agent Live\n(type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        # If we are collecting lead info → bypass intent detection
        if state["lead_stage"]:
            response = handle_lead_flow(user_input)
            print("Agent:", response)
            continue

        intent = detect_intent(user_input)
        state["intent"] = intent

        # ===== Responses =====
        if intent == "greeting":
            print("Agent: Hey. Ask something useful.")

        elif intent == "pricing":
            print("Agent:", get_pricing())

        elif intent == "high_intent":
            print("Agent: Good, someone decisive for once.")
            print("Agent: Let's get you started.")

            state["lead_stage"] = "collect_name"
            print("Agent: What's your name?")

        else:
            print("Agent: That didn't help me help you. Try asking about pricing or plans.")

# ===== Run =====
if __name__ == "__main__":
    chat()