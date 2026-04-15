from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Python pyörii Sinisessä Amazonissa! | 15.4.2026 integraation testaus"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)