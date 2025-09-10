# Car Counter CV

<img width="1284" height="753" alt="image" src="https://github.com/user-attachments/assets/02764988-d646-4821-9bd5-68b8abf6e94b" />


## About the Project

**Car Counter CV** is a Python-based computer vision application that automatically detects and counts cars in video streams. It is designed for traffic analysis, smart city applications, parking lot management, and educational demonstrations. The tool leverages OpenCV and custom tracking modules to provide accurate, real-time vehicle counting from both video files and live camera feeds.

When you run the car counter, it processes each frame of your video or webcam stream, detects all visible cars, tracks their movement across frames, and counts each unique car as it crosses a virtual counting line or region. The application overlays bounding boxes, tracking IDs, and live car counts directly onto the video, giving you immediate visual feedback and statistics. This makes it ideal for monitoring traffic flow, collecting data for research, or showcasing computer vision techniques in action.

### What Does It Do?
- **Reads video input** from a file or webcam.
- **Detects cars** in each frame using advanced image processing and object detection techniques.
- **Tracks each vehicle** as it moves through the scene, assigning a unique ID to every car.
- **Counts cars** as they cross a user-defined virtual line or region, ensuring each car is only counted once (no double-counting).
- **Displays results** by overlaying bounding boxes, tracking paths, and live car counts on the video output.
- **Provides live statistics** for traffic monitoring, research, or educational use.

This project is modular and easy to extend, making it suitable for:
- Traffic flow analysis
- Parking lot management
- Smart city research
- Educational demonstrations of computer vision techniques

### How it Works
1. **Video Input:** The program loads a video file or connects to a webcam stream.
2. **Car Detection:** Each frame is analyzed to detect cars using object detection algorithms.
3. **Object Tracking:** Detected cars are tracked across frames, so the same car keeps its ID as it moves.
4. **Counting Logic:** A virtual line or region is defined in the frame. When a tracked car crosses this line, the counter increases by one.
5. **Visualization:** The output video shows bounding boxes, tracking IDs, and the current car count, making it easy to see the system working in real time.

## Features

- 🚗 **Real-time car detection and counting**
- 🎥 Works with video files or live webcam streams
- 🧩 Modular codebase for easy customization and extension
- 🏁 Virtual counting lines or regions
- 📦 Example video assets included for quick testing
- 📝 Well-commented code for learning and adaptation

## Project Structure

```
cv_lib/
  apps/
    car_counter.py         # Main script to run car counting
    ...
  modules/
    ...                    # Core reusable modules (tracking, drawing, etc.)
  assets/
    demo_video/            # Example videos for testing
    images/                # Place for screenshots or demo images
    ...
  ml/
    ...                    # Machine learning assets (if needed)
  ...
```

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/car-counter-cv.git
cd car-counter-cv
```

### 2. Install Dependencies

Make sure you have Python 3.7+ installed.  
Install required packages (example using pip):

```sh
pip install opencv-python numpy
```

*(Add any other dependencies your project uses.)*

### 3. Run the Car Counter

To run the car counter on a demo video:

```sh
python -m apps.car_counter --mirror 0
```

- You can modify the script to use your own video files or webcam.
- Example videos are available in `assets/demo_video/`.

### 4. Project Customization

- The main logic is in the `modules` directory.  
- You can extend the functionality by modifying or adding modules.

## Example Usage

```sh
python -m apps.car_counter --mirror 0
```

## Contributing

Contributions are welcome! Please open issues or pull requests for suggestions and improvements.

## License

MIT License

## Acknowledgments

- Built with OpenCV and Python
- Example videos from open datasets

---

*For more details, see the code and comments in each file.*
