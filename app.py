import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

# Konfigurasi Twilio
account_sid = 'ACeefb17cb7a7f55d21b6a807bd5ab1a5b'
auth_token = 'c7229d70867cba9f9c34792b452bd800'
client = Client(account_sid, auth_token)

@app.route("/")
def home():
    return "Selamat datang di aplikasi Flask!"

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").lower()
    response = ""

    if incoming_msg == "halo":
        response = "Halo! Silakan pilih yang ingin kamu ketahui:\n1. Wisata\n2. Hotel\n3. Oleh-Oleh Khas"
    elif incoming_msg.lower() == "wisata":
        response = "Anda memilih Wisata. Silakan pilih jenis wisata yang ingin kamu ketahui:\n1. Wisata Alam\n2. Wisata Religi\n3. Wisata Buatan"
    elif incoming_msg.lower() == "hotel":
        response = "Anda memilih Hotel. Silakan pilih informasi yang ingin kamu ketahui:\n1. Hotel Bintang 5\n2. Hotel Bintang 4\n3. Hotel Bintang 3"
    elif incoming_msg.lower() == "oleh-oleh khas":
        response = "Anda memilih Oleh-Oleh Khas. Silakan pilih jenis oleh-oleh yang ingin kamu ketahui:\n1. Makanan Khas\n2. Barang Khas"
    else:
        response = "Maaf, saya tidak mengerti pesan Anda. Silakan ulangi."

    resp = MessagingResponse()
    resp.message(response)
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
