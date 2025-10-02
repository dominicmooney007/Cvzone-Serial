# CVZone Setup Guide

This guide will walk you through setting up CVZone on your system, from installation to running your first example.

## Prerequisites

Before you begin, ensure you have:
- **Python 3.8 - 3.12** installed on your system (for full functionality)
  - ⚠️ **Python 3.13+** is NOT yet supported by MediaPipe and TensorFlow
  - If you're on Python 3.13+, see the "Python 3.13+ Users" section below
- **pip** (Python package manager) installed
- A **webcam** (optional, for testing vision modules)
- An **Arduino** (optional, for testing serial communication)

### Check Your Python Version

```bash
python --version
# or
python3 --version
```

**IMPORTANT**: If you see Python 3.13 or higher, MediaPipe and TensorFlow modules will NOT work. You have two options:
1. Install Python 3.12 alongside your current version (recommended)
2. Use basic CVZone features only (see "Python 3.13+ Users" section below)

If Python is not installed, download **Python 3.12** from [python.org](https://www.python.org/downloads/).

---

## Step 1: Clone or Download the Repository

If you haven't already, clone this repository:

```bash
git clone <repository-url>
cd Cvzone-Serial
```

Or if you downloaded a ZIP file, extract it and navigate to the directory.

---

## Step 2: Create a Virtual Environment (Recommended)

Creating a virtual environment keeps your project dependencies isolated:

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` appear in your terminal prompt, indicating the virtual environment is active.

---

## Step 3: Install Dependencies

### For Python 3.8 - 3.12 (Full Installation)

Install all required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install:
- ✅ **opencv-python** - Core computer vision library
- ✅ **numpy** - Numerical computing
- ✅ **mediapipe** - Google's AI/ML solutions for face, hand, and pose detection
- ✅ **pyserial** - Serial communication for Arduino
- ✅ **tensorflow** - Deep learning framework for classification

### For Python 3.13+ (Basic Installation)

If you're on Python 3.13 or higher, use the basic requirements file:

```bash
pip install -r requirements-basic.txt
```

This installs only the compatible packages:
- ✅ **opencv-python** - Core computer vision library
- ✅ **numpy** - Numerical computing
- ✅ **pyserial** - Serial communication for Arduino

⚠️ **What won't work on Python 3.13+:**
- ❌ FaceMeshModule
- ❌ HandTrackingModule
- ❌ PoseModule
- ❌ FaceDetectionModule
- ❌ SelfiSegmentationModule
- ❌ ClassificationModule

✅ **What WILL work on Python 3.13+:**
- All utility functions (stackImages, cornerRect, putTextRect, etc.)
- FPS counter
- Plot module
- PID module
- Color detection
- Serial communication

### Installation Notes

**For Apple Silicon (M1/M2/M3) Macs with Python 3.8-3.12:**
If you encounter issues with TensorFlow, try:
```bash
pip install tensorflow-macos
pip install tensorflow-metal  # For GPU acceleration
```

**For systems without a display (servers):**
Use the headless version of OpenCV:
```bash
pip uninstall opencv-python
pip install opencv-python-headless
```

---

## Step 4: Install CVZone Package

Install CVZone in development mode so you can modify and test the code:

```bash
pip install -e .
```

Or for a standard installation:
```bash
python setup.py install
```

---

## Step 5: Verify Installation

Test that all modules are properly installed:

```bash
python -c "import cv2; import numpy; import mediapipe; import serial; import tensorflow; print('✅ All dependencies installed successfully!')"
```

If this command runs without errors, you're ready to go!

---

## Step 6: Run Your First Example

Let's test the installation with a simple example. Choose one based on what you want to try:

### Option A: Hand Tracking (Requires Webcam)

```bash
python Examples/HandTrackingExample.py
```

This will open your webcam and detect your hands in real-time, showing:
- Hand landmarks (21 points per hand)
- Bounding box around detected hands
- Hand type (Left/Right)
- Finger count

**Controls:** Press `Ctrl+C` in the terminal to exit.

### Option B: Face Detection (Requires Webcam)

```bash
python Examples/FaceDetectionExample.py
```

Detects faces with confidence scores and bounding boxes.

### Option C: Color Detection (Requires Webcam)

```bash
python Examples/ColorModuleExample.py
```

Use trackbars to adjust HSV values and detect specific colors in real-time.

### Option D: Stack Images Demo (Requires Webcam)

```bash
python Examples/StackImageExample.py
```

Shows multiple image processing results side-by-side.

### Option E: Test Without Webcam

If you don't have a webcam, test the utility functions:

```bash
python Examples/DownloadImageFromURL.py
```

---

## Step 7: Testing Serial Communication (Optional)

If you have an Arduino:

1. **Upload Arduino code** - See the Arduino example in [SerialModule.py](cvzone/SerialModule.py) lines 129-164
2. **Connect Arduino** via USB
3. **Run the Python example:**

```bash
python Examples/SerialModuleExample.py
```

The script will auto-detect your Arduino (looks for "Arduino" in device description).

---

## Troubleshooting

### "No module named 'cv2'"
```bash
pip install opencv-python
```

### "No module named 'mediapipe'"
```bash
pip install mediapipe
```

### Webcam not opening (Error with cv2.VideoCapture)
The examples use different camera indices. Try changing the camera index in the example file:
```python
# Change from:
cap = cv2.VideoCapture(2)
# To:
cap = cv2.VideoCapture(0)  # Try 0, 1, 2, etc.
```

### MediaPipe models downloading slowly
MediaPipe downloads AI models on first run. This is normal and only happens once. Ensure you have a stable internet connection.

### Permission denied errors on macOS
Grant camera permissions:
1. **System Preferences** → **Security & Privacy** → **Camera**
2. Enable camera access for **Terminal** or your IDE

### Serial port not found (Arduino)
- Ensure Arduino is connected via USB
- Check Arduino IDE can see the device
- Manually specify the port:
  ```python
  arduino = SerialObject(portNo="COM3", baudRate=9600)  # Windows
  arduino = SerialObject(portNo="/dev/ttyUSB0", baudRate=9600)  # Linux
  arduino = SerialObject(portNo="/dev/cu.usbmodem14201", baudRate=9600)  # macOS
  ```

---

## Next Steps

### Explore More Examples

All examples are in the `Examples/` directory:
- `FaceMeshExample.py` - 468 facial landmarks
- `PoseEstimationExample.py` - Full body tracking
- `ClassificationModuleExample.py` - Custom image classification
- `PlotModuleExample.py` - Live data plotting
- And more!

### Build Your Own Project

Check out the module documentation in [CLAUDE.md](CLAUDE.md) to understand:
- How each detector class works
- Available methods and parameters
- Return data formats
- Best practices

### Customize Detection Parameters

Most detectors accept configuration parameters:

```python
from cvzone.HandTrackingModule import HandDetector

# Adjust detection confidence and max hands
detector = HandDetector(
    maxHands=2,              # Detect up to 2 hands
    detectionCon=0.7,        # Higher = more strict detection
    minTrackCon=0.5          # Tracking confidence threshold
)
```

---

## Python 3.13+ Users: Installing Python 3.12

If you're on Python 3.13+ and want full CVZone functionality (MediaPipe, TensorFlow modules), install Python 3.12 alongside your current version.

### macOS (Using pyenv - Recommended)

```bash
# Install pyenv
brew install pyenv

# Install Python 3.12
pyenv install 3.12.0

# Set Python 3.12 for this project directory
cd /path/to/Cvzone-Serial
pyenv local 3.12.0

# Verify version
python --version  # Should show 3.12.0

# Now proceed with Step 2 (create virtual environment)
```

### macOS (Direct Download)

1. Download Python 3.12 from [python.org](https://www.python.org/downloads/release/python-3120/)
2. Install the package
3. Use `python3.12` instead of `python3` in commands:
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Windows (Using pyenv-win)

```bash
# Install pyenv-win
git clone https://github.com/pyenv-win/pyenv-win.git %USERPROFILE%\.pyenv

# Add to PATH, then:
pyenv install 3.12.0
pyenv local 3.12.0

# Verify
python --version
```

### Windows (Direct Download)

1. Download Python 3.12 from [python.org](https://www.python.org/downloads/release/python-3120/)
2. Install with "Add to PATH" checked
3. Use `py -3.12` in commands:
   ```bash
   py -3.12 -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Ubuntu/Debian Linux

```bash
# Add deadsnakes PPA
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update

# Install Python 3.12
sudo apt install python3.12 python3.12-venv

# Use python3.12 for this project
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Updating CVZone

To update to the latest version from this repository:

```bash
git pull origin main
pip install -r requirements.txt --upgrade
pip install -e . --upgrade
```

---

## Getting Help

- **Documentation**: See [CLAUDE.md](CLAUDE.md) for detailed module documentation
- **Examples**: All examples include detailed comments
- **CVZone Website**: [https://www.computervision.zone/](https://www.computervision.zone/)
- **OpenCV Docs**: [https://docs.opencv.org/](https://docs.opencv.org/)
- **MediaPipe Docs**: [https://google.github.io/mediapipe/](https://google.github.io/mediapipe/)

---

## Quick Reference

### Activate Virtual Environment
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Deactivate Virtual Environment
```bash
deactivate
```

### Reinstall All Dependencies
```bash
pip install -r requirements.txt --force-reinstall
```

### List Installed Packages
```bash
pip list
```

---

**You're all set! Happy coding with CVZone! 🎥🤖**
