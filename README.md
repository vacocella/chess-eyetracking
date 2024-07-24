# Chess Eye Tracking App

## Overview

Welcome to the Chess Eye Tracking App! This Python application allows you to play chess on Chess.com using only your eyes. By tracking your eye movements and detecting blinks, the app enables you to make moves effortlessly. Whether you have mobility impairments or simply want to experience a new way of playing chess, this app is designed to provide a seamless and engaging experience.

## Features

- **Eye Tracking**: Track your eye movements to navigate the chessboard.
- **Blink Detection**: Blink to select and move pieces.
- **Chess.com Integration**: Play directly on Chess.com.
- **User-Friendly Interface**: Intuitive and easy-to-use controls.
- **Customizable Settings**: Adjust sensitivity and other parameters to suit your preferences.

## Requirements

- Python 3.7+
- Virtual environment (venv)
- Dependencies listed in `requirements.txt`
- Webcam for eye tracking
- Chess.com account

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/chess-eye-tracking-app.git
    cd chess-eye-tracking-app
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Setup your Chess.com credentials:**

    Edit the `config.json` file and add your Chess.com username and password.

    ```json
    {
      "chess_com_username": "your_username",
      "chess_com_password": "your_password"
    }
    ```

2. **Adjust eye tracking and blink detection settings:**

    Edit the `settings.json` file to customize sensitivity and other parameters.

    ```json
    {
      "eye_tracking_sensitivity": 0.5,
      "blink_detection_threshold": 0.2
    }
    ```

## Usage

1. **Run the application:**

    ```bash
    python main.py
    ```

2. **Follow the on-screen instructions:**

    - Ensure your face is clearly visible to the webcam.
    - Calibrate the eye tracker by looking at specific points on the screen.
    - Start a game on Chess.com and use your eyes to navigate the board.
    - Blink to select pieces and make moves.

## Troubleshooting

- **Calibration Issues**: If the eye tracker is not accurately following your gaze, try recalibrating in a well-lit environment.
- **Blink Detection Sensitivity**: If blinks are not being detected correctly, adjust the `blink_detection_threshold` in `settings.json`.
- **Performance**: Ensure your system meets the minimum requirements and that no other intensive applications are running simultaneously.

