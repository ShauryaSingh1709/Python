import google.generativeai as genai

# Replace with your Gemini API key from AI Studio
genai.configure(api_key="AIzaSyDGgdOuFui2yhHiYSYYXYHXWu35EGJEdyY")

# ✅ Use one of your available models
model = genai.GenerativeModel("gemini-2.5-flash")   # or "gemini-2.5-flash" for faster replies

chat = model.start_chat(history=[])

print("\n💬 Gemini Terminal Chat (Gemini 2.5)")
print("Type 'exit' or 'quit' to end.\n")

while True:
    msg = input("You: ")
    if msg.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    try:
        response = chat.send_message(msg)
        print("Gemini:", response.text.strip(), "\n")
    except Exception as e:
        print("⚠️ Error:", e, "\n")