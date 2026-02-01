import cv2
import torch
import pyttsx3
import speech_recognition as sr
import threading
import queue
import os
import ssl
import time # Added for sleep
from ultralytics import YOLO
from transformers import AutoModelForCausalLM, AutoTokenizer
from face_animation import draw_ghost_face 

# --- SETUP ---
ssl._create_default_https_context = ssl._create_unverified_context
os.environ['CURL_CA_BUNDLE'] = ''

MODEL_PATH = "./Qwen2.5-1.5B-Instruct" 
vision_model = YOLO('yolov8n.pt')

voice_queue = queue.Queue()
is_speaking = False
is_thinking = False # NEW: Prevents ear from listening while brain works
last_ai_text = "Target locked."
current_objects = []
frame_count = 0

# --- VOICE WORKER ---
def ghost_voice_worker():
    global is_speaking
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    while True:
        text = voice_queue.get()
        is_speaking = True
        engine.say(text)
        engine.runAndWait()
        is_speaking = False

threading.Thread(target=ghost_voice_worker, daemon=True).start()

# --- THE BRAIN ---
print("--- Loading Brain... ---")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH, device_map="cpu", torch_dtype=torch.float16, low_cpu_mem_usage=True
)

def trigger_roast(obj_name):
    global last_ai_text, is_thinking
    # This MUST print in your terminal. If it doesn't, the thread didn't start.
    print(f"!!! BRAIN ENGAGED for: {obj_name} !!!") 
    
    try:
        prompt = f"<|im_start|>system\nYou are a savage ghost.<|im_end|>\n<|im_start|>user\nRoast this {obj_name} in one short sentence.<|im_end|>\n<|im_start|>assistant\n"
        inputs = tokenizer(prompt, return_tensors="pt").to("cpu")
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs, 
                max_new_tokens=20, 
                do_sample=False, # False is faster for low RAM
                pad_token_id=tokenizer.eos_token_id
            )
        
        response = tokenizer.decode(outputs[0], skip_special_tokens=True).split("assistant")[-1].strip()
        print(f"--- Ghost Success: {response} ---")
        last_ai_text = response
        voice_queue.put(response)
    except Exception as e:
        print(f"!!! BRAIN ERROR: {e} !!!")
    finally:
        # Give the CPU a moment to breathe before allowing more listening
        time.sleep(1)
        is_thinking = False

def listen_loop():
    global is_thinking
    r = sr.Recognizer()
    r.energy_threshold = 400 
    
    with sr.Microphone() as source:
        print("--- Mic: Calibrating for 1 second... ---")
        r.adjust_for_ambient_noise(source, duration=1)
        
        while True:
            # Check the flags
            if not is_speaking and not is_thinking:
                try:
                    print("--- GHOST IS LISTENING ---")
                    audio = r.listen(source, timeout=3, phrase_time_limit=2)
                    user_text = r.recognize_google(audio).lower()
                    print(f"-> Ghost heard: {user_text}")

                    # Use a local snapshot of objects to avoid empty list errors
                    if len(current_objects) > 0:
                        target = current_objects[0]
                        is_thinking = True # LOCK
                        print(f"-> Starting Roast Thread for {target}...")
                        t = threading.Thread(target=trigger_roast, args=(target,))
                        t.start()
                    else:
                        print("-> Heard you, but I don't see any objects to roast!")
                        
                except (sr.WaitTimeoutError, sr.UnknownValueError):
                    continue 
                except Exception as e:
                    print(f"Mic Loop Error: {e}")
            else:
                # Ghost is busy speaking or thinking, wait
                time.sleep(0.5)

threading.Thread(target=listen_loop, daemon=True).start()

# --- THE EYES ---
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, frame = cap.read()
    if not success: break
    frame_count += 1

    results = vision_model(frame, stream=True, conf=0.4, verbose=False)
    current_objects = []

    for r in results:
        for box in r.boxes:
            name = vision_model.names[int(box.cls[0])]
            current_objects.append(name)
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            scale = (x2 - x1) // 6

            draw_ghost_face(frame, cx, cy, scale, is_speaking, frame_count)

    if is_speaking:
        cv2.putText(frame, last_ai_text, (20, frame.shape[0]-20), 1, 1.2, (0, 255, 0), 2)

    cv2.imshow("GhostVision", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
