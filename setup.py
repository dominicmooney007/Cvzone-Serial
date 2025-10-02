from setuptools import setup

setup(
    name='cvzone',
    packages=['cvzone'],
    version='1.6',
    license='MIT',
    description='Computer Vision Helping Library',
    author='Computer Vision Zone',
    author_email='contact@computervision.zone',
    url='https://github.com/cvzone/cvzone.git',
    keywords=['ComputerVision', 'HandTracking', 'FaceTracking', 'PoseEstimation'],
    install_requires=[
        'opencv-python>=4.5.0',
        'numpy>=1.19.0,<2.0.0',
        'mediapipe>=0.10.0',
        'pyserial>=3.5',
        'tensorflow>=2.13.0',
    ],
    python_requires='>=3.8,<3.13',  # MediaPipe and TensorFlow support Python 3.8-3.12

    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
