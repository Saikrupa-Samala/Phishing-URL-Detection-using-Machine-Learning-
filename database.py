import mysql.connector


def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="saikrupa",
        database="phishing_detection"
    )


def save_prediction(
    url,
    prediction,
    confidence,
    features
):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
        INSERT INTO predictions (
            url,
            prediction,
            confidence,
            url_length,
            domain_length,
            num_dots,
            num_hyphens,
            num_slashes,
            num_at,
            num_question,
            num_equals,
            has_https,
            has_ip,
            suspicious_words
        )
        VALUES (
            %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s,
            %s, %s
        )
    """

    values = (
        url,
        prediction,
        confidence,
        features["url_length"],
        features["domain_length"],
        features["num_dots"],
        features["num_hyphens"],
        features["num_slashes"],
        features["num_at"],
        features["num_question"],
        features["num_equals"],
        features["has_https"],
        features["has_ip"],
        features["suspicious_words"]
    )

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()
