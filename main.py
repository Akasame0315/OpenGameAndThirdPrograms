import subprocess, os
import time, json
from logger_utils import setup_logger #for log error

logger = setup_logger()  # 預設就是寫到 debug.log
# 讀取 JSON 設定檔
with open("AppList.json", "r", encoding="utf-8") as f:
    app_sets = json.load(f)

# 顯示可選擇的啟動模式
print("🧭 請選擇要啟動的模式：")
modes = list(app_sets.keys())
for i, mode in enumerate(modes, start=1):
    print(f"{i}. {mode}")

# 讓使用者選擇
try:
    choice = int(input("輸入數字選擇："))
    selected_mode = modes[choice - 1]
except (IndexError, ValueError):
    print("❌ 無效的選擇")
    exit()

# 執行對應程式
print(f"\n🚀 正在啟動【{selected_mode}】...")
for path in app_sets[selected_mode]:
    try:
        subprocess.Popen([path])
        print(f"✅ 已啟動：{path}")        
        # logger.info(f"✅ 已啟動：{path}")
    except Exception as e:
        print(f"⚠️ 無法開啟 {path}：{e}")
        # logger.info(f"⚠️ 無法開啟 {path}：{e}")