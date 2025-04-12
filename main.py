import json
import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
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
    save_last_mode(mode)
    
    # 更新UI文字(上次開啟的模式)
    config["last_mode"] = mode
    save_json(CONFIG_FILE, config)
    last_mode_var.set(f"上次開啟：『{mode}』")

    if config.get("auto_close", False):
        root.destroy()  # ← 關閉 GUI


# 儲存時不蓋掉其他設定
def save_last_mode(mode):
    config["last_mode"] = mode
    save_json(CONFIG_FILE, config)

# 自動關閉GUI
def toggle_auto_close():
    config["auto_close"] = bool(auto_close_var.get())
    save_json(CONFIG_FILE, config)

# ========== 編輯功能 ==========
def edit_mode(mode):
    def save_edited():
        new_text = text_box.get("1.0", tk.END)
        new_list = [line.strip() for line in new_text.splitlines() if line.strip()]
        app_sets[mode] = new_list
        save_json(APP_FILE, app_sets)
        edit_window.destroy()
        refresh_ui()
        messagebox.showinfo("已儲存", f"『{mode}』已更新！")

    def add_file():
        file_path = filedialog.askopenfilename(
            title="選擇應用程式",
            filetypes=[("可執行檔", "*.exe")]
        )
        if file_path:
            text_box.insert(tk.END, file_path + "\n")

    # 建立編輯視窗
    edit_window = tk.Toplevel(root)
    edit_window.title(f"編輯模式：{mode}")
    edit_window.geometry("500x400")
    edit_window.minsize(500, 350)  # 限制編輯視窗不要太小
    
    text_box = tk.Text(edit_window, font=("Consolas", 10), height=15)
    text_box.pack(fill="both", expand=True, padx=10, pady=10)

    # 預填內容
    for path in app_sets.get(mode, []):
        text_box.insert(tk.END, path + "\n")

    btn_frame = tk.Frame(edit_window)
    btn_frame.pack(pady=5)
    btn_style = {"width": 15, "height": 2, "font": ("Arial", 10)}

    tk.Button(btn_frame, text="📂 加入檔案", command=add_file, **btn_style).pack(side="left", padx=5)
    tk.Button(btn_frame, text="💾 儲存", command=save_edited, **btn_style).pack(side="left", padx=5)

# ========== 刪除功能 ==========
def delete_mode(mode):
    if messagebox.askyesno("確認刪除", f"確定要刪除模式：『{mode}』？"):
        del app_sets[mode]
        save_json(APP_FILE, app_sets)
        refresh_ui()
        messagebox.showinfo("已刪除", f"『{mode}』模式已刪除。")

# ========== 新增功能 ==========
def add_mode():
    new_mode = simpledialog.askstring("新增模式", "請輸入新模式名稱：")
    if new_mode:
        if new_mode in app_sets:
            messagebox.showwarning("已存在", "這個模式名稱已經存在。")
        else:
            app_sets[new_mode] = []
            save_json(APP_FILE, app_sets)
            refresh_ui()
            messagebox.showinfo("成功", f"『{new_mode}』模式已新增！")

# 動態刷新 UI（重建按鈕列）
def refresh_ui():
    for widget in frame_container.winfo_children():
        widget.destroy()

    for mode in app_sets:
        frame = tk.Frame(frame_container)
        frame.pack(pady=5)

        tk.Button(frame, text=mode, width=18, command=lambda m=mode: launch_apps(m)).pack(side="left", padx=5)
        tk.Button(frame, text="✏️ 編輯", width=6, command=lambda m=mode: edit_mode(m)).pack(side="left")
        tk.Button(frame, text="🗑 刪除", width=6, fg="red", command=lambda m=mode: delete_mode(m)).pack(side="left")

# ========== 介面建立 ==========
app_sets = load_json(APP_FILE, {})
config = load_json(CONFIG_FILE, {})

root = tk.Tk()
root.title("程式啟動器 Launcher")
root.geometry("400x500")

tk.Label(root, text="請選擇要啟動的模式：", font=("Arial", 12)).pack(pady=10)

# 加入新增模式按鈕
tk.Button(root, text="➕ 新增模式", command=add_mode).pack(pady=5)

# 放模式按鈕的區域
frame_container = tk.Frame(root)
frame_container.pack(pady=10)

# UI提示init
last_mode_var = tk.StringVar()
last_mode_var.set(f"上次開啟：『{config.get('last_mode', '無')}』")

refresh_ui()

# 顯示上次模式
last_mode = config.get("last_mode")
if last_mode:
    tk.Label(root, textvariable=last_mode_var, fg="gray").pack(pady=10)

# 放在主畫面 UI 初始化區：
auto_close_var = tk.BooleanVar(value=config.get("auto_close", False))
tk.Checkbutton(root, text="啟動後自動關閉程式", variable=auto_close_var, command=toggle_auto_close).pack(pady=5)

root.mainloop()