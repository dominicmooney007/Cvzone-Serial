# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CVZone is a computer vision library that simplifies image processing and AI functions. It wraps [OpenCV](https://github.com/opencv/opencv) and [MediaPipe](https://github.com/google/mediapipe) to provide easy-to-use interfaces for common computer vision tasks.

This appears to be a customized version with added Serial communication capabilities for Arduino integration.

## Dependencies

**Core dependencies** (listed in [setup.py](setup.py)):
- `opencv-python` - Computer vision operations
- `numpy` - Array/matrix operations

**Additional dependencies** (required by various modules but not in setup.py):
- `mediapipe` - AI-powered face, hand, pose detection
- `pyserial` - Serial communication with Arduino
- `tensorflow` - Image classification

**Python version**: 3.6 or higher

## Installation

**From PyPI** (official package):
```bash
pip install cvzone
```

**Local development** (this repository):
```bash
pip install -e .
# Or install dependencies manually:
pip install opencv-python numpy mediapipe pyserial tensorflow
```

**Note**: The [setup.py](setup.py) file is missing mediapipe, pyserial, and tensorflow from `install_requires`. These must be installed separately for full functionality.

## Repository Structure

```
cvzone/
├── __init__.py              # Exports utility functions
├── Utils.py                 # Core utility functions (stackImages, cornerRect, etc.)
├── ClassificationModule.py  # Keras-based image classification
├── ColorModule.py           # HSV-based color detection
├── FaceDetectionModule.py   # MediaPipe face detection
├── FaceMeshModule.py        # 468 facial landmarks detection
├── HandTrackingModule.py    # Hand landmarks and gesture detection
├── PoseModule.py            # Body pose estimation
├── SelfiSegmentationModule.py # Background removal/segmentation
├── SerialModule.py          # Arduino serial communication
├── FPS.py                   # FPS counter utility
├── PlotModule.py            # Live data plotting
└── PIDModule.py             # PID controller for tracking

Examples/                    # Example scripts for each module
Results/                     # Example images/outputs
docs/                        # Documentation
```

## Module Architecture

### Design Pattern
All AI detection modules follow a consistent pattern:
1. **Detector class** with configuration parameters in `__init__()`
2. **Primary detection method** (e.g., `findFaces()`, `findHands()`, `findPose()`)
3. **Helper methods** for distance, angles, or specific features
4. **Return format**: Usually returns modified image and detection data

### Core Utility Functions (Utils.py)
- `stackImages(imgList, cols, scale)` - Combine multiple images in grid layout
- `cornerRect(img, bbox, ...)` - Draw styled corner rectangles
- `putTextRect(img, text, pos, ...)` - Text with background rectangle
- `overlayPNG(imgBack, imgFront, pos)` - Overlay transparent PNG images
- `rotateImage(img, angle, scale, keepSize)` - Rotate images with options
- `findContours(img, imgPre, ...)` - Find and filter contours by area/corners
- `downloadImageFromUrl(url, keepTransparency)` - Download images from URLs

### MediaPipe-based Modules
All MediaPipe modules require **BGR to RGB conversion** internally (handled automatically):

**FaceMeshModule** - 468 facial landmarks
- `FaceMeshDetector(staticMode, maxFaces, minDetectionCon, minTrackCon)`
- `findFaceMesh(img, draw)` → returns `(img, faces)` where faces is list of 468 [x,y] points
- `findDistance(p1, p2, img)` → calculates distance between landmarks

**HandTrackingModule** - Hand detection and gesture recognition
- `HandDetector(staticMode, maxHands, modelComplexity, detectionCon, minTrackCon)`
- `findHands(img, draw, flipType)` → returns `(hands, img)` with landmark lists, bbox, center, type
- `fingersUp(hand)` → returns list of which fingers are extended [thumb, index, middle, ring, pinky]
- `findDistance(p1, p2, img, color, scale)` → distance between landmarks

**PoseModule** - Full body pose estimation (33 landmarks)
- `PoseDetector(staticMode, modelComplexity, smoothLandmarks, enableSegmentation, ...)`
- `findPose(img, draw)` → returns image with pose drawn
- `findPosition(img, draw, bboxWithHands)` → returns landmark list and bounding box
- `findAngle(p1, p2, p3, img, ...)` → calculates angle between three points
- `angleCheck(myAngle, targetAngle, offset)` → checks if angle is within range

**FaceDetectionModule** - Face bounding boxes with confidence
- `FaceDetector(minDetectionCon, modelSelection)` (0=short-range 2m, 1=full-range 5m)
- `findFaces(img, draw)` → returns `(img, bboxs)` with id, bbox, score, center

**SelfiSegmentationModule** - Background removal
- `SelfiSegmentation(model)` (0=general, 1=landscape/faster)
- `removeBG(img, imgBg, cutThreshold)` → returns image with background replaced

### Non-MediaPipe Modules

**ClassificationModule** - TensorFlow/Keras image classification
- `Classifier(modelPath, labelsPath)`
- `getPrediction(img, draw, pos, scale, color)` → returns predictions list and top index
- Expects 224x224 input, uses Teachable Machine format

**ColorModule** - HSV color detection
- `ColorFinder(trackBar)` - Optional OpenCV trackbars for HSV tuning
- `update(img, myColor)` → returns color-masked image and binary mask
- myColor is dict: `{'hmin': 0, 'smin': 0, 'vmin': 0, 'hmax': 179, 'smax': 255, 'vmax': 255}`

**SerialModule** - Arduino communication
- `SerialObject(portNo, baudRate, digits, max_retries)`
- `sendData(data)` → sends list of values formatted as `$<val1><val2>...`
- `getData()` → receives data split by '#' delimiter
- Auto-detects Arduino if portNo=None

**FPS** - Frame rate counter
- `FPS(avgCount)` - avgCount for smoothing
- `update(img, pos, bgColor, textColor, scale, thickness)` → returns fps value and annotated image

**PlotModule** - Live plotting
- `LivePlot(w, yLimit, interval)`
- `update(val)` → returns plot image with new value added

**PIDModule** - PID controller for tracking
- `PID(pidVals, targetVal, axis, limit)` - pidVals=[P, I, D] coefficients
- `update(cVal)` → returns correction value
- `draw(img, cVal)` → visualizes target line and current position

## Common Development Tasks

**Run example scripts**:
```bash
python Examples/HandTrackingExample.py
python Examples/FaceMeshExample.py
python Examples/SerialModuleExample.py
# etc.
```

**Test a specific module**:
```bash
# Most modules have __main__ blocks for testing
python -m cvzone.HandTrackingModule
python -m cvzone.FaceMeshModule
python -m cvzone.ColorModule
```

**Install package locally**:
```bash
python setup.py install
# Or for development:
python setup.py develop
```

## Important Implementation Notes

### Webcam Index Convention
Throughout the codebase, examples use different camera indices:
- `cv2.VideoCapture(0)` - Built-in/default webcam
- `cv2.VideoCapture(2)` - Third camera (commonly used in examples)
- Adjust index based on your system configuration

### Image Format
- OpenCV uses **BGR** color format by default
- MediaPipe requires **RGB** (conversions handled internally by modules)
- When using custom OpenCV operations, remember the color space

### MediaPipe Model Paths
MediaPipe downloads models automatically on first use. Ensure internet connection for initial runs.

### Serial Communication Format
The [SerialModule.py](cvzone/SerialModule.py) uses a specific protocol:
- **Python to Arduino**: `$<digit1><digit2>...` (prefix with $, zero-padded based on `digits` param)
- **Arduino to Python**: `<val1>#<val2>#...` (values separated by #)
- See Arduino example code in [SerialModule.py](cvzone/SerialModule.py:129-164)

### Classification Module Requirements
- Expects Keras model format (`.h5` file)
- Labels in separate `.txt` file (one per line)
- Input images resized to 224x224 and normalized to [-1, 1]
- Compatible with [Teachable Machine](https://teachablemachine.withgoogle.com/) exports

### Performance Considerations
- MediaPipe models have `staticMode` parameter:
  - `False` (default) - Faster, tracks across frames
  - `True` - Slower, runs full detection every frame (better for static images)
- Use `modelComplexity=0` for faster processing on lower-end hardware
- Adjust confidence thresholds (`minDetectionCon`, `minTrackCon`) based on your use case

## Package Maintenance Notes

The [setup.py](setup.py) file is incomplete:
- Missing `mediapipe` dependency (required by 5+ modules)
- Missing `pyserial` dependency (required by SerialModule)
- Missing `tensorflow` dependency (required by ClassificationModule)

If updating the package, add these to `install_requires` in [setup.py](setup.py:13).
