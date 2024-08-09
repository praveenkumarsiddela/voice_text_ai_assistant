# app.py
from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Initialize the chatbot model
chatbot = pipeline("text-generation", model="deepset/roberta-base-squad2") 

def get_response(text):
    prompt = f"Respond to the following message in a helpful and informative manner:\n\n{text}"
    result = chatbot(prompt, max_length=100, num_return_sequences=1, temperature=0.7)
    return result[0]['generated_text']

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        print(f"Received user input: {user_input}")

        if user_input:
            try:
                response = get_response(user_input)
                print(f"API response: {response}")
                return render_template("index.html", user_input=user_input, response=response)
            except Exception as e:
                print(f"Error occurred: {e}")
                return render_template("index.html", user_input=user_input, response="An error occurred.")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
