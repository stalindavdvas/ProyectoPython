import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    word_count = None
    if request.method == "POST":
        text = request.form["text"]
        word_count = len(text.split())
    return render_template("index.html", word_count=word_count)

if __name__ == "__main__":
    # Railway asigna el puerto en la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))  # Usa el puerto que asigna Railway o el puerto 5000 por defecto
    app.run(host="0.0.0.0", port=port)  # Asegúrate de que Flask escuche en 0.0.0.0
