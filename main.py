import subprocess, os
import time
from logger_utils import setup_logger #for log error

logger = setup_logger()  # 預設就是寫到 debug.log

apps_to_open = [
    r"C:\Windows\system32\notepad.exe",
    r"C:\Windows\system32\calc.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe"
]

for app in apps_to_open:
    try:
        subprocess.Popen([app])
        logger.info(f"✅ 已啟動：{app}")
        time.sleep(1)  # 可選：每個程式間隔 1 秒開啟
    except Exception as e:
        logger.info(f"⚠️ 無法開啟 {app}：{e}")

files_to_open = [
    r"C:\Users\user\source\repos"
]

for file in files_to_open:
    try:
        os.startfile(file)
        logger.info(f"✅ 已開啟資料夾：{file}")
        time.sleep(1)  # 可選：每個程式間隔 1 秒開啟
    except Exception as e:
        logger.info(f"⚠️ 無法開啟資料夾： {file}：{e}")