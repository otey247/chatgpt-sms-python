from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def chatgpt():
    inb_msg = request.form['Body'].lower()
    print(inb_msg)

    chat_model = "gpt-3.5-turbo"

    system_message = "This is an assistant that can answer your queries."
    
    response = openai.ChatCompletion.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": inb_msg},
        ],
        max_tokens=3000,
        temperature=0.7
    )
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()
    # Add a message
    resp.message(response['choices'][0]['message']['content'])
    print(response['choices'][0]['message']['content'])

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
