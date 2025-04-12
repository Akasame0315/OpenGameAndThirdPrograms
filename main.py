import json, sys
import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog
import os

# ========== 資料存取 ==========
APP_FILE = "AppList.json"
CONFIG_FILE = "config.json"

# 讀取 程式清單 JSON 檔案
def load_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

# 更新 使用者習慣 JSON 檔案
def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# ========== 程式啟動功能 ==========
def launch_apps(mode):
    config = load_json(CONFIG_FILE, {})
    apps = app_sets.get(mode, [])
    if not apps:
        messagebox.showwarning("沒有程式", f"『{mode}』沒有設定任何程式。")
        return
    
    for path in apps:
        try:
            subprocess.Popen([path])
        except Exception as e:
            messagebox.showerror("錯誤", f"無法開啟：\n{path}\n{e}")

    # 記住上次開啟的模式
    save_json(CONFIG_FILE, {"last_mode": mode})
    # messagebox.showinfo("完成", f"『{mode}』模式啟動完成！")
    if config.get("auto_close", True):
        sys.exit()

# ========== 編輯功能 ==========
def edit_mode(mode):
    current_list = app_sets.get(mode, [])
    current_text = "\n".join(current_list)

    new_text = simpledialog.askstring(
        f"編輯模式：{mode}",
        "請輸入完整應用程式路徑，一行一個：",
        initialvalue=current_text
    )

    if new_text is not None:
        new_list = [line.strip() for line in new_text.splitlines() if line.strip()]
        app_sets[mode] = new_list
        save_json(APP_FILE, app_sets)
        messagebox.showinfo("已儲存", f"『{mode}』已更新！")

# ========== 介面建立 ==========
app_sets = load_json(APP_FILE, {})
config = load_json(CONFIG_FILE, {})

root = tk.Tk()
root.title("程式啟動器 Launcher")
root.geometry("360x400")

tk.Label(root, text="請選擇要啟動的模式：", font=("Arial", 12)).pack(pady=10)

for mode in app_sets:
    frame = tk.Frame(root)
    frame.pack(pady=5)

    tk.Button(frame, text=mode, width=18, command=lambda m=mode: launch_apps(m)).pack(side="left", padx=5)
    tk.Button(frame, text="✏️ 編輯", width=8, command=lambda m=mode: edit_mode(m)).pack(side="left")

# 顯示上次啟動的模式提示
last_mode = config.get("last_mode")
if last_mode:
    tk.Label(root, text=f"上次開啟：『{last_mode}』", fg="gray").pack(pady=10)

root.mainloop()