# Synthesized Audio Software Suite

The Synthesized Audio Software Suite is a collection of interactive applications designed for audio manipulation and music creation, including Syn Music Synthesis Program (Syn MSP) and Syn Audio Manipulation Program (Syn AMP).

## Prerequisites

Before you start using the Synthesized Audio Software Suite, ensure you have the following prerequisites installed and configured on your system:

- **Python:** The software suite is developed in Python. Make sure you have Python 3.6 or newer installed. You can download it from [python.org](https://www.python.org/downloads/).

- **Pygame:** This library is used for managing audio playback and user interface elements. Install Pygame via pip:

  ```bash
  pip install pygame
  ```

- **FFMPEG:** Both Syn MSP and Syn AMP make use of FFMPEG for handling various audio formats and operations. You must have FFMPEG installed and its path added to your system's environment variables for the software suite to function correctly. Follow these steps to set up FFMPEG:

  1. Download FFMPEG from [ffmpeg.org](https://ffmpeg.org/download.html).
  2. Extract the downloaded archive to a location on your system (e.g., `C:\FFMPEG`).
  3. Add the bin directory (e.g., `C:\FFMPEG\bin`) to your system's PATH environment variable. This allows the software to access FFMPEG from the command line.
  4. Verify the installation by opening a command prompt or terminal and typing `ffmpeg`. If the installation was successful, you should see FFMPEG's version information and available commands.

### Overview

Syn MSP is a digital piano application that allows users to play and manipulate synthesized sounds using their computer keyboard. It provides a user-friendly interface for adding sound samples and playing them in real-time.

### Features

- **Dynamic Sound Assignment:** Users can add WAV or MP3 audio files to specific keys on the digital piano.
- **Real-time Playback:** Play sounds using the computer keyboard with support for simultaneous sounds.
- **3x5 Grid Layout:** Keys are arranged in a 3x5 grid, mimicking a numeric keypad layout for intuitive playability.
- **Import from Syn AMP:** Import manipulated audio directly from Syn AMP using an encrypted code system.

### Keybinds

- **Numeric and Letter Keys (1-0, Q-P, A-L, Z-M):** Play assigned sounds.
- **S Key:** Stops all currently playing sounds.
- **Import Button:** Import sounds manipulated in Syn AMP using an encrypted code.

## Syn Audio Manipulation Program (Syn AMP)

### Overview

Syn AMP is an audio editing tool designed for quick and efficient manipulation of audio files. It allows users to apply various effects and adjustments to their audio files, such as speed and pitch adjustments.

### Features

- **Speed Adjustment:** Modify the playback speed of audio files without altering the pitch.
- **Pitch Adjustment:** Change the pitch of audio files without affecting the playback speed.
- **Export with Encryption:** Generate an encrypted code for the exported audio file for secure sharing or importing into Syn MSP.
- **Clipboard Support:** Encrypted codes are automatically copied to the clipboard for easy sharing.

### Keybinds

- **Browse Button:** Open a dialog to select an audio file for manipulation.
- **Export to S:MSP Button:** Apply changes and export the audio file for use in Syn MSP, including copying an encrypted code to the clipboard.

---

## Getting Started

To use the Synthesized Audio Software Suite, simply clone the repository or download the latest release. Ensure you have Python and Pygame installed on your system. Run `Syn MSP` for the digital piano functionality and `Syn AMP` for audio file manipulation.

