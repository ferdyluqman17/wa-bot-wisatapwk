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
        while True:  # Loop untuk menu wisata
            print("Anda memilih Wisata. Silakan pilih jenis wisata yang ingin kamu ketahui:")
            print("1. Wisata Alam\n2. Wisata Religi\n3. Wisata Buatan\n0. Kembali ke Menu Utama")
            sub_msg = input("Pilihan Anda: ")
            
            if sub_msg == "1":
                while True:  # Loop untuk menu wisata alam
                    print("Anda memilih Wisata Alam. Silakan pilih opsi:")
                    print("1. Tempat Wisata Alam A\n2. Tempat Wisata Alam B\n3. Tempat Wisata Alam C\n0. Kembali ke Menu Wisata Alam")
                    alam_msg = input("Pilihan Anda: ")
                    if alam_msg == "1":
                        response = "Anda memilih Tempat Wisata Alam A. Berikut informasinya..."
                    elif alam_msg == "2":
                        response = "Anda memilih Tempat Wisata Alam B. Berikut informasinya..."
                    elif alam_msg == "3":
                        response = "Anda memilih Tempat Wisata Alam C. Berikut informasinya..."
                    elif alam_msg == "0":
                        break  # Kembali ke menu wisata
                    else:
                        response = "Maaf, pilihan Tempat Wisata Alam tidak valid."

            elif sub_msg == "2":
                # Implementasi untuk Wisata Religi
                pass

            elif sub_msg == "3":
                # Implementasi untuk Wisata Buatan
                pass

            elif sub_msg == "0":
                break  # Kembali ke menu utama
            
            else:
                response = "Maaf, pilihan jenis wisata tidak valid."

    # ... (sisa kode untuk hotel dan oleh-oleh khas)
    else:
        response = "Maaf, saya tidak mengerti pesan Anda. Silakan ulangi."

    resp = MessagingResponse()
    resp.message(response)
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
