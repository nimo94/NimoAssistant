# Nimo Assistant


![Nimo Assistant Bannerpage](https://i.imgur.com/a43QWQJ.png)

Nimo Assistant is a powerful, cloud-synced virtual assistant that has evolved from a simple voice script into a polished, GUI-based desktop application. It combines Google Gemini AI, local system automation, real-time monitoring, and a unique "Hive Mind" shared-knowledge engine.

---

## 🚀 Key Features

### 🧠 Intelligent Core

* **Powered by Gemini** – Utilizes Google's Gemini 2.0 Flash model for fast, human-like responses.
* **Hive Mind Learning** – When one user teaches Nimo something new, the answer is saved to the cloud and instantly shared across all users.
* **Math Genius Mode** – Designed to break down and solve complex math problems step-by-step.

---

## 🖥️ Modern UI (v2.0 Exclusive)

* **Windows 11-Style Dark Interface** – Clean, modern, and aesthetically pleasing.
* **Splash Screen & Load Animations** – Smooth startup visuals.
* **Real-Time Dashboard** – Displays CPU, RAM, and Network usage.
* **System Tray Support** – Runs quietly in the background.

---

## 🛠️ Tools & Utilities

* **YouTube Downloader** – Built on `yt-dlp` with a visual progress bar.
* **Vision Mode** – Uses Google Cloud Vision for text extraction and image analysis.
* **System Control** – Perform shutdown, restart, or logoff via text commands.
* **App Launcher** – Open apps like Chrome, Spotify, etc., directly from chat.

---

## 📜 Version History

| Version  | Status           | Key Changes                                                                      |
| -------- | ---------------- | -------------------------------------------------------------------------------- |
| **v2.0** | Official Release | Full GUI (CustomTkinter), Multi-threading, Auto-Update visuals, System Dashboard |
| **v1.9** | Beta             | Migration to Google Gemini AI, Async text generation                             |
| **v1.6** | Beta             | OpenCV & Cloud Vision integration                                                |
| **v1.4** | Beta             | Integrated GPT-3.5 & System Controls                                             |
| **v1.2** | Beta             | Dropbox Syncing + YouTube Downloader                                             |
| **v1.1** | Beta             | Initial release with basic voice command support                                 |

---

## 🧠 Deep Dive: How the Hive Mind Works

The Hive Mind enables Nimo to "learn once, answer forever." Here's the flow:

1. **Query Sanitization**
   Your prompt becomes a safe filename. Example:
   *"Who is Iron Man?" → `who_is_iron_man_.dat`*

2. **Cloud Lookup**
   Nimo checks a shared Dropbox folder for the answer.

3. **Instant Retrieval**
   If found, Nimo serves that answer instantly—faster than calling Gemini.

4. **Collective Learning**
   If not found, Nimo generates the answer using Gemini, saves it locally, uploads it, and future users benefit automatically.

This creates a global, user-generated knowledge base.

---

## 📦 Installation

1. Download **NimoAssistant.exe** from the Releases page.
2. Run the installer.
3. On first launch, set up your user profile.

You're ready to go.

## Screenshots
### **Dark Mode**
![Nimo Assistant screenshots1](https://i.imgur.com/JRbAwK7.png)
![Nimo Assistant screenshots2](https://i.imgur.com/fi0Z1Tn.png)
![Nimo Assistant screenshots3](https://i.imgur.com/fi0Z1Tn.png)
### **Light Mode**
![Nimo Assistant screenshots4](https://i.imgur.com/iuTIs4o.png)
![Nimo Assistant screenshots5](https://i.imgur.com/h4kKHM3.png)
![Nimo Assistant screenshots6](https://i.imgur.com/5uJh65n.png)
