import subprocess
from tkinter import messagebox

from app_data import save_config
from constants import CONFIG_FILE

def launch_apps(mode, apps, config, root=None, update_ui_callback=None, set_status=None):
    if not apps:
        if set_status:
            set_status(f"『{mode}』沒有程式可以執行。")
        # messagebox.showwarning("沒有程式", f"『{mode}』沒有設定任何程式。")
        return

    for path in apps:
        if set_status:
            set_status(f"正在啟動：{path}")
        try:
            subprocess.Popen([path])
        except Exception as e:
            if set_status:
                set_status(f"❌ 啟動失敗：{path}")
            # messagebox.showerror("錯誤", f"無法開啟：\n{path}\n{e}")

    config["last_mode"] = mode
    save_config(config)

    if update_ui_callback:
        update_ui_callback(mode)

    if set_status:
        set_status(f"✅『{mode}』啟動完成")
    # messagebox.showinfo("完成", f"『{mode}』模式啟動完成！")

    if config.get("auto_close", False) and root:
        root.destroy()
