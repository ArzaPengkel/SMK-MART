# ==========================================
# SMK MART - SISTEM MANAJEMEN BARANG
# ==========================================
from datetime import datetime
import getpass
import random


# ==========================================
# FUNGSI BANTU TAMPILAN
# ==========================================
def bersihkan(teks):
    """Karakter '|' dipakai sebagai pemisah di file .txt, jadi diganti agar file tidak rusak."""
    return teks.replace("|", "/").strip()


def rupiah(angka):
    """Format angka: 15000 -> Rp15.000"""
    return "Rp" + f"{angka:,}".replace(",", ".")


def cetak_tabel_barang(daftar, tampil_status=False):
    """Mencetak daftar barang dalam tabel berbingkai (lebar kolom menyesuaikan isi)."""
    if not daftar:
        return

    # Setiap kolom: (judul, rata, daftar nilai)
    kolom = [
        ("No", ">", [str(i) for i in range(1, len(daftar) + 1)]),
        ("Kode", "<", [b["kode"] for b in daftar]),
        ("Nama Barang", "<", [b["nama"] for b in daftar]),
        ("Harga Beli", ">", [rupiah(b["harga_beli"]) for b in daftar]),
        ("Harga Jual", ">", [rupiah(b["harga_jual"]) for b in daftar]),
        ("Stok", ">", [str(b["stok"]) for b in daftar]),
    ]
    if tampil_status:
        kolom.append(("Status", "<", [b.get("status", "aktif") for b in daftar]))

    lebar = [max(len(judul), *(len(v) for v in nilai)) for judul, _, nilai in kolom]

    garis = "+" + "+".join("-" * (w + 2) for w in lebar) + "+"
    header = "|" + "|".join(f" {judul:^{w}} " for (judul, _, _), w in zip(kolom, lebar)) + "|"

    print(garis)
    print(header)
    print(garis)
    for i in range(len(daftar)):
        sel = [f" {nilai[i]:{rata}{w}} " for (_, rata, nilai), w in zip(kolom, lebar)]
        print("|" + "|".join(sel) + "|")
    print(garis)
    print(f"Total: {len(daftar)} barang")


# ==========================================
# MENYIMPAN KE FILE .TXT
# ==========================================
def simpan_users():
    with open("users.txt", "w", encoding="utf-8") as file:
        for id_user, data in users.items():
            file.write(
                id_user + "|" +
                data["Nama"] + "|" +
                data["Password"] + "|" +
                data["Posisi"] + "\n"
            )


def muat_users():
    try:
        with open("users.txt", "r", encoding="utf-8") as file:
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
    with open("barang.txt", "w", encoding="utf-8") as file:
        for barang in data_barang.values():
            file.write(
                barang["kode"] + "|" +
                barang["nama"] + "|" +
                str(barang["harga_beli"]) + "|" +
                str(barang["harga_jual"]) + "|" +
                str(barang["stok"]) + "|" +
                barang.get("status", "aktif") + "\n"
            )


def muat_barang():
    try:
        with open("barang.txt", "r", encoding="utf-8") as file:
            for baris in file:
                data = baris.strip().split("|")
                try:
                    if len(data) == 6:   
                        kode = data[0]
                        data_barang[kode] = {
                            "kode": kode,
                            "nama": data[1],
                            "harga_beli": int(data[2]),
                            "harga_jual": int(data[3]),
                            "stok": int(data[4]),
                            "status": data[5],
                        }
                    elif len(data) == 5:  
                        kode = data[0]
                        harga = int(data[2])
                        data_barang[kode] = {
                            "kode": kode,
                            "nama": data[1],
                            "harga_beli": harga,
                            "harga_jual": harga,
                            "stok": int(data[3]),
                            "status": data[4],
                        }
                except ValueError:
                    pass  
    except FileNotFoundError:
        pass


def simpan_transaksi():
    with open("transaksi.txt", "w", encoding="utf-8") as file:
        for data in transaksi:
            file.write(
                data["waktu"] + "|" +
                data["nama"] + "|" +
                data["kode"] + "|" +
                str(data["jumlah"]) + "|" +
                str(data["total"]) + "|" +
                str(data["harga_beli"]) + "\n"
            )


def muat_transaksi():
    try:
        with open("transaksi.txt", "r", encoding="utf-8") as file:
            for baris in file:
                data = baris.strip().split("|")
                try:
                    if len(data) == 6:
                        transaksi.append({
                            "waktu": data[0],
                            "nama": data[1],
                            "kode": data[2],
                            "jumlah": int(data[3]),
                            "total": int(data[4]),
                            "harga_beli": int(data[5])
                        })
                    elif len(data) == 5:
                        # Transaksi versi lama belum menyimpan harga beli.
                        # Gunakan harga beli dari barang.txt sebagai estimasi.
                        jumlah = int(data[3])
                        total = int(data[4])
                        barang = data_barang.get(data[2])
                        harga_beli = barang["harga_beli"] if barang else 0
                        transaksi.append({
                            "waktu": data[0],
                            "nama": data[1],
                            "kode": data[2],
                            "jumlah": jumlah,
                            "total": total,
                            "harga_beli": harga_beli,
                            "modal_estimasi": True
                        })
                except ValueError:
                    pass
    except FileNotFoundError:
        pass


def simpan_barang_masuk():
    with open("barang_masuk.txt", "w", encoding="utf-8") as file:
        for data in barang_masuk:
            file.write(
                data["nama"] + "|" +
                data["kode"] + "|" +
                str(data["jumlah"]) + "\n"
            )


def muat_barang_masuk():
    try:
        with open("barang_masuk.txt", "r", encoding="utf-8") as file:
            for baris in file:
                data = baris.strip().split("|")
                if len(data) == 3:
                    try:
                        barang_masuk.append({
                            "nama": data[0],
                            "kode": data[1],
                            "jumlah": int(data[2])
                        })
                    except ValueError:
                        pass
    except FileNotFoundError:
        pass


def simpan_barang_keluar():
    # Format baru: waktu|nama|kode|jumlah|alasan|harga_beli.
    # Baris lama dengan 4 kolom tetap dapat dibaca oleh muat_barang_keluar().
    with open("barang_keluar.txt", "w", encoding="utf-8") as file:
        for data in barang_keluar:
            file.write(
                str(data.get("waktu", "")) + "|" +
                data["nama"] + "|" +
                data["kode"] + "|" +
                str(data["jumlah"]) + "|" +
                str(data["alasan"]) + "|" +
                str(data.get("harga_beli", "")) + "\n"
            )


def muat_barang_keluar():
    try:
        with open("barang_keluar.txt", "r", encoding="utf-8") as file:
            for baris in file:
                data = baris.strip().split("|")
                try:
                    if len(data) == 6:
                        barang_keluar.append({
                            "waktu": data[0],
                            "nama": data[1],
                            "kode": data[2],
                            "jumlah": int(data[3]),
                            "alasan": data[4],
                            "harga_beli": int(data[5]) if data[5] else None
                        })
                    elif len(data) == 4:
                        # Format lama tidak memiliki tanggal dan harga beli.
                        barang_keluar.append({
                            "waktu": None,
                            "nama": data[0],
                            "kode": data[1],
                            "jumlah": int(data[2]),
                            "alasan": data[3],
                            "harga_beli": None
                        })
                except ValueError:
                    pass
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
def buat_id_user():
    """ID ACAK 6 DIGIT, UNIQUE"""
    while True:
        id_baru = str(random.randint(100000, 999999))
        if id_baru not in users:
            return id_baru


def daftar_akun(posisi_tetap=None):
    print("========================")
    print("      TAMBAHKAN AKUN")
    print("========================")

    id_user = buat_id_user()

    while True:
        nama_user = bersihkan(input("Nama: "))
        if nama_user == "":
            print("Nama User tidak boleh kosong.")
            continue
        break

    while True:
        password = bersihkan(input("Password: "))
        if len(password) < 8:
            print("Password minimal 8 karakter.")
            continue
        if not any(c.isdigit() for c in password):
            print("Password harus mengandung minimal 1 angka.")
            continue
        break

    if posisi_tetap:
        posisi = posisi_tetap
        print("Posisi: " + posisi + " (akun pertama otomatis menjadi Admin)")
    else:
        while True:
            posisi = input("Posisi (Admin/Kasir/Gudang): ").lower().strip()
            if posisi not in ("admin", "kasir", "gudang"):
                print("Posisi harus Admin, Kasir, atau Gudang.")
                continue
            break

    users[id_user] = {
        "Nama": nama_user,
        "Password": password,
        "Posisi": posisi
    }
    simpan_users()
    print("\nPendaftaran berhasil!")
    print("ID USER :", id_user)
    print("ID USER ini dipakai untuk login")


# ==========================================
# LOGIN
# ==========================================
def login():
    print("\n========================")
    print("         LOGIN")
    print("========================")
    if len(users) == 0:
        return "KOSONG"

    while True:
        login_id = input("ID User: ").strip()
        login_password = getpass.getpass("Password: ").strip()

        if login_id == "" or login_password == "":
            print("ID User dan Password tidak boleh kosong.")
        elif login_id in users and login_password == users[login_id]["Password"]:
            print("\nLogin berhasil!")
            print("Nama   :", users[login_id]["Nama"])
            print("Posisi :", users[login_id]["Posisi"])
            return users[login_id]["Posisi"].lower()
        else:
            print("ID User atau Password salah.")

        ulang = input("Coba lagi? (y/t): ").lower().strip()
        if ulang != "y":
            return None


def main_menu():
    while True:
        print("\n========================")
        print("       MENU LOGIN")
        print("========================")
        print("1. Login")
        print("0. Keluar")
        pilihan = input("Pilih menu (0-1): ").strip()

        if pilihan == "1":
            status = login()
            if status == "KOSONG":
                # Belum ada akun sama sekali -> buat akun Admin pertama
                print("Belum ada akun terdaftar. Buat akun Admin pertama.\n")
                daftar_akun(posisi_tetap="admin")
                continue
            elif status:
                print("Melanjutkan ke sistem sebagai " + str(status))
                return status
        elif pilihan == "0":
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

        nama = bersihkan(input("Nama Barang (0 untuk kembali): ")).lower()
        if nama == "0":
            return
        if nama == "":
            print("Nama barang tidak boleh kosong.")
            continue

        # Validasi duplikat berdasarkan nama
        if any(b["nama"].lower() == nama for b in data_barang.values()):
            print("Barang sudah ada dalam data.")
            continue

        try:
            harga_beli = int(input("Harga Beli  : "))
            harga_jual = int(input("Harga Jual  : "))
            stok = int(input("Stok        : "))
        except ValueError:
            print("Input harga dan stok harus berupa angka!")
            continue

        if harga_beli < 0 or harga_jual < 0 or stok < 0:
            print("Harga dan stok tidak boleh negatif.")
            continue

        data_barang[kode] = {
            "kode": kode,
            "nama": nama.title(),
            "harga_beli": harga_beli,
            "harga_jual": harga_jual,
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
    kode = input("\nKode barang yang ingin dinonaktifkan (0 untuk kembali): ").strip().upper()
    if kode == "0":
        return
    if kode not in data_barang:
        print("Barang tidak ditemukan.")
        return

    barang = data_barang[kode]
    if not barang_aktif(barang):
        print("Barang ini sudah berstatus nonaktif.")
        return

    print("\nKode   :", barang["kode"])
    print("Barang :", barang["nama"])
    print("Status :", barang.get("status", "aktif"))
    print("Stok   :", barang["stok"])

    konfirmasi = input("Yakin ingin menonaktifkan barang ini? (y/t): ").lower().strip()
    if konfirmasi != "y":
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
    cetak_tabel_barang(sorted(barang_nonaktif, key=lambda b: b["kode"]))

    kode = input("\nMasukkan Kode barang yang ingin diaktifkan kembali (0 untuk kembali): ").strip().upper()
    if kode == "0":
        return
    if kode not in data_barang:
        print("Barang tidak ditemukan.")
        return

    barang = data_barang[kode]
    if barang_aktif(barang):
        print("Barang ini sudah berstatus aktif.")
        return

    konfirmasi = input("Yakin ingin mengaktifkan barang ini? (y/t): ").lower().strip()
    if konfirmasi != "y":
        print("Pengaktifan dibatalkan.")
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
    kode = input("\nKode barang yang ingin diedit (0 untuk kembali): ").strip().upper()
    if kode == "0":
        return
    if kode not in data_barang:
        print("Barang tidak ditemukan.")
        return
    barang = data_barang[kode]

    print("\nData saat ini:")
    print("Kode       :", barang["kode"])
    print("Nama       :", barang["nama"])
    print("Harga Beli :", rupiah(barang["harga_beli"]))
    print("Harga Jual :", rupiah(barang["harga_jual"]))
    print("Stok       :", barang["stok"])

    print("\nMasukkan data baru (kosongkan jika tidak ingin diubah).")
    nama_baru = bersihkan(input("Nama baru       : "))
    harga_beli_str = input("Harga beli baru  : ").strip()
    harga_jual_str = input("Harga jual baru  : ").strip()
    stok_baru_str = input("Stok baru        : ").strip()

    if nama_baru == "":
        nama_baru = barang["nama"]
    elif any(b["nama"].lower() == nama_baru.lower() and b["kode"] != kode
             for b in data_barang.values()):
        print("Nama barang sudah dipakai barang lain.")
        return

    if harga_beli_str == "":
        harga_beli_baru = barang["harga_beli"]
    else:
        try:
            harga_beli_baru = int(harga_beli_str)
        except ValueError:
            print("Harga beli harus berupa angka!")
            return

    if harga_jual_str == "":
        harga_jual_baru = barang["harga_jual"]
    else:
        try:
            harga_jual_baru = int(harga_jual_str)
        except ValueError:
            print("Harga jual harus berupa angka!")
            return

    if stok_baru_str == "":
        stok_baru = barang["stok"]
    else:
        try:
            stok_baru = int(stok_baru_str)
        except ValueError:
            print("Stok harus berupa angka!")
            return

    if harga_beli_baru < 0 or harga_jual_baru < 0 or stok_baru < 0:
        print("Harga dan stok tidak boleh negatif.")
        return

    barang["nama"] = nama_baru.title()
    barang["harga_beli"] = harga_beli_baru
    barang["harga_jual"] = harga_jual_baru
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
        print("0. Kembali")
        pilihan = input("Pilihan: ").strip()

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            nonaktifkan_barang()
        elif pilihan == "3":
            aktifkan_barang()
        elif pilihan == "4":
            edit_barang()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak tersedia.")


# ==========================================
# TAMPILKAN BARANG
# ==========================================
def tampilkan_barang():
    print("\n=== DATA BARANG ===")
    daftar = sorted((b for b in data_barang.values() if barang_aktif(b)),
                    key=lambda b: b["kode"])
    if not daftar:
        print("Tidak ada data barang yang aktif.")
        return
    cetak_tabel_barang(daftar)


# ==========================================
# CARI BARANG
# ==========================================
def menu_cari():
    while True:
        print("\n====================")
        print("    MENU CARI")
        print("====================")
        print("1. Berdasarkan kode")
        print("2. Berdasarkan nama")
        print("0. Kembali")
        pilih = input("Pilih Menu (0-2): ").strip()
        if pilih == "1":
            cari_barang_kode()
        elif pilih == "2":
            cari_barang_nama()
        elif pilih == "0":
            break
        else:
            print("Pilihan tidak tersedia. Silakan pilih 0, 1, atau 2.")


def cari_barang_kode():
    print("====================")
    print("  PENCARIAN BERDASARKAN KODE")
    print("====================")
    if len(data_barang) == 0:
        print("Data masih kosong.")
        return

    kode_cari = input("Masukkan kode barang yang dicari: ").strip().lower()
    if kode_cari == "":
        print("Kode tidak boleh kosong.")
        return

    hasil = [b for b in data_barang.values()
             if barang_aktif(b) and kode_cari in b["kode"].lower()]

    if hasil:
        cetak_tabel_barang(sorted(hasil, key=lambda b: b["kode"]))
    else:
        print("Barang dengan kode tersebut tidak ditemukan.")


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

    hasil = [b for b in data_barang.values()
             if barang_aktif(b) and nama_cari in b["nama"].lower()]

    if hasil:
        cetak_tabel_barang(sorted(hasil, key=lambda b: b["kode"]))
    else:
        print("Barang dengan nama tersebut tidak ditemukan.")


# ==========================================
# SORTING BARANG
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
    print("2. Harga Jual")
    print("3. Abjad Nama Barang")
    pilihan = input("Pilih (1-3): ").strip()

    if pilihan == "1":
        kunci, judul = "stok", "STOK"
    elif pilihan == "2":
        kunci, judul = "harga_jual", "HARGA JUAL"
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
    cetak_tabel_barang(hasil)


# ==========================================
# TRANSAKSI PENJUALAN
# ==========================================
def transaksi_penjualan():
    if not any(barang_aktif(b) for b in data_barang.values()):
        print("Tidak ada barang aktif untuk dijual.")
        return

    keranjang = []
    total_belanja = 0

    while True:
        tampilkan_barang()

        print("\n--- Tambah Barang ke Keranjang ---")
        kode = input("Masukkan Kode barang: ").strip().upper()

        if kode not in data_barang or not barang_aktif(data_barang[kode]):
            print("Barang tidak ditemukan atau sudah nonaktif.")
        else:
            barang = data_barang[kode]
            print(f"Barang: {barang['nama']} | Harga: {rupiah(barang['harga_jual'])} | Stok: {barang['stok']}")
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
                subtotal = barang["harga_jual"] * jumlah

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

        tambah_lagi = input("\nTambah barang lain? (y/t): ").lower().strip()
        if tambah_lagi != "y":
            break

    if not keranjang:
        print("Transaksi dibatalkan (Keranjang kosong).")
        return

    print("\n============================")
    print("     RINGKASAN BELANJA")
    print("============================")
    for item in keranjang:
        print(f"{item['nama']} x{item['jumlah']} = {rupiah(item['subtotal'])}")
    print("----------------------------")
    print(f"Total Bayar  : {rupiah(total_belanja)}")

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
            "total": item["subtotal"],
            "harga_beli": item["barang_ref"]["harga_beli"]
        })

    simpan_barang()
    simpan_transaksi()

    print("\n============================")
    print("         SMK MART")
    print("============================")
    print(f"Waktu : {waktu_sekarang}")
    for item in keranjang:
        print(f"{item['nama']} x{item['jumlah']} = {rupiah(item['subtotal'])}")
    print("----------------------------")
    print(f"Total Harga : {rupiah(total_belanja)}")
    print(f"Bayar       : {rupiah(bayar)}")
    print(f"Kembalian   : {rupiah(kembalian)}")
    print("============================")


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
    print("0. Kembali")
    pilihan = input("Pilih (1/2/0): ").strip()

    if pilihan == "0":
        return
    if pilihan not in ("1", "2"):
        print("Pilihan tidak tersedia.")
        return

    tampilkan_barang()
    kode = input("\nKode barang: ").strip().upper()
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

    # === Barang Masuk ===
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

    # === Barang Keluar ===
    elif pilihan == "2":
        if jumlah > barang["stok"]:
            print("Stok tidak mencukupi.")
            return

        print("Contoh alasan: rusak, kedaluwarsa, retur, atau kebutuhan operasional.")
        alasan = bersihkan(input("Alasan barang keluar: "))
        if alasan == "":
            alasan = "-"

        barang["stok"] -= jumlah
        barang_keluar.append({
            "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nama": barang["nama"],
            "kode": barang["kode"],
            "jumlah": jumlah,
            "alasan": alasan,
            "harga_beli": barang["harga_beli"]
        })
        simpan_barang()
        simpan_barang_keluar()
        if "rusak" in alasan.lower():
            print("Barang rusak berhasil dicatat sebagai kerugian pada laporan laba/rugi.")
        else:
            print("Barang keluar berhasil dicatat. Alasan ini tidak dihitung sebagai kerugian barang rusak.")

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
    ubah = input("Ubah batas stok minimum? (y/t): ").lower().strip()

    if ubah == "y":
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

    menipis = [b for b in data_barang.values()
               if barang_aktif(b) and b["stok"] <= stok_minimum]

    if menipis:
        print(f"\nBarang dengan stok <= {stok_minimum}:")
        cetak_tabel_barang(sorted(menipis, key=lambda b: b["stok"]))
    else:
        print("Tidak ada barang yang mencapai batas stok minimum.")


# ==========================================
# LAPORAN PENJUALAN
# ==========================================
def laporan_penjualan():
    print("\n=== LAPORAN PENJUALAN BERDASARKAN RANGE TANGGAL ===")
    if len(transaksi) == 0:
        print("Belum ada transaksi.")
        return

    try:
        tanggal_awal = datetime.strptime(
            input("Tanggal awal (YYYY-MM-DD): ").strip(), "%Y-%m-%d"
        ).date()
        tanggal_akhir = datetime.strptime(
            input("Tanggal akhir (YYYY-MM-DD): ").strip(), "%Y-%m-%d"
        ).date()
    except ValueError:
        print("Format tanggal salah. Gunakan YYYY-MM-DD.")
        return

    if tanggal_awal > tanggal_akhir:
        print("Tanggal awal tidak boleh melewati tanggal akhir.")
        return

    data_filter = []
    for data in transaksi:
        try:
            tanggal_transaksi = datetime.strptime(
                data["waktu"], "%Y-%m-%d %H:%M:%S"
            ).date()
        except ValueError:
            continue
        if tanggal_awal <= tanggal_transaksi <= tanggal_akhir:
            data_filter.append(data)

    if not data_filter:
        print("Tidak ada transaksi pada rentang tanggal tersebut.")
        return

    lebar_nama = max(len("Barang"), max(len(d["nama"]) for d in data_filter))
    lebar_total = max(len("Total"), max(len(rupiah(d["total"])) for d in data_filter))
    header = (f"{'Waktu':<19} | {'Kode':<6} | {'Barang':<{lebar_nama}} | "
              f"{'Jml':>4} | {'Total':>{lebar_total}}")
    garis = "-" * len(header)

    print(f"\nPeriode: {tanggal_awal} s/d {tanggal_akhir}")
    print(garis)
    print(header)
    print(garis)

    total_penjualan = 0
    for data in data_filter:
        print(f"{data['waktu']:<19} | {data['kode']:<6} | {data['nama']:<{lebar_nama}} | "
              f"{data['jumlah']:>4} | {rupiah(data['total']):>{lebar_total}}")
        total_penjualan += data["total"]

    print(garis)
    print(f"Total penjualan: {rupiah(total_penjualan)}")

# ==========================================
# LAPORAN LABA/RUGI
# ==========================================
def laporan_laba_rugi():
    print("\n=== LAPORAN LABA/RUGI BERDASARKAN RANGE TANGGAL ===")
    if not transaksi and not barang_keluar:
        print("Belum ada transaksi penjualan atau barang keluar.")
        return

    try:
        tanggal_awal = datetime.strptime(
            input("Tanggal awal (YYYY-MM-DD): ").strip(), "%Y-%m-%d"
        ).date()
        tanggal_akhir = datetime.strptime(
            input("Tanggal akhir (YYYY-MM-DD): ").strip(), "%Y-%m-%d"
        ).date()
    except ValueError:
        print("Format tanggal salah. Gunakan YYYY-MM-DD.")
        return

    if tanggal_awal > tanggal_akhir:
        print("Tanggal awal tidak boleh melewati tanggal akhir.")
        return

    transaksi_filter = []
    for data in transaksi:
        try:
            tanggal = datetime.strptime(data["waktu"], "%Y-%m-%d %H:%M:%S").date()
        except (ValueError, KeyError, TypeError):
            continue
        if tanggal_awal <= tanggal <= tanggal_akhir:
            transaksi_filter.append(data)

    barang_rusak_filter = []
    barang_keluar_lama_tanpa_tanggal = 0
    for data in barang_keluar:
        if "rusak" not in str(data.get("alasan", "")).lower():
            continue
        if not data.get("waktu"):
            barang_keluar_lama_tanpa_tanggal += 1
            continue
        try:
            tanggal = datetime.strptime(data["waktu"], "%Y-%m-%d %H:%M:%S").date()
        except (ValueError, TypeError):
            barang_keluar_lama_tanpa_tanggal += 1
            continue
        if tanggal_awal <= tanggal <= tanggal_akhir:
            barang_rusak_filter.append(data)

    if not transaksi_filter and not barang_rusak_filter:
        print("Tidak ada transaksi atau barang rusak pada rentang tanggal tersebut.")
        if barang_keluar_lama_tanpa_tanggal:
            print(f"Catatan: {barang_keluar_lama_tanpa_tanggal} catatan barang rusak lama tidak memiliki tanggal sehingga tidak dapat dimasukkan ke periode tertentu.")
        return

    total_pendapatan = 0
    total_modal_terjual = 0
    jumlah_item = 0
    transaksi_estimasi = 0
    for data in transaksi_filter:
        jumlah = data.get("jumlah", 0)
        pendapatan = data.get("total", 0)
        harga_beli = data.get("harga_beli")
        if data.get("modal_estimasi"):
            transaksi_estimasi += 1
        if jumlah <= 0 or pendapatan < 0 or harga_beli is None or harga_beli < 0:
            print("Peringatan: data transaksi " + str(data.get("kode", "-")) + " tidak valid dan dilewati.")
            continue
        total_pendapatan += pendapatan
        total_modal_terjual += harga_beli * jumlah
        jumlah_item += 1

    total_kerugian_rusak = 0
    jumlah_barang_rusak = 0
    catatan_rusak_tanpa_modal = 0
    for data in barang_rusak_filter:
        jumlah = data.get("jumlah", 0)
        harga_beli = data.get("harga_beli")
        # Untuk catatan versi lama tanpa harga beli, gunakan harga beli barang saat ini sebagai estimasi.
        if harga_beli is None and data.get("kode") in data_barang:
            harga_beli = data_barang[data["kode"]].get("harga_beli")
        if jumlah <= 0 or harga_beli is None or harga_beli < 0:
            catatan_rusak_tanpa_modal += 1
            continue
        total_kerugian_rusak += harga_beli * jumlah
        jumlah_barang_rusak += jumlah

    laba = total_pendapatan - total_modal_terjual - total_kerugian_rusak

    print(f"\nPeriode: {tanggal_awal} s/d {tanggal_akhir}")
    print("-" * 48)
    print(f"Jumlah item penjualan : {jumlah_item}")
    print(f"Total Pendapatan      : {rupiah(total_pendapatan)}")
    print(f"Modal barang terjual  : {rupiah(total_modal_terjual)}")
    print(f"Jumlah barang rusak   : {jumlah_barang_rusak}")
    print(f"Kerugian barang rusak : {rupiah(total_kerugian_rusak)}")
    print("-" * 48)
    if laba > 0:
        print(f"LABA                  : {rupiah(laba)}")
    elif laba < 0:
        print(f"RUGI                  : {rupiah(abs(laba))}")
    else:
        print("IMPAS                 : Rp0")

    if transaksi_estimasi:
        print(f"Catatan: {transaksi_estimasi} item transaksi lama menggunakan estimasi harga beli dari barang.txt.")
    if barang_keluar_lama_tanpa_tanggal:
        print(f"Catatan: {barang_keluar_lama_tanpa_tanggal} catatan barang rusak lama tidak memiliki tanggal, sehingga tidak dimasukkan ke periode ini.")
    if catatan_rusak_tanpa_modal:
        print(f"Peringatan: {catatan_rusak_tanpa_modal} catatan barang rusak tidak memiliki data modal dan dilewati.")


# ==========================================
# LAPORAN STOK DAN AKTIVITAS GUDANG
# ==========================================
def laporan_gudang():
    print("\n=== LAPORAN STOK ===")
    if len(data_barang) == 0:
        print("Data barang masih kosong.")
    else:
        cetak_tabel_barang(sorted(data_barang.values(), key=lambda b: b["kode"]),
                           tampil_status=True)

    print("\n=== BARANG MASUK ===")
    if len(barang_masuk) == 0:
        print("Belum ada barang masuk.")
    else:
        lebar = max(len(d["nama"]) for d in barang_masuk)
        for data in barang_masuk:
            print(f"{data['kode']:<6} | {data['nama']:<{lebar}} | Jumlah: {data['jumlah']}")

    print("\n=== BARANG KELUAR ===")
    if len(barang_keluar) == 0:
        print("Belum ada barang keluar.")
    else:
        lebar = max(len(d["nama"]) for d in barang_keluar)
        for data in barang_keluar:
            print(f"{data['kode']:<6} | {data['nama']:<{lebar}} | "
                  f"Jumlah: {data['jumlah']:<5} | Alasan: {data['alasan']}")


# ==========================================
# TAMPILKAN USER
# ==========================================
def tampilkan_user():
    print("\n=== DAFTAR USER ===")
    if len(users) == 0:
        print("Belum ada user.")
        return

    i = max([len(k) for k in users] + [len("ID User")])
    n = max([len(d["Nama"]) for d in users.values()] + [len("Nama")])
    header = f"{'ID User':<{i}} | {'Nama':<{n}} | Posisi"
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    for id_user, data in users.items():
        print(f"{id_user:<{i}} | {data['Nama']:<{n}} | {data['Posisi']}")
    print("-" * len(header))


# ==========================================
# MENU TAMPILAN BARANG
# ==========================================
def menu_tampilan_barang():
    while True:
        print("\n=== TAMPILAN BARANG ===")
        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang")
        print("3. Urutkan Barang (Sorting)")
        print("0. Kembali")
        pilihan = input("Pilihan: ").strip()

        if pilihan == "1":
            tampilkan_barang()
        elif pilihan == "2":
            menu_cari()
        elif pilihan == "3":
            sorting_barang()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak tersedia.")


def menu_laporan():
    while True:
        print("\n=== LAPORAN ===")
        print("1. Laporan Penjualan")
        print("2. Laporan Laba/Rugi")
        print("3. Laporan Stok dan Aktivitas Gudang")
        print("0. Kembali")
        pilihan = input("Pilihan: ").strip()

        if pilihan == "1":
            laporan_penjualan()
        elif pilihan == "2":
            laporan_laba_rugi()
        elif pilihan == "3":
            laporan_gudang()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak tersedia.")


def menu_kelola_user():
    while True:
        print("\n=== KELOLA USER ===")
        print("1. Tampilkan User")
        print("2. Daftarkan Akun")
        print("0. Kembali")
        pilihan = input("Pilihan: ").strip()

        if pilihan == "1":
            tampilkan_user()
        elif pilihan == "2":
            daftar_akun()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak tersedia.")


# ==========================================
# PROGRAM MENU AWAL
# ==========================================
posisi = main_menu()

if posisi is not None:
    print("\n========================")
    print("        SMK MART")
    print("========================")

    while True:
        if posisi == "admin":
            print("\n=== ADMIN ===")
            print("1. Kelola Data Barang")
            print("2. Tampilan Barang")
            print("3. Kelola Stok Barang")
            print("4. Transaksi Penjualan")
            print("5. Laporan")
            print("6. Peringatan Stok Minimum")
            print("7. Kelola User")
            print("8. Log Out Akun")
            print("0. Keluar")

            pilihan = input("Pilih menu: ").strip()

            if pilihan == "1":
                kelola_data_barang()
            elif pilihan == "2":
                menu_tampilan_barang()
            elif pilihan == "3":
                kelola_stok()
            elif pilihan == "4":
                transaksi_penjualan()
            elif pilihan == "5":
                menu_laporan()
            elif pilihan == "6":
                peringatan_stok()
            elif pilihan == "7":
                menu_kelola_user()
            elif pilihan == "8":
                simpan_semua_data()
                posisi = main_menu()
                if posisi is None:
                    break
            elif pilihan == "0":
                simpan_semua_data()
                print("Program Selesai")
                break
            else:
                print("Pilihan tidak tersedia.")

        elif posisi == "kasir":
            print("\n=== KASIR ===")
            print("1. Tampilan Barang")
            print("2. Transaksi Penjualan")
            print("3. Log Out Akun")
            print("0. Keluar")

            pilihan = input("Pilih menu: ").strip()

            if pilihan == "1":
                menu_tampilan_barang()
            elif pilihan == "2":
                transaksi_penjualan()
            elif pilihan == "3":
                simpan_semua_data()
                posisi = main_menu()
                if posisi is None:
                    break
            elif pilihan == "0":
                simpan_semua_data()
                print("Program Selesai")
                break
            else:
                print("Pilihan tidak tersedia")

        elif posisi == "gudang":
            print("\n=== GUDANG ===")
            print("1. Tampilan Barang")
            print("2. Kelola Stok Barang")
            print("3. Peringatan Stok Minimum")
            print("4. Laporan Stok dan Aktivitas Gudang")
            print("5. Log Out Akun")
            print("0. Keluar")

            pilihan = input("Pilih Menu: ").strip()

            if pilihan == "1":
                menu_tampilan_barang()
            elif pilihan == "2":
                kelola_stok()
            elif pilihan == "3":
                peringatan_stok()
            elif pilihan == "4":
                laporan_gudang()
            elif pilihan == "5":
                simpan_semua_data()
                posisi = main_menu()
                if posisi is None:
                    break
            elif pilihan == "0":
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
