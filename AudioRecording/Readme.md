# Audio Recording Script

This Python script records audio for a specified duration and saves the recording as WAV files using two libraries: `scipy` and `wavio`. It is designed to be simple, flexible, and user-friendly.

## Features

- **Customizable Parameters**: Record audio with adjustable duration, sampling frequency, and number of channels.
- **Multiple Output Formats**: Saves audio files in WAV format using both `scipy` and `wavio` libraries.
- **Error Handling**: Ensures smooth execution with proper error messages in case of issues.

## Requirements

- Python 3.8 or higher
- Required libraries:
  - `sounddevice`
  - `scipy`
  - `wavio`

## Usage

1. Run the script:
   ```bash
   python audio_recording.py
   ```
2. Modify the script parameters in the `record_audio` function or pass them as arguments to customize:
   - `file_name`: Base name for the output files.
   - `duration`: Duration of the recording in seconds.
   - `freq`: Sampling frequency in Hz.
   - `channels`: Number of audio channels.

3. The recordings will be saved in the following formats:
   - `{file_name}_scipy.wav`: WAV file saved using the `scipy` library.
   - `{file_name}_wavio.wav`: WAV file saved using the `wavio` library.

## Example

To record 5 seconds of audio with default parameters:
```
Recording for 5 seconds...
Recording saved as recording_scipy.wav using scipy.
Recording saved as recording_wavio.wav using wavio.
```

## Error Handling

If an error occurs during recording or file saving, the script will display a message with the details of the issue.

## Author

- **Adnan Sattar**
  [GitHub Profile](https://github.com/AdnanSattar)

Feel free to modify this script or use it as a starting point for your own projects!
