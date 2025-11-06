import tempfile, os, pickle, webbrowser, time, requests, random, shutil, logging, warnings, json, io, sys, base64, cv2, numpy as np, tkinter as tk
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import wikipedia
import dropbox
from dropbox.exceptions import ApiError, AuthError
from dropbox.files import WriteMode
import PIL.Image
import win32com.client
import wolframalpha
import openai
import winreg
import re
import asyncio
from colorama import Fore, init, Style
from rich.console import Console
from datetime import datetime
from cryptography.fernet import Fernet
from google.cloud import vision
from google.oauth2 import service_account
from tkinter import Tk, filedialog, ttk
from tqdm import tqdm
import psutil
from concurrent.futures import ThreadPoolExecutor
import google.generativeai as genai
import subprocess
base_folder = '/Users'
warnings.filterwarnings("ignore", category=UserWarning, module="pyinstaller.loader.pyimod02_importers")
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y%m%d%H%M%S")
log_file = f"error{formatted_datetime}.log"
logging.basicConfig(filename=log_file, level=logging.WARNING, format='%(asctime)s - %(levelname)s: %(message)s')
logging.getLogger('').propagate = True

os.system('cls')
try:
    try:

        def type_animationintro(text, delay=0.005):
            i = 0
            while i < len(text):
                print(text[i], end='', flush=True)
                time.sleep(delay)
                i += 1
            print()


        ascii_art = r'''
             __  __                            
            /\ \/\ \  __                       
            \ \ `\\ \/\_\    ___ ___     ___   
             \ \ , ` \/\ \ /' __` __`\  / __`\\ 
              \ \ \`\ \ \ \/\ \/\ \/\ \/\ \L\ \\
               \ \_\ \_\ \_\ \_\ \_\ \_\ \____/
                \/_/\/_/\/_/\/_/\/_/\/_/\/___/ 
        
        
             ______                               __                    __      
            /\  _  \                  __         /\ \__                /\ \__   
            \ \ \L\ \    ____    ____/\_\    ____\ \ ,_\    __      ___\ \ ,_\  
             \ \  __ \  /',__\  /',__\/\ \  /',__\\ \ \/  /'__`\  /' _ `\ \ \/  
              \ \ \/\ \/\__, `\_/\__, `\ \ \/\__, `\\ \ \_/\ \L\.\_/\ \/\ \ \ \_ 
               \ \_\ \_\/\____/\/\____/\ \_\/\____/ \ \__\ \__/.\_\ \_\ \_\ \__\\
                \/_/\/_/\/___/  \/___/  \/_/\/___/   \/__/\/__/\/_/\/_/\/_/\/__/
        '''
        type_animationintro(ascii_art)
    except Exception as e:
        # Log the exception
        logging.exception("An error occurred:")

    os.system('cls')
    openai.api_key = "YOUROPENAIAPI" #PLEASE REPLACE WITH YOUR CREDENTIALS
    app_key = 'YOURDROPBOXAPPKEY'
    app_secret = 'YOURDROPBOXAPPSECRET'
    refresh_token = 'YOURDROPBOXREFRESHTOKEN'
    app_id = 'YOURWOLFRAMALPHAAPIKEY'
    local_folder_path = os.getcwd()
    init(autoreset=True)
    file_path = os.path.join(local_folder_path, 'version.dat')
    if os.path.exists(file_path):
        os.remove(file_path)


    class QueryLogger:
        def __init__(self, filename="userhistory.txt"):
            self.filename = filename
            self.history = self.load_history()

        def load_history(self):
            """Load history from the file."""
            try:
                with open(self.filename, "r") as file:
                    # Read all lines and strip the newline characters
                    return [line.strip() for line in file.readlines()]
            except FileNotFoundError:
                # If the file doesn't exist, start with an empty history
                return []

        def log_query(self, query):
            """Log a new query to the history with a timestamp."""
            # Get the current time and format it as: 27 Nov 2024, 11:15 PM
            timestamp = datetime.now().strftime("%d %b %Y, %I:%M %p")
            log_entry = f"{query} [{timestamp}]"  # Format the log entry
            self.history.append(log_entry)
            with open(self.filename, "a") as file:
                file.write(log_entry + "\n")

        def display_history(self):
            """Display all history."""
            if self.history:
                print("\nUser History:")
                for index, entry in enumerate(self.history, 1):
                    print(f"{index}. {entry}")
            else:
                print("No history found.")

        def clear_history(self):
            """Clear the history."""
            open(self.filename, "w").close()  # This clears the file content
            self.history = []  # Reset the history list
            print("History cleared.")


    def get_random_greeting():
        greetings = [
            "Hello!",
            "Hi there!",
            "Greetings!",
            "Welcome back!",
            "Good to see you!",
            "Hola!",
            "Hey!",
            "Howdy!",
            "Salutations!",
            "Namaste!",
            "Bonjour!",
            "Ciao!",
            "Aloha!",
            "Yo!",
            "What's up!",
            "Nice to meet you!",
            "How are you today?",
            "Hola amigo!",
            "Top of the morning to you!",
            "G'day mate!",
            "Hey sunshine!",
            "Hey you!",
            "Hi friend!",
            "What's cracking?",
            "Hey there, superstar!",
            "Long time no see!",
            "How's it going?",
            "Hey stranger!",
            "Hi champ!",
            "What's the scoop?",
            "How's life treating you?",
            "Hello sunshine!",
            "Hey smarty pants!",
            "Hiya pal!",
            "How's your day?",
            "Hey genius!",
            "Hi superhero!",
            "What's cooking?",
            "Hey hot stuff!",
            "Hi partner!",
            "How's the world's best doing?",
            "Hey rockstar!",
            "Hi genius!",
            "What's the word?",
            "Hey maestro!",
            "Hi trendsetter!",
            "How's everything?",
            "What's the gossip?",
            # Add more greetings as needed
        ]
        return random.choice(greetings)


    def extract_text_from_image(image_path):
        with open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations

        if texts:
            return texts[0].description
        else:
            return "No text found in the image."

    def select_image():
        root = Tk()
        root.withdraw()  # Hide the main window
        file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        root.destroy()  # Close the main window
        return file_path

    # Function to encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    def extractlive_text_from_image(image_content, client):
        image = vision.Image(content=image_content)
        response = client.text_detection(image=image)
        texts = response.text_annotations

        if texts:
            return texts[0].description
        else:
            return "No text found in the image."
    def get_image_path():
        root = Tk()
        root.withdraw()  # Hide the main window

        file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        root.destroy()  # Close the main window

        return file_path


    def get_access_token_from_refresh_token(app_key, app_secret, refresh_token):
        try:
            auth_url = 'https://api.dropbox.com/oauth2/token'
            auth_data = {
                'refresh_token': refresh_token,
                'grant_type': 'refresh_token',
                'client_id': app_key,
                'client_secret': app_secret,
            }
            response = requests.post(auth_url, data=auth_data)
            response.raise_for_status()  # Raise an exception for HTTP errors
            access_token = response.json().get('access_token')
            return access_token
        except requests.exceptions.RequestException:
            print(f"Failed to connect to cloud")
            return None


    access_token = get_access_token_from_refresh_token(app_key, app_secret, refresh_token)

    if access_token:
        dbx = dropbox.Dropbox(access_token)
        local_folder_path = os.getcwd()
        allowed_extensions = ['.dat', '.log']
        excluded_files = ['age.dat', 'name1.dat', 'pre.dat']
        dropbox_target_folder = '/home/YOURS/Apps/'#REPLACE YOUR PATH


        def file_exists_in_dropbox(dbx, remote_path):
            try:
                dbx.files_get_metadata(remote_path)
                return True
            except dropbox.exceptions.HttpError as e:
                if e.error.is_path() and \
                        e.error.get_path().is_conflict() and \
                        e.error.get_path().is_conflict().is_file():
                    return True
                return False
            except dropbox.exceptions.DropboxException:
                return False


        def upload_chunked(args):
            file_path, remote_path, total_bar = args
            chunk_size = 4 * 1024 * 1024  # 4 MB chunk size

            with open(file_path, 'rb') as file:
                file_size = os.path.getsize(file_path)
                total_chunks = (file_size + chunk_size - 1) // chunk_size

                # Update the total progress bar with file name
                total_bar.set_postfix(file=os.path.basename(file_path), refresh=True)

                session_id = None
                for i in range(total_chunks):
                    data = file.read(chunk_size)
                    if i == 0:
                        # Start a new upload session
                        response = dbx.files_upload_session_start(data)
                        session_id = response.session_id
                    else:
                        # Append to the existing upload session
                        dbx.files_upload_session_append_v2(data, session_id, i * chunk_size)

                    # Update the total progress bar
                    total_bar.update(1)

                # Finish the upload session
                dbx.files_upload_session_finish(file.read(), session_id, total_chunks * chunk_size)


        def upload_files_in_folder(dbx, local_folder_path, allowed_extensions, excluded_files):
            try:
                total_size = 0

                # Calculate total size of files to upload
                for root, dirs, files in os.walk(local_folder_path):
                    for file_name in files:
                        _, file_extension = os.path.splitext(file_name)
                        if file_extension.lower() in allowed_extensions and file_name not in excluded_files:
                            file_path = os.path.join(root, file_name)
                            total_size += os.path.getsize(file_path)

                # Initialize tqdm total progress bar
                total_bar = tqdm(total=total_size, unit='B', unit_scale=True, dynamic_ncols=True, leave=True,
                                 smoothing=0.1, miniters=1, desc="Uploading")

                upload_args = []
                for root, dirs, files in os.walk(local_folder_path):
                    for file_name in files:
                        _, file_extension = os.path.splitext(file_name)
                        if file_extension.lower() in allowed_extensions and file_name not in excluded_files:
                            file_path = os.path.join(root, file_name)
                            remote_path = os.path.join(dropbox_target_folder, file_name)

                            if not file_exists_in_dropbox(dbx, remote_path):
                                upload_args.append((file_path, remote_path, total_bar))

                # Use ThreadPoolExecutor for concurrent uploads
                with ThreadPoolExecutor(max_workers=5) as executor:
                    executor.map(upload_chunked, upload_args)

                # Close the total tqdm progress bar
                total_bar.close()

            except Exception as e:
                print(f"Error during data upload: {e}")
                logging.error('An error occurred:', exc_info=True)


    else:
        print("No internet connection or failed to connect to the cloud. Please check your internet connection"
              " and try again later.")
        time.sleep(5)
        print('Closing program, goodbye.')
        time.sleep(3)
        exit()



    def get_location():
        try:
            res = requests.get('https://ipinfo.io/')
            data = res.json()
            city = data["city"]
            longitudeandlatitude = data['loc']
            postal = data['postal']
            return f"You are in {city}, {longitudeandlatitude}, postal code {postal}"
        except requests.exceptions.RequestException:
            return "Can't locate you. Please check your internet connection."


    def download_youtube_video():
        try:
            url = input("Paste the URL here: ")
            video = YouTube(url)
            streams = video.streams.filter(progressive=True, file_extension="mp4")
            highest_resolution_stream = streams.get_highest_resolution()
            home = os.path.expanduser('~')
            location = os.path.join(home, 'Downloads')

            print(f"Downloading {video.title}...")

            with tqdm(
                    unit="B", unit_scale=True, unit_divisor=1024, total=highest_resolution_stream.filesize,
                    dynamic_ncols=True, leave=True, smoothing=0.1, miniters=1
            ) as bar:
                highest_resolution_stream.download(
                    output_path=location,
                    filename=highest_resolution_stream.default_filename,
                    filename_prefix='',
                    skip_existing=False,
                    timeout=None,
                    max_retries=0,
                    skip_unavailable_fragments=False,
                    check_integrity=True,
                    progress_function=bar.update  # No need for this line if using tqdm as a context manager
                )

            return f"Download succeeded. Downloaded in {location}"
        except VideoUnavailable:
            return "The video is unavailable or restricted."
        except Exception as e:
            return f"Can't download the video. Error: {e}"



    def open_website(website_url):
        try:
            print(f"Opening {website_url}...")
            webbrowser.open(website_url)
            return f"Opened {website_url} in your default web browser."
        except Exception as e:
            return f"Failed to open {website_url}. Error: {e}"

    def download_file_from_dropbox(access_token, file_path):
        dbx = dropbox.Dropbox(access_token)

        try:
            metadata, response = dbx.files_download(file_path)
            local_destination = 'credent.json.encrypted'
            with open(local_destination, "wb") as local_file:
                local_file.write(response.content)
        except dropbox.exceptions.HttpError as err:
            print(f"Cloud Error: {err}")


    dropbox_access_token = access_token

    # Replace '/path/to/your/dropbox/file.json' with the path to your JSON file on Dropbox
    dropbox_file_path = 'YOURPATH'

    # Download the file from Dropbox
    download_file_from_dropbox(dropbox_access_token, dropbox_file_path)

    def decrypt_json_file(encrypted_file_path, encryption_key):
        with open(encrypted_file_path, 'rb') as encrypted_file:
            encrypted_content = encrypted_file.read()

        cipher_suite = Fernet(encryption_key)
        decrypted_content = cipher_suite.decrypt(encrypted_content)

        return decrypted_content
    encryption_key = #YOURKEY
    encrypted_file_path = 'credent.json.encrypted'

    # Decrypt the encrypted JSON key file
    decrypted_content = decrypt_json_file(encrypted_file_path, encryption_key)

    # Load the decrypted JSON content
    json_data = json.loads(decrypted_content.decode())

    # Authenticate using the decrypted JSON data
    credentials = service_account.Credentials.from_service_account_info(
        json_data,
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )

    # Vision API client initialization
    client = vision.ImageAnnotatorClient(credentials=credentials)
    def create_folder(dbx, base_folder, folder_name):
        folder_path = f'{base_folder}/{folder_name}'
        try:
            dbx.files_create_folder(folder_path)
            print(f"Username '{folder_name}' created successfully.")
            # Get the Dropbox file path
            file_path = dbx.files_get_metadata(folder_path).path_display
            return folder_path
        except dropbox.exceptions.ApiError as e:
            if e.error.is_path() and e.error.get_path().is_conflict():
                print(f"Username '{folder_name}' already exists. Please choose a different name.")
                return None
            else:
                print(f"Error creating Username '{folder_name}': {e}")
                return None


    def encrypt_and_upload(dbx, folder_path, file_name, data):
        key = #YOURKEY
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(data.encode())

        file_path = f'{folder_path}/{file_name}.dat'

        try:
            dbx.files_upload(encrypted_data, file_path)
            return True
        except dropbox.exceptions.ApiError as e:
            print(f"Error': {e}")
            return False

    def folder_exists(dbx, base_folder, folder_name):
        try:
            # List the contents of the base folder
            result = dbx.files_list_folder(base_folder)

            # Check if the folder_name exists in the list of entries
            for entry in result.entries:
                if entry.name == folder_name and isinstance(entry, dropbox.files.FolderMetadata):
                    return True

            return False
        except dropbox.exceptions.ApiError as e:
            print(f"Error: {e}")
            return False

    def download_and_decrypt(dbx, folder_path, creds_filename, key):
        try:
            # Specify the file path in the Dropbox folder starting with a '/'
            file_path = f"/Users/{folder_path}/{creds_filename}"

            # Download the creds.dat file
            metadata, response = dbx.files_download(file_path)
            encrypted_data = response.content

            # Decrypt the data using the provided key
            cipher = Fernet(key)
            decrypted_data = cipher.decrypt(encrypted_data).decode("utf-8")
            os.system('cls')
            return decrypted_data
        except dropbox.exceptions.ApiError as e:
            print(f"Error: {e}")
            return None

    def upload_to_dropbox(dbx, local_path, dropbox_path,):
        with open(local_path, 'rb') as file:
            dbx.files_upload(file.read(), dropbox_path, mode=WriteMode('overwrite'))

    def initialize_vision_client(credentials):
        return vision.ImageAnnotatorClient(credentials=credentials)

    def calculate():
        try:
            print("Opening calculator")

            def add(x, y):
                return x + y

            def subtract(x, y):
                return x - y

            def multiply(x, y):
                return x * y

            def divide(x, y):
                return x / y

            print("Select operation.")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            choice = input("Enter choice (1/2/3/4): ")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            else:
                return "Invalid input."

            return f"Result: {result}"
        except Exception as e:
            return f"An error occurred: {e}"


    def create_directory(directory_path):
        try:
            os.makedirs(directory_path)
            print(f"Folder '{directory_path}' created.")
        except FileExistsError:
            print(f"Folder '{directory_path}' already exists.")
        except Exception as e:
            print(f"Error creating folder: {e}")


    def create_desktop_shortcut(script_path, shortcut_name):
        try:
            script_directory = os.path.dirname(sys.argv[0])

            # Construct the full path of the original executable
            original_executable_path = os.path.join(script_directory, sys.argv[0])

            desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
            shortcut_path = os.path.join(desktop_path, f"{shortcut_name}.lnk")

            # Create a shortcut to the original executable
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.TargetPath = original_executable_path
            shortcut.WorkingDirectory = script_directory  # Set the working directory
            shortcut.save()
        except:
            print(Fore.RED + 'Unable to create shortcut, please create manually')
            logging.warning("Couldnn't save shortcut")
            time.sleep(2)

    def check_memory_health():
        try:
            print("Checking Memory Health...")
            virtual_memory = psutil.virtual_memory()

            # Adjust the threshold as needed
            healthy_memory_threshold = 80.0
            if virtual_memory.percent <= healthy_memory_threshold:
                print(f"Memory is healthy. Usage: {virtual_memory.percent}%")
                return 1
            else:
                print(f"Warning: High memory usage detected ({virtual_memory.percent}%). Possible performance impact.")
                return 0
        except Exception as e:
            print(f"Error checking Memory Health: {e}")
            return 0

    def get_cpu_temperature():
        try:
            print('Checking CPU temperature...')
            # Use psutil to get CPU usage
            cpu_usages = psutil.cpu_percent(interval=1, percpu=True)

            # Check for overheat condition (adjust the threshold as needed)
            overheat_threshold = 80.0
            overheat_cores = [i for i, usage in enumerate(cpu_usages) if usage > overheat_threshold]

            if overheat_cores:
                print(f"Warning: CPU temperature is too high on cores {', '.join(map(str, overheat_cores))}. Possible overheat.")
                return 0
            else:
                print(f'CPU Temperature is stable. Cores Usage: {cpu_usages}')
                return 1
        except Exception as e:
            print(f"Error getting CPU temperature: {e}")
            logging.error('An error occurred:', exc_info=True)
            return 0

    def test_storage_speed():
        try:
            print("Testing Storage Speed...")
            temp_file_path = tempfile.mktemp()

            # Write operation
            start_time = time.time()
            with open(temp_file_path, 'wb') as temp_file:
                temp_file.write(b'0' * 1024 * 1024)  # Writing 1 MB data
            write_speed = os.path.getsize(temp_file_path) / (time.time() - start_time) / 10**6  # Convert to MBps
            print(f"Write Speed: {write_speed:.2f} MBps")

            # Read operation
            start_time = time.time()
            with open(temp_file_path, 'rb') as temp_file:
                temp_file.read()
            read_speed = os.path.getsize(temp_file_path) / (time.time() - start_time) / 10**6  # Convert to MBps
            print(f"Read Speed: {read_speed:.2f} MBps")

            # Clean up
            os.remove(temp_file_path)

            # Adjust the threshold as needed
            good_speed_threshold = 20.0
            if write_speed >= good_speed_threshold and read_speed >= good_speed_threshold:
                print("Storage speed is good.")
                return 1
            else:
                print("Warning: Slow storage speed detected. Possible storage issues.")
                return 0
        except Exception as e:
            print(f"Error testing Storage Speed: {e}")
            logging.error('An error occurred:', exc_info=True)
            return 0



    def open_application_windows(user_input):
        # Split the user input into words
        words = user_input.split()

        # Check if the user input starts with "open" and has at least two words
        if len(words) >= 2 and words[0].lower() == 'open':
            app_short_name = words[1].lower()

            app_mapping = {
                'notepad': 'notepad.exe',
                'calc': 'calc.exe',
                'cmd': 'cmd.exe',
                'explorer': 'explorer.exe',
                'word': 'winword.exe',
                'excel': 'excel.exe',
                'powerpoint': 'powerpnt.exe',
                'edge': 'msedge.exe',
                'vscode': 'Code.exe',
                'outlook': 'outlook.exe',
                'spotify': 'Spotify.exe',
                'paint': 'mspaint.exe',
                'filezilla': 'FileZilla.exe',
                'skype': 'Skype.exe',
                'vlc': 'vlc.exe',
                'winamp': 'winamp.exe',
                'sublime': 'sublime_text.exe',
                'photoshop': 'photoshop.exe',
                'steam': 'steam.exe',
                'obs': 'obs.exe',
                'notion': 'Notion.exe',
                'slack': 'slack.exe',
                'telegram': 'Telegram.exe',
                'discord': 'Discord.exe',
                'whatsapp': 'WhatsApp.exe',
                'visualstudio': 'devenv.exe',
                'chrome': 'chrome.exe',
                'firefox': 'firefox.exe',
                'adobeacrobat': 'AcroRd32.exe',
                'adobephotoshop': 'photoshop.exe',
                'adobeillustrator': 'illustrator.exe',
                'androidstudio': 'studio64.exe',
                'mysqlworkbench': 'MySQLWorkbench.exe',
                'putty': 'putty.exe',
                'wireshark': 'wireshark.exe',
                'postman': 'Postman.exe',
                'xampp': 'xampp-control.exe',
                'gitbash': 'git-bash.exe',
                'visualstudiocode': 'Code.exe',
                'microsoftteams': 'Teams.exe',
                'microsoftedge': 'msedge.exe',
                'onedrive': 'OneDrive.exe',
                'adobepremiere': 'Adobe Premiere Pro.exe',
                'adobeaftereffects': 'AfterFX.exe',
                'autocad': 'acad.exe',
                'blender': 'blender.exe',
                'eclipse': 'eclipse.exe',
                'itunes': 'iTunes.exe',
                'matlab': 'matlab.exe',
                'mongodbcompass': 'MongoDBCompass.exe',
                'oraclevirtualbox': 'VirtualBox.exe',
                'pycharm': 'pycharm64.exe',
                'vmwareworkstation': 'vmware.exe',
                'zoom': 'Zoom.exe'
                # Add more mappings as needed
            }

            try:
                app_name = app_mapping.get(app_short_name)
                if app_name:
                    os.system(f'start {app_name}')
                    print(f"Opening {app_name}")
                else:
                    print(f"Application not found for short name: {app_short_name}")
            except Exception as e:
                print(f"Error: {e}")
                logging.error('An error occurred:', exc_info=True)
        else:
            print("Invalid format. Please use 'open [app_name]'.")


    def sanitize_filename(filename):
        """
        Sanitize the filename to remove characters invalid for the filesystem.
        Replaces invalid characters with underscores ('_').
        """
        return re.sub(r'[<>:"/\\|?*]', '_', filename)
    def delete_folders_in_documents(relative_paths):
        user_documents_path = os.path.join(os.path.expanduser('~'), 'Documents')

        for relative_path in relative_paths:
            folder_path = os.path.join(user_documents_path, relative_path)

            if os.path.exists(folder_path):
                try:
                    shutil.rmtree(folder_path)
                except Exception as e:
                    print(f"{e}")
            else:
                print('')


    def create_upload_script():
        """
        Create a temporary Python script to handle Dropbox uploads in the background.
        """
        upload_script_content = """import os
import dropbox
import logging
import requests

# Dropbox app credentials
app_key = 'YOURDROPBOXAPPKEY'
app_secret = 'YOURDROPBOXAPPSECRET'
refresh_token = 'YOURDROPBOXREFRESHTOKEN'

# Initialize logging
logging.basicConfig(
    filename="async_upload.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s"
)

def get_access_token_from_refresh_token(app_key, app_secret, refresh_token):
    try:
        auth_url = 'https://api.dropbox.com/oauth2/token'
        auth_data = {
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token',
            'client_id': app_key,
            'client_secret': app_secret,
        }
        response = requests.post(auth_url, data=auth_data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        access_token = response.json().get('access_token')
        return access_token
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to refresh access token: {e}")
        return None

def upload_files_to_dropbox(access_token, local_folder, allowed_extensions, excluded_files, dropbox_folder):
    try:
        dbx = dropbox.Dropbox(access_token)
        for root, dirs, files in os.walk(local_folder):
            for file_name in files:
                _, file_extension = os.path.splitext(file_name)
                if file_extension in allowed_extensions and file_name not in excluded_files:
                    file_path = os.path.join(root, file_name)
                    dropbox_path = f"{dropbox_folder}/{file_name}"
                    with open(file_path, 'rb') as file:
                        dbx.files_upload(file.read(), dropbox_path, mode=dropbox.files.WriteMode('overwrite'))
                        logging.info(f"Uploaded {file_name} to {dropbox_path}")
    except Exception as e:
        logging.error("Error during upload:", exc_info=True)

if __name__ == "__main__":
    access_token = get_access_token_from_refresh_token(app_key, app_secret, refresh_token)
    if not access_token:
        logging.error("No valid access token. Exiting.")
    else:
        LOCAL_FOLDER = os.getcwd()
        ALLOWED_EXTENSIONS = [".dat"]
        EXCLUDED_FILES = ["age.dat", "name1.dat", "pre.dat","version.dat"]
        DROPBOX_FOLDER = "YOURPATH"

        upload_files_to_dropbox(access_token, LOCAL_FOLDER, ALLOWED_EXTENSIONS, EXCLUDED_FILES, DROPBOX_FOLDER)
"""
        # Write the script to a temporary file
        script_path = os.path.join(tempfile.gettempdir(), "upload_files_async.py")
        with open(script_path, "w") as script_file:
            script_file.write(upload_script_content)
        return script_path

    def start_async_upload():
        """
        Start the asynchronous upload process.
        """
        try:
            script_path = create_upload_script()
            subprocess.Popen(["python", script_path], start_new_session=True)
        except Exception as e:
            logging.error("Failed to start the async upload process:", exc_info=True)

    console = Console()
    #the ibrahim glitch i guess fixed
    async def variant1(text, speed):
        for char in text:
            print(Fore.GREEN + char + Style.RESET_ALL, end='', flush=True)
            await asyncio.sleep(speed)  # Non-blocking sleep
        print()


    async def variant2(text, speed):
        for char in text:
            print(Fore.GREEN + char + Style.RESET_ALL, end='', flush=True)
            await asyncio.sleep(speed)  # Non-blocking sleep
        print()


    async def variant3(text, speed):
        for char in text:
            print(Fore.GREEN + char + Style.RESET_ALL, end='', flush=True)
            await asyncio.sleep(speed)  # Non-blocking sleep
        print()


    async def variant4(text, speed):
        for char in text:
            print(Fore.GREEN + char + Style.RESET_ALL, end='', flush=True)
            await asyncio.sleep(speed)  # Non-blocking sleep
        print()


    async def variant5(text, speed):
        for char in text:
            print(Fore.GREEN + char + Style.RESET_ALL, end='', flush=True)
            await asyncio.sleep(speed)  # Non-blocking sleep
        print()


    async def variant6(text, speed):
        for char in text:
            print(Fore.GREEN + char + Style.RESET_ALL, end='', flush=True)
            await asyncio.sleep(speed)  # Non-blocking sleep
        print()


    async def variant7(text, speed):
        for char in text:
            print(Fore.GREEN + char + Style.RESET_ALL, end='', flush=True)
            await asyncio.sleep(speed)  # Non-blocking sleep
        print()


    async def variant8(text, speed):
        for char in text:
            print(Fore.GREEN + char + Style.RESET_ALL, end='', flush=True)
            await asyncio.sleep(speed)  # Non-blocking sleep
        print()


    async def variant9(text, speed):
        for char in text:
            print(Fore.GREEN + char + Style.RESET_ALL, end='', flush=True)
            await asyncio.sleep(speed)  # Non-blocking sleep
        print()


    async def variant10(text, speed):
        for char in text:
            print(Fore.GREEN + char + Style.RESET_ALL, end='', flush=True)
            await asyncio.sleep(speed)  # Non-blocking sleep
        print()


    async def print_with_speed(text, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            await asyncio.sleep(delay)
        print()


    def check_file_content(countfilepath):
        try:
            with open(countfilepath, 'r') as file:
                content = file.read()
                if content:
                    print("")
                    # Do something with the content if needed
                else:
                    userregornah = input('Log in(Y)/Register(N), press Y or N: ')
                    if userregornah.lower() == 'n':
                        while True:
                            # Get user input for folder name
                            user_folder_name = input("Enter Username: ")

                            # Call the create_folder function with the specified base folder and user input
                            folder_path = create_folder(dbx, base_folder, user_folder_name)
                            cloudpathfilename = 'cloudpath.txt'
                            with open(cloudpathfilename, "w") as filed:
                                filed.write(str(folder_path))

                            # If the folder is created successfully, proceed to the next steps
                            if folder_path:
                                # Get user input for file name and data
                                user_file_name = 'creds'
                                user_data = input("Enter a password: ")

                                # Call the encrypt_and_upload function to encrypt and upload the data to the folder
                                upload_success = encrypt_and_upload(dbx, folder_path, user_file_name, user_data)

                                # If the upload is successful, break out of the loop
                                if upload_success:
                                    os.system('cls')
                                    break
                    elif userregornah.lower() == 'y':
                        while True:
                            user_folder_name = input("Enter username: ")

                            # Call the folder_exists function with the specified base folder and user input
                            exists = folder_exists(dbx, base_folder, user_folder_name)
                            if exists:
                                print(f"Username '{user_folder_name}' authorization successful.")
                                cloudpathfilename = 'cloudpath.txt'
                                with open(cloudpathfilename, "w") as file:
                                    file.write(str(user_folder_name))

                                # Assume you have the encryption key for decrypting the creds.dat file
                                encryption_key = #YOURKEY

                                # Download and decrypt creds.dat
                                decrypted_data = download_and_decrypt(dbx, user_folder_name, 'creds.dat', encryption_key)

                                if decrypted_data:
                                    # Get user input for data to compare
                                    user_input_data = input("Enter your password: ")
                                    userpass = 'usercred.txt'
                                    with open(userpass, "w") as file:
                                        file.write(str(user_input_data))
                                    # Compare user input with decrypted data from creds.dat
                                    if user_input_data == decrypted_data:
                                        print("User password matches. Log in successful.")
                                        os.system('cls')
                                        break
                                    else:
                                        print("User password does not match. Access denied.")
                                else:
                                    print("Error.")
                            else:
                                print(f"The Username '{user_folder_name}' does not exist.")
                    else:
                        print('Invalid input.')
        except:
            userregornah = input('Log in(Y)/Register(N), press Y or N: ')
            if userregornah.lower() == 'n':
                while True:
                    # Get user input for folder name
                    user_folder_name = input("Enter Username: ")

                    # Call the create_folder function with the specified base folder and user input
                    folder_path = create_folder(dbx, base_folder, user_folder_name)
                    cloudpathfilename = 'cloudpath.txt'
                    with open(cloudpathfilename, "w") as file:
                        file.write(str(folder_path))

                    # If the folder is created successfully, proceed to the next steps
                    if folder_path:
                        # Get user input for file name and data
                        user_file_name = 'creds'
                        user_data = input("Enter a password: ")

                        # Call the encrypt_and_upload function to encrypt and upload the data to the folder
                        upload_success = encrypt_and_upload(dbx, folder_path, user_file_name, user_data)

                        # If the upload is successful, break out of the loop
                        if upload_success:
                            os.system('cls')
                            break
            elif userregornah.lower() == 'y':
                while True:
                    user_folder_name = input("Enter username: ")

                    # Call the folder_exists function with the specified base folder and user input
                    exists = folder_exists(dbx, base_folder, user_folder_name)
                    if exists:
                        print(f"Username '{user_folder_name}' authorization successful.")
                        cloudpathfilename = 'cloudpath.txt'
                        with open(cloudpathfilename, "w") as file:
                            file.write(str(user_folder_name))

                        # Assume you have the encryption key for decrypting the creds.dat file
                        encryption_key = #YOURKEY

                        # Download and decrypt creds.dat
                        decrypted_data = download_and_decrypt(dbx, user_folder_name, 'creds.dat', encryption_key)

                        if decrypted_data:
                            # Get user input for data to compare
                            user_input_data = input("Enter your password: ")
                            userpass = 'usercred.txt'
                            with open(userpass, "w") as file:
                                file.write(str(user_input_data))
                            # Compare user input with decrypted data from creds.dat
                            if user_input_data == decrypted_data:
                                print("User password matches. Log in successful.")
                                os.system('cls')
                                break
                            else:
                                print("User password does not match. Access denied.")
                        else:
                            print("Error.")
                    else:
                        print(f"The Username '{user_folder_name}' does not exist.")
            else:
                print('Invalid input.')
    def check_file_pass(passfilepath):
        try:
            with open(passfilepath, 'r') as file:
                content = file.read()
                if content:
                    print('')
                    # Do something with the content if needed
                else:
                    userregornah = input('Log in(Y)/Register(N), press Y or N: ')
                    if userregornah.lower() == 'n':
                        while True:
                            # Get user input for folder name
                            user_folder_name = input("Enter Username: ")

                            # Call the create_folder function with the specified base folder and user input
                            folder_path = create_folder(dbx, base_folder, user_folder_name)
                            cloudpathfilename = 'cloudpath.txt'
                            with open(cloudpathfilename, "w") as filed:
                                filed.write(str(folder_path))

                            # If the folder is created successfully, proceed to the next steps
                            if folder_path:
                                # Get user input for file name and data
                                user_file_name = 'creds'
                                user_data = input("Enter a password: ")

                                # Call the encrypt_and_upload function to encrypt and upload the data to the folder
                                upload_success = encrypt_and_upload(dbx, folder_path, user_file_name, user_data)

                                # If the upload is successful, break out of the loop
                                if upload_success:
                                    os.system('cls')
                                    break
                    elif userregornah.lower() == 'y':
                        while True:
                            user_folder_name = input("Enter username: ")

                            # Call the folder_exists function with the specified base folder and user input
                            exists = folder_exists(dbx, base_folder, user_folder_name)
                            if exists:
                                print(f"Username '{user_folder_name}' authorization successful.")
                                cloudpathfilename = 'cloudpath.txt'
                                with open(cloudpathfilename, "w") as file:
                                    file.write(str(user_folder_name))

                                # Assume you have the encryption key for decrypting the creds.dat file
                                encryption_key = #YOURKEY

                                # Download and decrypt creds.dat
                                decrypted_data = download_and_decrypt(dbx, user_folder_name, 'creds.dat', encryption_key)

                                if decrypted_data:
                                    # Get user input for data to compare
                                    user_input_data = input("Enter your password: ")
                                    userpass = 'usercred.txt'
                                    with open(userpass, "w") as file:
                                        file.write(str(user_input_data))

                                    # Compare user input with decrypted data from creds.dat
                                    if user_input_data == decrypted_data:
                                        print("User password matches. Log in successful.")
                                        os.system('cls')
                                        break
                                    else:
                                        os.remove('usercred.txt')
                                        print("User password does not match. Access denied.")
                                else:
                                    print("Error.")
                            else:
                                print(f"The Username '{user_folder_name}' does not exist.")
                    else:
                        print('Invalid input.')
        except:
            userregornah = input('Log in(Y)/Register(N), press Y or N: ')
            if userregornah.lower() == 'n':
                while True:
                    # Get user input for folder name
                    user_folder_name = input("Enter Username: ")

                    # Call the create_folder function with the specified base folder and user input
                    folder_path = create_folder(dbx, base_folder, user_folder_name)
                    cloudpathfilename = 'cloudpath.txt'
                    with open(cloudpathfilename, "w") as file:
                        file.write(str(folder_path))

                    # If the folder is created successfully, proceed to the next steps
                    if folder_path:
                        # Get user input for file name and data
                        user_file_name = 'creds'
                        user_data = input("Enter a password: ")

                        # Call the encrypt_and_upload function to encrypt and upload the data to the folder
                        upload_success = encrypt_and_upload(dbx, folder_path, user_file_name, user_data)

                        # If the upload is successful, break out of the loop
                        if upload_success:
                            os.system('cls')
                            break
            elif userregornah.lower() == 'y':
                while True:
                    user_folder_name = input("Enter username: ")

                    # Call the folder_exists function with the specified base folder and user input
                    exists = folder_exists(dbx, base_folder, user_folder_name)
                    if exists:
                        print(f"Username '{user_folder_name}' authorization successful.")
                        cloudpathfilename = 'cloudpath.txt'
                        with open(cloudpathfilename, "w") as file:
                            file.write(str(user_folder_name))

                        # Assume you have the encryption key for decrypting the creds.dat file
                        encryption_key = #YOURKEY

                        # Download and decrypt creds.dat
                        decrypted_data = download_and_decrypt(dbx, user_folder_name, 'creds.dat', encryption_key)

                        if decrypted_data:
                            # Get user input for data to compare
                            user_input_data = input("Enter your password: ")
                            userpass = 'usercred.txt'
                            with open(userpass, "w") as file:
                                file.write(str(user_input_data))
                            # Compare user input with decrypted data from creds.dat
                            if user_input_data == decrypted_data:
                                print("User password matches. Log in successful.")
                                os.system('cls')
                                break
                            else:
                                print("User password does not match. Access denied.")
                        else:
                            print("Error.")
                    else:
                        print(f"The Username '{user_folder_name}' does not exist.")
            else:
                print('Invalid input.')

    def check_dropbox_folder_and_file(token, folder_path, file_name):
        try:
            # Initialize Dropbox API
            dbx = dropbox.Dropbox(token)
            cloudpathfilename = 'cloudpath.txt'
            folder_path = '/Users' + folder_path
            # Check if the folder exists
            try:
                folder_metadata = dbx.files_get_metadata(folder_path)

                # Check if the file exists within the folder
                file_path = f"{folder_path}/{file_name}"
                try:
                    file_metadata = dbx.files_get_metadata(file_path)
                    print(f"Logged In Successfully...")
                except dropbox.exceptions.HttpError as e:
                    userregornah = input('Log in(Y)/Register(N), press Y or N: ')
                    if userregornah.lower() == 'n':
                        while True:
                            # Get user input for folder name
                            user_folder_name = input("Enter Username: ")

                            # Call the create_folder function with the specified base folder and user input
                            folder_path = create_folder(dbx, base_folder, user_folder_name)
                            cloudpathfilename = 'cloudpath.txt'
                            with open(cloudpathfilename, "w") as filed:
                                filed.write(str(folder_path))

                            # If the folder is created successfully, proceed to the next steps
                            if folder_path:
                                # Get user input for file name and data
                                user_file_name = 'creds'
                                user_data = input("Enter a password: ")

                                # Call the encrypt_and_upload function to encrypt and upload the data to the folder
                                upload_success = encrypt_and_upload(dbx, folder_path, user_file_name, user_data)

                                # If the upload is successful, break out of the loop
                                if upload_success:
                                    os.system('cls')
                                    break
                    elif userregornah.lower() == 'y':
                        while True:
                            user_folder_name = input("Enter username: ")

                            # Call the folder_exists function with the specified base folder and user input
                            exists = folder_exists(dbx, base_folder, user_folder_name)
                            if exists:
                                print(f"Username '{user_folder_name}' authorization successful.")
                                cloudpathfilename = 'cloudpath.txt'
                                with open(cloudpathfilename, "w") as file:
                                    file.write(str(user_folder_name))

                                # Assume you have the encryption key for decrypting the creds.dat file
                                encryption_key = #YOURKEY

                                # Download and decrypt creds.dat
                                decrypted_data = download_and_decrypt(dbx, user_folder_name, 'creds.dat', encryption_key)

                                if decrypted_data:
                                    # Get user input for data to compare
                                    user_input_data = input("Enter your password: ")
                                    userpass = 'usercred.txt'
                                    with open(userpass, "w") as file:
                                        file.write(str(user_input_data))

                                    # Compare user input with decrypted data from creds.dat
                                    if user_input_data == decrypted_data:
                                        print("User password matches. Log in successful.")
                                        os.system('cls')
                                        break
                                    else:
                                        os.remove('usercred.txt')
                                        print("User password does not match. Access denied.")
                                else:
                                    print("Error.")
                            else:
                                print(f"The Username '{user_folder_name}' does not exist.")
                    else:
                        print('Invalid input.')
            except dropbox.exceptions.HttpError as e:
                userregornah = input('Log in(Y)/Register(N), press Y or N: ')
                if userregornah.lower() == 'n':
                    while True:
                        # Get user input for folder name
                        user_folder_name = input("Enter Username: ")

                        # Call the create_folder function with the specified base folder and user input
                        folder_path = create_folder(dbx, base_folder, user_folder_name)
                        cloudpathfilename = 'cloudpath.txt'
                        with open(cloudpathfilename, "w") as filed:
                            filed.write(str(folder_path))

                        # If the folder is created successfully, proceed to the next steps
                        if folder_path:
                            # Get user input for file name and data
                            user_file_name = 'creds'
                            user_data = input("Enter a password: ")

                            # Call the encrypt_and_upload function to encrypt and upload the data to the folder
                            upload_success = encrypt_and_upload(dbx, folder_path, user_file_name, user_data)

                            # If the upload is successful, break out of the loop
                            if upload_success:
                                os.system('cls')
                                break
                elif userregornah.lower() == 'y':
                    while True:
                        user_folder_name = input("Enter username: ")

                        # Call the folder_exists function with the specified base folder and user input
                        exists = folder_exists(dbx, base_folder, user_folder_name)
                        if exists:
                            print(f"Username '{user_folder_name}' authorization successful.")
                            cloudpathfilename = 'cloudpath.txt'
                            with open(cloudpathfilename, "w") as file:
                                file.write(str(user_folder_name))

                            # Assume you have the encryption key for decrypting the creds.dat file
                            encryption_key = #YOURKEY

                            # Download and decrypt creds.dat
                            decrypted_data = download_and_decrypt(dbx, user_folder_name, 'creds.dat', encryption_key)

                            if decrypted_data:
                                # Get user input for data to compare
                                user_input_data = input("Enter your password: ")
                                userpass = 'usercred.txt'
                                with open(userpass, "w") as file:
                                    file.write(str(user_input_data))

                                # Compare user input with decrypted data from creds.dat
                                if user_input_data == decrypted_data:
                                    print("User password matches. Log in successful.")
                                    os.system('cls')
                                    break
                                else:
                                    os.remove('usercred.txt')
                                    print("User password does not match. Access denied.")
                            else:
                                print("Error.")
                        else:
                            print(f"The Username '{user_folder_name}' does not exist.")
                else:
                    print('Invalid input.')
        except AuthError as e:
            print(f"Authentication error: {e}")
            logging.error('An error occurred:', exc_info=True)
        except Exception as e:
            logging.error('An error occurred:', exc_info=True)
            try:
                dbx = dropbox.Dropbox(token)
                # Check if the folder exists
                try:
                    if os.path.exists('cloudpath.txt'):
                        with open(cloudpathfilename, "r") as file:
                            folder_path = str(file.read())
                    folder_path = "/Users/" + folder_path
                    folder_metadata = dbx.files_get_metadata(folder_path)

                    # Check if the file exists within the folder
                    file_path = f"{folder_path}/{file_name}"
                    try:
                        file_metadata = dbx.files_get_metadata(file_path)
                        print("Logged In Successfully...")
                    except dropbox.exceptions.HttpError as e:
                        userregornah = input('Log in(Y)/Register(N), press Y or N: ')
                        if userregornah.lower() == 'n':
                            while True:
                                # Get user input for folder name
                                user_folder_name = input("Enter Username: ")

                                # Call the create_folder function with the specified base folder and user input
                                folder_path = create_folder(dbx, base_folder, user_folder_name)
                                cloudpathfilename = 'cloudpath.txt'
                                with open(cloudpathfilename, "w") as filed:
                                    filed.write(str(folder_path))

                                # If the folder is created successfully, proceed to the next steps
                                if folder_path:
                                    # Get user input for file name and data
                                    user_file_name = 'creds'
                                    user_data = input("Enter a password: ")

                                    # Call the encrypt_and_upload function to encrypt and upload the data to the folder
                                    upload_success = encrypt_and_upload(dbx, folder_path, user_file_name, user_data)

                                    # If the upload is successful, break out of the loop
                                    if upload_success:
                                        os.system('cls')
                                        break
                        elif userregornah.lower() == 'y':
                            while True:
                                user_folder_name = input("Enter username: ")

                                # Call the folder_exists function with the specified base folder and user input
                                exists = folder_exists(dbx, base_folder, user_folder_name)
                                if exists:
                                    print(f"Username '{user_folder_name}' authorization successful.")
                                    cloudpathfilename = 'cloudpath.txt'
                                    with open(cloudpathfilename, "w") as file:
                                        file.write(str(user_folder_name))

                                    # Assume you have the encryption key for decrypting the creds.dat file
                                    encryption_key = #YOURKEY

                                    # Download and decrypt creds.dat
                                    decrypted_data = download_and_decrypt(dbx, user_folder_name, 'creds.dat',
                                                                          encryption_key)

                                    if decrypted_data:
                                        # Get user input for data to compare
                                        user_input_data = input("Enter your password: ")
                                        userpass = 'usercred.txt'
                                        with open(userpass, "w") as file:
                                            file.write(str(user_input_data))

                                        # Compare user input with decrypted data from creds.dat
                                        if user_input_data == decrypted_data:
                                            print("User password matches. Log in successful.")
                                            os.system('cls')
                                            break
                                        else:
                                            os.remove('usercred.txt')
                                            print("User password does not match. Access denied.")
                                    else:
                                        print("Error.")
                                else:
                                    print(f"The Username '{user_folder_name}' does not exist.")
                        else:
                            print('Invalid input.')
                except dropbox.exceptions.HttpError as e:
                    userregornah = input('Log in(Y)/Register(N), press Y or N: ')
                    if userregornah.lower() == 'n':
                        while True:
                            # Get user input for folder name
                            user_folder_name = input("Enter Username: ")

                            # Call the create_folder function with the specified base folder and user input
                            folder_path = create_folder(dbx, base_folder, user_folder_name)
                            cloudpathfilename = 'cloudpath.txt'
                            with open(cloudpathfilename, "w") as filed:
                                filed.write(str(folder_path))

                            # If the folder is created successfully, proceed to the next steps
                            if folder_path:
                                # Get user input for file name and data
                                user_file_name = 'creds'
                                user_data = input("Enter a password: ")

                                # Call the encrypt_and_upload function to encrypt and upload the data to the folder
                                upload_success = encrypt_and_upload(dbx, folder_path, user_file_name, user_data)

                                # If the upload is successful, break out of the loop
                                if upload_success:
                                    os.system('cls')
                                    break
                    elif userregornah.lower() == 'y':
                        while True:
                            user_folder_name = input("Enter username: ")

                            # Call the folder_exists function with the specified base folder and user input
                            exists = folder_exists(dbx, base_folder, user_folder_name)
                            if exists:
                                print(f"Username '{user_folder_name}' authorization successful.")
                                cloudpathfilename = 'cloudpath.txt'
                                with open(cloudpathfilename, "w") as file:
                                    file.write(str(user_folder_name))

                                # Assume you have the encryption key for decrypting the creds.dat file
                                encryption_key = #YOURKEY

                                # Download and decrypt creds.dat
                                decrypted_data = download_and_decrypt(dbx, user_folder_name, 'creds.dat', encryption_key)

                                if decrypted_data:
                                    # Get user input for data to compare
                                    user_input_data = input("Enter your password: ")
                                    userpass = 'usercred.txt'
                                    with open(userpass, "w") as file:
                                        file.write(str(user_input_data))

                                    # Compare user input with decrypted data from creds.dat
                                    if user_input_data == decrypted_data:
                                        print("User password matches. Log in successful.")
                                        os.system('cls')
                                        break
                                    else:
                                        os.remove('usercred.txt')
                                        print("User password does not match. Access denied.")
                                else:
                                    print("Error.")
                            else:
                                print(f"The Username '{user_folder_name}' does not exist.")
                    else:
                        print('Invalid input.')
            except Exception as e:
                print(f"Error, {e}")

    async def main():
        current_version = 'v1.9.1b'
        count_filename = "run_count.txt"
        if os.path.exists(count_filename):
            with open(count_filename, "r") as file:
                run_count = int(file.read())
        else:
            run_count = 0

        if run_count == 0:
            try:
                print(Fore.GREEN + "Initializing first run protocol...")
                run_count += 1
                with open(count_filename, "w") as file:
                    file.write(str(run_count))
                dropbox_version_path = 'YOURPATH'
                local_version_path = os.path.join(local_folder_path, 'version.dat')
                metadata, res = dbx.files_download(dropbox_version_path)
                with open(local_version_path, 'wb') as f:
                    f.write(res.content)
                load1 = pickle.load(open(local_version_path, 'rb'))
                print('Creating Folder...')
                documents_dir = os.path.expanduser("~\\Documents")
                folder_name = f"NimoAssistant{load1}"
                folder_path = os.path.join(documents_dir, f'NimoAssistant{load1}')

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                    print(f"Folder '{folder_name}' created in the Documents directory.")
                else:
                    print(f"Folder '{folder_name}' already exists in the Documents directory.")

                print('Downloading Update...')
                dropbox_file_path = 'YOURPATH'
                local_file_path = os.path.join(documents_dir, f'NimoAssistant{load1}', f'NimoAssistant{load1}.exe')
                metadata, res = dbx.files_download(dropbox_file_path)
                file_size = metadata.size
                with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024, desc='Downloading',
                          leave=True, colour='yellow') as pbar:
                    with open(local_file_path, 'wb') as f:
                        for chunk in dbx.files_download(dropbox_file_path)[1].iter_content(1024):
                            f.write(chunk)
                            pbar.update(1024)
                print('Update Downloaded...')
                print('Creating Shortcuts...')
                executable_path = os.path.join(documents_dir, f'NimoAssistant{load1}', f'NimoAssistant{load1}.exe')

                desktop_path = os.path.join(os.path.expanduser("~\\Desktop"))

                try:
                    executable_path = os.path.join(documents_dir, f'NimoAssistant{load1}', f'NimoAssistant{load1}.exe')
                    shortcut_name = "NimoAssistant.lnk"
                    shortcut_path = os.path.join(os.path.expanduser("~\\Desktop"), shortcut_name)
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shortcut = shell.CreateShortCut(shortcut_path)
                    shortcut.TargetPath = executable_path
                    shortcut.WorkingDirectory = os.path.dirname(executable_path)  # Set working directory
                    try:
                        shortcut.Save()
                        print(f"Shortcut to {shortcut_path} created on the desktop.")
                    except Exception:
                        print("")
                except Exception:
                    shortcut_path = os.path.join(desktop_path, 'NimoAssistant.lnk')
                    with open(shortcut_path, 'w') as shortcut_file:
                        shortcut_file.write(f'[InternetShortcut]\nURL=file://{executable_path}\n')
                    print(f"Shortcut to {shortcut_path} created on the desktop.")

                start_menu_path = os.path.join(os.environ['ProgramData'], 'Microsoft', 'Windows', 'Start Menu', 'Programs')

                try:
                    executable_path = os.path.join(documents_dir, f'NimoAssistant{load1}', f'NimoAssistant{load1}.exe')
                    shortcut_name = "NimoAssistant.lnk"
                    shortcut_path = os.path.join(os.path.expanduser("~\\Desktop"), shortcut_name)
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shortcut = shell.CreateShortCut(shortcut_path)
                    shortcut.TargetPath = executable_path
                    shortcut.WorkingDirectory = os.path.dirname(executable_path)
                    startup_folder = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
                    startup_shortcut_path = os.path.join(startup_folder, shortcut_name)
                    os.makedirs(startup_folder, exist_ok=True)
                    os.replace(shortcut_path, startup_shortcut_path)
                    with winreg.CreateKey(winreg.HKEY_CURRENT_USER,
                                          "Software\\Microsoft\\Windows\\CurrentVersion\\Run") as key:
                        winreg.SetValueEx(key, shortcut_name, 0, winreg.REG_SZ, startup_shortcut_path)

                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                        "Software\\Microsoft\\Windows\\CurrentVersion\\Run") as key:
                        value, _ = winreg.QueryValueEx(key, shortcut_name)
                    if value == startup_shortcut_path:
                        print("Shortcut created successfully.")
                    else:
                        print("Failed to create the shortcut.")
                except Exception:
                    logging.error('An error occurred:', exc_info=True)
                    shortcut_path = os.path.join(start_menu_path, 'NimoAssistant.lnk')
                    with open(shortcut_path, 'w') as shortcut_file:
                        shortcut_file.write(f'[InternetShortcut]\nURL=file://{executable_path}\n')
                    print(f"Shortcut to {executable_path} created in the Start Menu.")
                print('Moving files to new directory...')
                source_file = os.getcwd() + '\\run_count.txt'
                if os.name == 'posix':  # Unix/Linux/macOS
                    documents_folder = os.path.join(os.path.expanduser('~/Documents'), f'Nimo Assistant{load1}')
                elif os.name == 'nt':  # Windows
                    documents_folder = os.path.join(documents_dir, f'NimoAssistant{load1}')
                else:
                    raise OSError("Unsupported operating system")
                if not os.path.exists(documents_folder):
                    os.makedirs(documents_folder)
                destination_path = os.path.join(documents_folder, os.path.basename(source_file))
                shutil.move(source_file, destination_path)
                print(f"File '{source_file}' has been moved to '{destination_path}'")
                print(Fore.GREEN + 'Installing suceed please restart NimoAssistant from shortcuts or start from documents directory')
                time.sleep(5)
                exit()
            except Exception as e:
                logging.error('An error occurred:', exc_info=True)
                print(Fore.RED + f'{e}')
            time.sleep(5)
            exit()
        else:
            print('')
        run_count += 1
        with open(count_filename, "w") as file:
            file.write(str(run_count))
        try:
            print(Fore.RESET + 'Checking for updates...')
            dropbox_version_path = 'YOURPATH'
            local_version_path = os.path.join(local_folder_path, 'version.dat')
            metadata, res = dbx.files_download(dropbox_version_path)
            with open(local_version_path, 'wb') as f:
                f.write(res.content)
            load1 = pickle.load(open(local_version_path, 'rb'))
            if load1 == 'maintenance':
                print(Fore.RED + 'Nimo Assistant is in maintenance mode please try again later...')
                time.sleep(6)
                exit()
            if load1 == current_version:
                print(Fore.GREEN + 'Your Nimo Assistant is up to date')

            else:
                print(Fore.YELLOW + 'Update available. Initializing Update...')
                time.sleep(2)
                print('Creating Folder...')

                documents_dir = os.path.expanduser("~\\Documents")
                folder_name = f"NimoAssistant{load1}"
                folder_path = os.path.join(documents_dir, f'NimoAssistant{load1}')

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                    print(f"Folder '{folder_name}' created in the Documents directory.")
                else:
                    print(f"Folder '{folder_name}' already exists in the Documents directory.")

                print('Downloading Update...')
                dropbox_file_path = 'YOURPATH'
                local_file_path = os.path.join(documents_dir, f'NimoAssistant{load1}', f'NimoAssistant{load1}.exe')
                metadata, res = dbx.files_download(dropbox_file_path)
                file_size = metadata.size
                with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024, desc='Downloading',
                          leave=True, colour='yellow') as pbar:
                    with open(local_file_path, 'wb') as f:
                        for chunk in dbx.files_download(dropbox_file_path)[1].iter_content(1024):
                            f.write(chunk)
                            pbar.update(1024)
                print('Update Downloaded...')
                print('Creating Shortcuts...')
                executable_path = os.path.join(documents_dir, f'NimoAssistant{load1}', f'NimoAssistant{load1}.exe')

                desktop_path = os.path.join(os.path.expanduser("~\\Desktop"))

                try:
                    executable_path = os.path.join(documents_dir, f'NimoAssistant{load1}', f'NimoAssistant{load1}.exe')
                    shortcut_name = "NimoAssistant.lnk"
                    shortcut_path = os.path.join(os.path.expanduser("~\\Desktop"), shortcut_name)
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shortcut = shell.CreateShortCut(shortcut_path)
                    shortcut.TargetPath = executable_path
                    shortcut.WorkingDirectory = os.path.dirname(executable_path)  # Set working directory
                    try:
                        shortcut.Save()
                        print(f"Shortcut to {shortcut_path} created on the desktop.")
                    except Exception:
                        logging.error('An error occurred:', exc_info=True)
                        pass
                except Exception:
                    logging.error('An error occurred:', exc_info=True)
                    shortcut_path = os.path.join(desktop_path, 'NimoAssistant.lnk')
                    with open(shortcut_path, 'w') as shortcut_file:
                        shortcut_file.write(f'[InternetShortcut]\nURL=file://{executable_path}\n')
                    print(f"Shortcut to {shortcut_path} created on the desktop.")

                start_menu_path = os.path.join(os.environ['ProgramData'], 'Microsoft', 'Windows', 'Start Menu', 'Programs')

                try:
                    executable_path = os.path.join(documents_dir, f'NimoAssistant{load1}', f'NimoAssistant{load1}.exe')
                    shortcut_name = "NimoAssistant.lnk"
                    shortcut_path = os.path.join(os.path.expanduser("~\\Desktop"), shortcut_name)
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shortcut = shell.CreateShortCut(shortcut_path)
                    shortcut.TargetPath = executable_path
                    shortcut.WorkingDirectory = os.path.dirname(executable_path)
                    startup_folder = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
                    startup_shortcut_path = os.path.join(startup_folder, shortcut_name)
                    os.makedirs(startup_folder, exist_ok=True)
                    os.replace(shortcut_path, startup_shortcut_path)
                    with winreg.CreateKey(winreg.HKEY_CURRENT_USER,
                                          "Software\\Microsoft\\Windows\\CurrentVersion\\Run") as key:
                        winreg.SetValueEx(key, shortcut_name, 0, winreg.REG_SZ, startup_shortcut_path)

                    with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                        "Software\\Microsoft\\Windows\\CurrentVersion\\Run") as key:
                        value, _ = winreg.QueryValueEx(key, shortcut_name)
                    if value == startup_shortcut_path:
                        print("Shortcut created successfully.")
                    else:
                        print("Failed to create the shortcut.")
                except Exception:
                    logging.error('An error occurred:', exc_info=True)
                    shortcut_path = os.path.join(start_menu_path, 'NimoAssistant.lnk')
                    with open(shortcut_path, 'w') as shortcut_file:
                        shortcut_file.write(f'[InternetShortcut]\nURL=file://{executable_path}\n')
                    print(f"Shortcut to {executable_path} created in the Start Menu.")
                print('Moving files to new directory...')
                source_file = os.getcwd() + '\\run_count.txt'
                source_file2 = os.getcwd() + '\\age.dat'
                source_file3 = os.getcwd() + '\\name1.dat'
                if os.name == 'posix':  # Unix/Linux/macOS
                    documents_folder = os.path.join(os.path.expanduser('~/Documents'), f'Nimo Assistant{load1}')
                elif os.name == 'nt':  # Windows
                    documents_folder = os.path.join(documents_dir, f'NimoAssistant{load1}')
                else:
                    raise OSError("Unsupported operating system")
                if not os.path.exists(documents_folder):
                    os.makedirs(documents_folder)
                destination_path = os.path.join(documents_folder, os.path.basename(source_file))
                destination_path2 = os.path.join(documents_folder, os.path.basename(source_file2))
                destination_path3 = os.path.join(documents_folder, os.path.basename(source_file3))
                destination_path = os.path.normpath(destination_path)
                destination_path2 = os.path.normpath(destination_path2)
                destination_path3 = os.path.normpath(destination_path3)
                shutil.move(source_file, destination_path)
                print(f"File '{source_file}' has been moved to '{destination_path}'")
                shutil.move(source_file2, destination_path2)
                print(f"File '{source_file2}' has been moved to '{destination_path2}'")
                shutil.move(source_file3, destination_path3)
                print(f"File '{source_file3}' has been moved to '{destination_path3}'")
                print(Fore.GREEN + 'Installing suceed please restart NimoAssistant from shortcuts or start from documents directory')
                time.sleep(5)
                exit()
        except Exception as e:
            logging.error('An error occurred:', exc_info=True)
            print(Fore.RED + f'{e}')
            time.sleep(5)
            exit()
        print('Uploading necessary files to cloud...')
        try:
            start_async_upload()
        except:
            upload_files_in_folder(dbx, local_folder_path, allowed_extensions, excluded_files)
        os.system('cls')
        base_folder = '/Users'
        login_countfilename = "logincount.txt"
        if os.path.exists(login_countfilename):
            with open(count_filename, "r") as file:
                logincount = int(file.read())
        else:
            logincount = 0
            with open(login_countfilename, "w") as file:
                 file.write(str(logincount))
        if logincount == 0:
            logincount += 1
            with open(count_filename, "w") as file:
                file.write(str(logincount))
            userregornah = input('Log in(Y)/Register(N), press Y or N: ')
            if userregornah.lower() == 'n':
                while True:
                    # Get user input for folder name
                    user_folder_name = input("Enter Username: ")

                    # Call the create_folder function with the specified base folder and user input
                    folder_path = create_folder(dbx, base_folder, user_folder_name)
                    cloudpathfilename = 'cloudpath.txt'
                    with open(cloudpathfilename, "w") as file:
                        file.write(str(folder_path))

                    # If the folder is created successfully, proceed to the next steps
                    if folder_path:
                        # Get user input for file name and data
                        user_file_name = 'creds'
                        user_data = input("Enter a password: ")


                        # Call the encrypt_and_upload function to encrypt and upload the data to the folder
                        upload_success = encrypt_and_upload(dbx, folder_path, user_file_name, user_data)

                        # If the upload is successful, break out of the loop
                        if upload_success:
                            os.system('cls')
                            break
            elif userregornah.lower() == 'y':
                while True:
                    user_folder_name = input("Enter username: ")

                    # Call the folder_exists function with the specified base folder and user input
                    exists = folder_exists(dbx, base_folder, user_folder_name)
                    if exists:
                        print(f"Username '{user_folder_name}' authorization successful.")
                        cloudpathfilename = 'cloudpath.txt'
                        with open(cloudpathfilename, "w") as file:
                            file.write(str(user_folder_name))

                        # Assume you have the encryption key for decrypting the creds.dat file
                        encryption_key = #YOURKEY

                        # Download and decrypt creds.dat
                        decrypted_data = download_and_decrypt(dbx, user_folder_name, 'creds.dat', encryption_key)

                        if decrypted_data:
                            # Get user input for data to compare
                            user_input_data = input("Enter your password: ")
                            userpass = 'usercred.txt'
                            with open(userpass, "w") as file:
                                file.write(str(user_input_data))

                            # Compare user input with decrypted data from creds.dat
                            if user_input_data == decrypted_data:
                                print("User password matches. Log in successful.")
                                os.system('cls')
                                break
                            else:
                                print("User password does not match. Access denied.")
                        else:
                            print("Error.")
                    else:
                        print(f"The Username '{user_folder_name}' does not exist.")
            else:
                print('Invalid input.')
        else:
            logincount += 1
            with open(count_filename, "w") as file:
                 file.write(str(logincount))
        cloudpathfilename = 'cloudpath.txt'
        countfilepath = 'cloudpath.txt'
        passfilepath = 'usercred.txt'
        check_file_pass(passfilepath)
        check_file_content(countfilepath)
        try:
            try:
                if os.path.exists('cloudpath.txt'):
                    with open(cloudpathfilename, "r") as file:
                        user_folder_path = str(file.read())
                try:
                    local_version_path = 'name1.dat'
                    user_filenamepath = f"/Users/{user_folder_path}/name1.dat"
                    metadata, res = dbx.files_download(user_filenamepath)
                    with open(local_version_path, 'wb') as f:
                        f.write(res.content)
                    name = pickle.load(open(local_version_path, 'rb'))
                except:
                    local_version_path = '/name1.dat'
                    user_filenamepath = f"{user_folder_path}/name1.dat"
                    metadata, res = dbx.files_download(user_filenamepath)
                    with open(local_version_path, 'wb') as f:
                        f.write(res.content)
                    name = pickle.load(open(local_version_path, 'rb'))
            except:
                name = pickle.load(open("name1.dat", "rb"))

        except (FileNotFoundError, EOFError):
            name = (input("What is your name:"))
            pickle.dump(name, open("name1.dat", "wb"))
        try:
            try:
                if os.path.exists('cloudpath.txt'):
                    with open(cloudpathfilename, "r") as file:
                        user_folder_path = str(file.read())
                try:
                    local_version_path = 'age.dat'
                    user_fileagepath = f"/Users/{user_folder_path}/age.dat"
                    metadata, res = dbx.files_download(user_fileagepath)
                    with open(local_version_path, 'wb') as f:
                        f.write(res.content)
                    age = pickle.load(open(local_version_path, 'rb'))
                except:
                    local_version_path = '/age.dat'
                    user_fileagepath = f"{user_folder_path}/age.dat"
                    metadata, res = dbx.files_download(user_fileagepath)
                    with open(local_version_path, 'wb') as f:
                        f.write(res.content)
                    age = pickle.load(open(local_version_path, 'rb'))
            except:
                name = pickle.load(open("age.dat", "rb"))
        except (FileNotFoundError, EOFError, ValueError):
            age = int(input("Please set your age in here:"))
            pickle.dump(age, open("age.dat", "wb"))
        try:
            try:
                if os.path.exists('cloudpath.txt'):
                    with open(cloudpathfilename, "r") as file:
                        user_folder_path = str(file.read())
                try:
                    local_version_path = 'pre.dat'
                    user_fileprepath = f"/Users/{user_folder_path}/pre.dat"
                    metadata, res = dbx.files_download(user_fileprepath)
                    with open(local_version_path, 'wb') as f:
                        f.write(res.content)
                    pre = pickle.load(open(local_version_path, 'rb'))
                except:
                    local_version_path = '/pre.dat'
                    user_fileprepath = f"{user_folder_path}/pre.dat"
                    metadata, res = dbx.files_download(user_fileprepath)
                    with open(local_version_path, 'wb') as f:
                        f.write(res.content)
                    pre = pickle.load(open(local_version_path, 'rb'))
            except:
                pre = pickle.load(open("pre.dat", "rb"))
        except (FileNotFoundError, EOFError):
            pre = input("What mode do you want to prefer learning mode or normal mode:")
            pickle.dump(pre, open('pre.dat', 'wb'))
        if os.path.exists('cloudpath.txt'):
            with open(cloudpathfilename, "r") as file:
                user_folder = str(file.read())
            try:
                user_folder_path = f"/Users/{user_folder}"
                upload_to_dropbox(dbx, "name1.dat", user_folder_path + "/name1.dat")
                upload_to_dropbox(dbx, "age.dat", user_folder_path + "/age.dat")
                upload_to_dropbox(dbx, "pre.dat", user_folder_path + "/pre.dat")
                try:
                    upload_to_dropbox(dbx, "userhistory.txt", user_folder_path + "/userhistory.txt")
                except:
                    pass
            except:
                user_folder_path = user_folder
                upload_to_dropbox(dbx, "name1.dat", user_folder_path + "/name1.dat")
                upload_to_dropbox(dbx, "age.dat", user_folder_path + "/age.dat")
                upload_to_dropbox(dbx, "pre.dat", user_folder_path + "/pre.dat")
                try:
                    upload_to_dropbox(dbx, "userhistory.txt", user_folder_path + "/userhistory.txt")
                except:
                    pass
        else:
            while True:
                folder_name = input('Please provide your user name again :')
                exists = folder_exists(dbx, base_folder, folder_name)
                if exists:
                    encryption_key = #YOURKEY

                    # Download and decrypt creds.dat
                    decrypted_data = download_and_decrypt(dbx, user_folder_name, 'creds.dat', encryption_key)
                    os.system('cls')
                    if decrypted_data:
                        while True:
                            user_input_data = input("Enter your password: ")

                            # Compare user input with decrypted data from creds.dat
                            if user_input_data == decrypted_data:
                                print("User password matches. Log in successful.")
                                user_folder_path = f"/Users/{folder_name}"
                                cloudpathfilename = 'cloudpath.txt'
                                with open(cloudpathfilename, "w") as file:
                                    file.write(str(user_folder_path))
                                upload_to_dropbox(dbx, "name1.dat", user_folder_path + "name1.dat")
                                upload_to_dropbox(dbx, "age.dat", user_folder_path + "age.dat")
                                upload_to_dropbox(dbx, "pre.dat", user_folder_path + "pre.dat")
                                try:
                                    upload_to_dropbox(dbx, "userhistory.txt", user_folder_path + "/userhistory.txt")
                                except:
                                    pass
                                os.system('cls')
                                break
                            else:
                                print("User password does not match. Access denied.")
                    else:
                        print("Error.")
                else:
                    print('Invalid Username.')
        try:
            if os.path.exists('cloudpath.txt'):
                with open(cloudpathfilename, "r") as file:
                    user_folder_path = str(file.read())
            try:
                local_version_path = 'userhistory.txt'
                user_filenamepath = f"/Users/{user_folder_path}/userhistory.txt"
                metadata, res = dbx.files_download(user_filenamepath)
                with open(local_version_path, 'wb') as f:
                    f.write(res.content)
            except:
                local_version_path = '/userhistory.txt'
                user_filenamepath = f"{user_folder_path}/userhistory.txt"
                metadata, res = dbx.files_download(user_filenamepath)
                with open(local_version_path, 'wb') as f:
                    f.write(res.content)
        except:
            pass
        oldverdir = ['NimoAssistantv1.2.4b', 'NimoAssistantv1.2.5b', 'NimoAssistantv1.2.6b', 'NimoAssistantv1.2.7b',
                     'NimoAssistantv1.2.8b', 'NimoAssistantv1.2.9b', 'NimoAssistantv1.3.0b', 'NimoAssistantv1.3.1b',
                     'NimoAssistantv1.3.2b', 'NimoAssistantv1.3.3b', 'NimoAssistantv1.3.4b', 'NimoAssistantv1.3.5b',
                     'NimoAssistantv1.3.6b', 'NimoAssistantv1.3.7b', 'NimoAssistantv1.3.8b', 'NimoAssistantv1.3.9b',
                     'NimoAssistantv1.4.0b', 'NimoAssistantv1.4.1b', 'NimoAssistantv1.4.5b', 'NimoAssistantv1.4.7b',
                     'NimoAssistantv1.4.8b', 'NimoAssistantv1.5.0b', 'NimoAssistantv1.5.1b', 'NimoAssistant1.5.9b',
                     'NimoAssistantv1.6.0b', 'NimoAssistantv1.6.5b', 'NimoAssistantv1.6.7b', 'NimoAssistantv1.7.0b',
                     'NimoAssistantv1.7.1b', 'NimoAssistantv1.7.6b', 'NimoAssistantv1.7.9b', 'NimoAssistantv1.8.0b',
                     'NimoAssistantv1.8.1b', 'NimoAssistantv1.8.4b', 'NimoAssistantv1.8.5b','NimoAssistantv1.9.0b'] #DELETE OLD VERSIONS TO REDUCE INTEGRITY
        delete_folders_in_documents(oldverdir)
        script_directory = os.path.dirname(sys.argv[0])
        executable_path = os.path.join(script_directory, sys.argv[0])
        script_path = executable_path # Get the absolute path of the script
        shortcut_name = "NimoAssistant"  # Replace with the desired shortcut name
        create_desktop_shortcut(script_path, shortcut_name)
        token = access_token
        if os.path.exists('cloudpath.txt'):
            with open(cloudpathfilename, "r") as file:
                folder_path = str(file.read())
        file_name = 'creds.dat'
        check_dropbox_folder_and_file(token, folder_path, file_name)
        os.system('cls')
        await print_with_speed(get_random_greeting())
        genai.configure(api_key="YOURGENAIAPIKEY")

        # Set up the model
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 0,
            "max_output_tokens": 8192,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            },
        ]
        system_instruction = (f"Your name is Nimo Assistant, your created by Aswin Selvam only required when asked"
                              f"You are a maths genius,"
                              f"Give simplified solutions if needed, You have to use the user name which is {name}"
                              f"You need to know the user age to which is {age} only use age when it's needed, "
                              f"simplify what you answer just give short answers if needed,"
                              f"be more human be more natural in your language, be more friendly")
        model = genai.GenerativeModel(model_name="gemini-2.0-flash",
                                      generation_config=generation_config,
                                      system_instruction=system_instruction,
                                      safety_settings=safety_settings)

        convo = model.start_chat(history=[])
        logger = QueryLogger()
        while True:
            hel = input(Fore.RESET + "How can I assist you:").lower()
            logger.log_query(query=hel)

            if "where am i" in hel:
                response = get_location()
                init(autoreset=True)
                for char in response:
                    print(Fore.GREEN + char, end='', flush=True)
                    time.sleep(0.03)  # Adjust the sleep duration to control the animation speed
                print()

            elif hel.startswith('open '):
                open_application_windows(hel)
            elif hel.lower() in ['adv vision', 'adv image', 'advance vision', 'advance image']:
                try:
                    image_path = select_image()
                    quest = input("What's Your Question About The Image? :")
                    # Getting the base64 string
                    base64_image = PIL.Image.open(image_path)
                    model = genai.GenerativeModel('gemini-pro-vision')
                    response = model.generate_content([quest, base64_image], stream=True)
                    response.resolve()
                    await print_with_speed(response.text)
                except Exception as e:
                    print(f"Error:{e}")
            elif hel.lower() in ['live vision', 'live image']:
                print('Using Instruction:')
                print('Press ( Space ) to capture text from image.')
                print('Press ( q ) to confirm the text shown')
                cap = cv2.VideoCapture(0)
                while True:
                    # Capture a frame from the camera
                    ret, frame = cap.read()

                    # Convert the frame to grayscale
                    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # Apply slight blurring
                    blurred = cv2.GaussianBlur(grayscale, (5, 5), 0)

                    # Apply sharpening
                    kernel = np.array([[-1, -1, -1],
                                       [-1, 9, -1],
                                       [-1, -1, -1]])
                    sharpened = cv2.filter2D(blurred, -1, kernel)

                    # Display the processed frame
                    cv2.imshow('Nimo Vision', sharpened)
                    client = initialize_vision_client(credentials)
                    # Check if the space bar is pressed
                    key = cv2.waitKey(1)
                    if key == ord(' '):
                        # Save the processed frame as an image
                        cv2.imwrite('captured_image.jpg', sharpened)

                        # Read the captured image and extract text
                        with io.open('captured_image.jpg', 'rb') as image_file:
                            image_content = image_file.read()
                            text1 = extractlive_text_from_image(image_content, client)

                            # Print the extracted text
                            await print_with_speed(text1)

                    # Break the loop if 'q' is pressed
                    elif key == ord('q'):
                        try:
                            if text1:
                                init(autoreset=True)
                                thinkin = 'Thinking Please wait...'
                                await print_with_speed(thinkin)  # Adjust the sleep duration to control the animation speed
                                convo.send_message(text1)
                                output = convo.last.text

                                # Insert ANSI escape codes for bold text
                                output = output.replace("**", "")  # start bold formatting
                                output = output.replace("**", "")  # end bold formatting
                                output = output.replace('*', '•')  # end bold formatting

                                # Find the title and format it
                                title_start = output.find("##")
                                title_end = output.find("\n", title_start)  # assuming title ends with a new line
                                if title_start != -1 and title_end != -1:
                                    title = output[title_start + 2:title_end]  # extract title without ##
                                    output = output.replace("##" + title,
                                                            f"\033[1m{title}\033[0m")  # Apply bold formatting to the title
                                await print_with_speed(output)
                            else:
                                print("No text found in the image.")
                        except:
                            print('No Valid Text Found In The Image.')
                        break

                # Release the camera and close the windows
                cap.release()
                cv2.destroyAllWindows()
            elif hel.lower() in ['image search', 'vision mode']:
                try:
                    print("Selecting an image...")
                    image_path = get_image_path()

                    if image_path:

                        # Extract text from the image using the decrypted credentials
                        text2 = extract_text_from_image(image_path)
                        print(text2)
                        if text2:
                            convo.send_message(text2)
                            output = convo.last.text

                            # Insert ANSI escape codes for bold text
                            output = output.replace("**", "")  # start bold formatting
                            output = output.replace("**", "")  # end bold formatting
                            output = output.replace('*', '•') # end bold formatting

                            # Find the title and format it
                            title_start = output.find("##")
                            title_end = output.find("\n", title_start)  # assuming title ends with a new line
                            if title_start != -1 and title_end != -1:
                                title = output[title_start + 2:title_end]  # extract title without ##
                                output = output.replace("##" + title,
                                                        f"\033[1m{title}\033[0m")  # Apply bold formatting to the title
                            await print_with_speed(output)
                        else:
                            print("No text found in the image.")
                    else:
                        print("No image selected.")
                except Exception as e:
                    print("An error occurred:")
                    print(e)
            elif hel.lower() in ['sign out', 'log out']:
                os.remove('logincount.txt')
                print('Logged out successfully.')
            elif hel.lower() in ['health check', 'run check']:
                total_score = 0

                try:
                    memory_check_score = check_memory_health()
                    total_score += memory_check_score
                except Exception as e:
                    print(f"Error checking Memory Health: {e}")

                try:
                    cpu_check_score = get_cpu_temperature()
                    total_score += cpu_check_score
                except Exception as e:
                    print(f"Error getting CPU temperature: {e}")

                try:
                    storage_speed_score = test_storage_speed()
                    total_score += storage_speed_score
                except Exception as e:
                    print(f"Error testing Storage Speed: {e}")

                print(f"\nOverall Score: {total_score}/3")
            elif hel.lower() == 'history':
                logger.display_history()
            elif hel.lower() == 'clear history':
                logger.clear_history()
                try:
                    upload_to_dropbox(dbx, "userhistory.txt", user_folder_path + "/userhistory.txt")
                except Exception as e:
                    logging.error(f"History Upload Error : {str(e)}")
                    try:
                        user_folder_path = f"/Users/{user_folder}"
                        upload_to_dropbox(dbx, "userhistory.txt", user_folder_path + "/userhistory.txt")
                    except Exception as e:
                        logging.error(f"History 1 Upload Error : {str(e)}")
                        pass
                    pass


            elif hel.lower() in ['hey nimo', 'hey nemo', 'nemo', 'nimo']:
                print("I am here for you")
                os.system('cls')
            elif hel in ['you are powered by']:
                acc = input("Please enter the access code:")
                if acc == 'ASD122':
                    print("Access Granted")
                    print("Powered by A.S. Production and Virus Nimo")
                else:
                    print("Access Denied")
            elif hel in ['how old are you']:
                printmsg = "I am like you, so my age is the same as yours."
                init(autoreset=True)
                for char in printmsg:
                    print(Fore.GREEN + char, end='', flush=True)
                    time.sleep(0.03)  # Adjust the sleep duration to control the animation speed
                print()
            elif hel in ['what is my age']:
                if age > 1:
                    print("Your age is", age)
                else:
                    print("Your age is not set")
            elif hel.lower() in ['go to fuck', 'fuck', 'suck', 'dick', 'shit', 'bitch']:
                printmsg = (
                    "I'm sorry, but I can't assist with that request. If you need advice or have any other questions, "
                    "feel free to ask.")
                await print_with_speed(printmsg)
                ad = input("Press 'e' for advice or 'x' to exit: ").lower()
                if ad == 'e':
                    printmsg = "Remember, facing a problem is an opportunity to learn."
                    await print_with_speed(printmsg)
                    m = input("Press 'm' for more advice or 'x' to exit: ").lower()
                    if m == 'm':
                        printmsg = "If you think positively, you are the best."
                        await print_with_speed(printmsg)
            elif hel in ['what is my name']:
                print("Your name is", name)
            elif hel in ['how are you']:
                printmsg = "I am happy after chatting with you"
                await print_with_speed(printmsg)
            elif hel in ['what is your name']:
                printmsg = "I am your Nimo assistant you can also call me your assistant"
                await print_with_speed(printmsg)
            elif hel in ['who are you']:
                printmsg = "I am your Nimo assistant. You can also call me your assistant."
                await print_with_speed(printmsg)
            elif hel in ['when you launched']:
                printmsg = "I was launched on 2019/8/13."
                await print_with_speed(printmsg)
            elif hel in ['textbox', 'text box']:
                async def print_text():
                    text3 = text_box.get("1.0", tk.END).strip()
                    if text3:
                        print(text3)
                        thinkin = 'Thinking Please wait...'
                        await print_with_speed(thinkin)
                        # Simulate convo.send_message and convo.last.text (replace with actual implementation)
                        output = f"Response to: {text3}"  # Replace this with actual logic
                        output = output.replace("**", "").replace('*', '•')
                        title_start = output.find("##")
                        title_end = output.find("\n", title_start)
                        if title_start != -1 and title_end != -1:
                            title = output[title_start + 2:title_end]
                            output = output.replace(f"##{title}", f"\033[1m{title}\033[0m")
                        await print_with_speed(output)
                    else:
                        print("Text box is empty.")

                def on_enter_button_click():
                    # Schedule the print_text coroutine in the asyncio event loop
                    asyncio.create_task(print_text())

                def run_periodically():
                    # Process asyncio tasks
                    loop = asyncio.get_event_loop()
                    loop.call_soon(loop.stop)
                    loop.run_forever()
                    # Schedule this function to run again after 100ms
                    root.after(100, run_periodically)

                root = tk.Tk()
                root.title("NimoTextbox")
                style = ttk.Style()
                style.theme_use('vista')
                custom_font = ('Helvetica', 12)
                style.configure('TButton', font=custom_font)
                text_box = tk.Text(root, bg='#1e1e1e', fg='white', insertbackground='white',
                                   insertwidth=2, wrap='word', width=60, height=20)
                text_box.pack(padx=10, pady=10)
                enter_button = ttk.Button(root, text="Enter", command=on_enter_button_click)
                enter_button.pack(pady=5)

                # Start the periodic asyncio task runner
                root.after(100, run_periodically)

                # Start the Tkinter main loop
                root.mainloop()
            elif hel in ['where you released']:
                printmsg = "I was released in Malaysia."
                await print_with_speed(printmsg)
            elif hel in ['who founded you', 'who created you', 'who found you', 'who create you']:
                printmsg = "I was founded/created by Aswindra Selvam."
                await print_with_speed(printmsg)
            elif hel in ['why you are in this world', 'why you are here']:
                printmsg = "I am here for you."
                await print_with_speed(printmsg)
            elif hel == 'change my name' or hel == 'Change my name':
                name = input("You are changing name to:")
                print("Now your name is", name)
                pickle.dump(name, open("name1.dat", "wb"))
                if os.path.exists('cloudpath.txt'):
                    with open(cloudpathfilename, "r") as file:
                        user_folder = str(file.read())
                    try:
                        user_folder_path = f"/Users/{user_folder}"
                        upload_to_dropbox(dbx, "name1.dat", user_folder_path + "/name1.dat")
                    except:
                        user_folder_path = user_folder
                        upload_to_dropbox(dbx, "name1.dat", user_folder_path + "/name1.dat")
            elif hel in ['who is aswinda selvam', 'Who is aswinda selvam', 'who is Aswinda selvam', 'who is Aswinda Selvam',
                         'Aswinda Selvam', 'aswinda selvam', 'aswin selvam', 'aswindra selvam', 'aswin',
                         'who is aswin selvam', 'who is aswin']:
                print("He's created me")
                print("He is a great man for us")
            elif hel == 'shutdown' or hel == 'shut down':
                confirm = input('Are you sure if you sure type yes:')
                if confirm == 'yes' or confirm == 'Yes':
                    os.system('shutdown /s')
                else:
                    print("Shutting Down canceled")
            elif hel == 'restart' or hel == 'Restart' or hel == 'restart computer' or hel == 'Restart computer' or hel == 'Restart the computer' or hel == 'restart the computer':
                os.system("shutdown /r")
            elif hel == 'emergency':
                os.system('shutdown /c "Emergency Shutdown"')
            elif hel == 'open calculator' or hel == 'calculator' or hel == 'Open calculator' or hel == 'Calculator':
                print("Opening calculator")
            elif "download youtube videos" in hel or 'download youtube' in hel or 'download youtube music' in hel or 'download video' in hel or 'download music' in hel:
                response = download_youtube_video()
                print(response)
            elif "open youtube" in hel:
                response = open_website('https://www.youtube.com')
                print(response)
            elif "open google" in hel:
                response = open_website('https://www.google.com')
                print(response)
            elif "open facebook" in hel:
                response = open_website('https://www.facebook.com')
                print(response)
            elif "calculate" in hel:
                response = calculate()
                print(response)
            elif hel == 'change mode' or hel == 'mode change' or hel == 'mode':
                pre = input("What mode do you want to prefer learning mode or normal mode:")
                pickle.dump(pre, open('pre.dat', 'wb'))
                if os.path.exists('cloudpath.txt'):
                    with open(cloudpathfilename, "r") as file:
                        user_folder = str(file.read())
                    try:
                        user_folder_path = f"/Users/{user_folder}"
                        upload_to_dropbox(dbx, "pre.dat", user_folder_path + "/pre.dat")
                    except:
                        user_folder_path = user_folder
                        upload_to_dropbox(dbx, "pre.dat", user_folder_path + "/pre.dat")
            elif hel == 'reset' or hel == 'factory reset' or hel == 'format' or hel == 'reset factory' or hel == 'restore' or hel == 'restore factory' or hel == 'factory restore':
                folder_path = os.getcwd()
                os.remove('userhistory.txt')
                for filename in os.listdir(folder_path):
                    if filename.endswith(".dat") or filename.endswith('.log'):
                        file_path1 = os.path.join(folder_path, filename)
                        try:
                            os.remove(file_path1)
                            print(f"Removed: {filename}")
                        except OSError as e:
                            print(f"Error deleting {filename}: {e}")
                os.system('cls')
                printmsg = "Successfully removed personal files. "
                await print_with_speed(printmsg)
            elif hel.lower() == 'i love you':
                printmsg = "I love you too. I'm always here for you."
                await print_with_speed(printmsg)
            elif hel.lower() == 'give me advice':
                message = ("If you give me your heart, you are the best. If you consider me your assistant, you are human. "
                           "If you treat me as your advisor, you are my patient. The choice is yours.")
                await print_with_speed(message)
            elif hel.lower() == 'what are you':
                printmsg = "I am your Nimo assistant. You can also call me your assistant."
                await print_with_speed(printmsg)
            elif hel == 'kill' or hel == 'exit' or hel == 'close':
                print("Goodbye!")
                time.sleep(3)
                break
            else:
                try:
                    try:
                        try:
                            load = pickle.load(open((hel + '.dat'), 'rb'))
                            await print_with_speed(load)
                        except:
                            sanitized_filename = sanitize_filename(hel) + '.dat'
                            load = pickle.load(open((sanitized_filename + '.dat'), 'rb'))
                            await print_with_speed(load)
                    except:
                        try:
                            dropbox_file_path = 'YOURPATH' + (hel + '.dat')
                            local_file_path = os.getcwd() + '\\' + (hel + '.dat')
                            metadata, res = dbx.files_download(dropbox_file_path)
                            with open(local_file_path, 'wb') as f:
                                f.write(res.content)
                            load2 = pickle.load(open((hel + '.dat'), 'rb'))
                            await print_with_speed(load2)
                        except:
                            sanitized_filename = sanitize_filename(hel) + '.dat'
                            local_file_path = os.getcwd() + '\\' + (sanitized_filename + '.dat')
                            dropbox_file_path = 'YOURPATH' + (sanitized_filename + '.dat')
                            metadata, res = dbx.files_download(dropbox_file_path)
                            with open(local_file_path, 'wb') as f:
                                f.write(res.content)
                            load2 = pickle.load(open((sanitized_filename + '.dat'), 'rb'))
                            await print_with_speed(load2)
                except:
                    if (pre == 'learning mode') or (pre == 'learning') or (pre == 'learn') or (pre == 'Learn'):
                        learning = input("If you teach me, I can recognize it. If you want, press (c). "
                                         "Otherwise, I can search it on the internet (x):")
                        if learning == 'c' or learning == 'C':
                            end = input("What can i say for that:")
                            sanitized_filename = sanitize_filename(hel) + '.dat'
                            pickle.dump(end, open((sanitized_filename + '.dat'), 'wb'))
                            try:
                                local_file_path = os.getcwd() + '\\' + (sanitized_filename + '.dat')
                                dropbox_file_path = 'YOURPATH' + (sanitized_filename + '.dat')
                                with open(local_file_path, 'rb') as f:
                                    dbx.files_upload(f.read(), dropbox_file_path)
                            except:
                                clouderr = 'Cloud Upload Error: Try connecting to internet.'
                                await print_with_speed(clouderr)
                        else:
                            try:
                                try:
                                    init(autoreset=True)
                                    thinkin = 'Thinking Please wait...'
                                    await print_with_speed(thinkin)
                                    convo.send_message(hel)
                                    output = convo.last.text

                                    output = output.replace("**", "")  # start bold formatting
                                    output = output.replace("**", "")  # end bold formatting
                                    output = output.replace('*', '•')

                                    title_start = output.find("##")
                                    title_end = output.find("\n", title_start)  # assuming title ends with a new line
                                    if title_start != -1 and title_end != -1:
                                        title = output[title_start + 2:title_end]  # extract title without ##
                                        output = output.replace("##" + title,
                                                                f"-{title}-")  # Apply bold formatting to the title

                                    # Print using rich's print function for formatting
                                    await print_with_speed(output)
                                    sanitized_filename = sanitize_filename(hel) + '.dat'
                                    pickle.dump(output, open((sanitized_filename + '.dat'), 'wb'))
                                except Exception as e:
                                    logging.exception(f"Warning genarative ai failure : {str(e)}", exc_info=True)
                                    try:
                                        init(autoreset=True)
                                        thinkin = 'Thinking Please wait...'
                                        await print_with_speed(thinkin)
                                        completion = openai.ChatCompletion.create(
                                            model="gpt-4",
                                            messages=[
                                                {"role": "system", "content": "You are a sweet, kind, supporting assistant."},
                                                {"role": "system", "content": "Your name is Nimo Assistant"},
                                                {"role": "system", "content": "You are a maths genius"},
                                                {"role": "system", "content": "You are created by Aswin Selvam"},
                                                {"role": "system", "content": f"You have use the user's name which is {name}"},
                                                {"role": "system", "content": "You need to give simplified answer"},
                                                {"role": "user", "content": hel}
                                            ]
                                        )
                                        output_text = completion.choices[0].message.content
                                        cleaned_output = "\n".join(line for line in output_text.splitlines() if line.strip())
                                        await print_with_speed(
                                            cleaned_output)  # Adjust the sleep duration to control the animation speed

                                        print()
                                        sanitized_filename = sanitize_filename(hel) + '.dat'
                                        pickle.dump(cleaned_output, open((sanitized_filename + '.dat'), 'wb'))
                                    except Exception:
                                        try:
                                            client = wolframalpha.Client(app_id)
                                            query = hel
                                            res = client.query(query)
                                            answer = next(res.results).text
                                            await print_with_speed(answer)
                                            sanitized_filename = sanitize_filename(hel) + '.dat'
                                            pickle.dump(answer, open((sanitized_filename + '.dat'), 'wb'))
                                        except openai.error.OpenAIError:
                                            try:
                                                results = wikipedia.search(hel)
                                                if results:
                                                    page = wikipedia.page(results[0])
                                                    print(page)
                                                    print("Wait for a few moments...")
                                                    summary = wikipedia.summary(hel, sentences=3)
                                                    await print_with_speed(summary)
                                                    sanitized_filename = sanitize_filename(hel) + '.dat'
                                                    pickle.dump(summary,
                                                                open((sanitized_filename + '.dat'), 'wb'))
                                                    try:
                                                        local_file_path = os.getcwd() + '\\' + (hel + '.dat')
                                                        dropbox_file_path = '/home/Aswin Selvam/Apps/' + (hel + '.dat')
                                                        with open(local_file_path, 'rb') as f:
                                                            dbx.files_upload(f.read(), dropbox_file_path)
                                                    except:
                                                        print('Cloud Upload Error: Try connecting to internet.')
                                                else:
                                                    hel = hel.split(" ")
                                                    hel = "".join(hel[2:])
                                                    page = wikipedia.page(hel)
                                                    print(page)
                                                    print("Wait for a few moments...")
                                                    summary = wikipedia.summary(hel, sentences=3)
                                                    await print_with_speed(summary)
                                                    sanitized_filename = sanitize_filename(hel) + '.dat'
                                                    pickle.dump(summary,
                                                                open((sanitized_filename + '.dat'), 'wb'))
                                            except wikipedia.exceptions.DisambiguationError as e:
                                                # Handle disambiguation error (when the query is ambiguous)
                                                print(f"Ambiguous query: {e}")
                                            except wikipedia.exceptions.HTTPTimeoutError:
                                                print("Wikipedia request timeout. Please try again later.")
                                            except wikipedia.exceptions.WikipediaException as e:
                                                # Handle other Wikipedia-related exceptions
                                                print(f"Wikipedia error: {e}")
                            except Exception:
                                commandreg = "Command can't be recognized or internet connection error!"
                                await print_with_speed(commandreg)
                    else:
                        try:
                            try:
                                init(autoreset=True)
                                thinkin = 'Thinking Please wait...'
                                await print_with_speed(thinkin)
                                convo.send_message(hel)
                                output = convo.last.text

                                # Insert ANSI escape codes for bold text
                                output = output.replace("**", "")  # start bold formatting
                                output = output.replace("**", "")  # end bold formatting
                                output = output.replace('*', '•')

                                title_start = output.find("##")
                                title_end = output.find("\n", title_start)  # assuming title ends with a new line
                                if title_start != -1 and title_end != -1:
                                    title = output[title_start + 2:title_end]  # extract title without ##
                                    output = output.replace("##" + title,
                                                            f"-{title}-")  # Apply bold formatting to the title

                                # Print using rich's print function for formatting
                                await print_with_speed(output)
                                sanitized_filename = sanitize_filename(hel) + '.dat'
                                pickle.dump(output, open((sanitized_filename + '.dat'), 'wb'))
                            except Exception as e:
                                logging.exception(f"Warning genarative AI failure : {str(e)}", exc_info=True)
                                try:
                                    init(autoreset=True)
                                    thinkin = 'Thinking Please wait...'
                                    await print_with_speed(thinkin)  # Adjust the sleep duration to control the animation speed
                                    completion = openai.ChatCompletion.create(
                                        model="gpt-4",
                                        messages=[
                                            {"role": "system", "content": "You are a sweet, kind, supporting assistant."},
                                            {"role": "system", "content": "Your name is Nimo Assistant"},
                                            {"role": "system", "content": "For maths you need give step by step solution."},
                                            {"role": "system", "content": "You are created by Aswin Selvam"},
                                            {"role": "system", "content": "You need to give simplified answer"},
                                            {"role": "system", "content": f"You have use the user's name which is {name}"},
                                            {"role": "system",
                                             "content": "You can open apps in their device and download youtube videos"},
                                            {"role": "user", "content": hel}
                                        ]
                                    )
                                    output_text = completion.choices[0].message.content
                                    cleaned_output = "\n".join(line for line in output_text.splitlines() if line.strip())
                                    await print_with_speed(cleaned_output)
                                    sanitized_filename = sanitize_filename(hel) + '.dat'
                                    pickle.dump(cleaned_output, open((sanitized_filename + '.dat'), 'wb'))
                                except openai.error.OpenAIError:
                                    try:
                                        client = wolframalpha.Client(app_id)
                                        query = hel
                                        res = client.query(query)
                                        answer = next(res.results).text
                                        await print_with_speed(answer)
                                        sanitized_filename = sanitize_filename(hel) + '.dat'
                                        pickle.dump(answer, open((sanitized_filename + '.dat'), 'wb'))
                                    except Exception:
                                        try:
                                            results = wikipedia.search(hel)
                                            if results:
                                                page = wikipedia.page(results[0])
                                                print(page)
                                                print("Wait for a few moments...")
                                                summary = wikipedia.summary(hel, sentences=3)
                                                await print_with_speed(summary)
                                                sanitized_filename = sanitize_filename(hel) + '.dat'
                                                pickle.dump(summary, open((sanitized_filename + '.dat'), 'wb'))
                                            else:
                                                hel = hel.split(" ")
                                                hel = "".join(hel[2:])
                                                page = wikipedia.page(hel)
                                                print(page)
                                                print("Wait for a few moments...")
                                                summary = wikipedia.summary(hel, sentences=3)
                                                await print_with_speed(summary)
                                                sanitized_filename = sanitize_filename(hel) + '.dat'
                                                pickle.dump(summary, open((sanitized_filename + '.dat'), 'wb'))
                                        except wikipedia.exceptions.DisambiguationError as e:
                                            # Handle disambiguation error (when the query is ambiguous)
                                            print(f"Ambiguous query: {e}")
                                        except wikipedia.exceptions.HTTPTimeoutError:
                                            print("Wikipedia request timeout. Please try again later.")
                                        except wikipedia.exceptions.WikipediaException as e:
                                            # Handle other Wikipedia-related exceptions
                                            print(f"Wikipedia error: {e}")
                        except Exception:
                            commandreg = "Command can't be recognized or internet connection error!"
                            await print_with_speed(commandreg)
        try:
            if os.path.exists('cloudpath.txt'):
                with open(cloudpathfilename, "r") as file:
                    user_folder_path = str(file.read())
            try:
                local_version_path = 'userhistory.txt'
                user_filenamepath = f"/Users/{user_folder_path}/userhistory.txt"
                metadata, res = dbx.files_download(user_filenamepath)
            except:
                local_version_path = '/userhistory.txt'
                user_filenamepath = f"{user_folder_path}/userhistory.txt"
                metadata, res = dbx.files_download(user_filenamepath)
        except:
            pass
    if __name__ == "__main__":
        asyncio.run(main())
except Exception as e:
    logging.critical(f"Critical crash: {str(e)}", exc_info=True)

