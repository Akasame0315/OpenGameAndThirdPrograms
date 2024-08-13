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
    public partial class Form2 : Form
    {
        public string ButtonName { get; private set; }
        public string ButtonText { get; private set; }
        public string LabelText { get; private set; }
        public Form2()
        {
            InitializeComponent();
        }

        private void ConfirmAdd_Btn_Click(object sender, EventArgs e)
        {
            ButtonText = textBox2.Text;
            LabelText = textBox3.Text;

            // 關閉對話框並返回OK結果
            this.DialogResult = DialogResult.OK;
            this.Close();

        }
    }
}
