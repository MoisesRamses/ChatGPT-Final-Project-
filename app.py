import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "What follows is a conversation with an artificial intelligence assistant. The assistant is helpful, creative, intelligent and very nice.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>Personal ChatGPT for GPT Certified Developer. Project by Moises Jauregui</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)
