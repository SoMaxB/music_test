import pyaudio
import numpy as np


notes = {'C': 261,
         'C#': 277,
         'D': 293,
         'D#': 311,
         'E': 329,
         'F': 349,
         'F#': 369,
         'G': 391,
         'G#': 415,
         'A': 440,
         'A#': 466,
         'B': 493}


# Ask the user to enter a sequence of notes
user_notes = input('Enter a sequence of notes separated by commas (example: E,F,G): ').split(',')

# Ask the user to enter a sequence of durations
user_durations = input('Enter a sequence of durations in milliseconds separated by commas (example: 500,500,500): ').split(',')

# Convert durations to integers
user_durations = [int(duration) for duration in user_durations]

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open an audio stream
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

# Play the sequence of notes
for note, duration in zip(user_notes, user_durations):
    frequency = notes[note.upper()]
    samples = (np.sin(2 * np.pi * np.arange(44100 * duration / 1000) * frequency / 44100)).astype(np.float32)
    stream.write(samples.tobytes())

# Stops audio stream
stream.stop_stream()
stream.close()

# Stops PyAudio
p.terminate()
