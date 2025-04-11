# 🎯 Multi-Color and Object Detection System

This project is a Python-based computer vision system that uses OpenCV to detect multiple colors and objects in real-time from a webcam or video input. The system highlights detected objects and their corresponding colors, making it useful for robotics, automation, and visual tracking applications.

## 🧠 Features

- Real-time video capture using webcam
- Detection of multiple object colors (e.g., red, green, blue, yellow)
- Shape and contour detection
- Object bounding boxes with labels
- Adjustable color ranges using HSV
- Easy-to-modify code for adding new colors

## 📸 Demo

> 📷 Add a screenshot or GIF here (optional)

## 🧰 Technologies Used

- Python 3
- OpenCV
- NumPy

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Waser-Al-Karim/Multi-Color-and-Object-Detection-System.git
   cd Multi-Color-and-Object-Detection-System
   ```
1. **Install dependencies**
    
    ```bash
    pip install opencv-python numpy
    
    ```
    
2. **Run the script**
    
    ```bash
    python color_detection.py
    ```
    

> 💡 Make sure your webcam is connected and accessible.
> 

## 🛠 How It Works

- The system uses HSV (Hue, Saturation, Value) color space to filter specific color ranges.
- Contours are detected around the filtered areas to identify objects.
- Bounding boxes and labels are drawn on the live video feed for each detected object.

## 🧪 Color Range Settings

You can edit the HSV range values inside the script to add or modify colors:

```python
python
# Example HSV range for red
lower_red = np.array([161, 155, 84])
upper_red = np.array([179, 255, 255])

```

## 📁 File Structure

```
bash
├── color_detection.py   # Main script for detection
├── README.md            # Project documentation
└── requirements.txt     # (optional) List of dependencies

```

## 🚀 Future Improvements

- Integrate YOLO or other deep learning models for more accurate object detection
- Add a GUI interface to change color thresholds
- Enable video file input in addition to live webcam

## 🤝 Contributing

Pull requests and suggestions are welcome! Feel free to fork this repo and improve it.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
