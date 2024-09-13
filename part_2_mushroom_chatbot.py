"""A mushroom expert chatbot that responds to user queries about mushrooms.
"""
import gradio as gr
import random

def response(inputs, history):
    if "hello" in inputs["text"].lower():
        return "Hello! I am a mushroom expert. Ask me anything about mushrooms."
    elif "bye" in inputs["text"].lower():
        return "Goodbye! Have a great day."
    else:
        return random.choice([
            "I am not sure about that. Can you ask me something else?",
            "Could you reformulate your question? I am not sure I understand.",
            "I don't understand, can you ask someone else?",
            "What a stellar question! I am not sure about the answer though."
            "You know what? I am not cut out for this. I am going to take a break."
        ])

with gr.Blocks(fill_height=True) as demo:
    chatbot = gr.ChatInterface(
        fn=response,
        title="🍄 Your Personal Mushroom Expert 🍄‍🟫",
    )

if __name__ == "__main__":
    demo.launch()
