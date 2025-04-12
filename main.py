import json
import subprocess
import tkinter as tk
from tkinter import messagebox

# 讀取 JSON 檔案
def load_app_sets():
    try:
        with open("AppList.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        messagebox.showerror("錯誤", f"讀取 AppList.json 失敗：\n{e}")
        return {}

# 點擊按鈕後開啟對應應用程式
def launch_apps(mode):
    apps = app_sets.get(mode, [])
    if not apps:
        messagebox.showwarning("沒有程式", f"『{mode}』沒有設定任何程式。")
        return
    
    for path in apps:
        try:
            subprocess.Popen([path])
        except Exception as e:
            messagebox.showerror("錯誤", f"無法開啟：\n{path}\n{e}")

    messagebox.showinfo("完成", f"『{mode}』模式啟動完成！")

# 建立主視窗
app_sets = load_app_sets()
root = tk.Tk()
root.title("程式啟動器 Launcher")
root.geometry("300x200")

tk.Label(root, text="請選擇要啟動的模式：", font=("Arial", 12)).pack(pady=10)

# 動態建立按鈕
for mode in app_sets:
    tk.Button(root, text=mode, width=20, height=2, command=lambda m=mode: launch_apps(m)).pack(pady=5)

# 開始 GUI 主迴圈
root.mainloop()
