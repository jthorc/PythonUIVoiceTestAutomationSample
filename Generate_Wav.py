import numpy as np
import wave
import os

# Parameters
sample_rate = 44100  # Samples per second
duration = 5  # Duration in seconds
frequency = 5000  # Frequency in Hz
wav_type = "sine"
bit_type = 16

# Generate the sine wave
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
sine_wave = np.sin(2 * np.pi * frequency * t)

# Normalize to 16-bit PCM
sine_wave_normalized = (sine_wave * 32767).astype(np.int16)

output_dir = 'audio_wav'

# Save as WAV using wave module
output_file = os.path.join(output_dir, f"{wav_type}_{str(bit_type)}bit_{str(sample_rate)}_{str(duration)}s_{str(frequency)}hz.wav")

# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

with wave.open(output_file, 'w') as wav_file:
    wav_file.setnchannels(1)  # Mono
    wav_file.setsampwidth(2)  # 2 bytes per sample (16-bit)
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(sine_wave_normalized.tobytes())

print(f"Sine wave file '{output_file}' created successfully!")
