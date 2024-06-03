from flask import Blueprint, request, jsonify
from services.genai_service import ask_genai

genai_blueprint = Blueprint('genai_blueprint', __name__)

@genai_blueprint.route('/api/genai/ask', methods=['POST'])
def ask_question():
    question = request.json.get('question')
    if question:
        try:
            answer = ask_genai(question)
            if "error" in answer.lower():
                raise Exception(answer)
            return jsonify({"answer": answer}), 200
        except Exception as e:
            print(f"Error handling request: {e}")
            return jsonify({"error": str(e)}), 500
    return jsonify({"error": "No question provided"}), 400