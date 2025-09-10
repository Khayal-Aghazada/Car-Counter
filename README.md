# Car Counter CV

A Python-based computer vision application for counting cars in video streams using modular, reusable components.

## Overview

This project provides a robust car counting tool built with OpenCV and custom tracking modules. The main script, `apps/car_counter.py`, leverages reusable code from the `modules` directory, making it easy to extend or adapt for other object counting tasks.

## Features

- Real-time car detection and counting from video files or webcam streams
- Modular codebase for easy customization and extension
- Example video assets included for quick testing
- Designed for clarity and educational use

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
