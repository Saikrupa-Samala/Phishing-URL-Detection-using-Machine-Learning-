from flask import Flask, render_template, request

from prediction import predict_url
from database import save_prediction, get_connection

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    confidence = None

    if request.method == "POST":

        url = request.form["url"]

        result, confidence, features = predict_url(url)

        save_prediction(
            url,
            result,
            confidence,
            features
        )

    return render_template(
        "index.html",
        result=result,
        confidence=confidence
    )


@app.route("/history")
def history():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM predictions
        ORDER BY created_at DESC
        LIMIT 100
    """)

    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "history.html",
        records=records
    )


if __name__ == "__main__":
    app.run(debug=True)
