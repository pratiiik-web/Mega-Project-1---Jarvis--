import tkinter as tk
from tkinter import scrolledtext
import threading
from main import handle_voice_command
from speech_engine import speak
import time

class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis AI Assistant")
        self.root.geometry("600x500")
        self.root.configure(bg="#121212")  # pure dark mode

        # Header Label
        self.header = tk.Label(root, text="Jarvis - Your Personal AI Assistant", font=("Segoe UI", 16, "bold"), bg="#121212", fg="#00e6e6")
        self.header.pack(pady=10)

        # Status Indicator
        self.status_label = tk.Label(root, text="Idle", font=("Consolas", 12), bg="#0F0F0F", fg="lime")
        self.status_label.pack()

        # Chat display (scrollable)
        self.command_display = scrolledtext.ScrolledText(root, height=20, width=65, font=("Consolas", 12), bg="#1e1e1e", fg="#00ffcc", wrap="word")
        self.command_display.pack(pady=15)
        self.command_display.config(state=tk.DISABLED)

        # Listen button
        self.listen_button = tk.Button(root, text="Activate Jarvis", command=self.listen_command,
                                       font=("Arial", 14), bg="#00ace6", fg="white", activebackground="#007acc")
        self.listen_button.pack(pady=10)

    def listen_command(self):
        self.status_label.config(text="Listening...")
        threading.Thread(target=self.capture_command).start()

    def insert_text(self, speaker, text, color="white", delay_typing=True):
        self.command_display.config(state=tk.NORMAL)
        self.command_display.insert(tk.END, f"{speaker}: ", ("speaker",))
        if delay_typing:
            for char in text:
                self.command_display.insert(tk.END, char, ("reply",))
                self.command_display.update_idletasks()
                time.sleep(0.01)
        else:
            self.command_display.insert(tk.END, text, ("reply",))
        self.command_display.insert(tk.END, "\n\n")
        self.command_display.config(state=tk.DISABLED)
        self.command_display.see(tk.END)

    def capture_command(self):
        intro = "Initializing Jarvis... How can I assist you today?"
        self.insert_text("Jarvis", intro, color="#00ffcc", delay_typing=True)
        speak(intro)

        try:
            command, response = handle_voice_command()
            self.insert_text("You", command, delay_typing=False)
            self.insert_text("Jarvis", response, color="#00ffcc", delay_typing=True)
            speak(response)
        except Exception as e:
            self.insert_text("Jarvis", f"Error: {e}", color="red", delay_typing=True)
            speak("Sorry, something went wrong.")

        self.status_label.config(text="Idle")

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisGUI(root)
    root.mainloop()
