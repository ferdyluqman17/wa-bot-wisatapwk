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
            alam_msg = input("Anda memilih Wisata Alam. Silakan pilih opsi berikutnya:\n1. Grama Tirta Jatiluhur\n2. Desa Wisata Kampung Tajur\n3. Gunung Parang\n4. Gunung Bangkok\n5. Waduk Cirata\n6. Situ Wanayasa \n7. Curug Cipurut \n8. Ujung Aspal - Pasirmuncang \n9. Curug Cimata Indung \n10. Panarawangan Bukit Cinta \n11. Parang Gombong \n12. Gunung Lembu \n13. Leuwi Cidomas \n14. Kampung Sadang \n15. Curug Tilu \n16. Kampung Kahuripan \n17. Alam Sari Wates \n18. Ngaprak River Adventure \n19. Saung Manglid \n20. Taman Batu Mata Air Cijanun \n21. Sasak Panyawangan \n22. Skylodge Padjajaran Anyar \n23. Hidden Valley Hills  \n24. Bungursari Lake Park \n25. Gunung Cupu")
            if alam_msg == "1":
                response = "Anda memilih Tempat Wisata Alam A. Berikut informasinya..."
            elif alam_msg == "2":
                response = "Anda memilih Tempat Wisata Alam B. Berikut informasinya..."
            elif alam_msg == "3":
                response = "Anda memilih Tempat Wisata Alam C. Berikut informasinya..."
            else:
                response = "Maaf, pilihan Tempat Wisata Alam tidak valid."
        
        elif sub_msg.lower() == "wisata religi":
            religi_msg = input("Anda memilih Wisata Religi. Silakan pilih opsi:\n1. Tempat Wisata Religi A\n2. Tempat Wisata Religi B\n3. Tempat Wisata Religi C")
            if religi_msg == "1":
                response = "Anda memilih Tempat Wisata Religi A. Berikut informasinya..."
            elif religi_msg == "2":
                response = "Anda memilih Tempat Wisata Religi B. Berikut informasinya..."
            elif religi_msg == "3":
                response = "Anda memilih Tempat Wisata Religi C. Berikut informasinya..."
            else:
                response = "Maaf, pilihan Tempat Wisata Religi tidak valid."
        
        elif sub_msg.lower() == "wisata buatan":
            buatan_msg = input("Anda memilih Wisata Buatan. Silakan pilih opsi:\n1. Tempat Wisata Buatan A\n2. Tempat Wisata Buatan B\n3. Tempat Wisata Buatan C")
            if buatan_msg == "1":
                response = "Anda memilih Tempat Wisata Buatan A. Berikut informasinya..."
            elif buatan_msg == "2":
                response = "Anda memilih Tempat Wisata Buatan B. Berikut informasinya..."
            elif buatan_msg == "3":
                response = "Anda memilih Tempat Wisata Buatan C. Berikut informasinya..."
            else:
                response = "Maaf, pilihan Tempat Wisata Buatan tidak valid."
        
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
