import tkinter as tk
from tkinter import filedialog, messagebox, font
import pygame
import os
import json
import sys

class PianoApp:
    def __init__(self, root=None, cli_mode=False):
        self.cli_mode = cli_mode
        if not cli_mode:
            self.root = root
            self.root.title("Syn Music Synthesis Programme")
            self.root.configure(bg="#121212")
            pygame.mixer.init()
            self.setup_ui()
        else:
            pygame.mixer.init()

        self.sounds = {}
        self.channels = {}
        self.key_buttons = {}

        if cli_mode:
            self.run_cli_mode()

    def setup_ui(self):
        load_json_btn = tk.Button(self.root, text="Load JSON Configuration", command=self.load_json_configuration, bg="#282828", fg="#FFFFFF")
        load_json_btn.pack(pady=20)

    def load_json_configuration(self, json_path=None):
        if not json_path:
            json_path = filedialog.askopenfilename(title="Select JSON Configuration", filetypes=[("JSON files", "*.json")])
            if not json_path:
                return

        with open(json_path, 'r') as file:
            config = json.load(file)

        self.apply_json_configuration(config)

    def apply_json_configuration(self, config):
        for key, file_path in config.get("key_mappings", {}).items():
            if os.path.exists(file_path):
                self.sounds[key] = pygame.mixer.Sound(file_path)
                print(f"Loaded sound for key {key}: {file_path}")
            else:
                print(f"File not found for key {key}: {file_path}")
                if not self.cli_mode:
                    messagebox.showwarning("File Not Found", f"The file for key {key} was not found: {file_path}")

        if not self.cli_mode:
            messagebox.showinfo("Configuration Loaded", "The JSON configuration has been successfully loaded.")

    def run_cli_mode(self):
        print("Running in CLI mode. Please enter the path to the JSON configuration file:")
        json_path = input()
        if json_path:
            self.load_json_configuration(json_path=json_path)

def main():
    # Check if "gui" is in the command-line arguments to run in GUI mode
    gui_mode = "gui" in sys.argv
    
    if gui_mode:
        root = tk.Tk()
        root.geometry("600x400")
        app = PianoApp(root)
        root.mainloop()
    else:
        # Run in CLI mode by default
        app = PianoApp(cli_mode=True)

if __name__ == "__main__":
    main()
