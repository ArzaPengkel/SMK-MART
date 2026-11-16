namespace SMK_MART
{
    partial class FormKelolaBarang
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            DataGridViewCellStyle dataGridViewCellStyle1 = new DataGridViewCellStyle();
            DataGridViewCellStyle dataGridViewCellStyle2 = new DataGridViewCellStyle();
            DataGridViewCellStyle dataGridViewCellStyle3 = new DataGridViewCellStyle();
            tableLayoutPanel1 = new TableLayoutPanel();
            panel1 = new Panel();
            poisonDataGridView1 = new ReaLTaiizor.Controls.PoisonDataGridView();
            Column1 = new DataGridViewTextBoxColumn();
            Column2 = new DataGridViewTextBoxColumn();
            Column3 = new DataGridViewTextBoxColumn();
            Column4 = new DataGridViewTextBoxColumn();
            Column5 = new DataGridViewTextBoxColumn();
            Column6 = new DataGridViewTextBoxColumn();
            panel4 = new Panel();
            label1 = new Label();
            panel2 = new Panel();
            panel6 = new Panel();
            label8 = new Label();
            panel5 = new Panel();
            parrotButton2 = new ReaLTaiizor.Controls.ParrotButton();
            TextStok = new ReaLTaiizor.Controls.HopeTextBox();
            TextHarga = new ReaLTaiizor.Controls.HopeTextBox();
            label7 = new Label();
            label6 = new Label();
            TextBarang = new ReaLTaiizor.Controls.HopeTextBox();
            label5 = new Label();
            label4 = new Label();
            label2 = new Label();
            panel3 = new Panel();
            parrotButton3 = new ReaLTaiizor.Controls.ParrotButton();
            parrotButton1 = new ReaLTaiizor.Controls.ParrotButton();
            label3 = new Label();
            tableLayoutPanel1.SuspendLayout();
            panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)poisonDataGridView1).BeginInit();
            panel2.SuspendLayout();
            panel6.SuspendLayout();
            panel3.SuspendLayout();
            SuspendLayout();
            // 
            // tableLayoutPanel1
            // 
            tableLayoutPanel1.BackColor = Color.Gainsboro;
            tableLayoutPanel1.ColumnCount = 2;
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 65F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 35F));
            tableLayoutPanel1.Controls.Add(panel1, 0, 0);
            tableLayoutPanel1.Controls.Add(panel2, 1, 0);
            tableLayoutPanel1.Dock = DockStyle.Fill;
            tableLayoutPanel1.Location = new Point(0, 55);
            tableLayoutPanel1.Name = "tableLayoutPanel1";
            tableLayoutPanel1.RowCount = 1;
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 100F));
            tableLayoutPanel1.Size = new Size(901, 581);
            tableLayoutPanel1.TabIndex = 0;
            // 
            // panel1
            // 
            panel1.BackColor = Color.White;
            panel1.Controls.Add(poisonDataGridView1);
            panel1.Controls.Add(panel4);
            panel1.Controls.Add(label1);
            panel1.Dock = DockStyle.Fill;
            panel1.Location = new Point(20, 20);
            panel1.Margin = new Padding(20);
            panel1.Name = "panel1";
            panel1.Padding = new Padding(20, 20, 10, 20);
            panel1.Size = new Size(545, 541);
            panel1.TabIndex = 0;
            // 
            // poisonDataGridView1
            // 
            poisonDataGridView1.AllowUserToAddRows = false;
            poisonDataGridView1.AllowUserToResizeRows = false;
            poisonDataGridView1.AutoSizeColumnsMode = DataGridViewAutoSizeColumnsMode.Fill;
            poisonDataGridView1.AutoSizeRowsMode = DataGridViewAutoSizeRowsMode.AllCells;
            poisonDataGridView1.BackgroundColor = Color.FromArgb(255, 255, 255);
            poisonDataGridView1.BorderStyle = BorderStyle.None;
            poisonDataGridView1.CellBorderStyle = DataGridViewCellBorderStyle.None;
            poisonDataGridView1.ColumnHeadersBorderStyle = DataGridViewHeaderBorderStyle.None;
            dataGridViewCellStyle1.Alignment = DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle1.BackColor = Color.Gainsboro;
            dataGridViewCellStyle1.Font = new Font("Segoe UI Semibold", 15.75F, FontStyle.Bold, GraphicsUnit.Point, 0);
            dataGridViewCellStyle1.ForeColor = Color.Navy;
            dataGridViewCellStyle1.SelectionBackColor = Color.Gainsboro;
            dataGridViewCellStyle1.SelectionForeColor = Color.Navy;
            dataGridViewCellStyle1.WrapMode = DataGridViewTriState.True;
            poisonDataGridView1.ColumnHeadersDefaultCellStyle = dataGridViewCellStyle1;
            poisonDataGridView1.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            poisonDataGridView1.Columns.AddRange(new DataGridViewColumn[] { Column1, Column2, Column3, Column4, Column5, Column6 });
            dataGridViewCellStyle2.Alignment = DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle2.BackColor = Color.FromArgb(255, 255, 255);
            dataGridViewCellStyle2.Font = new Font("Segoe UI", 15.75F, FontStyle.Regular, GraphicsUnit.Point, 0);
            dataGridViewCellStyle2.ForeColor = Color.FromArgb(64, 64, 64);
            dataGridViewCellStyle2.SelectionBackColor = Color.DarkGray;
            dataGridViewCellStyle2.SelectionForeColor = Color.FromArgb(64, 64, 64);
            dataGridViewCellStyle2.WrapMode = DataGridViewTriState.False;
            poisonDataGridView1.DefaultCellStyle = dataGridViewCellStyle2;
            poisonDataGridView1.Dock = DockStyle.Fill;
            poisonDataGridView1.EnableHeadersVisualStyles = false;
            poisonDataGridView1.Font = new Font("Segoe UI", 11F, FontStyle.Regular, GraphicsUnit.Pixel);
            poisonDataGridView1.GridColor = Color.Silver;
            poisonDataGridView1.Location = new Point(20, 52);
            poisonDataGridView1.Name = "poisonDataGridView1";
            poisonDataGridView1.RowHeadersBorderStyle = DataGridViewHeaderBorderStyle.None;
            dataGridViewCellStyle3.Alignment = DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle3.BackColor = Color.FromArgb(0, 174, 219);
            dataGridViewCellStyle3.Font = new Font("Segoe UI", 11F, FontStyle.Regular, GraphicsUnit.Pixel);
            dataGridViewCellStyle3.ForeColor = Color.FromArgb(255, 255, 255);
            dataGridViewCellStyle3.SelectionBackColor = Color.FromArgb(0, 198, 247);
            dataGridViewCellStyle3.SelectionForeColor = Color.FromArgb(17, 17, 17);
            dataGridViewCellStyle3.WrapMode = DataGridViewTriState.True;
            poisonDataGridView1.RowHeadersDefaultCellStyle = dataGridViewCellStyle3;
            poisonDataGridView1.RowHeadersVisible = false;
            poisonDataGridView1.RowHeadersWidthSizeMode = DataGridViewRowHeadersWidthSizeMode.DisableResizing;
            poisonDataGridView1.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
            poisonDataGridView1.Size = new Size(515, 469);
            poisonDataGridView1.TabIndex = 1;
            poisonDataGridView1.CellContentClick += poisonDataGridView1_CellContentClick;
            // 
            // Column1
            // 
            Column1.FillWeight = 70F;
            Column1.HeaderText = "Kode";
            Column1.Name = "Column1";
            // 
            // Column2
            // 
            Column2.FillWeight = 180F;
            Column2.HeaderText = "Nama";
            Column2.Name = "Column2";
            // 
            // Column3
            // 
            Column3.FillWeight = 90F;
            Column3.HeaderText = "Harga";
            Column3.Name = "Column3";
            // 
            // Column4
            // 
            Column4.FillWeight = 90F;
            Column4.HeaderText = "Stok";
            Column4.Name = "Column4";
            // 
            // Column5
            // 
            Column5.FillWeight = 90F;
            Column5.HeaderText = "Status";
            Column5.Name = "Column5";
            // 
            // Column6
            // 
            Column6.FillWeight = 90F;
            Column6.HeaderText = "Aksi";
            Column6.Name = "Column6";
            // 
            // panel4
            // 
            panel4.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            panel4.BackColor = Color.Navy;
            panel4.Location = new Point(0, 0);
            panel4.Name = "panel4";
            panel4.Size = new Size(545, 10);
            panel4.TabIndex = 2;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Dock = DockStyle.Top;
            label1.Font = new Font("Segoe UI Semibold", 18F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label1.ForeColor = Color.Navy;
            label1.Location = new Point(20, 20);
            label1.Name = "label1";
            label1.Size = new Size(225, 32);
            label1.TabIndex = 0;
            label1.Text = "Kelola Data Barang";
            label1.TextAlign = ContentAlignment.TopCenter;
            // 
            // panel2
            // 
            panel2.BackColor = Color.White;
            panel2.Controls.Add(panel6);
            panel2.Controls.Add(panel5);
            panel2.Controls.Add(parrotButton2);
            panel2.Controls.Add(TextStok);
            panel2.Controls.Add(TextHarga);
            panel2.Controls.Add(label7);
            panel2.Controls.Add(label6);
            panel2.Controls.Add(TextBarang);
            panel2.Controls.Add(label5);
            panel2.Controls.Add(label4);
            panel2.Controls.Add(label2);
            panel2.Dock = DockStyle.Fill;
            panel2.Location = new Point(595, 20);
            panel2.Margin = new Padding(10, 20, 20, 20);
            panel2.Name = "panel2";
            panel2.Padding = new Padding(20, 15, 20, 20);
            panel2.Size = new Size(286, 541);
            panel2.TabIndex = 1;
            // 
            // panel6
            // 
            panel6.Anchor = AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            panel6.BackColor = Color.FromArgb(255, 192, 128);
            panel6.Controls.Add(label8);
            panel6.Font = new Font("Segoe UI", 26.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            panel6.Location = new Point(17, 377);
            panel6.Name = "panel6";
            panel6.Size = new Size(255, 136);
            panel6.TabIndex = 9;
            panel6.Paint += panel6_Paint;
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label8.Location = new Point(11, 28);
            label8.Name = "label8";
            label8.Size = new Size(96, 21);
            label8.TabIndex = 0;
            label8.Text = "Total Produk";
            // 
            // panel5
            // 
            panel5.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            panel5.BackColor = Color.FromArgb(5, 150, 105);
            panel5.Location = new Point(0, 0);
            panel5.Name = "panel5";
            panel5.Size = new Size(286, 12);
            panel5.TabIndex = 3;
            // 
            // parrotButton2
            // 
            parrotButton2.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            parrotButton2.BackgroundColor = Color.FromArgb(255, 128, 0);
            parrotButton2.ButtonImage = null;
            parrotButton2.ButtonStyle = ReaLTaiizor.Controls.ParrotButton.Style.MaterialRounded;
            parrotButton2.ButtonText = "Tambah Barang";
            parrotButton2.ClickBackColor = Color.DimGray;
            parrotButton2.ClickTextColor = Color.DimGray;
            parrotButton2.CornerRadius = 5;
            parrotButton2.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            parrotButton2.Horizontal_Alignment = StringAlignment.Center;
            parrotButton2.HoverBackgroundColor = Color.FromArgb(225, 225, 225);
            parrotButton2.HoverTextColor = Color.DodgerBlue;
            parrotButton2.ImagePosition = ReaLTaiizor.Controls.ParrotButton.ImgPosition.Left;
            parrotButton2.Location = new Point(13, 329);
            parrotButton2.Name = "parrotButton2";
            parrotButton2.Size = new Size(259, 42);
            parrotButton2.SmoothingType = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            parrotButton2.TabIndex = 8;
            parrotButton2.TextColor = Color.Black;
            parrotButton2.TextRenderingType = System.Drawing.Text.TextRenderingHint.ClearTypeGridFit;
            parrotButton2.Vertical_Alignment = StringAlignment.Center;
            parrotButton2.Click += parrotButton2_Click;
            // 
            // TextStok
            // 
            TextStok.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            TextStok.BackColor = Color.White;
            TextStok.BaseColor = Color.White;
            TextStok.BorderColorA = Color.DarkGray;
            TextStok.BorderColorB = Color.DarkGray;
            TextStok.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            TextStok.ForeColor = Color.FromArgb(48, 49, 51);
            TextStok.Hint = "";
            TextStok.Location = new Point(13, 267);
            TextStok.MaxLength = 32767;
            TextStok.Multiline = false;
            TextStok.Name = "TextStok";
            TextStok.PasswordChar = '\0';
            TextStok.ScrollBars = ScrollBars.None;
            TextStok.SelectedText = "";
            TextStok.SelectionLength = 0;
            TextStok.SelectionStart = 0;
            TextStok.Size = new Size(258, 42);
            TextStok.TabIndex = 7;
            TextStok.TabStop = false;
            TextStok.UseSystemPasswordChar = false;
            TextStok.Click += hopeTextBox3_Click;
            // 
            // TextHarga
            // 
            TextHarga.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            TextHarga.BackColor = Color.White;
            TextHarga.BaseColor = Color.White;
            TextHarga.BorderColorA = Color.DarkGray;
            TextHarga.BorderColorB = Color.DarkGray;
            TextHarga.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            TextHarga.ForeColor = Color.FromArgb(48, 49, 51);
            TextHarga.Hint = "";
            TextHarga.Location = new Point(13, 185);
            TextHarga.MaxLength = 32767;
            TextHarga.Multiline = false;
            TextHarga.Name = "TextHarga";
            TextHarga.PasswordChar = '\0';
            TextHarga.ScrollBars = ScrollBars.None;
            TextHarga.SelectedText = "";
            TextHarga.SelectionLength = 0;
            TextHarga.SelectionStart = 0;
            TextHarga.Size = new Size(258, 42);
            TextHarga.TabIndex = 6;
            TextHarga.TabStop = false;
            TextHarga.UseSystemPasswordChar = false;
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label7.ForeColor = Color.DimGray;
            label7.Location = new Point(13, 243);
            label7.Name = "label7";
            label7.Size = new Size(47, 21);
            label7.TabIndex = 5;
            label7.Text = "Stok :";
            label7.Click += label7_Click;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label6.ForeColor = Color.DimGray;
            label6.Location = new Point(14, 161);
            label6.Name = "label6";
            label6.Size = new Size(59, 21);
            label6.TabIndex = 4;
            label6.Text = "Harga :";
            // 
            // TextBarang
            // 
            TextBarang.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            TextBarang.BackColor = Color.White;
            TextBarang.BaseColor = Color.White;
            TextBarang.BorderColorA = Color.DarkGray;
            TextBarang.BorderColorB = Color.DarkGray;
            TextBarang.Font = new Font("Segoe UI", 14.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
            TextBarang.ForeColor = Color.Black;
            TextBarang.Hint = "";
            TextBarang.Location = new Point(14, 103);
            TextBarang.MaxLength = 32767;
            TextBarang.Multiline = false;
            TextBarang.Name = "TextBarang";
            TextBarang.PasswordChar = '\0';
            TextBarang.ScrollBars = ScrollBars.None;
            TextBarang.SelectedText = "";
            TextBarang.SelectionLength = 0;
            TextBarang.SelectionStart = 0;
            TextBarang.Size = new Size(258, 42);
            TextBarang.TabIndex = 3;
            TextBarang.TabStop = false;
            TextBarang.UseSystemPasswordChar = false;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.BackColor = Color.Transparent;
            label5.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label5.ForeColor = Color.DimGray;
            label5.Location = new Point(13, 79);
            label5.Name = "label5";
            label5.Size = new Size(112, 21);
            label5.TabIndex = 2;
            label5.Text = "Nama Barang :";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label4.ForeColor = Color.DimGray;
            label4.Location = new Point(13, 50);
            label4.Name = "label4";
            label4.Size = new Size(52, 21);
            label4.TabIndex = 1;
            label4.Text = "Kode :";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Segoe UI Semibold", 18F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label2.ForeColor = Color.FromArgb(5, 150, 105);
            label2.Location = new Point(2, 15);
            label2.Name = "label2";
            label2.Size = new Size(225, 32);
            label2.TabIndex = 0;
            label2.Text = "Tambahkan Barang";
            label2.Click += label2_Click;
            // 
            // panel3
            // 
            panel3.BackColor = Color.Navy;
            panel3.Controls.Add(parrotButton3);
            panel3.Controls.Add(parrotButton1);
            panel3.Controls.Add(label3);
            panel3.Dock = DockStyle.Top;
            panel3.Location = new Point(0, 0);
            panel3.Name = "panel3";
            panel3.Size = new Size(901, 55);
            panel3.TabIndex = 2;
            // 
            // parrotButton3
            // 
            parrotButton3.BackgroundColor = Color.Gold;
            parrotButton3.ButtonImage = null;
            parrotButton3.ButtonStyle = ReaLTaiizor.Controls.ParrotButton.Style.MaterialRounded;
            parrotButton3.ButtonText = "Kembali";
            parrotButton3.ClickBackColor = Color.FromArgb(195, 195, 195);
            parrotButton3.ClickTextColor = Color.DodgerBlue;
            parrotButton3.CornerRadius = 5;
            parrotButton3.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            parrotButton3.Horizontal_Alignment = StringAlignment.Center;
            parrotButton3.HoverBackgroundColor = Color.FromArgb(225, 225, 225);
            parrotButton3.HoverTextColor = Color.DodgerBlue;
            parrotButton3.ImagePosition = ReaLTaiizor.Controls.ParrotButton.ImgPosition.Left;
            parrotButton3.Location = new Point(170, 12);
            parrotButton3.Name = "parrotButton3";
            parrotButton3.Size = new Size(95, 37);
            parrotButton3.SmoothingType = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            parrotButton3.TabIndex = 4;
            parrotButton3.TextColor = Color.Black;
            parrotButton3.TextRenderingType = System.Drawing.Text.TextRenderingHint.ClearTypeGridFit;
            parrotButton3.Vertical_Alignment = StringAlignment.Center;
            parrotButton3.Click += parrotButton3_Click;
            // 
            // parrotButton1
            // 
            parrotButton1.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            parrotButton1.BackgroundColor = Color.Gold;
            parrotButton1.ButtonImage = null;
            parrotButton1.ButtonStyle = ReaLTaiizor.Controls.ParrotButton.Style.MaterialRounded;
            parrotButton1.ButtonText = "Log out";
            parrotButton1.ClickBackColor = Color.FromArgb(195, 195, 195);
            parrotButton1.ClickTextColor = Color.Black;
            parrotButton1.CornerRadius = 10;
            parrotButton1.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            parrotButton1.Horizontal_Alignment = StringAlignment.Center;
            parrotButton1.HoverBackgroundColor = Color.FromArgb(225, 225, 225);
            parrotButton1.HoverTextColor = Color.DodgerBlue;
            parrotButton1.ImagePosition = ReaLTaiizor.Controls.ParrotButton.ImgPosition.Left;
            parrotButton1.Location = new Point(802, 9);
            parrotButton1.Name = "parrotButton1";
            parrotButton1.Size = new Size(88, 37);
            parrotButton1.SmoothingType = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            parrotButton1.TabIndex = 3;
            parrotButton1.TextColor = Color.Black;
            parrotButton1.TextRenderingType = System.Drawing.Text.TextRenderingHint.ClearTypeGridFit;
            parrotButton1.Vertical_Alignment = StringAlignment.Center;
            parrotButton1.Click += parrotButton1_Click;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Segoe UI", 20.25F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label3.ForeColor = Color.Gold;
            label3.Location = new Point(3, 9);
            label3.Name = "label3";
            label3.Size = new Size(161, 37);
            label3.TabIndex = 0;
            label3.Text = "SMK MART";
            // 
            // FormKelolaBarang
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(901, 636);
            Controls.Add(tableLayoutPanel1);
            Controls.Add(panel3);
            Name = "FormKelolaBarang";
            Text = "FormKelolaBarang";
            WindowState = FormWindowState.Maximized;
            Load += FormKelolaBarang_Load;
            tableLayoutPanel1.ResumeLayout(false);
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)poisonDataGridView1).EndInit();
            panel2.ResumeLayout(false);
            panel2.PerformLayout();
            panel6.ResumeLayout(false);
            panel6.PerformLayout();
            panel3.ResumeLayout(false);
            panel3.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private TableLayoutPanel tableLayoutPanel1;
        private Panel panel1;
        private Label label1;
        private ReaLTaiizor.Controls.PoisonDataGridView poisonDataGridView1;
        private Panel panel2;
        private Label label2;
        private Panel panel3;
        private ReaLTaiizor.Controls.ParrotButton parrotButton1;
        private Label label3;
        private Label label4;
        private Label label5;
        private ReaLTaiizor.Controls.HopeTextBox TextBarang;
        private ReaLTaiizor.Controls.HopeTextBox TextStok;
        private ReaLTaiizor.Controls.HopeTextBox TextHarga;
        private Label label7;
        private Label label6;
        private ReaLTaiizor.Controls.ParrotButton parrotButton2;
        private Panel panel4;
        private Panel panel5;
        private ReaLTaiizor.Controls.ParrotButton parrotButton3;
        private DataGridViewTextBoxColumn Column1;
        private DataGridViewTextBoxColumn Column2;
        private DataGridViewTextBoxColumn Column3;
        private DataGridViewTextBoxColumn Column4;
        private DataGridViewTextBoxColumn Column5;
        private DataGridViewTextBoxColumn Column6;
        private Panel panel6;
        private Label label8;
    }
}