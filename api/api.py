from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer

app = Flask(__name__)


# Load MarianMT model
model_name = "/Users/patrikhrabanek/PycharmProjects/cooking/czech_model"  # Change this to your model
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

@app.route('/translate', methods=['GET'])
def translate():
    source_text = request.args.get("text", "")  # Get the text to translate
    source_lang = request.args.get("source", "")  # Source language
    target_lang = request.args.get("target", "")  # Target language

    if not source_text:
        return jsonify({"error": "No text provided"}), 400

    inputs = tokenizer(source_text, return_tensors="pt", padding=True)
    outputs = model.generate(**inputs)
    translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"translation": translation})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
