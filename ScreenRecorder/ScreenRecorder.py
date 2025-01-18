import pyautogui
import cv2
import numpy as np

def record_screen(output_file="Recording.avi", resolution=(1920, 1080), fps=30.0):
    """
    Records the screen and saves it as a video file.

    Parameters:
    - output_file: Name of the output video file (str).
    - resolution: Screen resolution (tuple of width and height).
    - fps: Frames per second for the video (float).
    """
    # Define video codec and create VideoWriter object
    codec = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_file, codec, fps, resolution)

    # Create a resizable display window
    cv2.namedWindow("Screen Recorder", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Screen Recorder", 480, 270)

    print("Recording... Press 'q' to stop.")
    try:
        while True:
            # Capture a screenshot
            screenshot = pyautogui.screenshot()

            # Convert screenshot to a NumPy array
            frame = np.array(screenshot)

            # Convert from RGB to BGR for OpenCV compatibility
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # Write the frame to the video file
            out.write(frame)

            # Display the current recording
            cv2.imshow("Screen Recorder", frame)

            # Stop recording if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Recording stopped.")
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Release resources
        out.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Customize the output file name, resolution, and FPS as needed
    record_screen(output_file="ScreenRecording.avi", resolution=(1280, 720), fps=60.0)
