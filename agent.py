def agent_step(user_input):
    intent = detect_intent(user_input)

    if intent == "pricing":
        docs = retrieve(user_input)
        return docs[0].page_content

    elif intent == "high_intent":
        return "collect_lead"

    return "fallback"