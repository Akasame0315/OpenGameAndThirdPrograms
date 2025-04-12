import re, logging
import os

class CleanEmojiFilter(logging.Filter):
    def filter(self, record):
        # 只允許常見中英文 + 標點符號（你可以依需求擴充）
        clean_msg = re.sub(r'[^\u4e00-\u9fff\w\s.,!?;:()「」【】《》\'"~\-—\[\]{}<>…·＠@／/]', '', record.getMessage())
        record.msg = clean_msg
        return True
    
def setup_logger(log_file='debug.log', level=logging.DEBUG):
    # 建立 logs 資料夾（可選）
    os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)

    # 建立格式器
    formatter = logging.Formatter(
        fmt='%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 建立 FileHandler，支援 UTF-8
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)

    # 建立主 logger
    logger = logging.getLogger()
    logger.setLevel(level)
    logger.addHandler(file_handler)

    # 可選：同時也輸出到 console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # ✅ 加上過濾器
    logger.addFilter(CleanEmojiFilter())
    
    return logger
