import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from pydub import AudioSegment
import os
import base64

class AudioManipulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Syn Audio Manipulation Tool")
        os.makedirs("temp", exist_ok=True)
        os.makedirs("exports", exist_ok=True)  # Ensure export directory exists
        self.setup_widgets()
        self.input_file_path = None
        self.temp_file_path = None

    def setup_widgets(self):
        input_file_frame = tk.Frame(self.root, bg="#333")
        input_file_frame.pack(pady=10)

        input_file_label = tk.Label(input_file_frame, text="Input File:", bg="#333", fg="white")
        input_file_label.pack(side=tk.LEFT)

        self.input_file_entry = tk.Entry(input_file_frame, width=40, bg="#444", fg="white")
        self.input_file_entry.pack(side=tk.LEFT, padx=(10, 0))

        browse_button = tk.Button(input_file_frame, text="Browse", command=self.browse_input_file, bg="#555", fg="white")
        browse_button.pack(side=tk.LEFT, padx=(10, 0))

        menu_frame = tk.Frame(self.root, bg="#333")
        menu_frame.pack(pady=10)

        menu_label = tk.Label(menu_frame, text="Modification:", bg="#333", fg="white")
        menu_label.pack(side=tk.LEFT)

        self.menu_var = tk.StringVar()
        self.menu_var.set("Select an option")
        menu_options = ["Speed Adjustment", "Pitch Adjustment"]
        menu = tk.OptionMenu(menu_frame, self.menu_var, *menu_options, command=self.perform_action)
        menu.config(bg="#444", fg="white", activebackground="#555", activeforeground="white")
        menu.pack(side=tk.LEFT, padx=(10, 0))

        export_button = tk.Button(self.root, text="Export to S:MSP", command=self.export_output_file, bg="#555", fg="white")
        export_button.pack(pady=10)

    def browse_input_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.input_file_path = file_path
            self.input_file_entry.delete(0, tk.END)
            self.input_file_entry.insert(tk.END, file_path)

    def perform_action(self, action):
        if not self.input_file_path:
            messagebox.showerror("Error", "Please select an input file.")
            return

        try:
            sound = AudioSegment.from_file(self.input_file_path)
            if action == "Speed Adjustment":
                self.speed_adjustment(sound)
            elif action == "Pitch Adjustment":
                self.pitch_adjustment(sound)
            else:
                messagebox.showerror("Error", "Invalid action selected.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def speed_adjustment(self, sound):
        speed = simpledialog.askfloat("Speed Adjustment", "Enter the speed adjustment factor:", parent=self.root)
        if speed:
            adjusted_sound = sound.speedup(playback_speed=speed)
            self.temp_file_path = os.path.join("temp", "speed_adjusted_audio.mp3")
            adjusted_sound.export(self.temp_file_path, format="mp3")
            messagebox.showinfo("Success", "Speed adjustment applied successfully!")

    def pitch_adjustment(self, sound):
        pitch = simpledialog.askfloat("Pitch Adjustment", "Enter the pitch adjustment factor:", parent=self.root)
        if pitch:
            adjusted_sound = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * pitch)})
            self.temp_file_path = os.path.join("temp", "pitch_adjusted_audio.mp3")
            adjusted_sound.export(self.temp_file_path, format="mp3")
            messagebox.showinfo("Success", "Pitch adjustment applied successfully!")

    def generate_encrypted_code(self, file_path):
        encoded_bytes = base64.urlsafe_b64encode(file_path.encode("utf-8"))
        return encoded_bytes.decode("utf-8")

    def export_output_file(self):
        if not self.temp_file_path:
            messagebox.showerror("Error", "No modifications made yet.")
            return

        export_file_path = os.path.join("exports", os.path.basename(self.temp_file_path))
        try:
            os.replace(self.temp_file_path, export_file_path)
            encrypted_code = self.generate_encrypted_code(export_file_path)
            self.root.clipboard_clear()  # Clear the clipboard
            self.root.clipboard_append(encrypted_code)  # Append encrypted code to the clipboard
            self.root.update()  # Now it stays on the clipboard after the window is closed
            messagebox.showinfo("Export Success", f"File exported successfully! Encrypted Code: {encrypted_code}\n\nThe encrypted code has been copied to your clipboard.")
            self.temp_file_path = None
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while exporting the file: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#222")
    app = AudioManipulationApp(root)
    root.mainloop()
