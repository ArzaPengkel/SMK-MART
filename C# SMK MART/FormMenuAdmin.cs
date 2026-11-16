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
    public partial class FormMenuAdmin : Form
    {
        public FormMenuAdmin()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            FormKelolaBarang halamanBarang = new FormKelolaBarang();
            halamanBarang.Show();

            this.Hide();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            FormTampilkanBarang halamantampilkan = new FormTampilkanBarang();
            halamantampilkan.Show();

            this.Hide();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            FormStok halamanStok = new FormStok();
            halamanStok.Show();

            this.Hide();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            FormDaftarUser halamanUser = new FormDaftarUser();
            halamanUser.Show();
            this.Hide();
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
                // Buka halaman Login dan tutup halaman Kelola Barang
                FormLogin halamanLogin = new FormLogin();
                halamanLogin.Show();
                this.Close();
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            FormLaporan halamanLapor = new FormLaporan();
            halamanLapor.Show();
            this.Close();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            FormTransaksi halamanTransaksi = new FormTransaksi();
            halamanTransaksi.Show();
            this.Close();
        }

       
    }
}
