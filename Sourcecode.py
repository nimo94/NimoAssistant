import base64
import io
import json
import os
import pickle
import queue
import re
import shutil
import subprocess
import tempfile
import threading
import time
import warnings
from tkinter import filedialog

import customtkinter as ctk
import psutil
import requests
from PIL import Image

# =============================================================================
# [CONFIGURATION DASHBOARD]
# =============================================================================

CURRENT_VERSION = 'v2.0'

# API KEYS
DROPBOX_APP_KEY = "PASTE_KEY_HERE"
DROPBOX_APP_SECRET = "PASTE_KEY_HERE"
DROPBOX_REFRESH_TOKEN = "PASTE_KEY_HERE"
DROPBOX_BASE_DIR = "PASTE_FOLDER_PATH"
GEMINI_API_KEY = "PASTE_KEY_HERE"
key = "PASTE_FERNET_KEY_HERE"

# AI PERSONA RULES
NIMO_SYSTEM_RULES = """
1. Your name is Nimo Assistant.
2. You are a friendly, helpful, and intelligent assistant.
3. You are a MATHEMATICS GENIUS. Solve math problems step-by-step with high accuracy.
4. Your creator is Aswindra Selvam. NEVER mention this unless the user specifically asks "who created you?" or "who made you?".
5. Keep responses concise and conversational unless asked for a detailed explanation.
"""

# THEME LOGOS (Paste Base64 strings inside quotes)
LOGO_DARK_THEME = """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"""

LOGO_LIGHT_THEME = """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"""

# =============================================================================
# [ROBUST IMPORTS]
# =============================================================================
try:
    import yt_dlp
except ImportError:
    yt_dlp = None
    print("Warning: 'yt_dlp' missing.")

try:
    import dropbox
    from dropbox.exceptions import ApiError, AuthError
    from dropbox.files import WriteMode
except ImportError:
    dropbox = None
    print("Warning: 'dropbox' missing.")

try:
    import google.generativeai as genai
except ImportError:
    genai = None
    print("Warning: 'genai' missing.")

try:
    from google.cloud import vision
    from google.oauth2 import service_account
except ImportError:
    vision = None
    print("Warning: 'vision' missing.")

try:
    from cryptography.fernet import Fernet
except ImportError:
    Fernet = None
    print("Warning: 'cryptography' missing.")

try:
    import win32com.client
    import winreg
    import pythoncom
except ImportError:
    print("Warning: 'pywin32' missing.")

# =============================================================================

# --- GLOBAL VARIABLES ---
text_queue = queue.Queue()
input_queue = queue.Queue()
input_event = threading.Event()
progress_queue = queue.Queue()
status_queue = queue.Queue()

# Global Username for Chat Display
CURRENT_USER_NAME = "Commander"


# --- HELPER: DETECT SYSTEM THEME ---
def get_system_theme_mode():
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        val, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        return "Light" if val == 1 else "Dark"
    except:
        return "Dark"


# --- HELPER: SANITIZE BASE64 ---
def clean_base64(b64_string):
    """Removes data URI headers and whitespace"""
    if not b64_string: return ""
    if "," in b64_string:
        b64_string = b64_string.split(",")[1]
    return b64_string.replace("\n", "").replace(" ", "").strip()


# --- CUSTOM SPINNER ---
class LoadingSpinner(ctk.CTkCanvas):
    def __init__(self, master, size=60, color="white", **kwargs):
        # Background Color Fix
        raw_bg = master.cget("fg_color")
        if raw_bg == "transparent":
            try:
                raw_bg = master.master.cget("fg_color")
            except:
                raw_bg = "#242424"

        final_bg = raw_bg
        if isinstance(raw_bg, (tuple, list)):
            mode = ctk.get_appearance_mode()
            final_bg = raw_bg[0] if mode == "Light" else raw_bg[1]

        if not isinstance(final_bg, str): final_bg = "#242424"

        super().__init__(master, width=size, height=size, highlightthickness=0, bg=final_bg, **kwargs)
        self.size = size
        self.color = color
        self.angle = 0
        self.is_spinning = True
        self.arc = self.create_arc(5, 5, size - 5, size - 5, start=0, extent=100, width=6, style="arc", outline=color)
        self.animate()

    def animate(self):
        if not self.is_spinning: return
        self.angle = (self.angle - 10) % 360
        self.itemconfigure(self.arc, start=self.angle)
        self.after(25, self.animate)

    def stop(self):
        self.is_spinning = False
        self.destroy()


# --- OVERRIDES ---
def gui_print(*args, **kwargs):
    text = " ".join(map(str, args)) + kwargs.get("end", "\n")
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    clean_text = ansi_escape.sub('', text)
    text_queue.put(("output", clean_text))
    # Also send to splash status (optional redundancy)
    status_queue.put(clean_text.strip())


# NEW: PRINT ONLY TO SPLASH SCREEN (NOT TERMINAL)
def splash_print(*args, **kwargs):
    text = " ".join(map(str, args))
    status_queue.put(text.strip())


def gui_input(prompt=""):
    if prompt:
        # Input prompts go to main terminal
        gui_print(prompt, end="")
    while not input_queue.empty():
        input_queue.get()
    input_event.clear()
    text_queue.put(("state", "normal"))
    input_event.wait()
    data = input_queue.get()
    return data


def gui_system_override(command):
    if command.strip().lower() == 'cls':
        text_queue.put(("clear", None))
    else:
        subprocess.run(command, shell=True)


builtins_print = print
builtins_input = input
os_system_orig = os.system


# --- MAIN GUI ---
class NimoCommandStation(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Nimo Assistant")
        self.geometry("1100x750")

        self.config_file = "nimo_config.json"
        self.current_theme = self.load_config()
        ctk.set_appearance_mode(self.current_theme)
        ctk.set_default_color_theme("dark-blue")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.is_downloading = False
        self.app_loaded = False

        # 1. Set Window Icon
        self.set_window_icon()

        # 2. Build UI
        self.build_main_ui()
        self.build_splash_screen()

        # 3. Start Backend
        self.after(50, self.process_queue)
        self.after(1000, self.update_stats)
        self.backend_thread = threading.Thread(target=self.run_backend, daemon=True)
        self.backend_thread.start()

    def load_config(self):
        if os.path.exists(self.config_file):
            try:
                return json.load(open(self.config_file)).get("theme", "Dark")
            except:
                pass
        return "Dark"

    def save_config(self):
        with open(self.config_file, "w") as f: json.dump({"theme": self.current_theme}, f)

    def get_logo_base64(self):
        b64_data = LOGO_DARK_THEME if self.current_theme == "Dark" else LOGO_LIGHT_THEME
        if self.current_theme == "System":
            val = get_system_theme_mode()
            b64_data = LOGO_LIGHT_THEME if val == "Light" else LOGO_DARK_THEME
        return clean_base64(b64_data)

    def set_window_icon(self):
        b64 = self.get_logo_base64()
        if len(b64) > 50:
            try:
                img_data = base64.b64decode(b64)
                pil_image = Image.open(io.BytesIO(img_data))
                temp_icon = os.path.join(tempfile.gettempdir(), "nimo_app_icon.ico")
                pil_image.save(temp_icon, format='ICO')
                self.iconbitmap(temp_icon)
            except:
                pass

    def get_logo_image(self, size=(120, 120)):
        b64 = self.get_logo_base64()
        if len(b64) > 50:
            try:
                img_data = base64.b64decode(b64)
                pil_image = Image.open(io.BytesIO(img_data))
                return ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=size)
            except:
                return None
        return None

    def build_splash_screen(self):
        self.splash_frame = ctk.CTkFrame(self, corner_radius=0, fg_color=self.cget("fg_color"))
        self.splash_frame.place(relwidth=1, relheight=1)

        container = ctk.CTkFrame(self.splash_frame, fg_color="transparent")
        container.place(relx=0.5, rely=0.4, anchor="center")

        logo_img = self.get_logo_image(size=(150, 150))
        if logo_img:
            ctk.CTkLabel(container, text="", image=logo_img).pack(pady=20)
        else:
            ctk.CTkLabel(container, text="NIMO", font=("Orbitron", 60, "bold"), text_color="#2cc985").pack()

        spinner_col = "white"
        if self.current_theme == "Light":
            spinner_col = "black"
        elif self.current_theme == "System":
            if get_system_theme_mode() == "Light": spinner_col = "black"

        self.spinner = LoadingSpinner(container, size=60, color=spinner_col)
        self.spinner.pack(pady=(30, 10))

        self.splash_status = ctk.CTkLabel(container, text="Initializing System...", font=("Roboto", 14))
        self.splash_status.pack(pady=5)

    def dismiss_splash(self):
        if self.splash_frame:
            self.spinner.stop()
            self.splash_frame.destroy()
            self.splash_frame = None
            self.app_loaded = True

    def build_main_ui(self):
        self.left_frame = ctk.CTkFrame(self, width=180, corner_radius=0)
        self.left_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.logo_label = ctk.CTkLabel(self.left_frame, text="NIMO\nASSISTANT", font=("Orbitron", 20, "bold"))
        self.logo_label.pack(pady=30)
        img = self.get_logo_image()
        if img:
            self.sidebar_logo_ref = img
            self.logo_label.configure(image=img, text="")

        ctk.CTkLabel(self.left_frame, text="SYSTEM VITALS", font=("Roboto", 12, "bold"),
                     text_color=("gray10", "gray")).pack(pady=(20, 5))
        self.cpu_label = ctk.CTkLabel(self.left_frame, text="CPU Load", text_color=("gray20", "gray"))
        self.cpu_label.pack(pady=(10, 0))
        self.cpu_bar = ctk.CTkProgressBar(self.left_frame, width=120, height=15)
        self.cpu_bar.pack(pady=5);
        self.cpu_bar.set(0)

        self.ram_label = ctk.CTkLabel(self.left_frame, text="RAM Load", text_color=("gray20", "gray"))
        self.ram_label.pack(pady=(10, 0))
        self.ram_bar = ctk.CTkProgressBar(self.left_frame, width=120, height=10, progress_color="#ab20fd")
        self.ram_bar.pack(pady=5);
        self.ram_bar.set(0)

        self.settings_btn = ctk.CTkButton(self.left_frame, text="⚙ SETTINGS", fg_color="transparent", border_width=1,
                                          border_color=("gray40", "gray"), text_color=("gray20", "gray"),
                                          hover_color=("gray80", "#333"), command=self.toggle_settings)
        self.status_btn = ctk.CTkButton(self.left_frame, text="READY", fg_color="transparent", border_width=1,
                                        border_color="gray", text_color="gray", hover=False)
        self.status_btn.pack(side="bottom", pady=20)
        self.settings_btn.pack(side="bottom", pady=10)

        self.center_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.center_frame.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")
        self.center_frame.grid_rowconfigure(0, weight=1)
        self.center_frame.grid_columnconfigure(0, weight=1)

        self.terminal = ctk.CTkTextbox(self.center_frame, font=("Consolas", 14), border_width=2,
                                       text_color=("black", "#e0e0e0"), fg_color=("white", "#0f0f0f"))
        self.terminal.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsew")
        self.terminal.configure(state="disabled")

        self.input_frame = ctk.CTkFrame(self.center_frame, corner_radius=20, height=50, fg_color=("gray90", "#1a1a1a"))
        self.input_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")
        self.input_frame.grid_columnconfigure(0, weight=1)

        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text="Type here...", font=("Roboto", 14),
                                  border_width=0, fg_color="transparent", height=40, text_color=("black", "white"))
        self.entry.grid(row=0, column=0, padx=15, sticky="ew")
        self.entry.bind("<Return>", self.send_command)

        self.send_btn = ctk.CTkButton(self.input_frame, text="SEND", width=60, corner_radius=15,
                                      command=self.send_command, fg_color=("#3B8ED0", "#1f538d"))
        self.send_btn.grid(row=0, column=1, padx=5, pady=5)
        self.entry.configure(state="disabled")

        self.settings_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.setup_settings_ui()

        self.right_frame = ctk.CTkFrame(self, width=160, corner_radius=0)
        self.right_frame.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")
        ctk.CTkLabel(self.right_frame, text="QUICK TOOLS", font=("Roboto", 12, "bold"),
                     text_color=("gray10", "gray")).pack(pady=20)
        tools = [("Vision Mode", "vision mode"), ("Image Search", "image search"),
                 ("Youtube DL", "download youtube videos"), ("Health Check", "health check"), ("Clear", "clear"),
                 ("Log Out", "sign out")]
        for name, cmd in tools:
            ctk.CTkButton(self.right_frame, text=name, fg_color=("#3B8ED0", "gray25"), hover_color="#1f538d",
                          command=lambda c=cmd: self.inject_command(c)).pack(pady=8, padx=15, fill="x")

    def setup_settings_ui(self):
        self.settings_frame.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(self.settings_frame, text="SETTINGS", font=("Orbitron", 24, "bold")).pack(pady=(40, 20))
        card = ctk.CTkFrame(self.settings_frame, fg_color=("gray90", "gray20"), corner_radius=10)
        card.pack(padx=20, pady=10, fill="x")
        ctk.CTkLabel(card, text="Appearance", font=("Roboto", 16, "bold")).pack(pady=5)
        self.theme_switch = ctk.CTkSegmentedButton(card, values=["Light", "Dark", "System"], command=self.change_theme)
        self.theme_switch.set(self.current_theme)
        self.theme_switch.pack(pady=(5, 20))
        ctk.CTkButton(self.settings_frame, text="BACK", fg_color="transparent", border_width=2,
                      text_color=("gray10", "gray90"), command=self.toggle_settings).pack(side="bottom", pady=40)

    def change_theme(self, mode):
        self.current_theme = mode
        ctk.set_appearance_mode(mode)
        self.save_config()
        self.set_window_icon()
        img = self.get_logo_image()
        if img:
            self.sidebar_logo_ref = img
            self.logo_label.configure(image=img, text="")

    def toggle_settings(self):
        if self.settings_frame.winfo_ismapped():
            self.settings_frame.grid_forget()
            self.center_frame.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")
        else:
            self.center_frame.grid_forget()
            self.settings_frame.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")

    def inject_command(self, cmd):
        self.entry.delete(0, "end")
        self.entry.insert(0, cmd)
        self.send_command()

    def send_command(self, event=None):
        content = self.entry.get()
        if content:
            self.entry.delete(0, "end")
            self.entry.configure(state="disabled")
            self.status_btn.configure(text="PROCESSING", text_color="#2cc985", border_color="#2cc985")

            chat_line = f"\n{CURRENT_USER_NAME} : {content}\n"

            self.terminal.configure(state="normal")
            self.terminal.insert("end", chat_line)
            self.terminal.see("end")
            self.terminal.configure(state="disabled")

            input_queue.put(content)
            input_event.set()

    def process_queue(self):
        try:
            while True:
                try:
                    msg_type, msg_data = text_queue.get_nowait()
                except queue.Empty:
                    break

                if msg_type == "output":
                    # FIX: Allow writing to terminal even if app_loaded is False
                    # This buffers the greeting text so it's visible when splash fades
                    self.terminal.configure(state="normal")
                    self.terminal.insert("end", msg_data)
                    self.terminal.see("end")
                    self.terminal.configure(state="disabled")

                elif msg_type == "clear":
                    self.terminal.configure(state="normal")
                    self.terminal.delete("1.0", "end")
                    self.terminal.configure(state="disabled")
                elif msg_type == "state":
                    if msg_data == "normal":
                        if not self.app_loaded:
                            self.dismiss_splash()
                            self.terminal.see("end")
                        self.entry.configure(state="normal")
                        self.status_btn.configure(text="READY", text_color=("#d67200", "#fab300"),
                                                  border_color=("#d67200", "#fab300"))
                        self.after(10, lambda: self.entry.focus_set())
                    else:
                        self.entry.configure(state="disabled")

            while not status_queue.empty():
                status_text = status_queue.get_nowait()
                if not self.app_loaded and self.splash_frame and status_text:
                    if len(status_text) > 3:
                        self.splash_status.configure(text=status_text.split('\n')[-1])

            while True:
                try:
                    latest = progress_queue.get_nowait()
                except queue.Empty:
                    break

                if latest:
                    val, active = latest
                    if active:
                        self.is_downloading = True
                        self.cpu_label.configure(text=">>> DOWNLOADING <<<", text_color=("black", "#00ff80"))
                        self.cpu_bar.configure(progress_color=("#2fa572", "#00ff80"))
                        self.cpu_bar.set(val)
                        self.status_btn.configure(text="NETWORK ACTIVE", text_color=("black", "#00ff80"))
                        if not self.app_loaded:
                            self.splash_status.configure(text=f"Updating: {int(val * 100)}%")
                    else:
                        if self.is_downloading:
                            self.cpu_bar.set(1.0)
                            self.is_downloading = False

        except Exception as e:
            print(f"GUI Error: {e}")
        self.after(50, self.process_queue)

    def update_stats(self):
        if not self.is_downloading and self.app_loaded:
            self.cpu_label.configure(text="CPU Load", text_color=("gray20", "gray"))
            self.cpu_bar.configure(progress_color="#1f538d")
            self.cpu_bar.set(psutil.cpu_percent() / 100)
        self.ram_bar.set(psutil.virtual_memory().percent / 100)
        self.after(1000, self.update_stats)

    def run_backend(self):
        global print, input
        print = gui_print
        input = gui_input
        os.system = gui_system_override

        try:
            import pythoncom
            pythoncom.CoInitialize()
        except:
            pass

        while True:
            try:
                self.execute_user_logic()
            except Exception as e:
                print(f"System Recovery: {e}")
                time.sleep(2)

    def execute_user_logic(self):
        warnings.filterwarnings("ignore")
        os.system('cls')

        # FIX: Define dropbox_base here for Thread Context
        dropbox_base = DROPBOX_BASE_DIR

        def get_access_token(app_key, app_secret, refresh_token):
            try:
                auth_url = 'https://api.dropbox.com/oauth2/token'
                data = {'refresh_token': refresh_token, 'grant_type': 'refresh_token', 'client_id': app_key,
                        'client_secret': app_secret}
                response = requests.post(auth_url, data=data)
                response.raise_for_status()
                return response.json().get('access_token')
            except:
                return None

        splash_print("Connecting to Cloud...")
        access_token = get_access_token(DROPBOX_APP_KEY, DROPBOX_APP_SECRET, DROPBOX_REFRESH_TOKEN)
        dbx = None
        if access_token and dropbox:
            dbx = dropbox.Dropbox(access_token)
            splash_print("Cloud Connection Established.")
        else:
            splash_print("Offline Mode.")

        def sanitize_filename(filename):
            return re.sub(r'[<>:"/\\|?*]', '_', filename)

        # --- INSTALLATION ---
        count_filename = "run_count.txt"
        run_count = 0
        if os.path.exists(count_filename):
            try:
                run_count = int(open(count_filename, "r").read())
            except:
                run_count = 0
        else:
            open(count_filename, "w").write("0")

        if run_count == 0 and dbx:
            try:
                splash_print("First Run: Downloading Assets...")
                local_ver_path = 'version.dat'
                _, res = dbx.files_download(f'{DROPBOX_BASE_DIR}/version.dat')
                with open(local_ver_path, 'wb') as f:
                    f.write(res.content)
                load1 = pickle.load(open(local_ver_path, 'rb'))

                documents_dir = os.path.expanduser("~\\Documents")
                folder_name = f"NimoAssistant{load1}"
                target_dir = os.path.join(documents_dir, folder_name)
                if not os.path.exists(target_dir): os.makedirs(target_dir)

                splash_print("Downloading Executable...")
                dropbox_file_path = f'{DROPBOX_BASE_DIR}/NimoAssistant.exe'
                local_exe_path = os.path.join(target_dir, f'NimoAssistant{load1}.exe')
                metadata = dbx.files_get_metadata(dropbox_file_path)

                with open(local_exe_path, 'wb') as f:
                    response = dbx.files_download(dropbox_file_path)[1]
                    downloaded = 0
                    for chunk in response.iter_content(4096):
                        f.write(chunk)
                        downloaded += len(chunk)
                        progress_queue.put((downloaded / metadata.size, True))

                progress_queue.put((1.0, True))
                time.sleep(0.5)
                progress_queue.put((0, False))

                splash_print("Installing...")
                try:
                    shell = win32com.client.Dispatch("WScript.Shell")
                    desktop = os.path.expanduser("~\\Desktop")
                    shortcut = shell.CreateShortCut(os.path.join(desktop, "NimoAssistant.lnk"))
                    shortcut.TargetPath = local_exe_path
                    shortcut.WorkingDirectory = target_dir
                    shortcut.Save()

                    key = winreg.HKEY_CURRENT_USER
                    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
                    with winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS) as reg:
                        winreg.SetValueEx(reg, "NimoAssistant", 0, winreg.REG_SZ, local_exe_path)
                except:
                    pass

                splash_print("Configuring User Data...")
                open(count_filename, "w").write("1")
                for f_name in ['run_count.txt', 'age.dat', 'name1.dat', 'version.dat']:
                    if os.path.exists(f_name):
                        try:
                            shutil.move(f_name, os.path.join(target_dir, f_name))
                        except:
                            pass

                splash_print("Installation Complete. Launching...")
                try:
                    os.startfile(local_exe_path)
                except:
                    subprocess.Popen([local_exe_path], shell=True)
                time.sleep(2)
                os._exit(0)
            except SystemExit:
                raise
            except Exception as e:
                splash_print(f"Install Error: {e}")
                time.sleep(2)

        open(count_filename, "w").write(str(run_count + 1))

        # --- UPDATE ---
        if dbx:
            try:
                splash_print("Checking Updates...")
                local_ver_path = 'version.dat'
                _, res = dbx.files_download(f'{DROPBOX_BASE_DIR}/version.dat')
                with open(local_ver_path, 'wb') as f:
                    f.write(res.content)
                remote_ver = pickle.load(open(local_ver_path, 'rb'))
                os.remove(local_ver_path)

                if remote_ver != CURRENT_VERSION and remote_ver != 'maintenance':
                    splash_print(f"Updating to {remote_ver}...")

                    dropbox_file_path = f'{DROPBOX_BASE_DIR}/NimoAssistant.exe'
                    metadata = dbx.files_get_metadata(dropbox_file_path)
                    documents_dir = os.path.expanduser("~\\Documents")
                    folder_name = f"NimoAssistant{remote_ver}"
                    target_dir = os.path.join(documents_dir, folder_name)
                    if not os.path.exists(target_dir): os.makedirs(target_dir)
                    local_exe_path = os.path.join(target_dir, f'NimoAssistant{remote_ver}.exe')

                    with open(local_exe_path, 'wb') as f:
                        response = dbx.files_download(dropbox_file_path)[1]
                        downloaded = 0
                        for chunk in response.iter_content(4096):
                            f.write(chunk)
                            downloaded += len(chunk)
                            progress_queue.put((downloaded / metadata.size, True))

                    progress_queue.put((1.0, True))
                    time.sleep(0.5)
                    progress_queue.put((0, False))

                    splash_print("Applying Update...")
                    try:
                        shell = win32com.client.Dispatch("WScript.Shell")
                        desktop = os.path.expanduser("~\\Desktop")
                        shortcut = shell.CreateShortCut(os.path.join(desktop, "NimoAssistant.lnk"))
                        shortcut.TargetPath = local_exe_path
                        shortcut.WorkingDirectory = target_dir
                        shortcut.Save()
                    except:
                        pass

                    splash_print("Restarting...")
                    try:
                        os.startfile(local_exe_path)
                    except:
                        subprocess.Popen([local_exe_path], shell=True)
                    time.sleep(2)
                    os._exit(0)
            except SystemExit:
                raise
            except:
                pass

        # --- LOGIN ---
        while True:
            user_folder_path = ""
            if dbx:
                while True:
                    if os.path.exists("cloudpath.txt"):
                        with open("cloudpath.txt", "r") as f:
                            user_folder_path = f.read().strip()
                            splash_print(f"Logging in: {user_folder_path}")
                            break

                    # Input still uses main UI
                    choice = input("Log in (Y) / Register (N): ").lower()
                    if choice == 'n':
                        user = input("Enter new username: ")
                        folder = f"/Users/{user}"
                        try:
                            try:
                                dbx.files_get_metadata(folder)
                                print("Username taken.")
                                continue
                            except:
                                pass
                            dbx.files_create_folder_v2(folder)
                            pwd = input("Set password: ")
                            if Fernet:
                                enc_pwd = Fernet(key).encrypt(pwd.encode())
                                dbx.files_upload(enc_pwd, f"{folder}/creds.dat", mode=WriteMode('overwrite'))
                            else:
                                dbx.files_upload(pwd.encode(), f"{folder}/creds.dat", mode=WriteMode('overwrite'))

                            with open("cloudpath.txt", "w") as f:
                                f.write(folder)
                            user_folder_path = folder
                            print("Success.")
                            break
                        except Exception as e:
                            print(f"Error: {e}")
                    elif choice == 'y':
                        user = input("Username: ")
                        folder = f"/Users/{user}"
                        try:
                            _, res = dbx.files_download(f"{folder}/creds.dat")
                            if Fernet:
                                dec_pwd = Fernet(key).decrypt(res.content).decode()
                            else:
                                dec_pwd = res.content.decode()

                            inp_pwd = input("Password: ")
                            if inp_pwd == dec_pwd:
                                print("Success.")
                                with open("cloudpath.txt", "w") as f:
                                    f.write(folder)
                                user_folder_path = folder
                                break
                            else:
                                print("Wrong Password.")
                        except:
                            print("User not found.")

            if dbx and user_folder_path:
                splash_print("Syncing...")
                for file in ['name1.dat', 'age.dat', 'pre.dat', 'userhistory.txt']:
                    try:
                        _, res = dbx.files_download(f"{user_folder_path}/{file}")
                        with open(file, 'wb') as f:
                            f.write(res.content)
                    except:
                        pass

            def trigger_cloud_sync():
                if not dbx or not user_folder_path: return

                def _sync():
                    try:
                        for file in ['name1.dat', 'age.dat', 'pre.dat', 'userhistory.txt']:
                            if os.path.exists(file):
                                with open(file, 'rb') as f:
                                    dbx.files_upload(f.read(), f"{user_folder_path}/{file}",
                                                     mode=WriteMode('overwrite'))
                    except:
                        pass

                threading.Thread(target=_sync, daemon=True).start()

            global CURRENT_USER_NAME

            if not os.path.exists("name1.dat"):
                name = input("What is your name? ")
                pickle.dump(name, open("name1.dat", "wb"))
                trigger_cloud_sync()
                CURRENT_USER_NAME = name
            else:
                name = pickle.load(open("name1.dat", "rb"))
                CURRENT_USER_NAME = name

            if not os.path.exists("age.dat"):
                try:
                    age = int(input("Your age: "))
                    pickle.dump(age, open("age.dat", "wb"))
                    trigger_cloud_sync()
                except:
                    pass

            if genai:
                genai.configure(api_key=GEMINI_API_KEY)
                try:
                    model = genai.GenerativeModel(
                        model_name="gemini-2.0-flash",
                        system_instruction=NIMO_SYSTEM_RULES
                    )
                    convo = model.start_chat(history=[])
                except:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    convo = model.start_chat(history=[])
            else:
                convo = None

            pre_mode = "normal"
            if os.path.exists("pre.dat"): pre_mode = pickle.load(open("pre.dat", "rb"))

            # FINAL GREETING (Sent to Chat)
            print(f"Nimo : System initialized. Hello {name}! How can I help you today?")

            session_active = True
            while session_active:
                try:
                    hel = input("").strip()
                    hel_lower = hel.lower()
                    if not hel: continue

                    trigger_cloud_sync()

                    if "open " in hel_lower:
                        app = hel_lower.replace("open ", "")
                        print(f"Opening {app}...")
                        os.system(f"start {app}")

                    elif hel_lower in ['sign out', 'log out']:
                        print("Logging out...")
                        if os.path.exists("cloudpath.txt"): os.remove("cloudpath.txt")
                        if os.path.exists("logincount.txt"): os.remove("logincount.txt")
                        os.system('cls')
                        session_active = False

                    elif hel_lower in ['change mode', 'mode']:
                        pre_mode = input("Mode (Learning/Normal): ").lower()
                        pickle.dump(pre_mode, open("pre.dat", "wb"))
                        trigger_cloud_sync()
                        print(f"Mode: {pre_mode}")

                    elif hel_lower == 'reset' or hel_lower == 'factory reset':
                        print("Resetting...")
                        time.sleep(1)
                        for f in ['name1.dat', 'age.dat', 'pre.dat', 'userhistory.txt', 'cloudpath.txt',
                                  'logincount.txt']:
                            if os.path.exists(f): os.remove(f)
                        print("Restarting...")
                        time.sleep(2)
                        os.system('cls')
                        session_active = False

                    elif hel_lower == 'change my name':
                        name = input("New name: ")
                        pickle.dump(name, open("name1.dat", "wb"))
                        trigger_cloud_sync()
                        CURRENT_USER_NAME = name
                        print(f"Updated to: {name}")

                    elif hel_lower in ['vision mode', 'image search']:
                        print("Select image...")
                        path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg;*.png;*.jpeg")])
                        if path:
                            print("Analyzing...")
                            if vision:
                                print("Vision requires GCP credentials setup.")
                            else:
                                print("Vision Library Missing.")
                        else:
                            print("Cancelled.")

                    elif "youtube" in hel_lower and "download" in hel_lower:
                        if not yt_dlp:
                            print("YouTube DL Library Missing.")
                            continue

                        url_match = re.search(r'(https?://\S+)', hel_lower)
                        target = url_match.group(0) if url_match else input("Paste URL: ")
                        if target:
                            print(f"Downloading...")

                            def yt_progress(d):
                                if d['status'] == 'downloading':
                                    try:
                                        p = d.get('_percent_str', '0%').replace('%', '')
                                        progress_queue.put((float(p) / 100, True))
                                    except:
                                        pass
                                if d['status'] == 'finished':
                                    progress_queue.put((1.0, True))

                            try:
                                path = os.path.join(os.path.expanduser('~'), 'Downloads')
                                opts = {'outtmpl': f'{path}/%(title)s.%(ext)s', 'quiet': True,
                                        'progress_hooks': [yt_progress]}
                                with yt_dlp.YoutubeDL(opts) as ydl:
                                    ydl.download([target])
                                print("Download Complete.")
                            except Exception as e:
                                print(f"Error: {e}")
                            progress_queue.put((0, False))

                    elif hel_lower in ['exit', 'quit']:
                        print("Goodbye.")
                        time.sleep(1)
                        os._exit(0)
                    elif "health" in hel_lower:
                        print(f"CPU: {psutil.cpu_percent()}% | RAM: {psutil.virtual_memory().percent}%")
                    elif "clear" in hel_lower:
                        os.system("cls")

                    else:
                        # HIVE MIND LOGIC (Fixed dropbox_base variable)
                        sanitized = sanitize_filename(hel_lower)
                        local_dat = f"{sanitized}.dat"
                        cloud_dat = f"{dropbox_base}/{local_dat}"
                        found = False

                        if os.path.exists(local_dat):
                            try:
                                print(f"Nimo : {pickle.load(open(local_dat, 'rb'))}")
                                found = True
                            except:
                                pass

                        if not found and dbx:
                            try:
                                _, res = dbx.files_download(cloud_dat)
                                with open(local_dat, "wb") as f:
                                    f.write(res.content)
                                print(f"Nimo : {pickle.load(open(local_dat, 'rb'))}")
                                found = True
                            except:
                                pass

                        if not found:
                            if "learn" in pre_mode:
                                ch = input("I don't know. Teach (C) or Auto (X)? ").lower()
                                if ch == 'c':
                                    ans = input("Say: ")
                                    pickle.dump(ans, open(local_dat, "wb"))
                                    if dbx:
                                        try:
                                            with open(local_dat, 'rb') as f:
                                                dbx.files_upload(f.read(), cloud_dat, mode=WriteMode('overwrite'))
                                            print("Uploaded to Hive.")
                                        except:
                                            print("Saved locally.")
                                else:
                                    if convo:
                                        print("Thinking...")
                                        ans = convo.send_message(hel).text.replace("**", "").replace("##", "")
                                        print(f"Nimo : {ans}")
                                    else:
                                        print("AI Offline.")
                            else:
                                if convo:
                                    print("Thinking...")
                                    ans = convo.send_message(hel).text.replace("**", "").replace("##", "")
                                    print(f"Nimo : {ans}")
                                    try:
                                        pickle.dump(ans, open(local_dat, "wb"))
                                        if dbx:
                                            with open(local_dat, 'rb') as f:
                                                dbx.files_upload(f.read(), cloud_dat, mode=WriteMode('overwrite'))
                                    except:
                                        pass
                                else:
                                    print("AI Offline.")

                except Exception as loop_e:
                    print(f"Error: {loop_e}")


if __name__ == "__main__":
    app = NimoCommandStation()
    app.mainloop()
