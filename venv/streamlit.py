import numpy as np
import cv2
import streamlit as st

def main():
    st.title("Multiple Color Detection in Real-Time")

    # Create a VideoCapture object for the webcam
    webcam = cv2.VideoCapture(0)

    while st.checkbox("Detect Colors", value=False):
        # Reading the video from the webcam in image frames
        _, imageFrame = webcam.read()

        # Convert the imageFrame to HSV color space
        hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

        # Define color ranges and masks
        red_lower = np.array([136, 87, 111], np.uint8)
        red_upper = np.array([180, 255, 255], np.uint8)
        red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

        green_lower = np.array([25, 52, 72], np.uint8)
        green_upper = np.array([102, 255, 255], np.uint8)
        green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

        blue_lower = np.array([94, 80, 2], np.uint8)
        blue_upper = np.array([120, 255, 255], np.uint8)
        blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

        # Morphological Transform, Dilation
        kernel = np.ones((5, 5), "uint8")

        # For red color
        red_mask = cv2.dilate(red_mask, kernel)
        res_red = cv2.bitwise_and(imageFrame, imageFrame, mask=red_mask)

        # For green color
        green_mask = cv2.dilate(green_mask, kernel)
        res_green = cv2.bitwise_and(imageFrame, imageFrame, mask=green_mask)

        # For blue color
        blue_mask = cv2.dilate(blue_mask, kernel)
        res_blue = cv2.bitwise_and(imageFrame, imageFrame, mask=blue_mask)

        # Creating contour to track colors
        detect_color(imageFrame, red_mask, "Red Colour", (0, 0, 255))
        detect_color(imageFrame, green_mask, "Green Colour", (0, 255, 0))
        detect_color(imageFrame, blue_mask, "Blue Colour", (255, 0, 0))

        # Display the image with detected colors
        st.image(imageFrame, channels="BGR", use_column_width=True)

def detect_color(imageFrame, color_mask, color_text, color_code):
    contours, hierarchy = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), color_code, 2)
            cv2.putText(imageFrame, color_text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color_code)

if __name__ == "__main__":
    main()
