namespace WindowsFormsApp1
{
    partial class OpenGameAndThirdPrograms
    {
        /// <summary>
        /// 設計工具所需的變數。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 清除任何使用中的資源。
        /// </summary>
        /// <param name="disposing">如果應該處置受控資源則為 true，否則為 false。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form 設計工具產生的程式碼

        /// <summary>
        /// 此為設計工具支援所需的方法 - 請勿使用程式碼編輯器修改
        /// 這個方法的內容。
        /// </summary>
        private void InitializeComponent()
        {
            this.ChooseGame = new System.Windows.Forms.Label();
            this.Confirm_Btn = new System.Windows.Forms.Button();
            this.Add_Btn = new System.Windows.Forms.Button();
            this.ChooseGame_List = new System.Windows.Forms.ComboBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // ChooseGame
            // 
            this.ChooseGame.AutoSize = true;
            this.ChooseGame.Location = new System.Drawing.Point(371, 26);
            this.ChooseGame.Name = "ChooseGame";
            this.ChooseGame.Size = new System.Drawing.Size(49, 12);
            this.ChooseGame.TabIndex = 1;
            this.ChooseGame.Text = "No Game";
            this.ChooseGame.Click += new System.EventHandler(this.label1_Click);
            // 
            // Confirm_Btn
            // 
            this.Confirm_Btn.Location = new System.Drawing.Point(558, 363);
            this.Confirm_Btn.Name = "Confirm_Btn";
            this.Confirm_Btn.Size = new System.Drawing.Size(167, 55);
            this.Confirm_Btn.TabIndex = 3;
            this.Confirm_Btn.Text = "確認";
            this.Confirm_Btn.UseVisualStyleBackColor = true;
            this.Confirm_Btn.Click += new System.EventHandler(this.Confirm_Btn_Click);
            // 
            // Add_Btn
            // 
            this.Add_Btn.Location = new System.Drawing.Point(66, 352);
            this.Add_Btn.Name = "Add_Btn";
            this.Add_Btn.Size = new System.Drawing.Size(167, 55);
            this.Add_Btn.TabIndex = 5;
            this.Add_Btn.Text = "新增";
            this.Add_Btn.UseVisualStyleBackColor = true;
            this.Add_Btn.Click += new System.EventHandler(this.Add_Btn_Click);
            // 
            // ChooseGame_List
            // 
            this.ChooseGame_List.FormattingEnabled = true;
            this.ChooseGame_List.Location = new System.Drawing.Point(333, 59);
            this.ChooseGame_List.Name = "ChooseGame_List";
            this.ChooseGame_List.Size = new System.Drawing.Size(121, 20);
            this.ChooseGame_List.TabIndex = 6;
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(93, 324);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(100, 22);
            this.textBox1.TabIndex = 7;
            // 
            // OpenGameAndThirdPrograms
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.ChooseGame_List);
            this.Controls.Add(this.Add_Btn);
            this.Controls.Add(this.Confirm_Btn);
            this.Controls.Add(this.ChooseGame);
            this.Name = "OpenGameAndThirdPrograms";
            this.Text = "OpenGameAndThirdPrograms";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label ChooseGame;
        private System.Windows.Forms.Button Confirm_Btn;
        private System.Windows.Forms.Button Add_Btn;
        private System.Windows.Forms.ComboBox ChooseGame_List;
        private System.Windows.Forms.TextBox textBox1;
    }
}

