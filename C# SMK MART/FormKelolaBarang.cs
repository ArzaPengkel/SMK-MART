using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SMK_MART
{
    public partial class FormKelolaBarang : Form
    {
        private string filePath = Path.Combine(
            Environment.GetFolderPath(Environment.SpecialFolder.UserProfile),
            @"Downloads\Ngoding\Pyhton SMK MART\barang.txt");

        private FileSystemWatcher? pemantauFile;

        public FormKelolaBarang()
        {
            InitializeComponent();
        }

        private void FormKelolaBarang_Load(object sender, EventArgs e)
        {

            // 1. Memuat data awal dari file .txt ke tabel
            MuatDataDariTxt();

            // 2. Mengaktifkan pemantau file otomatis (jika Python mengedit file .txt)
            MulaiPemantauFile();
        }

        private void MuatDataDariTxt()
        {
            if (!File.Exists(filePath)) return;

            poisonDataGridView1.Rows.Clear();
            string[] semuaBaris = File.ReadAllLines(filePath);

            foreach (string baris in semuaBaris)
            {
                if (string.IsNullOrWhiteSpace(baris)) continue;

                string[] data = baris.Split('|');
                if (data.Length >= 5)
                {
                    string kode = data[0].Trim();
                    string nama = data[1].Trim();
                    string harga = "Rp" + int.Parse(data[2].Trim()).ToString("N0"); // Format ribuan: Rp3.000
                    string stok = data[3].Trim();
                    string status = data[4].Trim();
                    string teksTombol = (status == "aktif") ? "Nonaktifkan" : "Aktifkan";

                    poisonDataGridView1.Rows.Add(kode, nama, harga, stok, status, teksTombol);
                }
            }
            int totalBarang = poisonDataGridView1.Rows.Count;
            int barangAktif = 0;
            int stokMenipis = 0;

            foreach (DataGridViewRow baris in poisonDataGridView1.Rows)
            {
                if (baris.Cells[4].Value?.ToString() == "aktif") barangAktif++;

                int stok = int.Parse(baris.Cells[3].Value?.ToString() ?? "0");
                if (stok <= 5) stokMenipis++;
            }

            label8.Text = $"Ringkasan Data:\n" +
                                      $"• Total Produk: {totalBarang} item\n" +
                                      $"• Status Aktif: {barangAktif} item\n" +
                                      $"• Stok Menipis (≤5): {stokMenipis} item";

            label4.Text = "Kode Barang: " + BuatKodeOtomatis();
        }
        private string BuatKodeOtomatis()
        {
            if (!File.Exists(filePath)) return "B001";

            string[] semuaBaris = File.ReadAllLines(filePath)
                                      .Where(b => !string.IsNullOrWhiteSpace(b))
                                      .ToArray();

            if (semuaBaris.Length == 0) return "B001";

            // Ambil baris terakhir (misal: B011|Air Putih|3000|10|aktif)
            string barisTerakhir = semuaBaris[semuaBaris.Length - 1];
            string kodeTerakhir = barisTerakhir.Split('|')[0].Trim(); // Hasil: "B011"

            int angkaBerikutnya = int.Parse(kodeTerakhir.Substring(1)) + 1;
            return "B" + angkaBerikutnya.ToString("D3"); // Hasil: "B012"
        }

       
        private void btnSimpanBarang_Click(object sender, EventArgs e)
        {
            if (string.IsNullOrWhiteSpace(TextBarang.Text) ||
                string.IsNullOrWhiteSpace(TextHarga.Text) ||
                string.IsNullOrWhiteSpace(TextStok.Text))
            {
                MessageBox.Show("Semua kolom harus diisi!", "Peringatan", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            string kodeBaru = BuatKodeOtomatis();
            string nama = TextBarang.Text.Trim();
            string harga = TextHarga.Text.Trim();
            string stok = TextStok.Text.Trim();
            string status = "aktif";

            string barisBaru = $"{kodeBaru}|{nama}|{harga}|{stok}|{status}";

            File.AppendAllText(filePath, Environment.NewLine + barisBaru);

            TextBarang.Clear();
            TextHarga.Clear();
            TextStok.Clear();
            MuatDataDariTxt();

            MessageBox.Show($"Barang {nama} ({kodeBaru}) berhasil disimpan!", "Sukses");
        }

        private void hopeTextBox3_Click(object sender, EventArgs e)
        {

        }

        private void label7_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void parrotButton2_Click(object sender, EventArgs e)
        {
            if (string.IsNullOrWhiteSpace(TextBarang.Text) ||
                string.IsNullOrWhiteSpace(TextHarga.Text) ||
                string.IsNullOrWhiteSpace(TextStok.Text))
            {
                MessageBox.Show("Semua kolom harus diisi!", "Peringatan", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            string kodeBaru = BuatKodeOtomatis();
            string nama = TextBarang.Text.Trim();
            string harga = TextHarga.Text.Trim();
            string stok = TextStok.Text.Trim();
            string status = "aktif";

            // Susun format baris persis seperti file Python: B012|Sabun|4500|20|aktif
            string barisBaru = $"{kodeBaru}|{nama}|{harga}|{stok}|{status}";

            File.AppendAllText(filePath, Environment.NewLine + barisBaru);

            // Kosongkan input dan muat ulang tabel
            TextBarang.Clear();
            TextHarga.Clear();
            TextStok.Clear();
            MuatDataDariTxt();

            MessageBox.Show($"Barang {nama} ({kodeBaru}) berhasil disimpan!", "Sukses");

        }

        private void poisonDataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            // Pastikan yang diklik adalah kolom tombol Aksi (indeks kolom ke-5)
            if (e.RowIndex >= 0 && e.ColumnIndex == 5)
            {
                string kodeDipilih = poisonDataGridView1.Rows[e.RowIndex].Cells[0].Value?.ToString() ?? "";
                string[] semuaBaris = File.ReadAllLines(filePath);

                for (int i = 0; i < semuaBaris.Length; i++)
                {
                    string[] data = semuaBaris[i].Split('|');
                    if (data.Length >= 5 && data[0].Trim() == kodeDipilih)
                    {
                        // Tukar status aktif <-> nonaktif
                        string statusBaru = (data[4].Trim() == "aktif") ? "nonaktif" : "aktif";
                        semuaBaris[i] = $"{data[0]}|{data[1]}|{data[2]}|{data[3]}|{statusBaru}";
                        break;
                    }
                }

                File.WriteAllLines(filePath, semuaBaris);
                MuatDataDariTxt();
            }

        }

        private void MulaiPemantauFile()
        {
            string folder = Path.GetDirectoryName(filePath) ?? "";
            string namaFile = Path.GetFileName(filePath);

            if (!Directory.Exists(folder)) return;

            pemantauFile = new FileSystemWatcher(folder, namaFile);
            pemantauFile.NotifyFilter = NotifyFilters.LastWrite;
            pemantauFile.Changed += (s, ev) =>
            {
                // Jalankan MuatDataDariTxt di thread UI dengan jeda singkat agar file selesai ditulis Python
                this.Invoke((MethodInvoker)delegate
                {
                    System.Threading.Thread.Sleep(100);
                    MuatDataDariTxt();
                });
            };
            pemantauFile.EnableRaisingEvents = true;
        }

        private void parrotButton1_Click(object sender, EventArgs e)
        {
            // Menampilkan kotak dialog konfirmasi Ya / Tidak
            DialogResult konfirmasi = MessageBox.Show(
                "Apakah Anda yakin ingin Log out dari akun ini?",
                "Konfirmasi Log Out",
                MessageBoxButtons.YesNo,
                MessageBoxIcon.Question
            );

            if (konfirmasi == DialogResult.Yes)
            {
                // Matikan pemantau file agar tidak berjalan di latar belakang setelah form ditutup
                if (pemantauFile != null)
                {
                    pemantauFile.EnableRaisingEvents = false;
                    pemantauFile.Dispose();
                }

                // Buka halaman Login dan tutup halaman Kelola Barang
                FormLogin halamanLogin = new FormLogin();
                halamanLogin.Show();
                this.Close();
            }
        }

        private void parrotButton3_Click(object sender, EventArgs e)
        {
            FormMenuAdmin halamanMenu = new FormMenuAdmin();
            halamanMenu.Show();
            this.Close();
        }

        private void panel6_Paint(object sender, PaintEventArgs e)
        {
           
        }
    }
}   
