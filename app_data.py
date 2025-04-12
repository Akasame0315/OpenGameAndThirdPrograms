import json
import os
from constants import APP_FILE, CONFIG_FILE, DEFAULT_CONFIG

def load_json(path, default):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_apps():
    return load_json(APP_FILE, {})

def save_apps(apps):
    save_json(APP_FILE, apps)

def load_config():
    return load_json(CONFIG_FILE, DEFAULT_CONFIG.copy())

def save_config(config):
    save_json(CONFIG_FILE, config)
