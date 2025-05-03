# Face Detection Script

This Python script performs real-time face detection using OpenCV.

## Dependencies

* **OpenCV (cv2):** A library for computer vision tasks. You can install it using pip:

    ```bash
    pip install opencv-python
    ```

* **Haar Cascade XML file:** A pre-trained Haar Cascade classifier for face detection.  The script assumes you have `haarcascade_frontalface_default.xml` in the same directory. You might need to download this file from the OpenCV GitHub repository or other sources.

## Functionality

1.  **Loads Haar Cascade Classifier:**
    * Loads the pre-trained Haar Cascade classifier for frontal face detection (`haarcascade_frontalface_default.xml`). [cite: 1] This classifier is used to detect faces in an image.
2.  **Opens Video Stream:**
    * Opens the default camera video stream (camera index 0). You can change the index if you have multiple cameras. [cite: 1]
3.  **Reads Frames and Detects Faces:**
    * Continuously reads frames from the video stream. [cite: 1]
    * Converts each frame to grayscale, as face detection works on grayscale images for efficiency. [cite: 1]
    * Detects faces in the grayscale frame using `face_cascade.detectMultiScale()`. This function returns a list of rectangles, where each rectangle represents a detected face. [cite: 1]
4.  **Draws Rectangles Around Faces:**
    * Draws rectangles around the detected faces in the original color frame. [cite: 1]
5.  **Displays Frames:**
    * Displays the grayscale frame and the frame with the detected faces in separate windows. [cite: 1]
6.  **Exits on Key Press:**
    * Waits for the 'q' key to be pressed. When pressed, it releases the video stream and closes all OpenCV windows. [cite: 1]
7.  **Releases Resources:**
    * Releases the video capture object (`cap`) and destroys all windows. [cite: 1]

## Code Explanation

```python
import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open the video stream (replace 0 with the index of your camera device)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video streamQ
    ret, frame = cap.read()

    if ret:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Gray',gray);

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (40, 255, 125), 5)

        # Display the frame with detected faces
        cv2.imshow('Face Detection', frame)

        # Wait for a key press to exit
        if cv2.waitKey(1) == ord('q'):
            break

# Release the video stream and close all windows
cap.release()
cv2.destroyAllWindows()
