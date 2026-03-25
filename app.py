from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import os

# mpesa imports
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
CORS(app)

# =========================
# CONFIG
# =========================
app.config["UPLOAD_FOLDER"] = "static/images"

# Ensure folder exists
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])

# =========================
# DB CONNECTION (FIXED)
# =========================
def connect_db():
    return pymysql.connect(
        host="mysql-bensontekes.alwaysdata.net",  # 🔥 CHANGE if different
        user="bensontekes",
        password="modcom1234",
        database="bensontekes_dailybite",
        cursorclass=pymysql.cursors.DictCursor
    )

# =========================
# HOME ROUTE
# =========================
@app.route("/")
def home():
    return "Daily Bite Backend Running 🚀"

# =========================
# SIGNUP
# =========================
@app.route("/api/signup", methods=["POST"])
def signup():
    conn = None
    try:
        username = request.form.get("username")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")

        conn = connect_db()
        cursor = conn.cursor()

        sql = "INSERT INTO users(username,email,phone,password) VALUES(%s,%s,%s,%s)"
        cursor.execute(sql, (username, email, phone, password))
        conn.commit()

        return jsonify({"message": "User registered successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})

    finally:
        if conn:
            conn.close()

# =========================
# SIGNIN
# =========================
@app.route("/api/signin", methods=["POST"])
def signin():
    conn = None
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        conn = connect_db()
        cursor = conn.cursor()

        sql = "SELECT * FROM users WHERE email=%s AND password=%s"
        cursor.execute(sql, (email, password))

        if cursor.rowcount == 0:
            return jsonify({"message": "Login failed"})
        else:
            user = cursor.fetchone()
            return jsonify({"message": "Login successful", "user": user})

    except Exception as e:
        return jsonify({"error": str(e)})

    finally:
        if conn:
            conn.close()

# =========================
# ADD PRODUCT (FIXED)
# =========================
@app.route("/api/add_product", methods=["POST"])
def add_product():
    conn = None
    try:
        product_name = request.form.get("product_name")
        product_description = request.form.get("product_description")
        product_cost = request.form.get("product_cost")
        product_photo = request.files.get("product_photo")

        if not product_photo:
            return jsonify({"error": "No image uploaded"})

        filename = product_photo.filename
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)

        product_photo.save(filepath)

        conn = connect_db()
        cursor = conn.cursor()

        sql = """
        INSERT INTO products(product_name, product_description, product_cost, product_photo)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (product_name, product_description, product_cost, filename))
        conn.commit()

        return jsonify({"message": "Product added successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})

    finally:
        if conn:
            conn.close()

# =========================
# GET PRODUCTS
# =========================
@app.route("/api/get_products", methods=["GET"])
def get_products():
    conn = None
    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        return jsonify(products)

    except Exception as e:
        return jsonify({"error": str(e)})

    finally:
        if conn:
            conn.close()

# =========================
# MPESA PAYMENT
# =========================
@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    try:
        amount = request.form['amount']
        phone = request.form['phone']

        consumer_key = "YOUR_CONSUMER_KEY"
        consumer_secret = "YOUR_CONSUMER_SECRET"

        # get access token
        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        access_token = "Bearer " + r.json()['access_token']

        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        passkey = "YOUR_PASSKEY"
        business_short_code = "174379"

        data = business_short_code + passkey + timestamp
        password = base64.b64encode(data.encode()).decode('utf-8')

        payload = {
            "BusinessShortCode": business_short_code,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/api/confirmation.php",
            "AccountReference": "Daily Bite",
            "TransactionDesc": "Payment"
        }

        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

        requests.post(url, json=payload, headers=headers)

        return jsonify({"message": "Check your phone to complete payment"})

    except Exception as e:
        return jsonify({"error": str(e)})

# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)