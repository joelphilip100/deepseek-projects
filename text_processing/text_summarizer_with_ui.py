import gradio as gr

from text_summarizer import summarize_text

interface = gr.Interface(fn=summarize_text, inputs=gr.Textbox(lines=10, placeholder="Enter text to summarize"),
                         outputs=gr.Textbox(label="Summarized Text"), title="AI-Powered Text Summarizer",
                         description="Enter a long text and get a summary with 3 interesting facts.")

if __name__ == "__main__":
    interface.launch()
