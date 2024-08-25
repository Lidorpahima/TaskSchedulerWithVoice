# TaskReminderBot

TaskReminderBot is a Python-based voice-controlled task reminder application. It allows users to add tasks and set reminders through voice commands, ensuring you never forget an important task again!

## Features

- **Voice Recognition:** Add tasks and set reminders using simple voice commands.
- **Customizable Reminders:** Specify the delay time, and get reminded with a sound notification.
- **Threaded Execution:** Reminders are handled in separate threads to allow for multiple reminders simultaneously.
- **Flexible Keyword Matching:** The application recognizes various pronunciations and minor errors in voice commands to ensure tasks are added accurately.

## How It Works

1. **Add a Task:** Simply say "add" followed by your task description, and the task will be stored.
2. **Set a Reminder:** After adding a task, specify the delay (in seconds) for when you want to be reminded.
3. **Reminder Notification:** When the time comes, the application will play a sound and display your task.

## Requirements

- Python 3.x
- Required Python libraries:
  - `SpeechRecognition`
  - `pyaudio`
  - `pygame` or `playsound` (depending on your choice for sound playback)
  - `threading` (part of the Python standard library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Lidorpahima/TaskSchedulerWithVoice.git
