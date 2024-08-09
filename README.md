# voice_text_ai_assistant

# Voice Text AI Assistant

![License](https://img.shields.io/badge/license-MIT-green)
![Python Version](https://img.shields.io/badge/python-3.11-blue)

## Overview

The **Voice Text AI Assistant** is a Python-based application designed to enhance productivity by converting voice commands into text and executing various tasks based on those commands. Leveraging state-of-the-art AI and natural language processing (NLP) technologies, this assistant can help users manage their daily activities more efficiently.

## Features

- **Voice Recognition:** Converts spoken words into text using advanced speech-to-text APIs.
- **Natural Language Processing:** Understands and interprets user commands to perform tasks.
- **Multi-platform Support:** Works on various platforms including Windows, macOS, and Linux.
- **Customizable Workflows:** Users can define custom actions for specific voice commands.
- **Integration with Third-party APIs:** Can be extended to interact with services like Google Calendar, Spotify, etc.

## Installation

### Prerequisites

- Python 3.11 or above
- Git
- Virtualenv (optional but recommended)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/praveenkumarsiddela/voice_text_ai_assistant.git
    cd voice_text_ai_assistant
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Activate the virtual environment if you haven't already:
    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Run the application:
    ```bash
    python main.py
    ```

3. Follow the on-screen instructions to interact with the voice assistant.

## Configuration

- You can modify the `config.json` file to customize the assistant's behavior and integrate it with other APIs.
- Add new voice commands and corresponding actions by editing the `commands.py` file.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [NLTK](https://www.nltk.org/)
- [PyTorch](https://pytorch.org/)

## Contact

If you have any questions or suggestions, feel free to reach out to me at [praveenkumarsiddelaasu@gmail.com](mailto:praveenkumarsiddelaasu@gmail.com).
