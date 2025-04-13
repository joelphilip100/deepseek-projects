import gradio as gr

from grammar_check import check_grammar

interface = gr.Interface(fn=check_grammar,
                         inputs=gr.Textbox(lines=10, placeholder="Enter text to check grammar"),
                         outputs=gr.Textbox(label="Corrected Text"),
                         title="AI-Powered Grammar Checker",
                         description="Enter a text and get the grammar corrected.")


if __name__ == "__main__":
    interface.launch()
