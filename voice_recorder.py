import tkinter as tk
import sounddevice
from scipy.io.wavfile import write
import threading

class VoiceRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")

        self.label = tk.Label(root, text="Enter recording time (seconds):")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.start_button = tk.Button(root, text="Start Recording", command=self.start_recording)
        self.start_button.pack()

        self.status_label = tk.Label(root, text="")
        self.status_label.pack()

    def start_recording(self):
        try:
            seconds = int(self.entry.get())
            self.status_label.config(text="Recording Started...")

            # Using threading to prevent GUI freezing during recording
            thread = threading.Thread(target=self.record_and_save, args=(seconds,))
            thread.start()

        except ValueError:
            self.status_label.config(text="Invalid input")

    def record_and_save(self, seconds):
        recording = sounddevice.rec((seconds * 44100), samplerate=44100, channels=1)
        sounddevice.wait()

        file = "record.wav"
        write(file, 44100, recording)

        self.status_label.config(text="Recording Finished")

        # Automatically close the program after 2 seconds
        self.root.after(2000, self.root.quit)

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()
