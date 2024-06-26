#TODO:
#edit the text box to display the recognized text's differences, in different colors https://www.geeksforgeeks.org/change-the-color-of-certain-words-in-the-tkinter-text-widget/
#add a button to start listening
#add a button to stop listening
#add a button to generate a new quote
#
import tkinter as tk
import Quote_finder as qf
import vosk
import pyaudio
import json, threading
model = vosk.Model(lang="en-us")
rec = vosk.KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
def listen():
    stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=8192)
    print("Listening for speech. Say 'Terminate' to stop.")
    # Start streaming and recognize speech
    while True:
        data = stream.read(4096)#read in chunks of 4096 bytes
        if rec.AcceptWaveform(data):#accept waveform of input voice
            # Parse the JSON result and get the recognized text
            result = json.loads(rec.Result())
            recognized_text = result['text']
            
            # Write recognized text to the file

            print(recognized_text)
            
            # Check for the termination keyword
            if "terminate" in recognized_text.lower():
                print("Termination keyword detected. Stopping...")
                break
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    quoted = qf.get_random_quote()
    quote = quoted[0]
    author = quoted[1]
    root = tk.Tk()
    root.title("Speechmate")
    root.geometry("800x600")
    root.configure(bg="black")
    titleholder = tk.Frame(root, bg="black", width=20)
    maintxt = tk.Label(titleholder, text="Welcome to Speechmate", bg="black", fg="white", font=("Arial", 12))
    textholder = tk.Text(root, bg="black", fg="white")
    textholder.insert(tk.END, quote)
    authortxt= tk.Label(root, text=f"Author: {author}", bg="black", fg="white", font=("Arial", 12))
    titleholder.pack(anchor="nw", pady=5)
    maintxt.pack(anchor="w")
    textholder.pack(anchor="center", pady=5)
    authortxt.pack(anchor="w")
    t1 = threading.Thread(target=listen)
    t1.start()
    root.mainloop()
