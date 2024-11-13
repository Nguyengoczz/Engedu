from flask import Flask, request, jsonify
from rasa.core.agent import Agent
from rasa.shared.core.interpreter import RasaNLUInterpreter

app = Flask(__name__)

# Load Rasa model
agent = Agent.load('models', interpreter=RasaNLUInterpreter())

@app.route("/webhooks/rasa/webhook", methods=["POST"])
def rasa_webhook():
    user_message = request.json.get("message")
    responses = agent.handle_text(user_message)
    return jsonify({"responses": responses})

if __name__ == "__main__":
    app.run(debug=True)
