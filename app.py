from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def process_message():
    try:
        data = request.get_json()
        user_message = data['message']

        # Send the user's message to OpenAI API for processing
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=50  # Adjust the max tokens based on your needs
        )

        # Get the generated response from OpenAI API
        ai_response = response['choices'][0]['text']

        # Return the response as JSON
        return jsonify({'message': ai_response})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
