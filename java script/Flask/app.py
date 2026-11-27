import json
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

mBASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICT_FILE = os.path.join(BASE_DIR, "dictionary.json")


def load_dictionary():
    if not os.path.exists(DICT_FILE):
        return {}
    with open(DICT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_dictionary(data):
    with open(DICT_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.route("/prime_number/<int:number>", methods=["GET"])
def prime_number(number):
    return jsonify({
        "Number": number,
        "isPrime": check_prime(number)
    })


@app.route("/translate/<string:word>", methods=["GET"])
def translate(word):
    dictionary = load_dictionary()
    lookup_word = word.lower()

    # Case-insensitive matching against dictionary keys
    for en_word, fi_word in dictionary.items():
        if en_word.lower() == lookup_word:
            return jsonify({
                "English": en_word,
                "Finnish": fi_word
            })

    return jsonify({"error": "Word not found"}), 404


@app.route("/words", methods=["GET"])
def get_words():
    dictionary = load_dictionary()
    return jsonify(list(dictionary.keys()))


@app.route("/add", methods=["GET", "POST"])
def add_word():
    en = request.args.get("en")
    fi = request.args.get("fi")

    if not en or not fi:
        return jsonify({"error": "Both 'en' and 'fi' query parameters are required"}), 400

    dictionary = load_dictionary()
    en_clean = en.strip().lower()
    fi_clean = fi.strip().lower()

    dictionary[en_clean] = fi_clean
    save_dictionary(dictionary)

    return jsonify({
        "message": "Word added successfully",
        "English": en_clean,
        "Finnish": fi_clean
    }), 201


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)