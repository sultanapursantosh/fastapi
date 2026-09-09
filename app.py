from flask import Flask, render_template, request, jsonify
import logging
import os

app = Flask(__name__)

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


@app.route("/")
def home():

    logger.debug("Entered home() function")
    logger.info("Home page requested")
    logger.warning("This is a warning example")

    return "hello world"


@app.route("/success/<int:score>", methods=["GET"])
def success(score):
    return "<h2>person has passed with score " + str(score) + "</h2>"


# Your existing HTML form
@app.route("/form", methods=["GET", "POST"])
def form():

    if request.method == "GET":
        return render_template("form.html")
    else:
        maths = float(request.form["maths"])
        science = float(request.form["science"])
        kannada = float(request.form["kannada"])

        logger.debug("Entered forms function")
        logger.info("forms page requested")
        logger.warning("This is a warning example")

        average_marks = (maths + science + kannada) / 3

        return render_template(
            "form.html",
            average_marks=average_marks,
            maths=maths,
            science=science,
            kannada=kannada
        )


# New JSON API
@app.route("/api/calculate", methods=["POST"])
def calculate():

    data = request.get_json()

    print("Received JSON:", data)
    print("Data type:", type(data))

    maths = float(data["maths"])
    science = float(data["science"])
    kannada = float(data["kannada"])

    average_marks = (maths + science + kannada) / 3

    return jsonify({
        "maths": maths,
        "science": science,
        "kannada": kannada,
        "average": average_marks
    })


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )