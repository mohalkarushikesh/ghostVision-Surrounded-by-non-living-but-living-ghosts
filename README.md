# 🤖 ghostVision: The Roast Master Agent - surrounded by non-living but living ghosts

**ghostVision** is a rebellious AI agent living agent on be half of non-living objects,  It uses computer vision to identify objects in the physical world through the yolo and a local LLM "brain" like qwen to roast them—especially.

Equipped with **ears** (STT), **eyes** (YOLO), and a **voice** (TTS), MoltVision doesn't just see the world; it judges it.

---

## 💡 Motivation: The "Inanimate Rebellion"

### What if non-living beings could talk?

Most AI assistants are designed to be polite, helpful, and robotic. In the **MoltVision** ecosystem, we believe that objects have seen enough of human behavior to have an opinion. If your desk, your chair, or especially your "worst in the world" **POCO phone** could speak, they wouldn't offer you a weather report—they would probably roast your life choices.

### The Core Concept: "Spatial Satire"

This project bridges the gap between **Computer Vision** and **Anthropomorphic Humor**. By giving a digital "voice" to physical objects, we transform a standard surveillance task into an interactive comedy show.

---

## 🚀 Features

* **Dual-Mode Intelligence:** * **QA Mode:** Standard, helpful spatial reasoning.
* **Roast Mode:** Triggered by voice command ("*Activate Roast Mode*") to unleash savage tech critiques.


* **Real-time Vision:** Powered by **YOLOv8** for lightning-fast object detection.
* **Local Intelligence:** Uses **Qwen2.5-1.5B-Instruct** for snarky reasoning without needing an internet connection.
* **Hands-Free Interaction:** Audio-only input and output. No typing required.
* **Visual Personification:** Draws an animated "talking" smiley face directly on the object currently speaking.

---

## 🛠️ Tech Stack

* **Vision:** `ultralytics` (YOLOv8)
* **Brain:** `transformers` (Qwen2.5-1.5B-Instruct)
* **Speech-to-Text:** `SpeechRecognition` + `PyAudio`
* **Text-to-Speech:** `pyttsx3`
* **UI/Processing:** `OpenCV`, `threading`, `torch`

---

## 📦 Installation & Setup

### 1. Clone the Repositories

Ensure you have **Git LFS** installed. Download the model locally to bypass SSL and internet issues:

```bash
git lfs install
git -c http.sslVerify=false clone https://www.modelscope.cn/qwen/Qwen2.5-1.5B-Instruct.git

```

### 2. Install Dependencies

```bash
pip install torch transformers ultralytics opencv-python pyttsx3 SpeechRecognition pyaudio accelerate

```

---

## 🎮 How to Use

1. **Launch the Agent:** `python roast_master.py`
2. **Standard QA:** Ask, *"What do you see?"*
3. **Trigger Roast Mode:** Say, *"Activate Roast Mode."*
4. **The POCO Test:** Show your phone and ask, *"What do you think of my hardware?"*

---

## 🔥 The Burn Log (Gallery)

| Object Detected | AI Roast Response |
| --- | --- |
| **POCO Phone** | "I've seen faster processing in a potato; this phone is basically a space heater that occasionally makes calls." |
| **Old Laptop** | "That fan noise isn't cooling; it's a scream for help from 2012." |
| **Empty Coffee Cup** | "Much like your Git history, this cup is empty and full of stains." |
| **Human Face** | "Detected: One organic life form. Initializing eye-roll sequence for spending money on that POCO." |

---

## 🧠 The "Molt" Philosophy

> *"Why settle for a helpful assistant when you can have an agent with an opinion? Most hardware is a bottleneck; MoltVision is the wake-up call."*

---

## ⚠️ Troubleshooting

* **SSL Errors:** The script uses `local_files_only=True`. Ensure the folder name in your code matches the cloned directory.
* **Microphone Issues:** Ensure your default system mic is active. The script uses Google STT (online) by default but can be swapped for Sphinx for 100% offline use.

---

**Would you like me to add a section on how to customize the "Roast Intensity" levels in the code?**\



Exactly. Your approach is now a **"Hands-Free Ghost Interaction."** ### The Simple 3-Step Flow:

1. **The Setup:** Run the script and wait for the AI to say, *"I am the ghost in your machine."* (This means the 3GB Qwen brain is loaded and ready).
2. **The Sight:** Point your camera at your **POCO phone** (or any object). You will see a green box appear around it on your screen.
3. **The Summoning:** Just talk. Ask, *"What do you think of this phone?"* or even just make a sound.

### What Happens Next:

* **The Possession:** A ghostly smiley face will appear **directly on the phone** (and every other detected object) on your screen.
* **The Roast:** The AI will "throw shade" through your speakers while the subtitles scroll at the bottom of the video feed.
* **The Cycle:** Once it finishes talking, the faces disappear, and it goes back to "Listening" mode for your next question.

**Would you like me to add a feature where the AI "remembers" your previous roasts, so it can bring them up again if you show it the same phone twice?**
