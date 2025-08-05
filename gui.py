import tkinter as tk
from tkinter import scrolledtext
import threading
from main import handle_voice_command, handle_text_command  # Ensure this is defined in main.py
from speech_engine import speak
import time

class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis AI Assistant")
        self.root.geometry("600x550")
        self.root.configure(bg="#121212")  # Dark theme

        # Header
        self.header = tk.Label(root, text="Jarvis - Your Personal AI Assistant",
                               font=("Segoe UI", 30, "bold"), bg="#121212", fg="#00e6e6")
        self.header.pack(pady=10)

        # Status Indicator
        self.status_label = tk.Label(root, text="Mic: OFF", font=("Consolas", 12),
                                     bg="#0F0F0F", fg="orange")
        self.status_label.pack()

        # Chat display area
        self.command_display = scrolledtext.ScrolledText(root, height=18, width=65,
                                                         font=("Consolas", 12), bg="#1e1e1e", fg="#00ffcc", wrap="word")
        self.command_display.pack(pady=10)
        self.command_display.config(state=tk.DISABLED)

        # Voice activation button
        self.listen_button = tk.Button(root, text="Activate Voice Command", command=self.listen_command,
                                       font=("Arial", 13), bg="#00ace6", fg="white", activebackground="#007acc")
        self.listen_button.pack(pady=5)

        # Text Entry Field (centered)
        self.text_entry = tk.Entry(root, font=("Consolas", 12), width=40,
                                   bg="#1e1e1e", fg="white", insertbackground="white")
        self.text_entry.pack(pady=10)

        # Send button for manual text input
        self.send_button = tk.Button(root, text="Send Command", command=self.send_text_command,
                                     font=("Arial", 12), bg="#00b386", fg="white", activebackground="#007a66")
        self.send_button.pack()

                # Manual input label
        self.manual_label = tk.Label(root, text="Type your command below:", font=("Arial", 12), bg="#121212", fg="white")
        self.manual_label.pack(pady=(20, 5))

        # Manual input entry
        self.manual_entry = tk.Entry(root, font=("Arial", 12), width=40)
        self.manual_entry.pack()

        # Manual submit button
        self.manual_button = tk.Button(root, text="Submit", font=("Arial", 12), bg="#444", fg="white",
                                       command=self.process_manual_input)
        self.manual_button.pack(pady=5)


    def listen_command(self):
        self.status_label.config(text="Mic: ON", fg="lime")
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

        self.status_label.config(text="Mic: OFF", fg="orange")

    def send_text_command(self):
        user_input = self.text_entry.get().strip()
        if not user_input:
            return
        self.text_entry.delete(0, tk.END)
        self.insert_text("You", user_input, delay_typing=False)

        try:
            response = handle_text_command(user_input)
            self.insert_text("Jarvis", response, color="#00ffcc", delay_typing=True)
            speak(response)
        except Exception as e:
            error_msg = f"Jarvis crashed while processing: {e}"
            print(error_msg)
            self.insert_text("Jarvis", error_msg, color="red", delay_typing=False)


    def process_manual_input(self):
        user_input = self.manual_entry.get()
        self.manual_entry.delete(0, tk.END)  # 🧽 Clear the entry field right away
        if user_input.strip() == "":
            return
        self.insert_text("You", user_input, delay_typing=False)
        response = handle_text_command(user_input)
        self.insert_text("Jarvis", response)
        speak(response)



if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisGUI(root)
    root.mainloop()
