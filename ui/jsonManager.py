import json
import os
import shutil

def load_saves(key_path):
    try:
        if os.path.exists("./saves.json"):
            with open("./saves.json", "r") as f:
                data = json.load(f)
                keys = key_path.split(".")
                for key in keys:
                    data = data.get(key, {})
                return data
    except:
        pass
    return None

def save_saves(key_path, value):
    try:
        data = {}
        if os.path.exists("./saves.json"):
            with open("./saves.json", "r") as f:
                data = json.load(f)
        
        keys = key_path.split(".")
        current = data
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        
        current[keys[-1]] = value
        
        with open("./saves.json", "w") as f:
            json.dump(data, f, indent=2)
        return True
    except:
        return False

def load_settings():
    return {
        "input_device": load_saves("audio.input_device") or "Default Microphone",
        "output_device": load_saves("audio.output_device") or "Default Speakers"
    }

def save_settings(input_device, output_device):
    save_saves("audio.input_device", input_device)
    save_saves("audio.output_device", output_device)

def load_soundboard_settings():
    return {
        "enabled": load_saves("audio.enabled") if load_saves("audio.enabled") is not None else True,
        "volume": load_saves("audio.volume") or 50
    }

def load_soundboards():
    sounds = load_uploaded_sounds()
    soundboards = [None] * 9
    
    for sound in sounds:
        button_idx = sound["button"] - 1
        if 0 <= button_idx < 9:
            soundboards[button_idx] = sound
    
    return soundboards

def save_soundboard_settings(enabled, volume):
    save_saves("audio.enabled", enabled)
    save_saves("audio.volume", volume)

def load_uploaded_sounds():
    try:
        if os.path.exists("./sounds/sounds.json"):
            with open("./sounds/sounds.json", "r") as f:
                data = json.load(f)
                return data.get("sounds", [])
    except:
        pass
    return []

def save_uploaded_sounds(sounds):
    try:
        os.makedirs("./sounds", exist_ok=True)
        with open("./sounds/sounds.json", "w") as f:
            json.dump({"sounds": sounds}, f, indent=2)
        return True
    except:
        return False

def validate_name(name):
    return name[:15] if name else "Sound"

def cleanup_unused_files():
    try:
        sounds = load_uploaded_sounds()
        referenced_files = {sound["file"] for sound in sounds}
        
        sounds_dir = "./sounds"
        if not os.path.exists(sounds_dir):
            return
        
        audio_extensions = {".mp3", ".wav", ".ogg", ".flac", ".mp4", ".m4a", ".aac"}
        
        for filename in os.listdir(sounds_dir):
            filepath = os.path.join(sounds_dir, filename)
            file_ext = os.path.splitext(filename)[1].lower()
            
            if file_ext in audio_extensions:
                normalized_path = f"sounds/{filename}"
                if normalized_path not in referenced_files:
                    try:
                        os.remove(filepath)
                    except:
                        pass
    except:
        pass

def delete_sound(button_num, refresh_callback):
    sounds = load_uploaded_sounds()
    sound_idx = next((i for i, s in enumerate(sounds) if s["button"] == button_num), None)
    
    if sound_idx is not None:
        sounds.pop(sound_idx)
        save_uploaded_sounds(sounds)
        cleanup_unused_files()
        refresh_callback()

def add_or_update_sound(button_num, name, file_path, source_file):
    try:
        filename = os.path.basename(source_file)
        dest_path = f"./sounds/{filename}"
        shutil.copy(source_file, dest_path)
        
        sounds = load_uploaded_sounds()
        existing_idx = next((i for i, s in enumerate(sounds) if s["button"] == button_num), None)
        
        new_sound = {
            "id": button_num,
            "button": button_num,
            "name": name,
            "file": file_path
        }
        
        if existing_idx is not None:
            sounds[existing_idx] = new_sound
        else:
            sounds.append(new_sound)
        
        return save_uploaded_sounds(sounds)
    except:
        return False