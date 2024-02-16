import gradio as gr
from transformers import pipeline

#Calling the pipeline for text generation
generator = pipeline('text-generation', model='FloVolo/mistral-flo-finetune-2-T4')

def generation_text(text):
    return generator(text, max_length=250, do_sample=False)[0]['generated_text']


demo = gr.Interface(
    fn=generation_text,
    inputs=["text"],
    outputs=["text"],
)

demo.launch()
