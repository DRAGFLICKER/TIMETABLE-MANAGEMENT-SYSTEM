import os
import numpy as np
import librosa
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split

# Function to load and preprocess audio files
def load_and_preprocess_audio(audio_path, target_size=(128, 128)):
    audio, sr = librosa.load(audio_path, sr=None)
    spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr)
    spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)
    spectrogram_db = np.expand_dims(spectrogram_db, axis=-1)
    spectrogram_resized = tf.image.resize(spectrogram_db, target_size)
    spectrogram_rgb = tf.image.grayscale_to_rgb(spectrogram_resized)
    return spectrogram_rgb

# Function to load dataset
def load_dataset(dataset_path):
    X = []
    y = []
    bird_species = sorted(os.listdir(dataset_path))
    for i, species in enumerate(bird_species):
        species_path = os.path.join(dataset_path, species)
        for audio_file in os.listdir(species_path):
            audio_path = os.path.join(species_path, audio_file)
            spectrogram_rgb = load_and_preprocess_audio(audio_path)
            X.append(spectrogram_rgb)
            y.append(i)  
    return np.array(X), np.array(y)

# Load dataset
dataset_path = 'static/trainaudio'
X, y = load_dataset(dataset_path)

# Split dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Define CNN model architecture
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

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32)

# Save model weights
model.save_weights('voicedetecctcheck.h5')
