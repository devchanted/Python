import openai
from flask import Flask, request, jsonify

openai.api_key = ''  # Replace with your OpenAI API key

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    
    response = openai.Completion.create(
        model="gpt-4o",  # You can also use the latest available model
        prompt=user_input,
        max_tokens=150
    )
    
    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)