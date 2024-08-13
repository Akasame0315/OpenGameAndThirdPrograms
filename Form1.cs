using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void LOL_Btn_Click(object sender, EventArgs e)
        {
            ChooseGame.Text = "Leage of Legends";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ChooseGame.Text = string.Empty;
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            ChooseGame.Text = "Maple Story";
        }

        private void Add_Btn_Click(object sender, EventArgs e)
        {
            // 打開輸入對話框
            var inputForm = new Form2();
            if (inputForm.ShowDialog() == DialogResult.OK)
            {
                // 創建新按鈕
                Button newButton = new Button();
                newButton.Name = inputForm.ButtonText;
                newButton.Text = inputForm.LabelText;
                newButton.Size = new Size(100, 30); // 設置按鈕大小
                newButton.Location = new Point(150, 100); // 設置按鈕位置 (你可以調整這個位置)
                newButton.Click += NewButton_Click;
                // 將新按鈕添加到主視窗
                this.Controls.Add(newButton);
            }

        }
        private void NewButton_Click(object sender, EventArgs e)
        {
            Button clickedButton = sender as Button;
            ChooseGame.Text = clickedButton.Text;
            //MessageBox.Show($"你點擊了按鈕: {clickedButton.Text}");
            // 你可以在這裡添加更多的功能邏輯
        }
    }
}
