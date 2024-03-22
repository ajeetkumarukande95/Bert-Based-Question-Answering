from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import gradio as gr
import time

# Author information
author = "Ajeetkumar Ukande"

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")
model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad")
qa_pipe = pipeline("question-answering", model=model, tokenizer=tokenizer)

def response(context, question):
    result = qa_pipe(context=context, question=question)
    return result['answer']

input_context = gr.Textbox(lines=10, label='Input Context', placeholder='Enter context here...')
input_question = gr.Textbox(label='Input Question', placeholder='Ask your question here...')
output_text = gr.Textbox(label="Response", placeholder='Response will display here..')

interface = gr.Interface(response, inputs=[input_context, input_question], outputs=output_text,
                        title="<div style='color: #336699; font-size: 24px; font-weight: bold; border: 2px solid #336699; padding: 10px; border-radius: 10px;'>Bert Based Question Answering</div>",
                        description=f"""<div style='color: #666666; font-family: Arial, sans-serif;'>
                                        <p style='margin-top: 10px;'>Enter context and question to get the response.</p>
                                        <p>Developed by <span style='color: #336699; font-weight: bold;'>{author}</span>.</p>
                                        </div>""",
                        theme="default" # Change theme to default
                        )

# Define example contexts, questions, and expected responses
examples = [
    ["The capital of France is Paris.", "What is the capital of France?", "Paris"],
    ["Water boils at 100 degrees Celsius or 212 degrees Fahrenheit.", "At what temperature does water boil?", "100 degrees Celsius"],
    ["The Mona Lisa was painted by Leonardo da Vinci.", "Who painted the Mona Lisa?", "Leonardo da Vinci"],
]

def simulate_interaction():
    for example in examples:
        context, question, expected_response = example
        input_context.value = context
        input_question.value = question
        time.sleep(2)  # Simulating user typing delay
        response_text = response(context, question)
        output_text.value = response_text
        time.sleep(2)  # Simulating response delay

# Simulate user interaction
simulate_interaction()
# Deploy the interface
interface.launch(share=True, debug=True)
