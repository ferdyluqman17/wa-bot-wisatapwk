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
        
    elif sub_msg.lower() == "wisata alam":
        alam_msg = input("Anda memilih Wisata Alam. Silakan pilih opsi berikutnya:\n1. Grama Tirta Jatiluhur\n2. Desa Wisata Kampung Tajur\n3. Gunung Parang\n4. Gunung Bangkok\n5. Waduk Cirata\n6. Situ Wanayasa \n7. Curug Cipurut \n8. Ujung Aspal - Pasirmuncang \n9. Curug Cimata Indung \n10. Panarawangan Bukit Cinta \n11. Parang Gombong \n12. Gunung Lembu \n13. Leuwi Cidomas \n14. Kampung Sadang \n15. Curug Tilu \n16. Kampung Kahuripan \n17. Alam Sari Wates \n18. Ngaprak River Adventure \n19. Saung Manglid \n20. Taman Batu Mata Air Cijanun \n21. Sasak Panyawangan \n22. Skylodge Padjajaran Anyar \n23. Hidden Valley Hills  \n24. Bungursari Lake Park \n25. Gunung Cupu")
        if alam_msg == "Grama Tirta Jatiluhur":
            response = "Anda memilih Grama Tirta Jatiluhur \n1. Deskripsi Wisata :\n2. Grama Tirta Jatiluhur merupakan kawasan yang menyajikan wisata serba air dari berperahu, selancar, kolam renang, hotel/penginapan, outbond, berkemah, hingga wisata kuliner. Dalam wilayah wisata Grama Tirta Jatiluhur, waduk jatiluhur berada. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/goADwYNqPqs36XAw9 \n5. HTM :  \n6. harga tiket masuk Grama Tirta Jatiluhur adalah Rp27,500.00. Sementara saat weekend, harga tiket masuk Grama Tirta Jatiluhur adalah Rp30,000.00 \n7. Waktu Buka/Tutup : \n8. setiap hari jam 08.00 - 17.00 \n9. Kontak \n10. (0264) 201087 \n11. Alternatif kontak \n12. - \n13. Ini adalah akhir cabang."
        elif alam_msg == "Desa Wisata Kampung Tajur":
            response = "Anda memilih Desa Wisata Kampung Tajur \n1. Deskripsi Wisata :\n2. Kampung Tajur dijadikan sebagai kampung wisata oleh Pemerintah Kabupaten Purwakarta. dirintis antara tahun 2002-2003, dan diresmikan sebagai kampung wisata dengan mencirikan dan menonjolkan adat istiadat dan kearifan lokal pada tahun 2004. jauh sebelum dijadikan Kampung wisata dan dikenal banyak orang dengan kampung yang mempertahankan adat kesundaan dan kearifan lokalnya, Kampung Tajur ternyata sudah ada sejak lama. bahkan ratusan tahun silam. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/rYFpsvmVGzHvruJb9 \n5. HTM :  \n6. tiket masuk dan menginap 6-8 orang 250.000/orang ; biaya makan 17.000-25.000/porsi \n7. Waktu Buka/Tutup : \n8. setiap hari 24 jam \n9. Kontak \n10. 087778614788 \n11. Alternatif kontak \n12. https://www.instagram.com/nusaena.tajur/ \n13. Ini adalah akhir cabang."
        elif alam_msg == "Gunung Parang":
            response = "Anda memilih Gunung Parang \n1. Deskripsi Wisata :\n2. Gunung setinggi 963 m dengan 3 puncak batu vulkanis terjal yang populer di kalangan pemanjat tebing. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/5AwdKQAER5u1W8fr9\n5. HTM :  \n6. Harga tiket (jalur biasa) 10.000/orang ; harga tiket jalur ferrata 100 meter 100.000/orang, 300 meter 150.000/orang, 750 meter 465.000/orang ; harga tiket jalur taraje berbentuk paket mulai dari 150.000-750.000 per orang \n7. Waktu Buka/Tutup : \n8. setiap hari 24 jam \n9. Fasilitas \n10. Area parkir, toilet, warung makanan dan minuman, penyewaan alat, guide \n11. Kontak \n12. 087770851010 \n13. Alternatif kontak \n12.  https://www.instagram.com/parangviaferrata/?hl=id \n13. Ini adalah akhir cabang."
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
        response = "Maaf, saya tidak mengerti pesan Anda. Silakan ulangi."

    resp = MessagingResponse()
    resp.message(response)
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
