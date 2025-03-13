from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure Gemini API
GENAI_API_KEY = "AIzaSyBl9nRaQ5J1umEzU-o7y28ds9pymsNAiJA"  # Replace with your actual API key
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

@app.route("/")  # NEW: This makes Flask serve the chatbot page
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chatbot():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = model.generate_content(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)














# import google.generativeai as genai

# # Set up API key
# genai.configure(api_key="AIzaSyBl9nRaQ5J1umEzU-o7y28ds9pymsNAiJA")  # Replace with your actual key

# # Initialize model
# model = genai.GenerativeModel("gemini-1.5-flash")

# def chatbot_response(prompt):
#     response = model.generate_content(prompt)
#     return response.text  # Extract text from response

# # Test chatbot
# user_input = input("You: ")
# print("Bot:", chatbot_response(user_input))

