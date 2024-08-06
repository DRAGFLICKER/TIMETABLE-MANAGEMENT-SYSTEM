import os
import numpy as np
import librosa
import tensorflow as tf
from tensorflow.keras import layers, models

# Function to load and preprocess audio files
def load_and_preprocess_audio(audio_path, target_size=(128, 128)):
    audio, sr = librosa.load(audio_path, sr=None)
    spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr)
    spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)
    spectrogram_db = np.expand_dims(spectrogram_db, axis=-1)
    spectrogram_resized = tf.image.resize(spectrogram_db, target_size)
    spectrogram_rgb = tf.image.grayscale_to_rgb(spectrogram_resized)
    return spectrogram_rgb

# Function to predict bird species
def predict_bird_species(audio_file_path, model):
    spectrogram_rgb = load_and_preprocess_audio(audio_file_path)
    prediction = model.predict(np.expand_dims(spectrogram_rgb, axis=0))
    predicted_class = np.argmax(prediction)
    return predicted_class

# Load the model architecture
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(24, activation='softmax')
])


# Load model weights
model.load_weights('bird_sound_detection_model_cov.h5')

# Example usage:
audio_file_path = 'Bird_Sound_Wav/Fork-tailed Drongo-Cuckoo (Surniculus dicruroides)/XC355137 copy 2.wav'
predicted_bird_species_index = predict_bird_species(audio_file_path, model)
print("predicted_bird_species_index : ",predicted_bird_species_index)
