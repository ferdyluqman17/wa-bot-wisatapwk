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
        sub_msg = input("Anda memilih Wisata. Silakan pilih jenis wisata yang ingin kamu ketahui:\n1. Wisata Alam\n2. Wisata Religi\n3. Wisata Buatan")
        
        if sub_msg.lower() == "wisata alam":
            # Lakukan sesuatu untuk opsi wisata alam
            alam_msg = input("Anda memilih Wisata Alam. Silakan pilih opsi berikutnya:\n1. Tempat Wisata Alam A\n2. Tempat Wisata Alam B\n3. Tempat Wisata Alam C")
            if alam_msg == "1":
                response = "Anda memilih Tempat Wisata Alam A. Berikut informasinya..."
            elif alam_msg == "2":
                response = "Anda memilih Tempat Wisata Alam B. Berikut informasinya..."
            elif alam_msg == "3":
                response = "Anda memilih Tempat Wisata Alam C. Berikut informasinya..."
            else:
                response = "Maaf, pilihan Tempat Wisata Alam tidak valid."
        elif sub_msg.lower() == "wisata religi":
            # Lakukan sesuatu untuk opsi wisata religi
            response = "Anda memilih Wisata Religi."
        elif sub_msg.lower() == "wisata buatan":
            # Lakukan sesuatu untuk opsi wisata buatan
            response = "Anda memilih Wisata Buatan."
        else:
            response = "Maaf, pilihan jenis wisata tidak valid."

    else:
        response = "Maaf, saya tidak mengerti pesan Anda. Silakan ulangi."

    resp = MessagingResponse()
    resp.message(response)
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
