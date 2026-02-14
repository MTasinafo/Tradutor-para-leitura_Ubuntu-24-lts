import time
import subprocess
import threading

CHECK_INTERVAL = 0.5
TARGET_LANG = "pt"

def get_selected_text():
    """Lê o texto selecionado usando xclip."""
    try:
        result = subprocess.run(
            ["xclip", "-o", "-selection", "primary"],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"[ERROR] Could not read selection: {e}")
        return ""

def translate_with_crow(text, target_lang="pt"):
    """Traduz o texto usando o Crow Translate via terminal."""
    try:
        result = subprocess.run(
            ["crow", "-t", target_lang, text],
            capture_output=True,
            text=True
        )
        return result.stdout.strip() or "[No translation returned]"
    except Exception as e:
        print(f"[ERROR] Crow Translate failed: {e}")
        return "[Translation error]"

def show_notification(message):
    """Mostra tradução como notificação no Ubuntu."""
    try:
        subprocess.run([
            "notify-send",
            "-t", "5000",
            "Translation",
            message
        ])
    except Exception as e:
        print(f"[ERROR] Could not show notification: {e}")

def monitor_selection():
    last_text = ""
    while True:
        current_text = get_selected_text()
        if current_text and current_text != last_text:
            last_text = current_text
            threading.Thread(
                target=lambda: show_notification(
                    translate_with_crow(current_text, TARGET_LANG)
                )
            ).start()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    print("[INFO] Clipboard Translator running with Crow Translate...")
    monitor_selection()
