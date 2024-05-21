# A.I. Speech to Text Game 🎤🕹️

Python-based Minecraft with words recognizer (Convolutional Neural Network), with our own dataset and training. By saying one of the five words, it changes the block to use within the game. Great project to learn about speech recognition and A.I. from training to implementation.

## 🌟 Features

- **Speech Recognition**: Recognizes predefined words to change the block type in the game.
- **Custom Dataset**: Uses a custom dataset collected and trained by our team.
- **Interactive Gameplay**: Integrates speech recognition with gameplay for an immersive experience.
- **Deep Learning**: Utilizes Convolutional Neural Networks (CNN) for speech recognition.

## 🚀 Technologies

- **Python**: Core programming language.
- **CNN**: Convolutional Neural Networks for speech recognition.
- **Colab & Jupyter Notebook**: Tools for model training and experimentation.
- **Ursina**: Game engine for Python.
- **h5py & Keras**: Libraries for saving and loading trained models.
- **Threading**: To handle speech recognition and game simultaneously.
- **Speech Recognizer**: For processing audio inputs.
- **FFT**: Fast Fourier Transform for audio signal processing.
- **TensorFlow**: Backend for Keras.

## 📚 Project Overview

### Custom Dataset and Training

We trained a custom model using a dataset collected by our team. The model recognizes five specific words that correspond to different block types in the game.

### Code Explanation

The code integrates various components like speech recognition, real-time gameplay, and CNN-based predictions. Here's a brief explanation of the main parts:

- **Predictor Function**: Listens for specific words, processes the audio using FFT, and predicts the word using a pre-trained CNN model.
- **Ursina Game Setup**: Sets up the game environment using Ursina, including the player, blocks, and textures.
- **Multithreading**: Uses threading to run the speech recognition in parallel with the game loop.

## 📦 Installation

### Prerequisites

- [Python 3.7+](https://www.python.org/)
- [Pip](https://pip.pypa.io/en/stable/)

### Steps

1. **Clone the repository**
    ```sh
    git clone https://github.com/xlgabriel/ai-speech-to-text-game.git
    cd ai-speech-to-text-game
    ```

2. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application**
    ```sh
    python main.py
    ```

## 🛠️ Usage

1. **Launch the Game**
    - Run the application using the command above.
    - Follow the in-game instructions to use speech commands to change blocks.

2. **Interact with the Game**
    - Say one of the predefined words (e.g., "blanco", "naranja") to change the block type in the game.

## 🤝 Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

## 📝 License

This project is licensed under the MIT License.

## 📧 Contact

For any questions or feedback, please contact [gabriel.jeannot.personal@gmail.com](mailto:gabriel.jeannot.personal@gmail.com).
