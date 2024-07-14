# 🤖 HEYBOT Voice Assistant

HEYBOT is a desktop voice assistant designed to perform various tasks such as telling the time and date, searching Wikipedia, opening websites, taking screenshots, and more.

## ✨ Features

- 🎉 **Greet the User**: Wishes the user based on the time of day.
- ⏰ **Time and Date**: Tells the current time and date.
- 📚 **Wikipedia Search**: Searches Wikipedia and reads out the summary.
- 🌐 **Open Websites**: Opens popular websites like YouTube, Google, and Stack Overflow.
- 🎵 **Play Music**: Plays a random song from the user's Music directory.
- 📸 **Take Screenshot**: Takes a screenshot and saves it in the Pictures directory.
- 🗣️ **Voice Commands**: Recognizes and executes various voice commands.

## 📋 Prerequisites

- 🐍 Python 3.x

## 🛠️ Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/heybot-voice-assistant.git
    cd heybot-voice-assistant
    ```

2. **Create a Virtual Environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate      # On Windows: venv\Scripts\activate
    ```

3. **Install Required Libraries**:
    ```sh
    pip install pyttsx3 SpeechRecognition wikipedia pyautogui
    ```

## 🚀 Usage

1. **Run the Script**:
    ```sh
    python voice_assistant.py
    ```

2. The assistant will greet you and await your commands. Use voice commands to interact with HEYBOT.

## 🎙️ Voice Commands

- **"What is the time?"**: ⏰ Tells the current time.
- **"What is the date?"**: 📅 Tells the current date.
- **"Who are you?"**: 🤖 Introduces HEYBOT.
- **"How are you?"**: 🗣️ Responds to your greeting.
- **"Search Wikipedia for [query]"**: 🔍 Searches Wikipedia for the given query and reads the summary.
- **"Open YouTube"**: 📺 Opens YouTube in a web browser.
- **"Open Google"**: 🌐 Opens Google in a web browser.
- **"Open Stack Overflow"**: 💻 Opens Stack Overflow in a web browser.
- **"Play music"**: 🎵 Plays a random song from your Music directory.
- **"Take a screenshot"**: 📸 Takes a screenshot and saves it in the Pictures directory.
- **"Remember that [something]"**: 💾 Remembers the specified information.
- **"Do you remember anything?"**: 🔍 Recalls the remembered information.
- **"Go offline"**: 📴 Exits the voice assistant.

## 📝 Notes

- 🎤 Ensure your microphone is working properly as the assistant relies on voice commands.
- 🌐 The voice recognition requires an internet connection to function.
- 🛠️ Modify the paths and commands in the script according to your system's configuration if needed.

## 🤝 Contributing

Feel free to fork the repository and submit pull requests for improvements or additional features.

## 📜 License

This project is licensed under the MIT License.

---

✨ Happy Coding! ✨
