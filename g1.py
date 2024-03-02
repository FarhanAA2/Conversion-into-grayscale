import cv2

# Open the video file
video_capture = cv2.VideoCapture('C://Users//Asus//Downloads//1705951007967.mp4')

# Get the width and height of the video
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter('output_video_grayscale.avi', fourcc, 30.0, (frame_width, frame_height), isColor=False)

# Process each frame of the video
while video_capture.isOpened():
    ret, frame = video_capture.read()

    if not ret:
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Write the grayscale frame to the output video
    output_video.write(gray_frame)

    cv2.imshow('Grayscale Video', gray_frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything when done
video_capture.release()
output_video.release()
cv2.destroyAllWindows()
