
from flask import Flask,render_template,request,flash,request,jsonify
from pyaspeller import YandexSpeller

from flask_cors import CORS
from bot import chatbot

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=['POST'])
def ask():

    message = str(request.form['messageText'])
    print("Received Message :",message)
    # Handle the grammar correction
    speller = YandexSpeller()
    corrected_text = speller.spelled(message)

    print(corrected_text)
    
    print(f"User Input: {message}")
    print(f"Corrected Text: {corrected_text}")

    bot_response = chatbot(corrected_text) 
    print(f"Bot Response: {bot_response}")
    # print(bot_response)
    return jsonify({'status':'OK','answer':bot_response})


app.run(debug=True)