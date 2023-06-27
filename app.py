import gradio as gr
import re



gradio_ui = gr.Interface(
    fn=inference,
    title="Form Understanding using LayoutLMv3 Multimodal Transformer ",
    description="Enter an image and get the annotated image with tags and a csv file for analysis",
    inputs=image,
    outputs=[
        gr.outputs.Textbox(label="Sentiment Label"),
        gr.outputs.Textbox(label="Sentiment Score"),
    ],
)
gr.Interface(
    fn=predict_input_image, 
    inputs=image, 
    outputs=label,
    interpretation='default').launch(debug='True')



gradio_ui.launch()