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

    if incoming_msg ==  "halo":
        response = "Halo! Silakan pilih yang ingin kamu ketahui:\n1. Wisata (code : wst) \n2. Hotel (code : htl) \n3. Oleh-Oleh Khas (code : ook) "

    elif incoming_msg == "wst":
        response = "Anda memilih Wisata. Silakan pilih jenis wisata yang ingin kamu ketahui\n1. Wisata Alam (code : wa) \n2. Wisata Religi(code : wr) \n3. Wisata Buatan (code : wb) " 
    
    elif incoming_msg == "wa":
        response = "Anda memilih Wisata Alam. Silakan pilih opsi berikutnya:\n1. Grama Tirta Jatiluhur (code : gtj) \n2. Desa Wisata Kampung Tajur(code : dwkt) \n3. Gunung Parang(code : gp) \n4. Gunung Bangkok(code : gb) \n5. Waduk Cirata(code : wc)\n6. Situ Wanayasa(code : sw)  \n7. Curug Cipurut (code : cct)  \n8. Ujung Aspal - Pasirmuncang(code : uap)  \n9. Curug Cimata Indung (code : cci) \n10. Panarawangan Bukit Cinta (code : pbc)  \n11. Parang Gombong (code : pg)  \n12. Gunung Lembu (code : gl) \n13. Leuwi Cidomas (code : lc)  \n14. Kampung Sadang(code : ks)  \n15. Curug Tilu (code : ct)  \n16. Kampung Kahuripan (code : kk)  \n17. Alam Sari Wates (code : asw)  \n18. Ngaprak River Adventure (code : nra)  \n19. Saung Manglid (code : sm)  \n20. Taman Batu Mata Air Cijanun (code : tbmac)  \n21. Sasak Panyawangan (code : sp)  \n22. Skylodge Padjajaran Anyar (code : spa)  \n23. Hidden Valley Hills (code : hvh)  \n24. Bungursari Lake Park (code : blp)  \n25. Gunung Cupu(code : gc) " 
    elif incoming_msg == "gtj":
        response = "Anda memilih Grama Tirta Jatiluhur \n Deskripsi Wisata :\n Grama Tirta Jatiluhur merupakan kawasan yang menyajikan wisata serba air dari berperahu, selancar, kolam renang, hotel/penginapan, outbond, berkemah, hingga wisata kuliner. Dalam wilayah wisata Grama Tirta Jatiluhur, waduk jatiluhur berada. \n\n Lokasi Wisata :\nhttps://goo.gl/maps/goADwYNqPqs36XAw9 \n\n HTM :  \n harga tiket masuk Grama Tirta Jatiluhur adalah Rp27,500.00. Sementara saat weekend, harga tiket masuk Grama Tirta Jatiluhur adalah Rp30,000.00 \n\n Waktu Buka/Tutup : \n setiap hari jam 08.00 - 17.00 \n\n Kontak \n (0264) 201087 \n\n Alternatif kontak \n - \n\n  Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "dwkt":
        response = "Anda memilih Desa Wisata Kampung Tajur \n\n Deskripsi Wisata :\n Kampung Tajur dijadikan sebagai kampung wisata oleh Pemerintah Kabupaten Purwakarta. dirintis antara tahun 2002-2003, dan diresmikan sebagai kampung wisata dengan mencirikan dan menonjolkan adat istiadat dan kearifan lokal pada tahun 2004. jauh sebelum dijadikan Kampung wisata dan dikenal banyak orang dengan kampung yang mempertahankan adat kesundaan dan kearifan lokalnya, Kampung Tajur ternyata sudah ada sejak lama. bahkan ratusan tahun silam. \n\n Lokasi Wisata :\n https://goo.gl/maps/rYFpsvmVGzHvruJb9 \n\n HTM :  \n tiket masuk dan menginap 6-8 orang 250.000/orang ; biaya makan 17.000-25.000/porsi \n\n Waktu Buka/Tutup : \n setiap hari 24 jam \n\n Kontak \n 087778614788 \n\n Alternatif kontak \n https://www.instagram.com/nusaena.tajur/ \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "gp":
        response = "Anda memilih Gunung Parang \n\n Deskripsi Wisata :\n Gunung setinggi 963 m dengan 3 puncak batu vulkanis terjal yang populer di kalangan pemanjat tebing. \n\n Lokasi Wisata :\n https://goo.gl/maps/5AwdKQAER5u1W8fr9\n\n HTM :  \n Harga tiket (jalur biasa) 10.000/orang ; harga tiket jalur ferrata 100 meter 100.000/orang, 300 meter 150.000/orang, 750 meter 465.000/orang ; harga tiket jalur taraje berbentuk paket mulai dari 150.000-750.000 per orang \n\n Waktu Buka/Tutup : \n setiap hari 24 jam \n\n Fasilitas \n Area parkir, toilet, warung makanan dan minuman, penyewaan alat, guide \n\n Kontak \n 087770851010 \n\n Alternatif kontak \n  https://www.instagram.com/parangviaferrata/?hl=id \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "gb":
        response = "Anda memilih Gunung Bangkok\n\n Deskripsi Wisata :\n Puncak berbatu dengan area berkemah & pemandangan luas ke danau & lembah berhutan dari puncak. \n\n Lokasi Wisata :\n https://goo.gl/maps/gYgpNC3Gw9peNzpX7 \n\n HTM :  \n Tiket masuk 12.000/orang ; parkir motor 5.000/motor ; parkir mobil 10.000/mobil ; sewa tenda atau saung 10.000 \n\n Waktu Buka/Tutup : \n setiap hari 24 jam \n\n Fasilitas \n Area parkir luas, toilet dan kamar mandi, musholla beserta perlengkapan shalat, warung makan dan minuman, jasa pemandu wisata, gazebo, arena outbond \n\n Kontak \n - \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "wc":
        response = "Anda memilih Waduk Cirata\n\n Deskripsi Wisata :\n  Bendungan besar untuk PLTA yang selesai tahun 1990-an ini populer untuk pemancingan air tawar & naik perahu.\n\n Lokasi Wisata :\n https://goo.gl/maps/Bo9PbenBKdf5zVPZ7 \n\n HTM :  \n harga tiket masuk Rp.3.000 untuk sepeda motor dan Rp.5.000 untuk mobil. \n\n Waktu Buka/Tutup : \n setiap hari 24 jam \n\n Fasilitas \n Tempat parkir kendaraan wisata, Warung-warung wisata, Toilet, Spot Foto Instagenic, Wahana permainan air dan adventure, Mushola, Penginapan, Gazebo, Perahu wisata \n\n Kontak \n - \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "sw":
        response = "Anda memilih Situ Wanayasa \n\n Deskripsi Wisata :\n Waduk buatan dan area rekreasi dengan kafe di tepi waduk dan penginapan standar, yang berlatar pegunungan. \n\n Lokasi Wisata :\n https://goo.gl/maps/BuyzT5BVBfX6TNeq8 \n\n HTM : \n Tiket Masuk Gratis ; Parkir Sepeda Motor Rp2.000/motor ; Parkir Mobil Rp5.000/mobil \n\n Waktu Buka/Tutup : \n setiap hari 24 jam \n\n Fasilitas \n Area parkir, toilet, Mushola \n\n Kontak \n - \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "cct":
        response = "Anda memilih Curug Cipurut \n\n Deskripsi Wisata :\n Curug Cipurut ini merupakan destinasi wisata alam yang berada di bawah kaki kaki Gunung Burangrang. Air di Curug ini sangat jernih dan bersih serta sangat asri karena berada ditengah hutan yang rindang. Wisata hits ini sering dijadikan tempat spot foto yang Instagramable, tempat kemah, kegiatan piknik bersama keluarga dan kegiatan outbond lainnya dapat Anda lakukan disini. \n\n Lokasi Wisata :\n https://goo.gl/maps/UVk9SFauV6Qgftms5 \n\n HTM :  \n Tiket Masuk Rp20.000 ; Parkir Sepeda Motor Rp1.000/motor ; Parkir Mobil Rp2.000/mobil \n\n Waktu Buka/Tutup : \n setiap hari jam 08.00 - 17.00 \n\n Fasilitas \n mushola, gazebo, area parkir kendaraan, area perkemahan, tempat sampah, pos penjagaan \n\n Kontak \n - \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "uap":
        response = "Anda memilih Ujung Aspal - Pasirmuncang \n\n Deskripsi Wisata :\n Ujung Aspal Purwakarta adalah wisata alam yang populer, dan hits di kalangan masyarakat, sekaligus menjadi rumah besar bagi goa bersejarah, serta air terjun yang cantik di Purwakarta. \n\n Lokasi Wisata :\n https://goo.gl/maps/2UW8RQXFtXyZPNBx8 \n\n HTM :  \n Tiket Masuk Wisata Rp10.000 ; Tiket Camping Rp20.000 ; Tiket Masuk Jembatan Gantung Rp10.000 ; Sewa Hammock Rp20.000 \n\n Waktu Buka/Tutup : \n setiap hari 24 jam \n\n Kontak \n https://www.instagram.com/ujungaspal_pasirmuncang/ \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "cci":
        response = "Anda memilih Curug Cimata Indung \n\n Deskripsi Wisata :\n Curug Cimata Indung di Kecamatan Sukasari, merupakan salah satu lokasi wisata yang menghadirkan aliran air terjun kecil yang indah di Kabupaten Purwakarta, Jawa Barat. Segarnya air pegunungan dan pemandangan alam, membuat para pengunjunganya terhipnotis sehingga betah berlama-lama menikmati keindahan Curug tersebut. Curug Cimata Indung atau dalam bahasa Indonesia curug air mata bunda ini, biasanya diminati wisatawan ketika musim panas.  Bukan hanya wisatawan lokal, para pelancong luar negeri juga tak jarang berkunjung ke sana. \n\n Lokasi Wisata :\n https://goo.gl/maps/3tf8LeyLYaLNhSyLA  \n\n HTM :  \n biaya masuk sukarela namun ada biaya parkir sebesar 5.000 \n\n Waktu Buka/Tutup : \n 07.00 - 17.00 WIB \n\n Kontak \n 087879777542 \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "pbc":
        response = "Anda memilih Panarawangan Bukit Cinta \n\n Deskripsi Wisata :\n Sesuai namanya, tempat wisata ini menyuguhkan suasana alam dari atas perbukitan yang didukung dengan beragam spot foto menarik sehingga bisa dibilang, konsep yang diusung adalah perpaduan antara wisata alam dengan sentuhan modern. Disana wisatawan tidak hanya bisa menikmati suasana alam saja, namun juga bisa hunting foto sepuasnya. \n\n Lokasi Wisata :\n https://goo.gl/maps/vyPBjBZ59BYtbVGb7  \n\n HTM :  \n 5.000/orang \n\n Waktu Buka/Tutup : \n setiap hari jam 08.00 - 21.00 \n\n Kontak \n - \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "pg":
        response = "Anda memilih Parang Gombong \n\n Deskripsi Wisata :\n Parang Gombong Purwakarta merupakan area lahan luas berumput hijau dengan pemandangan danau. Tempat tersebut sangat sejuk dan alami. Area wisata akan terasa agak panas pada siang hari dan sejuk pada malam hari. Panoram alam tersebut juga dapat menjadi spot selfie yang instagramable. \n\n Lokasi Wisata :\n https://goo.gl/maps/nxqDAa1XxqZJHkTB8 \n\n HTM :  \n Tiket Masuk 10.000/orang ; parkir motor 5.000/motor ; parkir mobil 10.000/mobil \n\n Waktu Buka/Tutup : \n setiap hari 24 jam \n\n Kontak \n https://www.instagram.com/paranggombong_pwk/ \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "gl":
        response = "Anda memilih Gunung Lembu \n\n Deskripsi Wisata :\n Gunung Lembu memiliki ketinggian 792 mdpl dengan jalur pendakian cukup menantang dan sebuah batu besar yang dijuluki dengan batu lembu sebagai puncaknya, dimana akan terlihat pemandangan waduk Jatiluhur yang berada persis di bawahnya. Saat petang, mulai terlihat kerlip lampu-lampu di Kota Purwakarta.  \n\n Lokasi Wisata :\n https://goo.gl/maps/hvhddVkArBAizf8R9 \n\n HTM :  \n Tiket Masuk 10.000/orang ; Tiket Parkir 5.000 \n\n Waktu Buka/Tutup : \n setiap hari 24 jam \n\n Kontak \n - \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "lc":
        response = "Anda memilih Leuwi Cidomas \n\n Deskripsi Wisata :\n Sebuah objek wisata alam yang menampilkan keindahan sungai. Bukan sembarang sungai di pedesaan, sungai yang satu ini memiliki pesona yang memikat banyak wisatawan. Salah satu pesonanya adalah warna airnya yang cantik, hijau kebiru-biruan. Suasana di sekitar sungai juga begitu damai dan asri. \n\n Lokasi Wisata :\n https://goo.gl/maps/GF6CTSkGrCjaU7sC6  \n\n HTM :  \n Gratis (Tapi Ada Biaya Parkir Seikhlasnya) \n\n Waktu Buka/Tutup : \n Tidak memiliki jam resmi namun disarankan datang saat cuaca cerah \n\n Kontak \n - \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "ks":
        response = "Anda memilih Kampung Sadang \n\n Deskripsi Wisata :\n Kampoeng Sadang merupakan kawasan wisata alam yang cocok buat kegiatan gathering komunitas, outbond sekolah, dan juga kegiatan lainnya yang memerlukan lahan luas. Kampoeng Sadang pun sangat pas digunakan untuk aktivitas family gathering atau kids adventure \n\n Lokasi Wisata :\n https://goo.gl/maps/xuBxBeBpRoQjYbQaA  \n\n HTM :  \n 35.000/orang \n\n Waktu Buka/Tutup : \n setiap hari kecuali senin jam 09.00 - 16.00 \n\n Kontak \n (0264) 8306621 \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "ct":
        response = "Anda memilih Curug Tilu \n\n Deskripsi Wisata :\n Curug Purwakarta merupakan sebuah curug atau air terjun yang ada di Purwakarta, meskipun cukup tersembunyi curug ini tak pernah sepi dari pengunjung. Curug yang satu ini masih asri dan alami, hal tersebut ditandai dengan masih rindangnya pepohonan yang ada di sekitar curug. Udara sejuk diiringi angin sepoi-sepoi serta suara air yang mengalir, menjadi alunan musik alam yang menenangkan. Maka tak heran jika Curug Tilu selalu ramai dikunjungi wisatawan, apalagi di akhir pekan banyak keluarga yang mengajak anak-anak untuk menghabiskan waktu bersama. \n\n Lokasi Wisata :\n https://goo.gl/maps/GF9arVPWswHquHBi7 \n\n HTM :  \n Tiket masuk: Rp. 7.500 ; Parkir: Rp. 5.000 ; Sewa pelampung: Rp. 5.000 \n\n Waktu Buka/Tutup : \n setiap hari jam 08.00 - 16.00 \n\n Kontak \n - \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "kk":
        response = "Anda memilih Kampung Kahuripan \n\n Deskripsi Wisata :\n Merupakan kawasan eduwisata pengenalan lingkungan dan budaya Sunda dengan fasilitas alat permainan khas Sunda, kesenian khas Sunda seperti Calung dan Angklung, hingga energi alternatif tenaga surya dan air. Terdapat juga spot taman bermain, saung-saung dan camping ground. \n\n Lokasi Wisata :\n https://goo.gl/maps/SZGYMvT9ZNQ8diKK6 \n\n HTM :  \n Tiket Masuk Weekday Rp18.000 ; Tiket Masuk Weekend Rp20.000 ; Tiket Masuk Kolam Renang Weekday Rp16.000 ; Tiket Masuk Kolam Renang Weekend Rp20.000 ; Harga Tiket Wahana Panahan Rp10.000 ; Outbound, Flying Fox, ATV, Soang-Soangan, Sepeda Layang, Sisingaan, Gerabah, Pertanian (Menangkap Ikan, Memandikan Kerbau) Rp20.000 \n\n Waktu Buka/Tutup : \n setiap hari jam 08.00 - 17.00 \n\n Fasilitas \n tempat parkir, toilet, musala, dan tempat cuci tangan. \n\n Kontak \n 0811164642 \n\n Alternatif kontak \n 087828474148 \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "asw":
        response = "Anda memilih Alam Sari Wates \n\n Deskripsi Wisata :\n Alam Sari Wates Adventure adalah wisata Purwakarta yang menyajikan beragam wahana wisata, hingga penginapan, dalam satu kawasan yang sama. \n\n Lokasi Wisata :\n https://goo.gl/maps/p3h57jXmgcTk2a5c9 \n\n HTM :  \n Photobooth Rp15.000 ; Waterboom Rp15.000 ; Mini Motocross/ATV Rp15.000 ; Flying Fox Rp10.000 ; Flying Fox Extreme Rp15.000 ; Playground/Taman Rp15.000 ; Waterball/Ban Rp5.000 ; Airwalk Rp10.000 ; Mandi bola Rp5.000 ; Skyswing Rp10.000 ; Tong Gandeng Rp10.000 ; Sepatu Roda Rp10.000 ; Tiket Terusan Rp35.000 || Suite Room 225.000 (permalam weekday) 300.000 (permalam weekend) ; Deluxe Room 175.000 (permalam weekday) 200.000 (permalam weekend) ; Deluxe AC Room 175.000 (permalam weekday) 200.000 (permalam weekend) ;  Deluxe AC Room 175.000 (permalam weekday) 200.000 (permalam weekend) ; Standard Room 140.000 (permalam weekday) 160.000 (permalam weekend) ; Guest House 750.000 (permalam weekday) 1.000.000 (permalam weekend) ; Family Room 450.000 (permalam weekday) 550.000 (permalam weekend) \n\n Waktu Buka/Tutup : \n Penginapan Buka 24 Jam \n\n Fasilitas \n Area parkir, Toilet, Mushola, Restoran, atau cafe, Spot foto, Wahana permainan, Taman, Kolam renang. \n\n Kontak \n (0264) 620123 \n\n Alternatif kontak \n 0811465650 \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "nra":
        response = "Anda memilih Ngaprak River Adventure  \n\n Deskripsi Wisata :\n Purwakarta memiliki surga tersembunyi bagi penikmat arum jeram, mengingat sensasinya dijamin sangat berbeda dan bisa bikin puas dan ketagihan. Wisata arum jeram ini bisa Anda temukan di Kampung Tanjaknangsi, Desa Raharja, Kecamatan Wanayasa, Kabupaten Purwakarta. Di tempat tersebut menawarkan sensasi susur sungai mengunakan ban dalam karet atau yang disebut dengan river tubing lewat pengelolaan wisata yang dikenal dengan nama Ngaprak River Adventure. BACA JUGA:  3 Destinasi Wisata di Pasuruan, Penasaran Nggak? Wisata arum jeram ini mengajak Anda menelusuri Sungai Ciherang sepanjang 5 kilometer dengan waktu tempuh selama 3 jam. \n\n Lokasi Wisata :\n https://goo.gl/maps/GpAKFirLihfNV2es6 \n\n HTM :  \n biaya sebesar Rp 120 ribu termasuk biaya makan dan dokumentasi serta angkutan mobil \n\n Waktu Buka/Tutup : \n setiap hari kecuali jumat jam 08.00 - 16.00 \n\n Kontak \n 081299260872 \n\n Alternatif kontak \n https://www.instagram.com/ngaprakriver/ \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "sm":
        response = "Anda memilih Saung Manglid \n\n Deskripsi Wisata :\n Saung Manglid ini merupakan sebuah kawasan agrowisata yang lengkap. Di dalamnya terdapat area kebun bunga berbagai jenis yang bisa Anda jadikan lokasi berfoto. Tidak hanya kebun atau taman bunga yang cantik, di berbagai area juga disediakan area yang memang digunakan khusus untuk berfoto. \n\n Lokasi Wisata :\n https://goo.gl/maps/9qd3Bvf5NFqSm5UG8 \n\n HTM :  \n 10.000/orang \n\n Waktu Buka/Tutup : \n setiap hari jam 09.00 - 21.00 \n\n Kontak \n 081211379491 \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "tbmac":
        response = "Anda memilih Taman Batu Mata Air Cijanun \n\n Deskripsi Wisata :\n Taman yang berada di di Kecamatan Bojong ini cocok buat Anda yang hobi berenang tanpa campuran bahan kimia di airnya. Karena di kolam ini sumber airnya berasal dari mata air pegunungan. Mata air di sini sangat jernih. Kedalamannya 3 meter. Kolam tersebut dimanfaatkan untuk kebutuhan penduduk sekitar. Kolam itu berada di area hijau. Pepohonan menghiasi sekitarnya. \n\n Lokasi Wisata :\n https://goo.gl/maps/7Sg1XjHewupXStks7  \n\n HTM :  \n 20.000/orang \n\n Waktu Buka/Tutup : \n setiap hari jam 08.00 - 17.00 \n\n Kontak \n 0811820101 \n\n Alternatif kontak \n https://www.instagram.com/tamanbatu.pwk/ \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "sp":
        response = "Anda memilih Sasak Panyawangan \n\n Deskripsi Wisata :\n Sasak Panyawangan Purwakarta merupakan sebuah destinasi wisata alam yang menyuguhkan pemandangan gunung batu. Wisata ini terapit di antara dua gunung batu dan dekat dengan bendungan yang legendaris, yakni Bendungan Jatiluhur. Ada beberapa wahana menarik yang bisa wisatawan explore di tempat ini. \n\n Lokasi Wisata :\n https://goo.gl/maps/XghbD3MUyr1vrf2N7 \n\n HTM :  \n 10.000/orang \n\n Waktu Buka/Tutup : \n setiap hari jam 08.00 - 16.00 \n\n Fasilitas \n Tempat parkir kendaraan wisatawan cukup luas, Pusat Informasi dan loket destinasi, Toilet umum, Mushola, Spot foto instagenic, Kolam renang, Gazebo, Wahana permainan seru, Camping ground, Outbond arena, Penginapan, Warung wisata \n\n Kontak \n12 081388078484 \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "spa":
        response = "Anda memilih Skylodge Padjajaran Anyar\n\n Deskripsi Wisata :\n Skylodge Padjajaran Anyar merupakan hotel gantung pertama di Indonesia yang disebut-sebut menyaingi hotel gantung di Peru yang terkenal. Bebeda dengan hotel lain yang dibangun di atas tanah, Skylodge Padjajaran Anyar berada 500 mdpl di atas tebing bebatuan Gunung Parang. \n\n Lokasi Wisata :\n https://goo.gl/maps/JiJGADJJqwpEEPs59 \n\n HTM :  \n Rp. 3.000.000 hingga Rp. 5.000.000/malam \n\n Waktu Buka/Tutup : \n setiap hari 24 jam \n\n Fasilitas \n 4 buah tempat tidur, toilet portable, listrik,  AC, TV, meja makan, wastafel, oven, handy talkie untuk berkomunikasi, tirai untuk penutup dinding kamar  hingga balkon dengan view Bendungan Jatiluhur. \n\n Kontak \n12 087874708230 \n\n Alternatif kontak \n - \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "hvh":
        response = "Anda memilih Grama Tirta Jatiluhur \n\n Deskripsi Wisata :\n Hidden Valley Hills adalah negeri dongeng di atas awan yang tercipta dari inspirasi ditemukannya tugu peninggalan zaman Belanda Anno 1898M di lokasi ini, yang terkait erat dengan G. Cupu dengan ketinggian yang sama 362 mdpl. \n\n Lokasi Wisata :\n https://goo.gl/maps/jaSb2WNpJ8z4hr64A \n\n HTM :  \n HTM Hidden Valley Hills Purwakarta sebesar Rp 35.000 per orang dan jika anda ingin renang akan dikenakan tarif sebesar Rp 25.000 per orang. \n\n Waktu Buka/Tutup : \n Setiap hari jam 08.00 - 19.00 \n\n Fasilitas \n Resort, Outdoor Event, Meeting Room dan juga terdapat Kolam Renang  \n\n Kontak \n12 085959672424 \n\n Alternatif kontak \n https://www.hiddenvalleyhills.com/ \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "blp":
        response = "Anda memilih Bungursari Lake Park \n\n Deskripsi Wisata :\n Bungursari Lake Park ini merupakan destinasi wisata alam yang juga menawarkan sisi edukasi pada para pengunjungnya. Di destinasi ini, pengunjung akan disuguhkan dengan pesona pemandangan danau. \n\n Lokasi Wisata :\n https://goo.gl/maps/8tuThxYGLrTCnncQ8 \n\n HTM :  \n HTM 15.000/orang (weekday) ; 20.000/orang (weekend) \n\n Waktu Buka/Tutup : \n setiap hari jam 08.00 - 19.00 \n\n Fasilitas \n Area parkir, toilet, spot foto, wahana perahu, wisata budaya, cafe & resto \n\n Kontak \n12 085889372022 \n\n Alternatif kontak \n http://bungursarilakepark.com/ \n\n   Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == "gc":
        response = "Anda memilih Gunung Cupu \n\n Deskripsi Wisata :\n Gunung Cupu adalah salah satu gunung yang tergolong sangat unik di Indonesia. Jika ingin mendaki gunung ini akan berhadapan dengan bebatuan. \n\n Lokasi Wisata :\n https://goo.gl/maps/UhrLFRNou5KgkqFA8 \n\n HTM :  \n Gratis ; 2.000/motor ; 5.000/mobil \n\n Waktu Buka/Tutup : \n Setiap hari 24 jam \n\n Kontak \n 087725139681 \n\n Alternatif kontak \n  \n\n   Selamat liburan, hati-hati di jalan." 

    elif incoming_msg == "wisata religi":
        response = "Anda memilih Wisata Religi. Silakan pilih opsi berikutnya:\n1. Makam Syech Ba'ing Yusuf \n2. Makam Mama Sempur \n3. Makam Eyang Pandita Tajur & Sekitarnya \n4. Makam Eyang Gandasoli."
    elif incoming_msg == "1":
        response = "Anda memilih Makam Syech Ba'ing Yusuf \n1. Deskripsi Wisata :\n2. Makam Syech Baing Yusuf berlokasi di pusat kota, tepatnya di belakang Masjid Agung Baing Yusuf Purwakarta. Berdasarkan cerita berkembang, Syech Baing Yusuf merupakan salah satu tokoh sejarah yang menyebarkan Islam di Purwakarta. Beliau merupakan guru Syech Nawawi Al Bantani ulama Indonesia yang menjadi Imam di Masjidil Haram. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/gg4kUMTavUtMoT3w5 \n5. HTM :  \n6. Gratis \n7. Waktu Buka/Tutup : \n8.  setiap hari 24 jam \n9. Kontak \n10. - \n11. Alternatif kontak \n12. - \n13. Ini adalah akhir cabang."
    elif incoming_msg == "2":
        response = "Anda memilih Makam Mama Sempur\n1. Deskripsi Wisata :\n2. Makam Mama Sempur berlokasi di Desa Sempur, Kecamatan Plered. Nama lengkapnya adalah KH Tubagus Ahmad Bakri bin KH Tubagus Syeda bin KH Tubagus Arsyad. Mama Sempur adalah salah satu tokoh muslim di Purwakarta yang menyebarkan agama Islam. Beliau saat ini dikenal sebagai Mama Sempur. Dia mendapat garis layak dari Keraton Banten (Istana Banten), diambil dari garis layak KH Tubagus Arsyad dari Keraton Banten. Di akhir setiap Dzulqaidah (11 bulan tahun Hijriah), di tempat itu selalu diadakan Haulan, sebuah peristiwa untuk mengingat wafatnya Mama Sempur. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/odzmWtxeaf4xscZs8 \n5. HTM :  \n6. Gratis \n7. Waktu Buka/Tutup : \n8.  setiap hari 24 jam \n9. Kontak \n10. - \n11. Alternatif kontak \n12. - \n13. Ini adalah akhir cabang."
    elif incoming_msg == "3":
        response = "Anda memilih Makam Eyang Pandita Tajur & Sekitarnya \n1. Deskripsi Wisata :\n2. Oleh masyarakat setempat Eyang Pandita dipercaya sebagai sesepuh Desa Pasanggrahan. Keunikan dari makam ini adalah lokasinya yang berada di atas bukit, sehingga dapat terlihat pemandangan gunung Burangrang, area pesawahan, perkebunan sayur warga, dan kawasan hutan.  \n3. Lokasi Wisata :\n4. https://goo.gl/maps/iVe5jrfPX8mZNU8C6 \n5. HTM :  \n6. Gratis \n7. Waktu Buka/Tutup : \n8.  setiap hari 24 jam \n9. Kontak \n10. 083149397123 \n11. Alternatif kontak \n12. - \n13. Ini adalah akhir cabang."

    elif incoming_msg == "wisata buatan":
        response = "Anda memilih wisata Buatan. Silakan pilih opsi berikutnya:\n1. Taman Sribaduga \n2. Taman Surawisesa \n3. Taman Pancawarna \n4. Taman Pasanggrahan Pajajaran \n5. Taman Maya Datar \n6. Bale Panyawangan Diorama Nusantara \n7 Workshop Litbang Keramik \n8. Kolam Renang Giri Tirta \n9. Kolam Renang Cihanjawar \n10. Kolam Tjek Tse Long \n11. Jaya Tirta Abadi Waterboom \n12. Bale Indung Rahayu \n13. Galeri Wayang \n14. Kuya Maranggi Waterpark \n15. Taman Pancaniti \n16. Taman Parcom \n17. Taman Citra Resmi \n18. Taman Pembaharuan \n19. Green Valley Water Park \n20. Kolam Renang Cisabuk \n21. Kolam Renang Tajur Indah \n22. Castle Lampion \n23. Cikao Park \n24. Tirta Kahuripan Wanayasa \n25. Kolam Renang Ciloa \n26. Batu Apung Alam Hijau \n27.  Kolam Renang Pusaka Water Park \n28. Kolam Renang Babakan Jati."
    elif incoming_msg == "1":
        response = "Anda memilih Taman Sribaduga \n1. Deskripsi Wisata :\n2. Taman Air Mancur Sri Baduga adalah sebuah destinasi liburan yang lokasinya berada di Alun-Alun Purwakarta, Jawa Barat. Obyek wisata ini menyajikan atraksi air menari yang dilengkap dengan lampu warna warni yang cantik dan memukau. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/ctuHLjE6tCY6o1at5 \n5. HTM :  \n6. Gratis \n7. Waktu Buka/Tutup : \n8. Area Sekitar Taman Dibuka. Namun untuk pertunjukan Air Mancur jadwalnya tidak menentu karena masalah debit air yang turun. \n9. Fasilitas \n10. Tempat parkir kendaraan, Toilet, Mushola, Warung makan, Gazebo, Tempat duduk wisata \n11. Kontak \n12  \n13. Alternatif kontak \n14. - \n15. Ini adalah akhir cabang."
    elif incoming_msg == "2":
        response = "Anda memilih Taman Surawisesa \n1. Deskripsi Wisata :\n2. Taman edukasi untuk anak-anak dengan berbagai fasilitas, seperti layar besar berisi film edukatif bertema sosial, teropong bintang hingga air mancur mini. Dihadirkan pula permainan tradisional seperti egrang, songlah, congklak, lompat tali, panggal (gasing dari kayu), kelerang dan lainnya. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/G3LrER9jD9oaP6dL7 \n5. HTM :  \n6. Gratis \n7. Waktu Buka/Tutup : \n8.  Jumat (Malam Sabtu) \n9. Fasilitas \n10. Layar besar berisi film edukatif bertema sosial, teropong bintang hingga air mancur mini. \n11. Kontak \n12 - \n13. Alternatif kontak \n14. - \n15. Ini adalah akhir cabang."
    elif incoming_msg == "3":
        response = "Anda memilih Taman Pancawarna \n1. Deskripsi Wisata :\n2. Obyek Wisata Taman Pancawarna di Purwakarta Jawa Barat sangat cocok untuk mengisi kegiatan liburan anda, apalagi saat liburan panjang seperti libur nasional, ataupun hari ibur lainnya. Keindahan Obyek Wisata Taman Pancawarna di Purwakarta Jawa Barat ini sangatlah baik bagi anda semua yang berada di dekat atau di kejauhan untuk merapat mengunjungi tempat Obyek Wisata Taman Pancawarna di Purwakarta Jawa Barat di kota purwakarta. \n3. Lokasi Wisata :\n4. https://goo.gl/maps/c3Q9eZVa9UHiQX3H9 \n5. HTM :  \n6. Gratis \n7. Waktu Buka/Tutup : \n8.  08.00 - 18.00 WIB \n9. Kontak \n10. - \n11. Alternatif kontak \n12. - \n13. Ini adalah akhir cabang."


    elif incoming_msg == ["ook"]:
        response = "Anda memilih Oleh-Oleh Khas. Silakan pilih opsi berikutnya:\n1. Galeri Menong (code : gmo)  \n2. Pusat Oleh-Oleh Purwakarta Simping(code : pops)  49\n3. Priangan Family (code : pfo)  3\n4. Pusat Oleh-Oleh dan Manisan Manah Rasa(code : podmr) \n5. Sate Maranggi Haji Yetty(code : smhy) \n6. Sate Maranggi Bah Use (code : smbu) " 
    elif incoming_msg == ["gmo"]:
        response = "Anda memilih Galeri Menong\n\n Lokasi Hotel :\n https://goo.gl/maps/87chNyNMHoMEKfVB8 \n\n Kontak \n 087725139681 \n\n Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == ["pops"]:
        response = "Anda memilih Pusat Oleh-Oleh Purwakarta Simping 49\n\n Lokasi Hotel :\n https://goo.gl/maps/tnyN9JrWEZNARsDZA \n\n Kontak \n 087879991990 \n\n Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == ["pfo"]:
        response = "Anda memilih Priangan Family 3\n\n Lokasi Hotel :\n https://goo.gl/maps/fZnjqqc3vYq68c3h9 \n\n Kontak \n 081383334470 \n\n Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == ["podmr"]:
        response = "Anda memilih Pusat Oleh-Oleh dan Manisan Manah Rasa\n\n Lokasi Hotel :\n https://goo.gl/maps/SAARoXEPBc36Z8ba6 \n\n Kontak \n 087779751296 \n\n Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == ["smhy"]:
        response = "Anda memilih Sate Maranggi Haji Yetty\n\n Lokasi Hotel :\n https://goo.gl/maps/WfdhuwvAfsL7UxGL6 \n\n Kontak \n 0264351077 \n\n Kontak Alternatif \n https://www.instagram.com/satemaranggihajiyettycibungur/?hl=id \n\n Selamat liburan, hati-hati di jalan." 
    elif incoming_msg == ["smbu"]:
        response = "Anda memilih Sate Maranggi Bah Use\n\n Lokasi Hotel :\n https://goo.gl/maps/GXwE1qzeM1pGoNnq8 \n\n Kontak \n 082115322899 \n\n Selamat liburan, hati-hati di jalan." 
    
    else:
        response = "Maaf, saya tidak mengerti pesan kamu."


    resp = MessagingResponse()
    resp.message(response)
    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
