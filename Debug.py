import numpy as np
import wave
import os

# Parameters
sample_rate = 44100  # Samples per second
duration = 10  # Duration in seconds
frequency = 5000  # Frequency in Hz

# Generate the sine wave
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
sine_wave = np.sin(2 * np.pi * frequency * t)

# Normalize to 16-bit PCM
sine_wave_normalized = (sine_wave * 32767).astype(np.int16)

# Save as WAV using wave module
output_file = f"sine_wave_{frequency}hz_{duration}s.wav"

output_dir = "Audio_Input"
output_file_full_path = os.path.join(output_dir, output_file)

# Ensure the Audio_Input folder exists
os.makedirs(output_dir, exist_ok=True)
with wave.open(output_file_full_path, 'w') as wav_file:
    wav_file.setnchannels(1)  # Mono
    wav_file.setsampwidth(2)  # 2 bytes per sample (16-bit)
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(sine_wave_normalized.tobytes())


