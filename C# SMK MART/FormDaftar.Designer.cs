namespace SMK_MART
{
    partial class FormDaftar
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
            tableLayoutPanel1 = new TableLayoutPanel();
            panel1 = new Panel();
            button1 = new Button();
            textBox4 = new TextBox();
            textBox3 = new TextBox();
            label5 = new Label();
            label4 = new Label();
            label3 = new Label();
            textBox2 = new TextBox();
            label2 = new Label();
            textBox1 = new TextBox();
            label1 = new Label();
            tableLayoutPanel1.SuspendLayout();
            panel1.SuspendLayout();
            SuspendLayout();
            // 
            // tableLayoutPanel1
            // 
            tableLayoutPanel1.BackColor = Color.FromArgb(41, 57, 178);
            tableLayoutPanel1.ColumnCount = 3;
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Absolute, 470F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.Controls.Add(panel1, 1, 1);
            tableLayoutPanel1.Dock = DockStyle.Fill;
            tableLayoutPanel1.Location = new Point(0, 0);
            tableLayoutPanel1.Name = "tableLayoutPanel1";
            tableLayoutPanel1.RowCount = 3;
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Absolute, 400F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.Size = new Size(669, 406);
            tableLayoutPanel1.TabIndex = 0;
            tableLayoutPanel1.Paint += tableLayoutPanel1_Paint;
            // 
            // panel1
            // 
            panel1.BackColor = Color.White;
            panel1.Controls.Add(button1);
            panel1.Controls.Add(textBox4);
            panel1.Controls.Add(textBox3);
            panel1.Controls.Add(label5);
            panel1.Controls.Add(label4);
            panel1.Controls.Add(label3);
            panel1.Controls.Add(textBox2);
            panel1.Controls.Add(label2);
            panel1.Controls.Add(textBox1);
            panel1.Controls.Add(label1);
            panel1.Dock = DockStyle.Fill;
            panel1.Location = new Point(102, 6);
            panel1.Name = "panel1";
            panel1.Size = new Size(464, 394);
            panel1.TabIndex = 0;
            // 
            // button1
            // 
            button1.BackColor = Color.FromArgb(41, 57, 178);
            button1.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            button1.ForeColor = Color.White;
            button1.Location = new Point(27, 342);
            button1.Name = "button1";
            button1.Size = new Size(402, 35);
            button1.TabIndex = 9;
            button1.Text = "Daftar";
            button1.UseVisualStyleBackColor = false;
            button1.Click += button1_Click;
            // 
            // textBox4
            // 
            textBox4.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            textBox4.Location = new Point(27, 280);
            textBox4.Name = "textBox4";
            textBox4.PlaceholderText = "Kasir/Gudang/Admin";
            textBox4.Size = new Size(402, 29);
            textBox4.TabIndex = 8;
            textBox4.TextChanged += textBox4_TextChanged;
            // 
            // textBox3
            // 
            textBox3.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            textBox3.Location = new Point(27, 224);
            textBox3.Name = "textBox3";
            textBox3.Size = new Size(402, 29);
            textBox3.TabIndex = 7;
            textBox3.TextChanged += textBox3_TextChanged;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label5.Location = new Point(27, 256);
            label5.Name = "label5";
            label5.Size = new Size(41, 21);
            label5.TabIndex = 6;
            label5.Text = "Role";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label4.Location = new Point(27, 200);
            label4.Name = "label4";
            label4.Size = new Size(76, 21);
            label4.TabIndex = 5;
            label4.Text = "Password";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label3.Location = new Point(27, 144);
            label3.Name = "label3";
            label3.Size = new Size(61, 21);
            label3.TabIndex = 4;
            label3.Text = "ID User";
            // 
            // textBox2
            // 
            textBox2.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            textBox2.Location = new Point(27, 168);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(402, 29);
            textBox2.TabIndex = 3;
            textBox2.TextChanged += textBox2_TextChanged;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            label2.Location = new Point(27, 88);
            label2.Name = "label2";
            label2.Size = new Size(81, 21);
            label2.TabIndex = 2;
            label2.Text = "Username";
            // 
            // textBox1
            // 
            textBox1.Font = new Font("Segoe UI", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            textBox1.Location = new Point(27, 112);
            textBox1.Name = "textBox1";
            textBox1.Size = new Size(402, 29);
            textBox1.TabIndex = 1;
            textBox1.TextChanged += textBox1_TextChanged;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.BackColor = Color.White;
            label1.Font = new Font("Segoe UI", 20.25F, FontStyle.Bold, GraphicsUnit.Point, 0);
            label1.ForeColor = Color.FromArgb(41, 57, 178);
            label1.Location = new Point(142, 15);
            label1.Name = "label1";
            label1.Size = new Size(173, 37);
            label1.TabIndex = 0;
            label1.Text = "Daftar Akun";
            // 
            // FormDaftar
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(669, 406);
            Controls.Add(tableLayoutPanel1);
            Name = "FormDaftar";
            Text = "FormAdmin";
            tableLayoutPanel1.ResumeLayout(false);
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private TableLayoutPanel tableLayoutPanel1;
        private Panel panel1;
        private Label label1;
        private Label label2;
        private TextBox textBox1;
        private Label label5;
        private Label label4;
        private Label label3;
        private TextBox textBox2;
        private TextBox textBox4;
        private TextBox textBox3;
        private Button button1;
    }
}