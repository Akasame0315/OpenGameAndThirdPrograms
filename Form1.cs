using System;
using System.IO;
using System.Collections.Generic;
using System.Windows.Forms;
using Newtonsoft.Json;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
namespace WindowsFormsApp1
{
    public partial class OpenGameAndThirdPrograms : Form
    {
        public class ComboBoxItem
        {
            public string Text { get; set; }
            public string Path { get; set; }
            public string OtherOption { get; set; }
        }
        public OpenGameAndThirdPrograms()
        {
            InitializeComponent();
            // 添加選項
            if (File.Exists("GameList.json"))
            {
                string json = File.ReadAllText("gamelist.json");
                var items = JsonConvert.DeserializeObject<List<ComboBoxItem>>(json);
                foreach (var item in items)
                {
                    ChooseGame_List.Items.Add(item.Text);
                }
            }

            // 設置默認選項
            if (ChooseGame_List.Items.Count > 0)
            {
                ChooseGame_List.SelectedIndex = 0; // 選擇第一個項目
            }

            // 將 ComboBox 添加到窗體
            this.Controls.Add(ChooseGame_List);
        }

        private void label1_Click(object sender, EventArgs e)
        {
            MessageBox.Show(ChooseGame.Text);
        }
        private void Add_Btn_Click(object sender, EventArgs e)
        {
            // 要添加的新項目文字
            string newItemText = textBox1.Text; 
            string newItemPath = "指定路徑"; // 假設這是從另一個控制項取得的資料
            string otherOption = "其他選項"; // 假設這是另一個資料

            if (!string.IsNullOrWhiteSpace(newItemText))
            {
                ComboBoxItem newItem = new ComboBoxItem
                {
                    Text = newItemText,
                    Path = newItemPath,
                    OtherOption = otherOption
                };

                List<ComboBoxItem> items = new List<ComboBoxItem>();
                if (File.Exists("GameList.json"))
                {
                    string json = File.ReadAllText("GameList.json");
                    items = JsonConvert.DeserializeObject<List<ComboBoxItem>>(json);
                }
                items.Add(newItem);

                string newJson = JsonConvert.SerializeObject(items, Formatting.Indented);
                File.WriteAllText("GameList.json", newJson);

                ChooseGame_List.Items.Add(newItemText);
                ChooseGame_List.SelectedItem = newItemText;

                MessageBox.Show("已添加並保存項目: " + newItemText);
                string filePath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "GameList.json");
                if (File.Exists(filePath))
                {
                    string fileContent = File.ReadAllText(filePath);
                    MessageBox.Show("檔案內容: " + fileContent);
                }

            }
            else
            {
                MessageBox.Show("請輸入有效的文字");
            }
        }
        private void Confirm_Btn_Click(object sender, EventArgs e)
        {
            // 確認 ComboBox 中有選項被選擇
            if (ChooseGame_List.SelectedItem != null)
            {
                string selectedItem = ChooseGame_List.SelectedItem.ToString();
                ChooseGame.Text = selectedItem;
            }
            else
            {
                MessageBox.Show("尚未選擇任何項目");
            }
        }
    }
}
