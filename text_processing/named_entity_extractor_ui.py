import gradio as gr

from named_entity_extractor import extract_named_entities

interface = gr.Interface(fn=extract_named_entities,
                         inputs=[gr.Textbox(lines=10, placeholder="Enter text to extract named entities"),
                                 gr.Textbox(lines=2, placeholder="Enter named entities to extract")],
                         outputs=gr.Textbox(label="Named Entities"),
                         title="AI-Powered Named Entity Extractor",
                         description="Enter a text and get the named entities."
                         )

if __name__ == "__main__":
    interface.launch()
