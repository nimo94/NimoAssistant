# Nimo Assistant

![Nimo Assistant Bannerpage](https://i.imgur.com/a43QWQJ.png)

**Nimo Assistant** is a powerful, cloud-synced virtual assistant that has evolved from a simple voice script into a polished, full-featured desktop application. It combines **Groq’s ultra-fast LPU inference**, **local system automation**, **real-time monitoring**, and a unique **Hive Mind shared-knowledge engine** to deliver instant, intelligent responses across devices and users.

---

## 🚀 Key Features

### 🧠 Intelligent Core

- **Powered by Groq AI**  
  Utilizes the **openai oss 20b** via Groq’s LPU Inference Engine for lightning-fast, human-like responses with extremely low latency.

- **Hive Mind Learning**  
  When one user teaches Nimo something new, the knowledge is saved to the cloud and instantly shared with all users — *learn once, answer forever*.

- **Math & Coding Expert**  
  Designed to break down complex math problems step-by-step and write clean, functional, well-structured code across multiple languages.

---

## 🖥️ Modern UI (v3.0 Enhanced)

- **Messenger-Style Chat Interface**  
  Clean, bubble-based chat UI with rich text formatting (bold text, headers, tables, and structured output).

- **Smart File Previews**  
  Visual “chips” for uploaded files and images, allowing users to review content before sending.

- **Real-Time System Dashboard**  
  Sidebar display showing CPU usage, RAM consumption, and overall system health.

- **Splash Screen & Auto-Update Checks**  
  Smooth startup animations with automatic version validation on launch.

---

## 🛠️ Tools & Utilities

- **YouTube Downloader**  
  Built on `yt-dlp` with a visual progress bar and background execution.

- **Vision Mode**  
  Drag-and-drop image analysis powered by **Llama 3.2 Vision** for OCR and visual understanding.

- **Smart Compression Engine**  
  Automatically compresses images and truncates large text files to prevent API and token-limit errors.

- **App Launcher**  
  Launch applications such as Chrome, Spotify, and system tools directly from chat commands.

---

## 📜 Version History

| Version | Status   | Key Changes |
|--------|----------|-------------|
| **v3.0** | Current | Groq Integration, Llama 3.3 70B, Chat UI Overhaul (Segoe UI), File Staging Area, Image Compression |
| **v2.5** | Stable  | Fixed input loops, Added spam protection, Dedicated login GUI |
| **v2.1** | Legacy  | Initial Dropbox Sync, Basic file uploading |
| **v2.0** | Legacy  | Full GUI (CustomTkinter), Multi-threading, System Dashboard |
| **v1.9** | Beta    | Migration to async text generation |

---

## 🧠 Deep Dive: How the Hive Mind Works

The **Hive Mind** enables Nimo to *learn once, answer forever*.

### How it works:

1. **Query Sanitization**  
   Each prompt is converted into a safe filename.  
   Example:  
   `"Who is Iron Man?" → who_is_iron_man_.dat`

2. **Cloud Lookup**  
   Nimo checks a shared Dropbox knowledge folder for an existing answer.

3. **Instant Retrieval**  
   If found, the answer is served instantly — faster than calling the AI model.

4. **Collective Learning**  
   If not found, Nimo generates the answer using **Groq**, saves it locally, uploads it, and future users instantly benefit.

This creates a **global, user-generated knowledge base** that grows smarter over time.

---

## 📦 Installation

1. Download **`NimoAssistant.exe`** from the Releases page  
2. Run the installer  
3. On first launch, the **auto-updater** ensures you are running **v3.0**  
4. **Log in or register** to enable Hive Mind cloud syncing  

You’re ready to go.

---

## 📸 Screenshots

### **Dark Mode**

![Nimo Assistant screenshots1](https://i.imgur.com/JRbAwK7.png)
![Nimo Assistant screenshots2](https://i.imgur.com/fi0Z1Tn.png)
![Nimo Assistant screenshots3](https://i.imgur.com/fi0Z1Tn.png)

---

### **Light Mode**

![Nimo Assistant screenshots4](https://i.imgur.com/iuTIs4o.png)
![Nimo Assistant screenshots5](https://i.imgur.com/h4kKHM3.png)
![Nimo Assistant screenshots6](https://i.imgur.com/5uJh65n.png)
