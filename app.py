from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

API_KEY = "AIzaSyAspGWS2HfUFuBLj43USvfit9sCLXgaXRE"

@app.route("/genai", methods=["POST"])
def generate_ai_response():
    genai.configure(api_key=API_KEY)


    # Récupérer le contenu du message de la requête POST
    data = request.get_json()
   

    content = request.json.get('content')
    # Utiliser l'API Generative AI pour générer le contenu
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(content)

    # Retourner la réponse sous forme de JSON
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)
