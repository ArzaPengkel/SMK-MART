namespace SMK_MART
{
    public partial class FormLogin : Form
    {
        public FormLogin()
        {
            InitializeComponent();
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void panel2_Paint(object sender, PaintEventArgs e)
        {

        }

        private void textBox1_TextChanged_1(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {

        }

        private void panel1_Paint_1(object sender, PaintEventArgs e)
        {

        }

        private void label8_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

            // 1. Cek apakah ID user atau Password kosong
            if (string.IsNullOrWhiteSpace(hopeTextBox1.Text) || string.IsNullOrWhiteSpace(hopeTextBox2.Text))
            {
                MessageBox.Show("ID user dan Password wajib diisi!", "Peringatan", MessageBoxButtons.OK, MessageBoxIcon.Warning);

                // Arahkan kursor kembali ke kotak yang masih kosong
                if (string.IsNullOrWhiteSpace(textBox1.Text))
                {
                    hopeTextBox1.Focus();
                }
                else
                {
                    hopeTextBox2.Focus();
                }

                return; // Menghentikan proses agar tidak lanjut mengecek ke bawah
            }

            // 2. Cek kecocokan ID user dan Password
            if (hopeTextBox1.Text == "5678" && hopeTextBox2.Text == "admin123")
            {
                MessageBox.Show("Login berhasil! Selamat datang di SMK MART.", "Informasi", MessageBoxButtons.OK, MessageBoxIcon.Information);

                FormMenuAdmin menu = new FormMenuAdmin();
                menu.Show();
                this.Hide();
            }
            else
            {
                MessageBox.Show("ID user atau Password salah!", "Peringatan", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                hopeTextBox2.Clear(); // Mengosongkan password agar pengguna mudah mengetik ulang
                hopeTextBox2.Focus();
            }

        }

        private void hopeTextBox1_Click(object sender, EventArgs e)
        {

        }

        private void hopeTextBox2_Click(object sender, EventArgs e)
        {

        }
    }
}
