# AutoStream AI Agent 🎬

## Overview

AutoStream AI Agent is a conversational AI system designed to convert user interactions into qualified leads. It simulates a real-world SaaS assistant capable of understanding user intent, retrieving relevant product information, and triggering backend actions.

This project is built as part of the **ServiceHive – Inflx Agentic Workflow Assignment**.

---

## Features

* **Intent Detection**

  * Classifies user input into:

    * Greeting
    * Pricing Inquiry
    * High-Intent Lead

* **RAG-based Knowledge Retrieval**

  * Retrieves accurate responses from a local knowledge base
  * Covers pricing, features, and company policies

* **Lead Capture Workflow**

  * Detects high-intent users
  * Collects:

    * Name
    * Email
    * Platform (YouTube/Instagram)
  * Triggers a mock API only after complete data collection

* **Multi-turn Conversation Memory**

  * Maintains state across multiple interactions
  * Ensures structured flow for lead qualification

* **Interactive Dashboard (Streamlit)**

  * User-friendly chat interface
  * Real-time responses
  * Clear workflow visualization

---

## Tech Stack

* **Language:** Python 3.9+
* **Framework/UI:** Streamlit
* **Architecture:** State-based conversational agent
* **Knowledge Base:** Local JSON (RAG simulation)

---

## Project Structure

```
autostream-agent/
│
├── app.py                # CLI version of agent
├── streamlit_app.py     # Dashboard UI
├── knowledge_base.json  # RAG data source
├── requirements.txt
└── README.md
```

---

## How to Run

### 1. Clone Repository

```
git clone https://github.com/YOUR_USERNAME/autostream-ai-agent.git
cd autostream-ai-agent
```

### 2. Install Dependencies

```
pip install streamlit
```

### 3. Run Dashboard

```
streamlit run streamlit_app.py
```

---

## Agent Workflow

The system follows a structured pipeline:

```
User Input
   ↓
Intent Detection
   ↓
Knowledge Retrieval (RAG)
   ↓
Decision Logic
   ↓
Lead Qualification
   ↓
Tool Execution (Mock API)
```

---

## Example Flow

1. User asks about pricing
2. Agent retrieves and responds with plan details
3. User shows interest in Pro plan
4. Agent detects high intent
5. Agent collects user details
6. Lead is captured successfully

---

## WhatsApp Integration (Concept)

To integrate with WhatsApp:

* Use **WhatsApp Business API (via Twilio)**
* Set up a webhook using Flask/FastAPI
* Route incoming messages to the agent
* Send responses back via API
* Maintain session state per user for multi-turn conversations

---

## Demo

The demo showcases:

* Pricing query handling
* Intent detection
* Lead capture flow
* Successful tool execution

---

## Key Highlights

* Clean separation of logic and UI
* Controlled tool execution (no premature triggers)
* Simple but effective RAG implementation
* Designed to simulate real-world agent workflows

---

## Conclusion

This project demonstrates how conversational AI can go beyond chatbots to become actionable agents capable of driving business outcomes such as lead generation.

---