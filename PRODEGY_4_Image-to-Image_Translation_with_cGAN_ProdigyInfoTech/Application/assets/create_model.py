import tensorflow as tf
import os
import numpy as np

def create_pix2pix_model():
    # Create the generator model
    def build_generator():
        inputs = tf.keras.layers.Input(shape=(128, 128, 3))
        
        # Encoder
        x = tf.keras.layers.Conv2D(64, 4, strides=2, padding='same')(inputs)
        x = tf.keras.layers.LeakyReLU(0.2)(x)
        
        x = tf.keras.layers.Conv2D(128, 4, strides=2, padding='same')(x)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.LeakyReLU(0.2)(x)
        
        x = tf.keras.layers.Conv2D(256, 4, strides=2, padding='same')(x)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.LeakyReLU(0.2)(x)
        
        # Decoder with skip connections
        x = tf.keras.layers.Conv2DTranspose(128, 4, strides=2, padding='same')(x)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.ReLU()(x)
        
        x = tf.keras.layers.Conv2DTranspose(64, 4, strides=2, padding='same')(x)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.ReLU()(x)
        
        x = tf.keras.layers.Conv2DTranspose(3, 4, strides=2, padding='same')(x)
        outputs = tf.keras.layers.Activation('tanh')(x)
        
        return tf.keras.Model(inputs=inputs, outputs=outputs)

    # Create and compile the model
    model = build_generator()
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0002, beta_1=0.5),
                 loss='mse')
    
    return model

def create_sample_data():
    # Create a simple pattern for training
    x = np.zeros((1, 128, 128, 3))
    y = np.zeros((1, 128, 128, 3))
    
    # Create a simple building pattern in input
    x[0, 32:96, 32:96, :] = 1.0  # White square in the middle
    
    # Create a more detailed building in output
    y[0, 32:96, 32:96, 0] = 0.8  # Red walls
    y[0, 32:96, 32:96, 1] = 0.8  # Green walls
    y[0, 32:96, 32:96, 2] = 0.8  # Blue walls
    
    # Add some windows
    y[0, 40:60, 40:60, :] = 0.2  # Dark windows
    y[0, 40:60, 68:88, :] = 0.2  # Dark windows
    y[0, 68:88, 40:60, :] = 0.2  # Dark windows
    y[0, 68:88, 68:88, :] = 0.2  # Dark windows
    
    return x, y

if __name__ == '__main__':
    # Create model directory if it doesn't exist
    os.makedirs('model', exist_ok=True)
    
    # Create the model
    model = create_pix2pix_model()
    
    # Create sample data
    x_train, y_train = create_sample_data()
    
    # Train the model for a few epochs
    print("Training model...")
    model.fit(x_train, y_train, epochs=50, verbose=1)
    
    # Save the model in .h5 format
    model.save('model/pix2pix_model.h5')
    print("Model created, trained, and saved successfully!") 