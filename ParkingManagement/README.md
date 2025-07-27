# Smart Parking Management System

This project implements a real-time system to monitor parking lot occupancy using computer vision. It leverages a fine-tuned YOLOv8 model to detect vehicles and maps them to predefined parking spaces to determine if they are occupied or available.


*(Replace the link above with a GIF or image of your final output video)*

## Table of Contents
- [Smart Parking Management System](#smart-parking-management-system)
  - [Table of Contents](#table-of-contents)
  - [Key Features](#key-features)
  - [Tech Stack](#tech-stack)
  - [File Descriptions](#file-descriptions)
  - [Installation and Usage](#installation-and-usage)
    - [Step 1: Setup](#step-1-setup)
    - [Step 2: Define Parking Spaces](#step-2-define-parking-spaces)
    - [Step 3: Train the Detection Model](#step-3-train-the-detection-model)
    - [Step 4: Run the Application](#step-4-run-the-application)
  - [Future Improvements](#future-improvements)

## Key Features
- **Vehicle Detection:** Utilizes a custom-trained YOLOv8 model to accurately detect vehicles.
- **Occupancy Monitoring:** Classifies each defined parking spot as "Occupied" or "Available".
- **Real-time Vacancy Count:** Displays a live counter of available parking spots.
- **Visual Output:** Generates a processed video file with color-coded parking spaces and vehicle detections.

## Tech Stack
- **Language:** Python
- **Core Libraries:** [PyTorch](https://pytorch.org/), [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics), OpenCV

## File Descriptions
Here is a breakdown of the key files in this project:

| File Name                         | Description                                                                                             |
| --------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `main.py`                         | The main script to run the parking management application. It processes the input video.                  |
| `slot_specification.py`           | A utility script to manually define parking space polygons by clicking on a template image.           |
| `video1_frame.jpg`                | A still frame extracted from the input video, used as a template for `slot_specification.py`.           |
| `bounding_boxes_1920x1080.json`   | The JSON file containing the coordinates of all predefined parking spaces, scaled for a 1920x1080 video. |
| `cars.yaml`                       | The dataset configuration file used by YOLO for training.                                               |
| `yolov8n.pt`                      | The pre-trained YOLOv8 Nano model, used as a base for fine-tuning.                                      |
| `runs/detect/train/weights/best.pt`| The final, fine-tuned model weights after training on the custom car dataset.                             |
| `datasets/`                       | Contains the training/validation images, labels, and the input video (`video1.mp4`).                    |
| `sam.py` & `sam2.1_b.pt`          | Experimental scripts and models for automated labeling using the Segment Anything Model (SAM).          |

## Installation and Usage

### Step 1: Setup
1.  **Clone the repository:**
    ```bash
    git clone https://your-repo-url.com/ParkingManagement.git
    cd ParkingManagement
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install ultralytics opencv-python
    ```

### Step 2: Define Parking Spaces
The system requires a map of all parking spots.
1.  Run the `slot_specification.py` script, using `video1_frame.jpg` as the input.
2.  Manually click the vertices of each parking spot polygon. Right-click to complete a spot.
3.  Save the output as `bounding_boxes.json`. If the frame and video resolutions differ, use a rescaling script to generate the final `bounding_boxes_1920x1080.json`.

### Step 3: Train the Detection Model
This step is best performed on a GPU-enabled platform like Kaggle or Google Colab.
1.  **Prepare Data:** Ensure your custom dataset of car images and labels is in the `datasets/` folder.
2.  **Configure:** Check that `cars.yaml` points to the correct train/validation paths.
3.  **Train:** Use fine-tuning for the best results.
    ```bash
    # Example training command
    yolo detect train data=cars.yaml model=yolov8n.pt epochs=150 imgsz=1920 batch=1
    ```
4. **Test:** After training the model, you can test it.
   ```bash
    # Example testing command
    yolo detect predict model=best.pt source=../datasets/video/video1.mp4
    ```
5.  **Get Model:** After training, copy the best model from `runs/detect/train/weights/best.pt` to the root directory of the project.

### Step 4: Run the Application
This is the final step to see the system in action.
1.  **Check Paths:** Open `main.py` and ensure the paths for the model, JSON file, and input video are correct.
    - Model: `best.pt`
    - JSON File: `bounding_boxes_1920x1080.json`
    - Input Video: `datasets/video/video1.mp4`
2.  **Execute the script:**
    ```bash
    python main.py
    ```
The script will process the video and save the output as `parking_management.avi` (or as specified in the code).

## Future Improvements
- Integrate with IP cameras for real-time stream processing.
- Develop a web-based dashboard (using Flask/Django) to display the parking status.
- Optimize the model (e.g., using TensorRT) for faster inference on edge devices.
- Expand the model to detect other vehicle types like motorcycles and trucks.