import os
import sys
import time
import threading
from PIL import Image
import pystray
from pystray import MenuItem as item, Icon
import requests
import tkinter as tk
from tkinter import simpledialog

# Global variable to store Volumio URL
volumio_url = "http://volumio.local"

# Function to skip to the next song
def skip_to_next_song(icon, item):
    perform_volumio_action("next", "Successfully skipped to the next song.")

# Function to play the previous song
def play_previous_song(icon, item):
    perform_volumio_action("prev", "")
    perform_volumio_action("prev", "Successfully played the previous song.")

# Function to play/pause the current song
def play_pause(icon, item):
    perform_volumio_action("toggle", "Successfully toggled play/pause.")

# Function to perform Volumio actions (next, prev, toggle)
def perform_volumio_action(action, success_message):
    try:
        # Replace 'http://volumio.local' with the actual IP or hostname of your Volumio instance
        volumio_api_url = volumio_url
        # Define the endpoint for the Volumio action
        endpoint = f"/api/v1/commands/?cmd={action}"

        # Construct the full API URL
        full_url = volumio_api_url + endpoint

        # Send a GET request to perform the Volumio action
        response = requests.get(full_url)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            print(success_message)
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Function to update the Volumio URL and save it to a file
def update_volumio_url(icon, item):
    global volumio_url
    new_url = ask_for_volumio_url(icon)

    if new_url:
        volumio_url = new_url
        save_volumio_url_to_file(new_url)

# Function to open a settings window and get a new Volumio URL
def ask_for_volumio_url(icon):
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Create a Toplevel window for settings
    settings_window = tk.Toplevel(root)

    # Set the window title
    settings_window.title("Volumio Settings")

    # Create and pack the label
    label = tk.Label(settings_window, text="Enter the Volumio URL:")
    label.pack(padx=10, pady=10)

    # Create and pack the entry widget
    entry = tk.Entry(settings_window)
    entry.insert(0, volumio_url)
    entry.pack(padx=10, pady=10)

    # Create and pack the OK button
    ok_button = tk.Button(settings_window, text="OK", command=lambda: set_new_url(entry.get(), settings_window))
    ok_button.pack(pady=10)

    # Run the window's main loop
    root.mainloop()

# Function to set the new Volumio URL and close the settings window
def set_new_url(new_url, settings_window):
    global volumio_url
    if new_url:
        volumio_url = new_url
        save_volumio_url_to_file(new_url)
    settings_window.destroy()

# Function to save the Volumio URL to a file
def save_volumio_url_to_file(new_url):
    with open("volumio_url.txt", "w") as file:
        file.write(new_url)

# Function to read the Volumio URL from a file
def read_volumio_url_from_file():
    try:
        with open("volumio_url.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

# Function to create the system tray icon
def create_tray_icon():
    image = Image.open("icon.png")  # Replace with the path to your icon image

    # Create menu items
    menu = (
        item('Previous Song', play_previous_song),
        item('Play/Pause', play_pause),
        item('Skip to Next Song', skip_to_next_song),
        item('Settings', update_volumio_url),
        item('Quit', lambda icon, item: icon.stop())
    )

    # Create system tray icon
    icon = Icon("name", image, menu=menu)
    return icon

# Create and run the system tray icon
def main():
    global volumio_url
    # Read the Volumio URL from the file
    saved_url = read_volumio_url_from_file()
    if saved_url:
        volumio_url = saved_url

    icon = create_tray_icon()
    icon.run()

if __name__ == "__main__":
    # Run the application in a separate thread to avoid blocking the main thread
    app_thread = threading.Thread(target=main)
    app_thread.start()

    # Main loop to keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Handle Ctrl+C to gracefully exit
        sys.exit(0)
