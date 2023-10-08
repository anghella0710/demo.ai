import cv2
import numpy as np
from keras.models import load_model

# Load pretrained model
model = load_model('model.h5')

# Define class names for each class ID
classes = {0: 'Speed limit (20km/h)', 
           1: 'Speed limit (30km/h)', 
           2: 'Speed limit (50km/h)', 
           3: 'Speed limit (60km/h)', 
           4: 'Speed limit (70km/h)', 
           5: 'Speed limit (80km/h)', 
           6: 'End of speed limit (80km/h)', 
           7: 'Speed limit (100km/h)', 
           8: 'Speed limit (120km/h)', 
           9: 'No passing', 
           10: 'No passing veh over3.5 tons', 
           11: 'Right-of-way at intersection', 
           12: 'Priority road', 
           13: 'Yield', 
           14: 'Stop', 
           15: 'No vehicles', 
           16: 'Veh > 3.5 tons prohibited', 
           17: 'No entry', 
           18: 'General caution', 
           19: 'Dangerous curve left', 
           20: 'Dangerous curve right', 
           21: 'Double curve', 
           22: 'Bumpy road', 
           23: 'Slippery road', 
           24: 'Road narrows on the right', 
           25: 'Road work', 
           26: 'Traffic signals', 
           27: 'Pedestrians', 
           28: 'Children crossing', 
           29: 'Bicycles crossing', 
           30: 'Beware of ice/snow', 
           31: 'Wild animals crossing', 
           32: 'End speed + passing limits', 
           33: 'Turn right ahead', 
           34: 'Turn left ahead', 
           35: 'Ahead only', 
           36: 'Go straight or right', 
           37: 'Go straight or left', 
           38: 'Keep right', 
           39: 'Keep left', 
           40: 'Roundabout mandatory', 
           41: 'End of no passing', 
           42: 'End no passing veh > 3.5 tons'}

# Set up camera capture
cap = cv2.VideoCapture(0)

while True:
    # Capture image from camera
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess image for object detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    if len(contours) > 0:
        # Find the largest object among the detected objects
        areas = [cv2.contourArea(c) for c in contours]
        max_index = np.argmax(areas)
        cnt = contours[max_index]

        # If the largest object's area is above a threshold
        if areas[max_index] > 1200:
            # Draw bounding box around the detected object
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Extract the region of interest and resize it to the required size
            sign_frame = frame[y: y + h, x: x + w]
            sign_frame = cv2.resize(sign_frame, (30, 30))
            sign_frame = np.expand_dims(sign_frame, axis=0)

            # Predict the class of the detected object
            pred = model.predict(sign_frame)
            pred_class = np.argmax(pred, axis=1)[0]
            sign = classes[pred_class]

            # Draw the predicted class name on the image
            cv2.putText(frame, sign, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

 # Display the result
    cv2.imshow("Traffic sign classification", frame)

    # Exit when the close button 'X' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty("Traffic sign classification", cv2.WND_PROP_VISIBLE) <1:
        break

# Cleanup and release resources
cap.release()
cv2.destroyAllWindows()
