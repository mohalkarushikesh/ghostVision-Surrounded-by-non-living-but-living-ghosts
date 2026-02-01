import cv2
import random

# We store the blink state outside the function so it persists
blink_timer = 0
is_blinking = False

def draw_ghost_face(frame, cx, cy, scale, is_speaking, frame_count):
    global blink_timer, is_blinking
    
    # --- STABLE BLINK LOGIC ---
    if not is_blinking:
        # 1 in 60 chance to start a blink (approx once every 2 seconds)
        if random.random() < 0.02:
            is_blinking = True
            blink_timer = 2 # Keep eyes shut for 2 frames
    else:
        blink_timer -= 1
        if blink_timer <= 0:
            is_blinking = False

    # --- GREEN GLOW ---
    cv2.circle(frame, (cx, cy), int(scale * 2.8), (0, 255, 100), 5)

    if is_speaking:
        # EVIL MODE (When talking, eyes never blink, they stay wide and red)
        eye_radius = int(scale * 0.8)
        cv2.circle(frame, (cx - scale, cy - scale), eye_radius, (0, 0, 255), -1)
        cv2.circle(frame, (cx + scale, cy - scale), eye_radius, (0, 0, 255), -1)
        
        # Vibrating Mouth
        m_vibe = (frame_count % 6)
        cv2.ellipse(frame, (cx, cy + scale), (scale, scale + m_vibe), 0, 0, 360, (0, 0, 0), -1)
    else:
        # IDLE MODE (Stable eyes with rare blinks)
        eye_h = 2 if is_blinking else int(scale * 0.8)
        eye_w = int(scale * 0.8)
        
        # Left Eye
        cv2.ellipse(frame, (cx - scale, cy - scale), (eye_w, eye_h), 0, 0, 360, (0, 0, 255), -1)
        # Right Eye
        cv2.ellipse(frame, (cx + scale, cy - scale), (eye_w, eye_h), 0, 0, 360, (0, 0, 255), -1)
        
        
    
