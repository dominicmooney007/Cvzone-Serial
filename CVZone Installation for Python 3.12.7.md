# Python 3.12.7 Setup Guide for CVZone

This guide walks you through setting up CVZone with Python 3.12.7 on macOS.

## Prerequisites

You should have **Python 3.12.7** installed on your system.

### Verify Python Installation

```bash
python3.12 --version
```

You should see: `Python 3.12.7`

If you don't have Python 3.12.7 installed:
1. Download from: https://www.python.org/downloads/release/python-3127/
2. Run the `.pkg` installer for macOS
3. Verify installation with the command above

---

## Step-by-Step Setup

### Step 1: Navigate to the Project Directory

```bash
cd /Users/dominicmooney/Documents/Cvzone-Serial
```

### Step 2: Create a Virtual Environment

This keeps your project dependencies isolated from other Python projects.

```bash
python3.12 -m venv venv
```

This creates a `venv` folder in your project directory.

### Step 3: Activate the Virtual Environment

```bash
source venv/bin/activate
```

Your terminal prompt should now show `(venv)` at the beginning, indicating the virtual environment is active.

**Important:** You need to activate the virtual environment every time you open a new terminal session to work on this project.

### Step 4: Upgrade pip

Ensure you have the latest version of pip:

```bash
pip install --upgrade pip
```

### Step 5: Install CVZone and All Dependencies

Use the `setup.py` file to install CVZone in editable mode along with all required dependencies:

```bash
pip install -e .
```

This single command will install:
- ✅ **opencv-python** (≥4.5.0) - Computer vision operations
- ✅ **numpy** (≥1.19.0, <2.0.0) - Array/matrix operations
- ✅ **mediapipe** (≥0.10.0) - AI-powered face, hand, pose detection
- ✅ **pyserial** (≥3.5) - Serial communication with Arduino
- ✅ **tensorflow** (≥2.13.0) - Image classification

The `-e` flag installs in "editable" mode, meaning changes to the source code are immediately available without reinstalling.

### Step 6: Verify Installation

Test that all modules are installed correctly:

```bash
python -c "import cv2, numpy, mediapipe, serial, tensorflow; print('✅ All modules imported successfully!')"
```

If you see the success message, your setup is complete!

### Step 7: Test with an Example

Try running an example to verify everything works:

```bash
python Examples/HandTrackingExample.py
```

Press `q` to quit the example when done.

---

## What's Available

With this setup, you have access to **all CVZone modules**:

### AI/MediaPipe Modules
- ✅ **FaceMeshModule** - 468 facial landmarks detection
- ✅ **HandTrackingModule** - Hand detection and gesture recognition
- ✅ **PoseModule** - Full body pose estimation (33 landmarks)
- ✅ **FaceDetectionModule** - Face bounding boxes with confidence
- ✅ **SelfiSegmentationModule** - Background removal/replacement

### Computer Vision Modules
- ✅ **ClassificationModule** - TensorFlow/Keras image classification
- ✅ **ColorModule** - HSV-based color detection

### Utility Modules
- ✅ **SerialModule** - Arduino serial communication
- ✅ **FPS** - Frame rate counter
- ✅ **PlotModule** - Live data plotting
- ✅ **PIDModule** - PID controller for tracking

### Utility Functions
- ✅ `stackImages()` - Combine multiple images in grid layout
- ✅ `cornerRect()` - Draw styled corner rectangles
- ✅ `putTextRect()` - Text with background rectangle
- ✅ `overlayPNG()` - Overlay transparent PNG images
- ✅ `rotateImage()` - Rotate images with options
- ✅ `findContours()` - Find and filter contours

---

## Available Examples

All examples should work with your setup:

```bash
# MediaPipe Examples
python Examples/HandTrackingExample.py
python Examples/FaceMeshExample.py
python Examples/PoseEstimationExample.py
python Examples/FaceDetectionExample.py
python Examples/SelfieSegmentationExample.py

# Computer Vision Examples
python Examples/ClassificationModuleExample.py
python Examples/ColorModuleExample.py

# Utility Examples
python Examples/SerialModuleExample.py
python Examples/FpsExample.py
python Examples/PlotModuleExample.py
python Examples/CornerRectangleExample.py
python Examples/PutTextRectExample.py
python Examples/StackImageExample.py
python Examples/RotateImageExample.py
python Examples/OverlayPNGExample.py
python Examples/FindCountrousExample.py
```

---

## Common Tasks

### Deactivate Virtual Environment

When you're done working on the project:

```bash
deactivate
```

### Reactivate Virtual Environment

Next time you work on the project:

```bash
cd /Users/dominicmooney/Documents/Cvzone-Serial
source venv/bin/activate
```

### Update Dependencies

If dependencies are updated in `setup.py`:

```bash
pip install -e . --upgrade
```

### Install Additional Packages

While the virtual environment is active:

```bash
pip install <package-name>
```

---

## Troubleshooting

### "No module named 'cv2'" or similar import errors

Make sure:
1. Virtual environment is activated: `source venv/bin/activate`
2. Dependencies are installed: `pip install -e .`

### "python: command not found"

Use `python3.12` explicitly:

```bash
python3.12 -m venv venv
```

### Camera not opening in examples

Examples use different camera indices. Try editing the example file:
- Change `cv2.VideoCapture(2)` to `cv2.VideoCapture(0)` for default webcam
- Or try other indices: 1, 2, 3, etc.

### MediaPipe or TensorFlow installation fails

Ensure you're using Python 3.12.7 (not 3.13+):

```bash
python --version  # Should show Python 3.12.7 when venv is active
```

If it shows a different version, recreate the virtual environment with `python3.12`.

---

## Quick Reference

**One-time setup:**
```bash
cd /Users/dominicmooney/Documents/Cvzone-Serial
python3.12 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -e .
```

**Daily workflow:**
```bash
cd /Users/dominicmooney/Documents/Cvzone-Serial
source venv/bin/activate
python Examples/HandTrackingExample.py  # or any other script
deactivate  # when done
```

**Verify everything works:**
```bash
python -c "import cv2, numpy, mediapipe, serial, tensorflow; print('✅ All modules imported successfully!')"
```

---

## Next Steps

- Explore the [Examples/](Examples/) folder for sample code
- Read [CLAUDE.md](CLAUDE.md) for detailed module documentation
- Check [SETUP.md](SETUP.md) for additional setup information
- Modify examples to build your own computer vision projects!
