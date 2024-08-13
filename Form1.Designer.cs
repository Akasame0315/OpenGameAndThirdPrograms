namespace WindowsFormsApp1
{
    partial class Form1
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
            this.LOL_Btn = new System.Windows.Forms.Button();
            this.ChooseGame = new System.Windows.Forms.Label();
            this.Clear_Btn = new System.Windows.Forms.Button();
            this.Confirm_Btn = new System.Windows.Forms.Button();
            this.MS_Btm = new System.Windows.Forms.Button();
            this.Add_Btn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // LOL_Btn
            // 
            this.LOL_Btn.Location = new System.Drawing.Point(67, 59);
            this.LOL_Btn.Name = "LOL_Btn";
            this.LOL_Btn.Size = new System.Drawing.Size(167, 55);
            this.LOL_Btn.TabIndex = 0;
            this.LOL_Btn.Text = "LOL";
            this.LOL_Btn.UseVisualStyleBackColor = true;
            this.LOL_Btn.Click += new System.EventHandler(this.LOL_Btn_Click);
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
            // Clear_Btn
            // 
            this.Clear_Btn.Location = new System.Drawing.Point(313, 363);
            this.Clear_Btn.Name = "Clear_Btn";
            this.Clear_Btn.Size = new System.Drawing.Size(167, 55);
            this.Clear_Btn.TabIndex = 2;
            this.Clear_Btn.Text = "清除";
            this.Clear_Btn.UseVisualStyleBackColor = true;
            this.Clear_Btn.Click += new System.EventHandler(this.button1_Click);
            // 
            // Confirm_Btn
            // 
            this.Confirm_Btn.Location = new System.Drawing.Point(558, 363);
            this.Confirm_Btn.Name = "Confirm_Btn";
            this.Confirm_Btn.Size = new System.Drawing.Size(167, 55);
            this.Confirm_Btn.TabIndex = 3;
            this.Confirm_Btn.Text = "確認";
            this.Confirm_Btn.UseVisualStyleBackColor = true;
            // 
            // MS_Btm
            // 
            this.MS_Btm.Location = new System.Drawing.Point(313, 59);
            this.MS_Btm.Name = "MS_Btm";
            this.MS_Btm.Size = new System.Drawing.Size(167, 55);
            this.MS_Btm.TabIndex = 4;
            this.MS_Btm.Text = "MS";
            this.MS_Btm.UseVisualStyleBackColor = true;
            this.MS_Btm.Click += new System.EventHandler(this.button1_Click_1);
            // 
            // Add_Btn
            // 
            this.Add_Btn.Location = new System.Drawing.Point(67, 363);
            this.Add_Btn.Name = "Add_Btn";
            this.Add_Btn.Size = new System.Drawing.Size(167, 55);
            this.Add_Btn.TabIndex = 5;
            this.Add_Btn.Text = "新增";
            this.Add_Btn.UseVisualStyleBackColor = true;
            this.Add_Btn.Click += new System.EventHandler(this.Add_Btn_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.Add_Btn);
            this.Controls.Add(this.MS_Btm);
            this.Controls.Add(this.Confirm_Btn);
            this.Controls.Add(this.Clear_Btn);
            this.Controls.Add(this.ChooseGame);
            this.Controls.Add(this.LOL_Btn);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button LOL_Btn;
        private System.Windows.Forms.Label ChooseGame;
        private System.Windows.Forms.Button Clear_Btn;
        private System.Windows.Forms.Button Confirm_Btn;
        private System.Windows.Forms.Button MS_Btm;
        private System.Windows.Forms.Button Add_Btn;
    }
}

