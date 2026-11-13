# ==========================================
# MENYIMPAN KE FILE .TXT
# ==========================================
from datetime import datetime


def bersihkan(teks):
    """Karakter '|' dipakai sebagai pemisah di file .txt, jadi diganti agar file tidak rusak."""
    return teks.replace("|", "/").strip()


def simpan_users():
    with open("users.txt", "w") as file:
        for id_user, data in users.items():
            file.write(
                id_user + "|" +
                data["Nama"] + "|" +
                data["Password"] + "|" +
                data["Posisi"] + "\n"
            )


def muat_users():
    try:
        with open("users.txt", "r") as file:
            for baris in file:
                data = baris.strip().split("|")
                if len(data) == 4:
                    id_user = data[0]
                    users[id_user] = {
                        "Nama": data[1],
                        "Password": data[2],
                        "Posisi": data[3]
                    }
    except FileNotFoundError:
        pass


def simpan_barang():
    with open("barang.txt", "w") as file:
        for barang in data_barang.values():
            file.write(
                barang["kode"] + "|" +
                barang["nama"] + "|" +
                str(barang["harga"]) + "|" +
                str(barang["stok"]) + "|" +
                barang.get("status", "aktif") + "\n"
            )


def muat_barang():
    try:
        with open("barang.txt", "r") as file:
            for baris in file:
                data = baris.strip().split("|")
                if len(data) == 5:
                    kode = data[0]
                    nama = data[1]
                    harga = int(data[2])
                    stok = int(data[3])
                    status = data[4]
                    data_barang[kode] = {
                        "kode": kode,
                        "nama": nama,
                        "harga": harga,
                        "stok": stok,
                        "status": status,
                    }
    except FileNotFoundError:
        pass


def simpan_transaksi():
    with open("transaksi.txt", "w") as file:
        for data in transaksi:
            file.write(
                data["waktu"] + "|" +
                data["nama"] + "|" +
                data["kode"] + "|" +
                str(data["jumlah"]) + "|" +
                str(data["total"]) + "\n"
            )


def muat_transaksi():
    try:
        with open("transaksi.txt", "r") as file:
            for baris in file:
                data = baris.strip().split("|")
                if len(data) == 5:
                    transaksi.append({
                        "waktu": data[0],
                        "nama": data[1],
                        "kode": data[2],
                        "jumlah": int(data[3]),
                        "total": int(data[4])
                    })
    except FileNotFoundError:
        pass


def simpan_barang_masuk():
    with open("barang_masuk.txt", "w") as file:
        for data in barang_masuk:
            file.write(
                data["nama"] + "|" +
                data["kode"] + "|" +
                str(data["jumlah"]) + "\n"
            )


def muat_barang_masuk():
    try:
        with open("barang_masuk.txt", "r") as file:
            for baris in file:
                data = baris.strip().split("|")
                if len(data) == 3:
                    barang_masuk.append({
                        "nama": data[0],
                        "kode": data[1],
                        "jumlah": int(data[2])
                    })
    except FileNotFoundError:
        pass


def simpan_barang_keluar():
    with open("barang_keluar.txt", "w") as file:
        for data in barang_keluar:
            file.write(
                data["nama"] + "|" +
                data["kode"] + "|" +
                str(data["jumlah"]) + "|" +
                str(data["alasan"]) + "\n"
            )


def muat_barang_keluar():
    try:
        with open("barang_keluar.txt", "r") as file:
            for baris in file:
                data = baris.strip().split("|")
                if len(data) == 4:
                    barang_keluar.append({
                        "nama": data[0],
                        "kode": data[1],
                        "jumlah": int(data[2]),
                        "alasan": data[3]
                    })
    except FileNotFoundError:
        pass


# ==========================================
# MENYIMPAN BATAS STOK MINIMUM KE FILE .TXT
# ==========================================
def simpan_stok_minimum():
    with open("stok_minimum.txt", "w", encoding="utf-8") as file:
        file.write(str(stok_minimum))


def muat_stok_minimum():
    try:
        with open("stok_minimum.txt", "r", encoding="utf-8") as file:
            batas = int(file.read().strip())
            if batas >= 0:
                return batas
    except (FileNotFoundError, ValueError):
        pass
    return 5  # Batas awal jika file belum tersedia


def simpan_semua_data():
    simpan_users()
    simpan_barang()
    simpan_transaksi()
    simpan_barang_masuk()
    simpan_barang_keluar()
    simpan_stok_minimum()


# ==========================================
# INISIALISASI DATA
# ==========================================
users = {}
transaksi = []
barang_masuk = []
barang_keluar = []
data_barang = {}
stok_minimum = muat_stok_minimum()

muat_users()
muat_barang()
muat_transaksi()
muat_barang_masuk()
muat_barang_keluar()


def barang_aktif(barang):
    return barang.get("status", "aktif") == "aktif"


# ==========================================
# DAFTAR AKUN
# ==========================================
def daftar_akun():
    print("========================")
    print("      TAMBAHKAN AKUN")
    print("========================")
    id_user = bersihkan(input("ID User: "))
    if id_user == "":
        print("ID User tidak boleh kosong.")
        return
    if id_user in users:
        print("ID User sudah terdaftar.")
        return

    nama_user = bersihkan(input("Nama: "))
    if nama_user == "":
        print("Nama User tidak boleh kosong.")
        return

    password = bersihkan(input("Password: "))
    if password == "":
        print("Password tidak boleh kosong.")
        return

    posisi = input("Posisi (Admin/Kasir/Gudang): ").lower().strip()
    if posisi not in ("admin", "kasir", "gudang"):
        print("Posisi harus Admin, Kasir, atau Gudang.")
        return

    users[id_user] = {
        "Nama": nama_user,
        "Password": password,
        "Posisi": posisi
    }
    simpan_users()
    print("\nPendaftaran berhasil!")


# ==========================================
# LOGIN
# ==========================================
def login():
    print("\n========================")
    print("         LOGIN")
    print("========================")
    if len(users) == 0:
        print("Belum ada akun terdaftar. Silakan daftar akun terlebih dahulu.")
        return "KOSONG"

    while True:
        login_id = input("ID User: ").strip()
        login_password = input("Password: ").strip()

        if login_id in users and login_password == users[login_id]["Password"]:
            print("\nLogin berhasil!")
            print("Nama   :", users[login_id]["Nama"])
            print("Posisi :", users[login_id]["Posisi"])
            return users[login_id]["Posisi"]

        print("ID User atau Password salah.")
        ulang = input("Coba lagi? (ya/tidak): ").lower().strip()
        if ulang != "ya":
            return None


def main_menu():
    while True:
        print("\n=======================")
        print("       MENU AWAL ")
        print("========================")
        print("1. Login")
        print("2. Keluar")
        pilihan = input("Pilih menu (1-2): ").strip()

        if pilihan == "1":
            status = login()
            if status == "KOSONG":
                continue
            elif status:
                print("Melanjutkan ke sistem sebagai " + str(status))
                return status
        elif pilihan == "2":
            print("Terima kasih!")
            return None
        else:
            print("Pilihan tidak valid.")


# ==========================================
# TAMBAH BARANG
# ==========================================
def buat_kode_barang():
    terbesar = 0
    for barang in data_barang.values():
        try:
            terbesar = max(terbesar, int(barang["kode"][1:]))
        except ValueError:
            pass
    return "B" + str(terbesar + 1).zfill(3)


def tambah_barang():
    while True:
        tampilkan_barang()
        print("\n=== TAMBAH DATA BARANG ===")
        kode = buat_kode_barang()
        print(f"Kode Barang: {kode}")

        nama = bersihkan(input("Nama Barang : ")).lower()
        if nama == "":
            print("Nama barang tidak boleh kosong.")
            continue

        # Validasi duplikat berdasarkan nama
        ada_nama = any(b["nama"].lower() == nama for b in data_barang.values())
        if ada_nama:
            print("Barang sudah ada dalam data.")
            continue

        try:
            harga = int(input("Harga       : "))
            stok = int(input("Stok        : "))
        except ValueError:
            print("Input harga dan stok harus berupa angka!")
            continue

        if harga < 0 or stok < 0:
            print("Harga dan stok tidak boleh negatif.")
            continue

        data_barang[kode] = {
            "kode": kode,
            "nama": nama.title(),
            "harga": harga,
            "stok": stok,
            "status": "aktif"
        }
        simpan_barang()
        print("Data berhasil ditambahkan!")

        tambah_lagi = input("\nTambah barang lagi? (y/t): ").lower().strip()
        if tambah_lagi != "y":
            break


# ==========================================
# NONAKTIFKAN BARANG
# ==========================================
def nonaktifkan_barang():
    print("\n=== NONAKTIFKAN DATA BARANG ===")
    if len(data_barang) == 0:
        print("Data barang masih kosong.")
        return

    tampilkan_barang()
    kode = input("\nKode barang yang ingin dinonaktifkan: ").strip()
    if kode not in data_barang:
        print("Barang tidak ditemukan.")
        return

    barang = data_barang[kode]
    if not barang_aktif(barang):
        print("Barang ini sudah berstatus nonaktif.")
        return

    print("Kode :", barang["kode"])
    print("\nBarang :", barang["nama"])
    print("Status :", barang.get("status", "aktif"))
    print("Stok   :", barang["stok"])

    hapus = input("Yakin ingin menonaktifkan barang ini? (ya/tidak): ").lower().strip()
    if hapus != "ya":
        print("Penonaktifan dibatalkan.")
        return

    barang["status"] = "nonaktif"
    simpan_barang()
    print("Data barang berhasil dinonaktifkan")


# ==========================================
# AKTIFKAN BARANG
# ==========================================
def aktifkan_barang():
    print("\n=== AKTIFKAN KEMBALI BARANG ===")
    barang_nonaktif = [b for b in data_barang.values() if not barang_aktif(b)]

    if len(barang_nonaktif) == 0:
        print("Tidak ada barang yang berstatus nonaktif.")
        return

    print("\nDaftar Barang Nonaktif:")
    for barang in barang_nonaktif:
        print(f"- {barang['nama']} (Kode: {barang['kode']}) | Stok: {barang['stok']}")

    kode = input("\nMasukkan Kode barang yang ingin diaktifkan kembali: ").strip()
    if kode not in data_barang:
        print("Barang tidak ditemukan.")
        return

    barang = data_barang[kode]
    if barang_aktif(barang):
        print("Barang ini sudah berstatus aktif.")
        return

    hapus = input("Yakin ingin Aktifkan barang ini? (ya/tidak): ").lower().strip()
    if hapus != "ya":
        print("Pengaktifkan dibatalkan.")
        return

    barang["status"] = "aktif"
    simpan_barang()
    print(f"Barang '{barang['nama']}' berhasil diaktifkan kembali")


# ==========================================
# EDIT BARANG
# ==========================================
def edit_barang():
    print("\n=== EDIT DATA BARANG ===")
    if len(data_barang) == 0:
        print("Data barang masih kosong.")
        return

    tampilkan_barang()
    kode = input("\nKode barang yang ingin diedit: ").strip()
    if kode not in data_barang:
        print("Barang tidak ditemukan.")
        return
    barang = data_barang[kode]

    print("\nData saat ini:")
    print("Kode  :", barang["kode"])
    print("Nama  :", barang["nama"])
    print("Harga :", barang["harga"])
    print("Stok  :", barang["stok"])

    print("\nMasukkan data baru (kosongkan jika tidak ingin diubah).")
    nama_baru = bersihkan(input("Nama baru  : "))
    harga_baru_str = input("Harga baru : ").strip()
    stok_baru_str = input("Stok baru  : ").strip()

    if nama_baru == "":
        nama_baru = barang["nama"]

    if harga_baru_str == "":
        harga_baru = barang["harga"]
    else:
        try:
            harga_baru = int(harga_baru_str)
        except ValueError:
            print("Harga harus berupa angka!")
            return

    if stok_baru_str == "":
        stok_baru = barang["stok"]
    else:
        try:
            stok_baru = int(stok_baru_str)
        except ValueError:
            print("Stok harus berupa angka!")
            return

    if harga_baru < 0 or stok_baru < 0:
        print("Harga dan stok tidak boleh negatif.")
        return

    barang["nama"] = nama_baru.title()
    barang["harga"] = harga_baru
    barang["stok"] = stok_baru

    simpan_barang()
    print("\nData barang berhasil diedit!")


# ==========================================
# KELOLA BARANG
# ==========================================
def kelola_data_barang():
    while True:
        print("\n=== KELOLA DATA BARANG ===")
        print("1. Tambah Data Barang")
        print("2. Nonaktifkan Data Barang")
        print("3. Aktifkan Barang")
        print("4. Edit Data Barang")
        print("5. Kembali")
        pilihan = input("Pilihan: ").strip()

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            nonaktifkan_barang()
        elif pilihan == "3":
            aktifkan_barang()
        elif pilihan == "4":
            edit_barang()
        elif pilihan == "5":
            return
        else:
            print("Pilihan tidak tersedia.")


# ==========================================
# TAMPILKAN BARANG
# ==========================================
def tampilkan_barang():
    print("\n=== DATA BARANG ===")
    if len(data_barang) == 0:
        print("Data masih kosong.")
    else:
        ditemukan = False
        for kode, barang in data_barang.items():
            if barang_aktif(barang):
                print(
                    barang["kode"],"\t", barang["nama"],"\t" + "Rp"
                    + str(barang["harga"]),"\t" + " | Stok:", barang["stok"]),"\t"
                ditemukan = True
            
        if not ditemukan:
            print("Tidak ada data barang yang aktif.")


# ==========================================
# CARI BARANG BERDASARKAN KODE
# ==========================================
def menu_cari():
    print("====================")
    print("    MENU CARI")
    print("====================")
    print("1.Berdasarkan kode")
    print("2.Berdasarkan nama")
    pilih = input("Pilih Menu: ")

    if pilih == "1":
       cari_barang_kode()
    if pilih == "2":
       cari_barang_nama()
    else:
       print("Pilihan tidak tersedia")
       return


def cari_barang_kode():
    print("====================")
    print("  PENCARIAN BARANG")
    print("====================")
    if len(data_barang) == 0:
        print("Data masih kosong.")
        return

    kode_cari = input("Masukkan kode barang yang dicari: ").strip()
    if kode_cari == "":
        print("Kode tidak boleh kosong.")
        return

    ditemukan = False
    for kode, barang in data_barang["nama"].items():
        if barang_aktif(barang) and kode_cari in kode:
            print(barang["nama"],
                  "(" + barang["kode"] + ") "
                  "- Rp" + str(barang["harga"]) +
                  " | Stok:", barang["stok"])
            ditemukan = True

    if not ditemukan:
        print("Barang dengan kode tersebut tidak ditemukan.")

# ==========================================
# CARI BARANG BERDASARKAN NAMA
# ==========================================
def cari_barang_nama():
    print("====================")
    print("  PENCARIAN BARANG")
    print("====================")
    if len(data_barang) == 0:
        print("Data masih kosong.")
        return

    nama_cari = input("Masukkan nama barang yang dicari: ").lower().strip()
    if nama_cari == "":
        print("Nama barang tidak boleh kosong.")
        return

    ditemukan = False
    for barang in data_barang.values():
        if barang_aktif(barang) and nama_cari in barang["nama"].lower():
            print(barang["nama"],
                  "(" + barang["kode"] + ") "
                  "- Rp" + str(barang["harga"]) +
                  " | Stok:", barang["stok"])
            ditemukan = True

    if not ditemukan:
        print("Barang dengan nama tersebut tidak ditemukan.")


# ==========================================
# SORTING STOK
# ==========================================
def nilai_urut(barang, kunci):
    if kunci == "nama":
        return barang["nama"].lower()
    return barang[kunci]

def quick_sort(data, kunci="stok"):
    if len(data) <= 1:
        return data
    pivot = data[0]
    kiri = []
    kanan = []

    for barang in data[1:]:
        if nilai_urut(barang, kunci) <= nilai_urut(pivot, kunci):
            kiri.append(barang)
        else:
            kanan.append(barang)

    return quick_sort(kiri, kunci) + [pivot] + quick_sort(kanan, kunci)


def sorting_barang():
    data = [b for b in data_barang.values() if barang_aktif(b)]
    if len(data) == 0:
        print("Tidak ada data barang aktif.")
        return

    print("\n=== QUICK SORT BARANG ===")
    print("Urutkan berdasarkan:")
    print("1. Stok")
    print("2. Harga")
    print("3. Abjad Nama Barang")
    pilihan = input("Pilih (1-3): ").strip()

    if pilihan == "1":
        kunci, judul = "stok", "STOK"
    elif pilihan == "2":
        kunci, judul = "harga", "HARGA"
    elif pilihan == "3":
        kunci, judul = "nama", "ABJAD NAMA"
    else:
        print("Pilihan tidak tersedia.")
        return

    print("\nArah pengurutan:")
    print("1. Terkecil/A ke terbesar/Z")
    print("2. Terbesar/Z ke terkecil/A")
    arah = input("Pilih (1/2): ").strip()
    if arah not in ("1", "2"):
        print("Pilihan tidak tersedia.")
        return

    hasil = quick_sort(data, kunci)
    if arah == "2":
        hasil.reverse()

    arah_teks = "NAIK" if arah == "1" else "TURUN"
    print(f"\n=== DATA BARANG SETELAH SORTING (BERDASARKAN {judul}, {arah_teks}) ===")
    for barang in hasil:
        print(barang["kode"], barang["nama"], "Rp" + str(barang["harga"]), "Stok:", barang["stok"])


# ==========================================
# TRANSAKSI PENJUALAN 
# ==========================================
def transaksi_penjualan():
    if len(data_barang) == 0:
        print("Data barang masih kosong")
        return

    keranjang = []
    total_belanja = 0

    while True:
        tampilkan_barang()

        print("\n--- Tambah Barang ke Keranjang ---")
        kode = input("Masukkan Kode barang: ").strip()

        if kode not in data_barang or not barang_aktif(data_barang[kode]):
            print("Barang tidak ditemukan atau sudah nonaktif.")
        else:
            barang = data_barang[kode]
            print(f"Barang: {barang['nama']} | Harga: Rp{barang['harga']} | Stok: {barang['stok']}")
            try:
                jumlah = int(input("Jumlah beli: "))
            except ValueError:
                print("Jumlah harus berupa angka.")
                jumlah = 0

            if jumlah <= 0:
                print("Jumlah tidak valid.")
            elif jumlah > barang["stok"]:
                print("Stok tidak mencukupi.")
            else:
                subtotal = barang["harga"] * jumlah

                keranjang.append({
                    "barang_ref": barang,
                    "nama": barang["nama"],
                    "kode": barang["kode"],
                    "jumlah": jumlah,
                    "subtotal": subtotal
                })

                barang["stok"] -= jumlah
                total_belanja += subtotal
                print(f"-> {barang['nama']} (x{jumlah}) berhasil ditambahkan ke keranjang.")

        tambah_lagi = input("\nTambah barang lain? (ya/tidak): ").lower().strip()
        if tambah_lagi != "ya":
            break

    if not keranjang:
        print("Transaksi dibatalkan (Keranjang kosong).")
        return

    print("\n============================")
    print("     RINGKASAN BELANJA")
    print("============================")
    for item in keranjang:
        print(f"{item['nama']} x{item['jumlah']} = Rp{item['subtotal']}")
    print("----------------------------")
    print(f"Total Bayar  : Rp{total_belanja}")

    while True:
        try:
            bayar = int(input("Uang bayar (0 untuk batal): Rp"))
        except ValueError:
            print("Pembayaran harus berupa angka.")
            continue

        if bayar == 0:
            for item in keranjang:
                item["barang_ref"]["stok"] += item["jumlah"]
            print("Transaksi dibatalkan. Stok dikembalikan.")
            return

        if bayar < total_belanja:
            print("Uang kurang, silakan masukkan jumlah yang pas/lebih.")
        else:
            break

    kembalian = bayar - total_belanja

    waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for item in keranjang:
        transaksi.append({
            "waktu": waktu_sekarang,
            "nama": item["nama"],
            "kode": item["kode"],
            "jumlah": item["jumlah"],
            "total": item["subtotal"]
        })

    simpan_barang()
    simpan_transaksi()

    print("\n============================")
    print("         SMK MART")
    print("============================")
    print(f"Waktu : {waktu_sekarang}")
    for item in keranjang:
        print(f"{item['nama']} x{item['jumlah']} = Rp{item['subtotal']}")
    print("------------------------------")
    print(f"Total Harga : Rp{total_belanja}")
    print(f"Bayar       : Rp{bayar}")
    print(f"Kembalian   : Rp{kembalian}")
    print("==============================")


# ==========================================
# KELOLA STOK 
# ==========================================
def kelola_stok():
    print("\n=== KELOLA STOK BARANG ===")
    if len(data_barang) == 0:
        print("Data barang masih kosong.")
        return

    print("1. Barang Masuk")
    print("2. Barang Keluar")
    pilihan = input("Pilih (1/2): ").strip()

    if pilihan not in ("1", "2"):
        print("Pilihan tidak tersedia.")
        return

    kode = input("Kode barang: ").strip()
    if kode not in data_barang:
        print("Barang tidak ditemukan.")
        return

    barang = data_barang[kode]
    if not barang_aktif(barang):
        print("Barang berstatus nonaktif. Aktifkan terlebih dahulu.")
        return

    print("\nKode   :", barang["kode"])
    print("Barang :", barang["nama"])
    print("Stok sekarang:", barang["stok"])

    try:
        jumlah = int(input("Masukkan Jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka.")
        return

    if jumlah <= 0:
        print("Jumlah tidak valid.")
        return

    # ===Barang Masuk===
    if pilihan == "1":
        barang["stok"] += jumlah
        barang_masuk.append({
            "nama": barang["nama"],
            "kode": barang["kode"],
            "jumlah": jumlah
        })
        simpan_barang()
        simpan_barang_masuk()
        print("Barang masuk berhasil dicatat.")

    # ===Barang Keluar===
    elif pilihan == "2":
        if jumlah > barang["stok"]:
            print("Stok tidak mencukupi.")
            return

        alasan = bersihkan(input("Alasan barang keluar: "))
        barang["stok"] -= jumlah
        barang_keluar.append({
            "nama": barang["nama"],
            "kode": barang["kode"],
            "jumlah": jumlah,
            "alasan": alasan
        })
        simpan_barang()
        simpan_barang_keluar()
        print("Barang keluar berhasil dicatat.")

    print("Stok sekarang:", barang["stok"])


# ==========================================
# PERINGATAN STOK MINIMUM
# ==========================================
def peringatan_stok():
    global stok_minimum

    print("\n=== PERINGATAN STOK MINIMUM ===")
    if len(data_barang) == 0:
        print("Data barang masih kosong.")
        return

    print("Batas stok minimum saat ini:", stok_minimum)
    ubah = input("Ubah batas stok minimum? (ya/tidak): ").lower().strip()

    if ubah == "ya":
        try:
            batas_baru = int(input("Masukkan batas stok minimum baru: "))
            if batas_baru < 0:
                print("Batas stok tidak boleh kurang dari 0.")
                return
        except ValueError:
            print("Input batas harus berupa angka.")
            return

        stok_minimum = batas_baru
        simpan_stok_minimum()
        print("Batas stok minimum berhasil disimpan ke stok_minimum.txt.")

    ditemukan = False
    for kode, barang in data_barang.items():
        if barang_aktif(barang) and barang["stok"] <= stok_minimum:
            print("PERINGATAN:", barang["nama"], "| Stok:", barang["stok"])
            ditemukan = True

    if not ditemukan:
        print("Tidak ada barang yang mencapai batas stok minimum.")


# ==========================================
# LAPORAN PENJUALAN
# ==========================================
def laporan_penjualan():
    print("\n=== LAPORAN PENJUALAN ===")
    if len(transaksi) == 0:
        print("Belum ada transaksi.")
        return

    total_penjualan = 0
    for data in transaksi:
        print("[" + data["waktu"] + "]", "Barang:", data["nama"], "| Kode:", data["kode"],
              "| Jumlah:", data["jumlah"], "| Total: Rp" + str(data["total"]))
        total_penjualan += data["total"]

    print("-----------------------------")
    print("Total penjualan: Rp" + str(total_penjualan))


# ==========================================
# LAPORAN STOK DAN AKTIVITAS GUDANG
# ==========================================
def laporan_gudang():
    print("\n=== LAPORAN STOK ===")
    if len(data_barang) == 0:
        print("Data barang masih kosong.")
    else:
        for kode, barang in data_barang.items():
            print(barang["nama"], "| Stok:", barang["stok"], "| Status:", barang.get("status", "aktif"))

    print("\n=== BARANG MASUK ===")
    if len(barang_masuk) == 0:
        print("Belum ada barang masuk.")
    else:
        for data in barang_masuk:
            print(data["nama"], "| Kode:", data["kode"], "| Jumlah:", data["jumlah"])

    print("\n=== BARANG KELUAR ===")
    if len(barang_keluar) == 0:
        print("Belum ada barang keluar.")
    else:
        for data in barang_keluar:
            print(data["nama"],
                  "| Kode:", data["kode"],
                  "| Jumlah:", data["jumlah"],
                  "| Alasan:", data["alasan"])


def tampilkan_user():
    print("\n=== DAFTAR USER ===")
    if len(users) == 0:
        print("Belum ada user.")
        return
    for id_user, data in users.items():
        print("ID:", id_user, "| Nama:", data["Nama"], "| Posisi:", data["Posisi"])


# ==========================================
# PROGRAM MENU AWAL
# ==========================================
posisi = main_menu()

if posisi is not None:
    print("\n======================")
    print("        SMK MART")
    print("========================")

    while True:
        if posisi == "admin":
            print("\n=== ADMIN ===")
            print("1. Kelola Data Barang")
            print("2. Tampilkan Data Barang")
            print("3. Cari Data Barang")
            print("4. Sorting Barang ")
            print("5. Kelola Stok Barang")
            print("6. Peringatan Stok Minimum")
            print("7. Transaksi Penjualan")
            print("8. Laporan Penjualan")
            print("9. Laporan Stok dan Aktivitas Gudang")
            print("10. Tampilkan User")
            print("11. Daftarkan Akun")
            print("12. Log Out Akun")
            print("13. Keluar")

            pilihan = input("Pilih menu: ").strip()

            if pilihan == "1":
                kelola_data_barang()
            elif pilihan == "2":
                tampilkan_barang()
            elif pilihan == "3":
                menu_cari()
            elif pilihan == "4":
                sorting_barang()
            elif pilihan == "5":
                kelola_stok()
            elif pilihan == "6":
                peringatan_stok()
            elif pilihan == "7":
                transaksi_penjualan()
            elif pilihan == "8":
                laporan_penjualan()
            elif pilihan == "9":
                laporan_gudang()
            elif pilihan == "10":
                tampilkan_user()
            elif pilihan == "11":
                daftar_akun()
            elif pilihan == "12":
                simpan_semua_data()
                posisi = main_menu()
                if posisi is None:
                    break
            elif pilihan == "13":
                simpan_semua_data()
                print("Program Selesai")
                break
            else:
                print("Pilihan tidak tersedia.")

        elif posisi == "kasir":
            print("\n=== KASIR ===")
            print("1. Tampilkan Data Barang")
            print("2. Cari Data Barang")
            print("3. Transaksi Penjualan")
            print("4. Log Out Akun")
            print("5. Keluar")

            pilihan = input("Pilih menu: ").strip()

            if pilihan == "1":
                tampilkan_barang()
            elif pilihan == "2":
                menu_cari()
            elif pilihan == "3":
                transaksi_penjualan()
            elif pilihan == "4":
                simpan_semua_data()
                posisi = main_menu()
                if posisi is None:
                    break
            elif pilihan == "5":
                simpan_semua_data()
                print("Program Selesai")
                break
            else:
                print("Pilihan tidak tersedia")

        elif posisi == "gudang":
            print("\n=== GUDANG ===")
            print("1. Tampilkan Data Barang")
            print("2. Cari Data Barang")
            print("3. Kelola Stok Barang")
            print("4. Sorting Barang")
            print("5. Peringatan Stok Minimum")
            print("6. Laporan Stok dan Aktivitas Gudang")
            print("7. Log Out Akun")
            print("8. Keluar")

            pilihan = input("Pilih Menu: ").strip()

            if pilihan == "1":
                tampilkan_barang()
            elif pilihan == "2":
                menu_cari()
            elif pilihan == "3":
                kelola_stok()
            elif pilihan == "4":
                sorting_barang()
            elif pilihan == "5":
                peringatan_stok()
            elif pilihan == "6":
                laporan_gudang()
            elif pilihan == "7":
                simpan_semua_data()
                posisi = main_menu()
                if posisi is None:
                    break
            elif pilihan == "8":
                simpan_semua_data()
                print("Program Selesai")
                break
            else:
                print("Pilihan tidak tersedia")

        else:
            print("Posisi akun tidak dikenali.")
            posisi = main_menu()
            if posisi is None:
                break
