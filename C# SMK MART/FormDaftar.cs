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
    public partial class FormDaftar : Form
    {

        string filepath = Path.Combine(Application.StartupPath, "dataUser.txt");

        public FormDaftar()
        {
            InitializeComponent();
        }


        private void button1_Click(object sender, EventArgs e)
        {

            // Mengambil data dari TextBox
            string username = textBox1.Text.Trim();
            string idUser = textBox2.Text.Trim();
            string password = textBox3.Text;
            string role = textBox4.Text.Trim().ToLower();

            // Memeriksa apakah semua data sudah diisi
            if (username == "" || idUser == "" ||
                password == "" || role == "")
            {
                MessageBox.Show("Semua data harus diisi!",
                    "Peringatan",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
                return;
            }

            // Memeriksa Role
            if (role != "admin" &&
                role != "gudang" &&
                role != "kasir")
            {
                MessageBox.Show("Role hanya boleh admin, gudang, atau kasir!",
                    "Role Tidak Valid",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Warning);
                return;
            }

            // Membuat file jika belum tersedia
            if (!File.Exists(filepath))
            {
                File.Create(filepath).Close();
            }

            // Memeriksa Username dan ID User agar tidak duplikat
            string[] dataUser = File.ReadAllLines(filepath);

            foreach (string data in dataUser)
            {
                string[] kolom = data.Split('|');

                if (kolom.Length >= 2)
                {
                    if (kolom[0] == username)
                    {
                        MessageBox.Show("Username sudah digunakan!");
                        return;
                    }

                    if (kolom[1] == idUser)
                    {
                        MessageBox.Show("ID User sudah digunakan!");
                        return;
                    }
                }
            }

            // Menyimpan data akun
            string dataBaru = username + "|" +
                              idUser + "|" +
                              password + "|" +
                              role;

            File.AppendAllText(filepath, dataBaru + Environment.NewLine);

            MessageBox.Show("Pendaftaran akun berhasil!",
                "Berhasil",
                MessageBoxButtons.OK,
                MessageBoxIcon.Information);

            // Mengosongkan TextBox
            textBox1.Clear();
            textBox2.Clear();
            textBox3.Clear();
            textBox4.Clear();

            textBox1.Focus();
        }


        private void textBox1_TextChanged(object sender, EventArgs e)
        {
           
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
           
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {
          
        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {
            
        }


        
        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {
        
        }

        private void label3_Click(object sender, EventArgs e)
        {
            
        }

        private void label4_Click(object sender, EventArgs e)
        {
            
        }

        private void label5_Click(object sender, EventArgs e)
        {
           
        }


        private void tableLayoutPanel1_Paint(object sender, PaintEventArgs e)
        {
           
        }

        }
    }