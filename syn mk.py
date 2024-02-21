import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import pygame
import os
import base64

class PianoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("S:MSP")
        self.sounds = {}
        self.channels = []
        self.key_buttons = {}  # Track key buttons for updates

        self.grid_size = (5, 3)  # Define grid size for keys

        self.root.configure(bg="#121212")
        self.label_fg = "#FFFFFF"
        self.button_bg = "#282828"
        self.button_fg = "#FFFFFF"
        self.entry_bg = "#3A3A3A"
        self.entry_fg = "#FFFFFF"

        self.setup_controls()
        self.setup_piano()

        self.root.focus_set()
        self.root.bind("<KeyPress>", self.key_press_handler)

    def setup_controls(self):
        self.controls_frame = tk.Frame(self.root, bg="#121212")
        self.controls_frame.pack(side=tk.LEFT, padx=20)

        self.add_key_button = tk.Button(self.controls_frame, text="Add Key", command=self.add_key, bg=self.button_bg, fg=self.button_fg)
        self.add_key_button.pack(pady=5)

        import_button = tk.Button(self.controls_frame, text="Import from S:AMS", command=self.import_from_ams, bg=self.button_bg, fg=self.button_fg)
        import_button.pack(pady=5)

    def setup_piano(self):
        self.piano_frame = tk.Frame(self.root, bg="#121212")
        self.piano_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        for row in range(self.grid_size[0]):
            for col in range(self.grid_size[1]):
                key_frame = tk.Frame(self.piano_frame, bg=self.button_bg, width=100, height=100)
                key_frame.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
                self.piano_frame.grid_rowconfigure(row, weight=1)
                self.piano_frame.grid_columnconfigure(col, weight=1)

    def add_key(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.wav;*.mp3"), ("All files", "*.*")], parent=self.root)
        if file_path:
            self.add_key_specific(file_path)

    def add_key_specific(self, file_path):
        key_name = str(len(self.sounds) + 1)
        self.sounds[key_name] = pygame.mixer.Sound(file_path)
        if key_name not in self.key_buttons:  # Check if key button needs to be created
            row = (len(self.sounds) - 1) // self.grid_size[1]
            col = (len(self.sounds) - 1) % self.grid_size[1]
            key_button = tk.Button(self.piano_frame, text=key_name, command=lambda k=key_name: self.play_sound(k), bg=self.button_bg, fg=self.button_fg)
            key_button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            self.key_buttons[key_name] = key_button

    def play_sound(self, key):
        if key in self.sounds:
            if len(self.channels) < 5:
                channel = pygame.mixer.Channel(len(self.channels))
                self.channels.append(channel)
                sound = self.sounds[key]
                channel.play(sound, loops=-1)

    def stop_sound(self, key):
        if key in self.sounds:
            for channel in self.channels:
                if channel.get_busy() and channel.get_sound() == self.sounds[key]:
                    channel.stop()
                    self.channels.remove(channel)

    def stop_all_sounds(self):
        for channel in self.channels[:]:  # Iterate over a copy of the list
            channel.stop()
        self.channels.clear()  # Clear the list of channels after stopping all sounds

    def key_press_handler(self, event):
        key = event.char
        if key in self.sounds:
            self.play_sound(key)
        elif key == 's':  # Check if 'S' key is pressed
            self.stop_all_sounds()  # Call the method to stop all sounds
        elif event.keysym == 'BackSpace':
            if key in self.sounds:
                self.stop_sound(key)
        elif event.keysym in self.keys:
            self.stop_sound(event.keysym)

    def decode_encrypted_code(self, code):
        decoded_bytes = base64.urlsafe_b64decode(code.encode("utf-8"))
        return decoded_bytes.decode("utf-8")

    def import_from_ams(self):
        code = simpledialog.askstring("Import from S:AMS", "Enter the encrypted code:", parent=self.root)
        if code:
            file_path = self.decode_encrypted_code(code)
            if os.path.exists(file_path):
                self.add_key_specific(file_path)
            else:
                messagebox.showerror("Error", "Invalid code or file does not exist.")

def main():
    pygame.mixer.init()
    root = tk.Tk()
    root.geometry("800x600")  # Adjust window size to better fit the 5x5 grid
    app = PianoApp(root)
    root.mainloop()
    pygame.mixer.quit()

if __name__ == "__main__":
    main()
