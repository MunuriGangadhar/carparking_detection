# Car Parking Space Detection Project

This project implements a car parking space detection system using OpenCV and cvzone. It allows users to manually mark parking spaces on a static image and detect the occupancy of these spaces in another static image.

---

## 📑 Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Mark Parking Spaces](#mark-parking-spaces)
  - [Detect Parking Space Occupancy](#detect-parking-space-occupancy)
- [Files](#files)
- [Troubleshooting](#troubleshooting)

---

## 📌 Overview

The project consists of two main scripts:

- **`ParkingSpacePicker.py`**: A script to manually select parking space coordinates on a static image (`carpark2.jpeg`). Users can left-click to mark parking spaces and right-click to remove them. The coordinates are saved in a `CarParkPos` file using `pickle`.

- **`main.py`**: A script that reads the saved parking space coordinates and processes a static image (`output2.png`) to detect parking space occupancy. It displays the image with marked parking spaces, slot numbers, and a count of free spaces.

---

## ✅ Prerequisites

- Python 3.6 or higher
- Required Python libraries:
  - `opencv-python`
  - `numpy`
  - `cvzone`
- Input files:
  - `carpark2.jpeg` (for marking spaces)
  - `output2.png` (for occupancy detection)

---

## 🔧 Installation



1. Install the required dependencies:

   ```bash
   pip install opencv-python-headless numpy cvzone
   ```

2. Ensure the following files are present in the directory:

   * `carpark2.jpeg`
   * `output2.png`
   * `ParkingSpacePicker.py`
   * `main.py`

---

## ▶️ Usage

### 🅿️ Mark Parking Spaces

Run `ParkingSpacePicker.py` to mark parking spaces on the image:

```bash
python ParkingSpacePicker.py
```

* **Left-click** to add a parking space.
* **Right-click** inside a marked space to remove it.
* The coordinates are saved to the file `CarParkPos` automatically.
* Close the window to exit.

### 🚗 Detect Parking Space Occupancy

Run `main.py` to process `output2.png` and detect occupancy:

```bash
python main.py
```

* The script will display the image with:

  * Parking spaces marked as **green (free)** or **red (occupied)**
  * Slot numbers and pixel counts
  * Summary of **free spaces and their slot numbers** at the top
* Press any key to close the window

---

## 📁 Files

* `carpark2.jpeg` – Static image of the parking lot for marking spaces
* `output2.png` – Static image for detecting occupancy
* `ParkingSpacePicker.py` – Script to select and save parking space coordinates
* `main.py` – Script to detect parking space occupancy
* `CarParkPos` – Pickle file storing saved parking space coordinates (generated)

---

## ❗ Troubleshooting

### File Not Found Errors

* Ensure `carpark2.jpeg` and `output2.png` are in the same directory as the scripts
* Ensure `CarParkPos` is generated after running `ParkingSpacePicker.py`

### Incorrect Occupancy Detection

* Adjust the threshold (`count < 900`) in `main.py` if slots are misclassified
* Check pixel counts displayed on image to help determine a better threshold
* Ensure `output2.png` is consistent with `carpark2.jpeg` (same angle/lighting)

### Slot Numbering Issues

* Ensure parking slots in `CarParkPos` follow a consistent order (left-to-right, top-to-bottom)
* Re-run `ParkingSpacePicker.py` if needed to correct slot coordinates

### Dependency Issues

* Reinstall libraries if import errors occur:

  ```bash
  pip install --force-reinstall cvzone
  ```

