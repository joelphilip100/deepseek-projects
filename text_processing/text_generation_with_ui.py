import gradio as gr

from text_generation import generate_text


interface = gr.Interface(
    fn=generate_text,
    inputs=[gr.Textbox(lines=5, placeholder="Enter your prompt"),
            gr.Slider(minimum=50, maximum=500, step=50, label="Word Limit"),
            gr.Dropdown(choices=["English", "Hindi", "Spanish"], label="Language")
            ],
    outputs=gr.Textbox(label="Generated Text"),
    title="AI-Powered Text Generator",
    description="Enter a prompt and get a generated text based on it."
)

if __name__ == '__main__':
    interface.launch()
