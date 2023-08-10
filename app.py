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
        response = "Halo! Silakan pilih yang ingin kamu ketahui:\n1. Wisata\n\n2. Hotel\n3. Oleh-Oleh Khas"
    elif incoming_msg == "wisata":
        response = "Anda memilih Wisata. Silakan pilih jenis wisata yang ingin kamu ketahui:\n1. Wisata Alam\n2. Wisata Religi\n3. Wisata Buatan"   
    elif incoming_msg == "wisata alam":
        response = "Anda memilih Wisata Alam. Silakan pilih opsi berikutnya:\n1. Grama Tirta Jatiluhur\n2. Desa Wisata Kampung Tajur\n3. Gunung Parang\n4. Gunung Bangkok\n5. Waduk Cirata\n6. Situ Wanayasa \n7. Curug Cipurut \n8. Ujung Aspal - Pasirmuncang \n9. Curug Cimata Indung \n10. Panarawangan Bukit Cinta \n11. Parang Gombong \n12. Gunung Lembu \n13. Leuwi Cidomas \n14. Kampung Sadang \n15. Curug Tilu \n16. Kampung Kahuripan \n17. Alam Sari Wates \n18. Ngaprak River Adventure \n19. Saung Manglid \n20. Taman Batu Mata Air Cijanun \n21. Sasak Panyawangan \n22. Skylodge Padjajaran Anyar \n23. Hidden Valley Hills  \n24. Bungursari Lake Park \n25. Gunung Cupu"
    elif incoming_msg == "1":
        response = "Anda memilih Grama Tirta Jatiluhur \n1. Deskripsi Wisata :\n2. Grama Tirta Jatiluhur merupakan kawasan yang menyajikan wisata serba air dari berperahu, selancar, kolam renang, hotel/penginapan, outbond, berkemah, hingga wisata kuliner. Dalam wilayah wisata Grama Tirta Jatiluhur, waduk jatiluhur berada. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/goADwYNqPqs36XAw9 \n5. HTM :  \n6. harga tiket masuk Grama Tirta Jatiluhur adalah Rp27,500.00. Sementara saat weekend, harga tiket masuk Grama Tirta Jatiluhur adalah Rp30,000.00 \n7. Waktu Buka/Tutup : \n8. setiap hari jam 08.00 - 17.00 \n9. Kontak \n10. (0264) 201087 \n11. Alternatif kontak \n12. - \n13. Ini adalah akhir cabang."
    elif incoming_msg == "2":
        response = "Anda memilih Desa Wisata Kampung Tajur \n1. Deskripsi Wisata :\n2. Kampung Tajur dijadikan sebagai kampung wisata oleh Pemerintah Kabupaten Purwakarta. dirintis antara tahun 2002-2003, dan diresmikan sebagai kampung wisata dengan mencirikan dan menonjolkan adat istiadat dan kearifan lokal pada tahun 2004. jauh sebelum dijadikan Kampung wisata dan dikenal banyak orang dengan kampung yang mempertahankan adat kesundaan dan kearifan lokalnya, Kampung Tajur ternyata sudah ada sejak lama. bahkan ratusan tahun silam. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/rYFpsvmVGzHvruJb9 \n5. HTM :  \n6. tiket masuk dan menginap 6-8 orang 250.000/orang ; biaya makan 17.000-25.000/porsi \n7. Waktu Buka/Tutup : \n8. setiap hari 24 jam \n9. Kontak \n10. 087778614788 \n11. Alternatif kontak \n12. https://www.instagram.com/nusaena.tajur/ \n13. Ini adalah akhir cabang."
    elif incoming_msg == "3":
        response = "Anda memilih Gunung Parang \n1. Deskripsi Wisata :\n2. Gunung setinggi 963 m dengan 3 puncak batu vulkanis terjal yang populer di kalangan pemanjat tebing. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/5AwdKQAER5u1W8fr9\n5. HTM :  \n6. Harga tiket (jalur biasa) 10.000/orang ; harga tiket jalur ferrata 100 meter 100.000/orang, 300 meter 150.000/orang, 750 meter 465.000/orang ; harga tiket jalur taraje berbentuk paket mulai dari 150.000-750.000 per orang \n7. Waktu Buka/Tutup : \n8. setiap hari 24 jam \n9. Fasilitas \n10. Area parkir, toilet, warung makanan dan minuman, penyewaan alat, guide \n11. Kontak \n12. 087770851010 \n13. Alternatif kontak \n12.  https://www.instagram.com/parangviaferrata/?hl=id \n13. Ini adalah akhir cabang."

    elif incoming_msg == "wisata religi":
        response = "Anda memilih Wisata Religi. Silakan pilih opsi berikutnya:\n1. Makam Syech Ba'ing Yusuf \n2. Makam Mama Sempur \n3. Makam Eyang Pandita Tajur & Sekitarnya \n4. Makam Eyang Gandasoli."
    elif incoming_msg == "1":
        response = "Anda memilih Makam Syech Ba'ing Yusuf \n1. Deskripsi Wisata :\n2. Makam Syech Baing Yusuf berlokasi di pusat kota, tepatnya di belakang Masjid Agung Baing Yusuf Purwakarta. Berdasarkan cerita berkembang, Syech Baing Yusuf merupakan salah satu tokoh sejarah yang menyebarkan Islam di Purwakarta. Beliau merupakan guru Syech Nawawi Al Bantani ulama Indonesia yang menjadi Imam di Masjidil Haram. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/gg4kUMTavUtMoT3w5 \n5. HTM :  \n6. Gratis \n7. Waktu Buka/Tutup : \n8.  setiap hari 24 jam \n9. Kontak \n10. - \n11. Alternatif kontak \n12. - \n13. Ini adalah akhir cabang."
    elif incoming_msg == "2":
        response = "Anda memilih Makam Mama Sempur\n1. Deskripsi Wisata :\n2. Makam Mama Sempur berlokasi di Desa Sempur, Kecamatan Plered. Nama lengkapnya adalah KH Tubagus Ahmad Bakri bin KH Tubagus Syeda bin KH Tubagus Arsyad. Mama Sempur adalah salah satu tokoh muslim di Purwakarta yang menyebarkan agama Islam. Beliau saat ini dikenal sebagai Mama Sempur. Dia mendapat garis layak dari Keraton Banten (Istana Banten), diambil dari garis layak KH Tubagus Arsyad dari Keraton Banten. Di akhir setiap Dzulqaidah (11 bulan tahun Hijriah), di tempat itu selalu diadakan Haulan, sebuah peristiwa untuk mengingat wafatnya Mama Sempur. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/odzmWtxeaf4xscZs8 \n5. HTM :  \n6. Gratis \n7. Waktu Buka/Tutup : \n8.  setiap hari 24 jam \n9. Kontak \n10. - \n11. Alternatif kontak \n12. - \n13. Ini adalah akhir cabang."
    elif incoming_msg == "3":
        response = "Anda memilih Makam Eyang Pandita Tajur & Sekitarnya \n1. Deskripsi Wisata :\n2. Oleh masyarakat setempat Eyang Pandita dipercaya sebagai sesepuh Desa Pasanggrahan. Keunikan dari makam ini adalah lokasinya yang berada di atas bukit, sehingga dapat terlihat pemandangan gunung Burangrang, area pesawahan, perkebunan sayur warga, dan kawasan hutan.  \n3. Lokasi Wisata :\n4. https://goo.gl/maps/iVe5jrfPX8mZNU8C6 \n5. HTM :  \n6. Gratis \n7. Waktu Buka/Tutup : \n8.  setiap hari 24 jam \n9. Kontak \n10. 083149397123 \n11. Alternatif kontak \n12. - \n13. Ini adalah akhir cabang."

    elif incoming_msg == "wisata buatan":
        response = "Anda memilih Wisata Buatan. Silakan pilih opsi berikutnya:\n1. Taman Sribaduga \n2. Taman Surawisesa \n3. Taman Pancawarna \n4. Taman Pasanggrahan Pajajaran \n5. Taman Maya Datar \n6. Bale Panyawangan Diorama Nusantara \n7 Workshop Litbang Keramik \n8. Kolam Renang Giri Tirta \n9. Kolam Renang Cihanjawar \n10. Kolam Tjek Tse Long \n11. Jaya Tirta Abadi Waterboom \n12. Bale Indung Rahayu \n13. Galeri Wayang \n14. Kuya Maranggi Waterpark \n15. Taman Pancaniti \n16. Taman Parcom \n17. Taman Citra Resmi \n18. Taman Pembaharuan \n19. Green Valley Water Park \n20. Kolam Renang Cisabuk \n21. Kolam Renang Tajur Indah \n22. Castle Lampion \n23. Cikao Park \n24. Tirta Kahuripan Wanayasa \n25. Kolam Renang Ciloa \n26. Batu Apung Alam Hijau \n27.  Kolam Renang Pusaka Water Park \n28. Kolam Renang Babakan Jati."
    elif incoming_msg == "1":
        response = "Anda memilih Taman Sribaduga \n1. Deskripsi Wisata :\n2. Taman Air Mancur Sri Baduga adalah sebuah destinasi liburan yang lokasinya berada di Alun-Alun Purwakarta, Jawa Barat. Obyek wisata ini menyajikan atraksi air menari yang dilengkap dengan lampu warna warni yang cantik dan memukau. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/ctuHLjE6tCY6o1at5 \n5. HTM :  \n6. Gratis \n7. Waktu Buka/Tutup : \n8. Area Sekitar Taman Dibuka. Namun untuk pertunjukan Air Mancur jadwalnya tidak menentu karena masalah debit air yang turun. \n9. Fasilitas \n10. Tempat parkir kendaraan, Toilet, Mushola, Warung makan, Gazebo, Tempat duduk wisata \n11. Kontak \n12  \n13. Alternatif kontak \n14. - \n15. Ini adalah akhir cabang."
    elif incoming_msg == "2":
        response = "Anda memilih Taman Surawisesa \n1. Deskripsi Wisata :\n2. Taman edukasi untuk anak-anak dengan berbagai fasilitas, seperti layar besar berisi film edukatif bertema sosial, teropong bintang hingga air mancur mini. Dihadirkan pula permainan tradisional seperti egrang, songlah, congklak, lompat tali, panggal (gasing dari kayu), kelerang dan lainnya. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/G3LrER9jD9oaP6dL7 \n5. HTM :  \n6. Gratis \n7. Waktu Buka/Tutup : \n8.  Jumat (Malam Sabtu) \n9. Fasilitas \n10. Layar besar berisi film edukatif bertema sosial, teropong bintang hingga air mancur mini. \n11. Kontak \n12 - \n13. Alternatif kontak \n14. - \n15. Ini adalah akhir cabang."
    elif incoming_msg == "3":
        response = "Anda memilih Taman Pancawarna \n1. Deskripsi Wisata :\n2. Obyek Wisata Taman Pancawarna di Purwakarta Jawa Barat sangat cocok untuk mengisi kegiatan liburan anda, apalagi saat liburan panjang seperti libur nasional, ataupun hari ibur lainnya. Keindahan Obyek Wisata Taman Pancawarna di Purwakarta Jawa Barat ini sangatlah baik bagi anda semua yang berada di dekat atau di kejauhan untuk merapat mengunjungi tempat Obyek Wisata Taman Pancawarna di Purwakarta Jawa Barat di kota purwakarta. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/c3Q9eZVa9UHiQX3H9 \n5. HTM :  \n6. Gratis \n7. Waktu Buka/Tutup : \n8.  08.00 - 18.00 WIB \n9. Kontak \n10. - \n11. Alternatif kontak \n12. - \n13. Ini adalah akhir cabang."

    else:
        response = "Maaf, saya tidak mengerti pesan Anda. Silakan ulangi."

    resp = MessagingResponse()
    resp.message(response)
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
