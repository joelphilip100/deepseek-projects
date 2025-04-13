import gradio as gr

from sentimental_analysis import analyze_sentiment

interface = gr.Interface(fn=analyze_sentiment,
                         inputs=gr.Textbox(lines=10, placeholder="Enter text to analyze sentiment"),
                         outputs=gr.Textbox(label="Sentiment"),
                         description="Enter a text and get the sentiment.",
                         title="AI-Powered Sentimental Analysis")

if __name__ == "__main__":
    interface.launch()
