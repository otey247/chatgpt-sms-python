# ChatGPT-SMS: An OpenAI Assistant on SMS powered by Twilio

This is a guide to set up a Python Flask app that uses the OpenAI GPT model to create an AI assistant that communicates over SMS using Twilio.

## Requirements

You will need:

- Python installed in your local machine.
- [Twilio](https://www.twilio.com/) account for SMS integration.
- [ngrok](https://ngrok.com/) for making your local server publicly accessible.
- [OpenAI](https://openai.com/) account to access the GPT models.

## Setup

1. Clone the repository to your local machine:

    ```bash
    git clone <your-repo-url>
    ```

2. Navigate to your project's root directory:

    ```bash
    cd chatgpt-sms-python
    ```

3. Set up a virtual environment and activate it:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

4. Install the necessary dependencies:

    ```bash
    pip install openai twilio flask python-dotenv
    ```

5. Create a `.env` file in your project's root directory and enter the following line of text, making sure to replace `<YOUR-OPENAI-KEY>` with your actual key:

    ```bash
    OPENAI_API_KEY= <YOUR-OPENAI-KEY>
    ```

## Making your app visible to the web

1. Install ngrok and expose your application:

    ```bash
    ngrok http 5000
    ```

    This should be done in a new terminal tab and the directory your code is in.

2. Grab the ngrok Forwarding URL that looks something like this: `http://<your-ngrok-id>.ngrok.io`

## Twilio setup

1. Go to your [Twilio Console](https://www.twilio.com/console).
2. Under Active Numbers, scroll to the Messaging section.
3. Modify the phone number’s routing by pasting the ngrok URL followed by `/sms` in the textbox corresponding to when "A Message Comes In" and click save.

    For example, if your ngrok URL is `http://12345abc.ngrok.io`, you would enter `http://12345abc.ngrok.io/sms`.

## Running your app

1. Run your Python Flask app with the following command:

    ```bash
    python app.py
    ```

2. You can now text your new AI assistant using the Twilio number you have configured!

## Need Help?

If you run into issues, please file a bug report on the GitHub issue tracker. We're always happy to assist.

## License

This project is open source, under the MIT License.
