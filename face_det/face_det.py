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
