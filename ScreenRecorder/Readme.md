# Screen Recorder Script

A Python script to record the screen and save it as a video file. This tool is designed to be flexible, user-friendly, and efficient, with customizable parameters such as resolution and frame rate.

## Features

- **Customizable Output**: Choose the resolution, frame rate, and output file name.
- **Live Preview**: Displays the recording in a resizable preview window.
- **Simple Controls**: Press 'q' to stop recording at any time.
- **Error Handling**: Ensures resources are released even if an error occurs.

## Requirements

- Python 3.8 or higher
- Required libraries:
  - `pyautogui`
  - `cv2` (OpenCV)
  - `numpy`

## Usage

1. Run the script:
   ```bash
   python screen_recorder.py
   ```
2. Customize the parameters in the `record_screen` function or directly in the script:
   - `output_file`: Name of the output video file (default: `ScreenRecording.avi`).
   - `resolution`: Resolution of the recording (default: `(1280, 720)`).
   - `fps`: Frames per second (default: `60.0`).

3. While the script is running:
   - A preview window will display the recording in real time.
   - Press 'q' to stop recording.

## Example

To record a 1280x720 screen at 60 FPS:
```python
record_screen(output_file="MyRecording.avi", resolution=(1280, 720), fps=60.0)
```

## Output

The script generates a video file in AVI format, saved with the specified file name. For example:
```
ScreenRecording.avi
```

## Troubleshooting

- **Script crashes or freezes**: Ensure your Python environment and dependencies are correctly installed.
- **Incorrect resolution**: Make sure the resolution matches your screen size.
- **Performance issues**: Lower the frame rate or resolution if the recording lags.

## Author

- **Adnan Sattar**  
  [GitHub Profile](https://github.com/AdnanSattar)

Feel free to fork and customize this project for your needs!
