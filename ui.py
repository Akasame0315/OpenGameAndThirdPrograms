import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

from constants import *
from app_data import load_apps, save_apps, load_config, save_config
from launcher_logic import launch_apps

def create_main_window():
    apps = load_apps()
    config = load_config()

    root = tk.Tk()
    root.title("程式啟動器")
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    last_mode_var = tk.StringVar()
    last_mode_var.set(f"上次開啟：『{config.get('last_mode', '無')}』")

    def refresh_ui():
        for widget in frame_container.winfo_children():
            widget.destroy()
        for mode in apps:
            frame = tk.Frame(frame_container)
            frame.pack(pady=5)

            tk.Button(frame, text=mode, width=18,
                      command=lambda m=mode: launch_apps(m, apps[m], config, root, update_last_mode, set_status=lambda msg: status_var.set(msg)
                        )).pack(side="left", padx=5)
            tk.Button(frame, text="✏️ 編輯", width=6, command=lambda m=mode: edit_mode(m)).pack(side="left")
            tk.Button(frame, text="🔤 更名", width=6, command=lambda m=mode: rename_mode(m)).pack(side="left")
            tk.Button(frame, text="🗑 刪除", width=6, fg="red", command=lambda m=mode: delete_mode(m)).pack(side="left")

    def rename_mode(old_name):
        new_name = simpledialog.askstring("重新命名", f"將『{old_name}』改為：")
        if not new_name:
            return
        if new_name in apps:
            messagebox.showerror("名稱重複", "此名稱已經存在，請換一個。")
            return

        # 執行更名
        apps[new_name] = apps.pop(old_name)

        # 同步更新 last_mode 如果需要
        if config.get("last_mode") == old_name:
            config["last_mode"] = new_name
            save_config(config)

        save_apps(apps)
        refresh_ui()
        messagebox.showinfo("成功", f"『{old_name}』已重新命名為『{new_name}』")

    def update_last_mode(mode):
        last_mode_var.set(f"上次開啟：『{mode}』")

    def add_mode():
        name = simpledialog.askstring("新增模式", "請輸入新模式名稱：")
        if name:
            if name in apps:
                messagebox.showwarning("已存在", "此模式已存在")
            else:
                apps[name] = []
                save_apps(apps)
                refresh_ui()

    def delete_mode(mode):
        if messagebox.askyesno("確認刪除", f"確定刪除模式：『{mode}』？"):
            del apps[mode]
            save_apps(apps)
            refresh_ui()

    def edit_mode(mode):
        def save_edited():
            new_text = text_box.get("1.0", tk.END)
            new_list = [line.strip() for line in new_text.splitlines() if line.strip()]
            apps[mode] = new_list
            save_apps(apps)
            edit_window.destroy()
            refresh_ui()
            messagebox.showinfo("已儲存", f"『{mode}』已更新！")

        def add_file():
            file_path = filedialog.askopenfilename(
                title="選擇應用程式", filetypes=[("可執行檔", "*.exe")]
            )
            if file_path:
                text_box.insert(tk.END, file_path + "\n")

        edit_window = tk.Toplevel(root)
        edit_window.title(f"編輯模式：{mode}")
        edit_window.geometry(f"{EDITOR_WIDTH}x{EDITOR_HEIGHT}")
        edit_window.minsize(400, 300)

        text_box = tk.Text(edit_window, font=("Consolas", 10), height=15)
        text_box.pack(fill="both", expand=True, padx=10, pady=(10, 5))

        for path in apps.get(mode, []):
            text_box.insert(tk.END, path + "\n")

        btn_frame = tk.Frame(edit_window)
        btn_frame.pack(pady=10)

        btn_style = {"width": 15, "height": 2, "font": FONT}
        tk.Button(btn_frame, text="📂 加入檔案", command=add_file, **btn_style).pack(side="left", padx=10)
        tk.Button(btn_frame, text="💾 儲存", command=save_edited, **btn_style).pack(side="left", padx=10)

    # UI Layout
    tk.Label(root, text="🧭 請選擇要啟動的模式：", font=FONT).pack(pady=10)
    tk.Button(root, text="➕ 新增模式", command=add_mode).pack(pady=5)

    auto_close_var = tk.BooleanVar(value=config.get("auto_close", False))
    tk.Checkbutton(root, text="啟動後自動關閉程式", variable=auto_close_var,
                   command=lambda: update_auto_close(auto_close_var.get())).pack(pady=5)

    frame_container = tk.Frame(root)
    frame_container.pack(pady=10)

    tk.Label(root, textvariable=last_mode_var, fg="gray").pack(pady=10)

    status_var = tk.StringVar()
    status_var.set("準備就緒")

    status_bar = tk.Label(root, textvariable=status_var, fg="gray", anchor="w")
    status_bar.pack(fill="x", side="bottom", padx=10, pady=5)

    def update_auto_close(value):
        config["auto_close"] = value
        save_config(config)

    refresh_ui()
    
    return root
