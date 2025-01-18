import sounddevice as sd
from scipy.io.wavfile import write
import wavio

def record_audio(file_name, duration=5, freq=44100, channels=2):
    """
    Record audio and save it to a file.

    Parameters:
    - file_name: Base name for the audio files (str).
    - duration: Duration of the recording in seconds (int).
    - freq: Sampling frequency in Hz (int).
    - channels: Number of audio channels (int).
    """
    try:
        print(f"Recording for {duration} seconds...")
        # Start recording
        audio_data = sd.rec(int(duration * freq), samplerate=freq, channels=channels)
        sd.wait()  # Wait until recording is finished

        # Save the recording in WAV format using scipy
        wav_file_name = f"{file_name}_scipy.wav"
        write(wav_file_name, freq, audio_data)
        print(f"Recording saved as {wav_file_name} using scipy.")

        # Save the recording in WAV format using wavio
        wavio_file_name = f"{file_name}_wavio.wav"
        wavio.write(wavio_file_name, audio_data, freq, sampwidth=2)
        print(f"Recording saved as {wavio_file_name} using wavio.")

    except Exception as e:
        print(f"An error occurred while recording audio: {e}")

if __name__ == "__main__":
    # Default parameters for recording
    base_file_name = "recording"
    record_duration = 5  # seconds
    sampling_frequency = 44100  # Hz

    # Call the function to record audio
    record_audio(base_file_name, duration=record_duration, freq=sampling_frequency)
