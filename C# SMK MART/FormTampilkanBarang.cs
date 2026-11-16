using ReaLTaiizor.Controls;
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
    public partial class FormTampilkanBarang : Form
    {
        private string filePath = Path.Combine(
        Environment.GetFolderPath(Environment.SpecialFolder.UserProfile),
        @"Downloads\Ngoding\Pyhton SMK MART\barang.txt");


        private FileSystemWatcher? pemantauFile;

        public FormTampilkanBarang()
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

            poisonDataGridView2.Rows.Clear();
            string[] semuaBaris = File.ReadAllLines(filePath);

            foreach (string baris in semuaBaris)
            {
                if (string.IsNullOrWhiteSpace(baris)) continue;

                string[] data = baris.Split('|');
                if (data.Length >= 4)
                {
                    string kode = data[0].Trim();
                    string nama = data[1].Trim();
                    string harga = "Rp" + int.Parse(data[2].Trim()).ToString("N0"); // Format ribuan: Rp3.000
                    string stok = data[3].Trim();
                    string status = data[4].Trim();

                    if (status.Equals("aktif", StringComparison.OrdinalIgnoreCase))


                        poisonDataGridView2.Rows.Add(kode, nama, harga, stok);
                }
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

                this.Invoke((MethodInvoker)delegate
                {
                    System.Threading.Thread.Sleep(100);
                    MuatDataDariTxt();
                });
            };
            pemantauFile.EnableRaisingEvents = true;
        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void parrotButton2_Click(object sender, EventArgs e)
        {

            DialogResult konfirmasi = MessageBox.Show(
                "Apakah Anda yakin ingin Log out dari akun ini?",
                "Konfirmasi Log Out",
                MessageBoxButtons.YesNo,
                MessageBoxIcon.Question
            );

            if (konfirmasi == DialogResult.Yes)
            {

                if (pemantauFile != null)
                {
                    pemantauFile.EnableRaisingEvents = false;
                    pemantauFile.Dispose();
                }

                FormLogin halamanLogin = new FormLogin();
                halamanLogin.Show();
                this.Close();
            }
        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void poisonDataGridView2_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void parrotButton3_Click(object sender, EventArgs e)
        {
            FormMenuAdmin halamanMenu = new FormMenuAdmin();
            halamanMenu.Show();
            this.Close();
        }
    }
}
