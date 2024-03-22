# Bert-Based-Question-Answering

This is a question answering application based on the BERT model. Users can input a context and a question, and the model will generate an answer based on the context.

## Usage

1. Install dependencies:

    ```bash
    pip install torch transformers gradio
    ```

2. Run the application:

    ```bash
    python app.py
    ```

3. Once the application is running, open the provided URL in your web browser. You can then enter the context and question to get the model's response.

## Example Interactions

The application comes preloaded with some example interactions. Here are a few examples:

- **Context**: "The capital of France is Paris."
  - **Question**: "What is the capital of France?"
  - **Expected Response**: "Paris"

- **Context**: "Water boils at 100 degrees Celsius or 212 degrees Fahrenheit."
  - **Question**: "At what temperature does water boil?"
  - **Expected Response**: "100 degrees Celsius"

- **Context**: "The Mona Lisa was painted by Leonardo da Vinci."
  - **Question**: "Who painted the Mona Lisa?"
  - **Expected Response**: "Leonardo da Vinci"

## Interface Customization

The interface is customizable and includes styling for a better user experience. You can further customize it by modifying the code in `app.py`.

## Author

Developed by [Ajeetkumar Ukande](https://github.com/Ajeetkumar-Ukande).
