from flask import Flask,render_template,request
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

@app.route("/success/<int:score>",methods=["GET"])
def success(score):
    return "<h2>person has passed with score "+str(score)+"</h2>"

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template("form.html")
    else:
        maths=float(request.form["maths"])
        science=float(request.form["science"])
        kannada=float(request.form["kannada"])
        print("Maths value:", maths)
        print("Maths type:", type(maths))

        print("Science value:", science)
        print("Science type:", type(science))

        print("Kannada value:", kannada)
        print("Kannada type:", type(kannada))
    average_marks=(maths+science+kannada)/3
    return render_template("form.html",average_marks=average_marks,
                            maths=maths,
                            science=science,
                            kannada=kannada)


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )