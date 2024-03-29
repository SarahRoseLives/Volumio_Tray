# Volumio Skip Tray App

## Overview

This repository contains a simple system tray application for controlling Volumio music playback. Volumio is a popular open-source music player for Raspberry Pi and other single-board computers. The tray app allows users to easily skip to the next song, play/pause the current song, and play the previous song directly from the system tray.

## Features

- **Skip to Next Song:** Easily move to the next track in your playlist.
- **Play/Pause:** Toggle play and pause for the currently playing song.
- **Play Previous Song:** Move to the previous track in your playlist.
- **Settings:** Configure the Volumio server URL and save it for future use.

## Requirements

- Python 3.x
- Dependencies (listed in `requirements.txt`)
- Compatible with Volumio instances accessible over the network

## Getting Started

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/volumio-skip-tray.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the tray app:

    ```bash
    python volumio_tray.py
    ```

4. Access the system tray icon to control your Volumio music playback.

## Configuration

To configure the Volumio server URL, access the "Settings" option from the system tray icon. Enter the URL, and the app will save it for future use.

## License

This project is placed in the public domain through the [Unlicense](LICENSE).

---

