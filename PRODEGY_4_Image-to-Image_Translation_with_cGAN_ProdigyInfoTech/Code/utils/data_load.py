import tensorflow as tf
import os
import glob

AUTOTUNE = tf.data.AUTOTUNE

def load_image(image_file):
    """Load and decode a single image from file"""
    image = tf.io.read_file(image_file)
    image = tf.image.decode_jpeg(image)

    # Split the image into input and real images (for image-to-image tasks)
    w = tf.shape(image)[1]
    w = w // 2
    input_image = image[:, :w, :]
    real_image = image[:, w:, :]

    input_image = tf.cast(input_image, tf.float32)
    real_image = tf.cast(real_image, tf.float32)

    return input_image, real_image

def resize(input_image, real_image, height, width):
    """Resize images to the given height and width"""
    input_image = tf.image.resize(input_image, [height, width],
                                  method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    real_image = tf.image.resize(real_image, [height, width],
                                 method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    return input_image, real_image

def normalize(input_image, real_image):
    """Normalize images to the range [-1, 1]"""
    input_image = (input_image / 127.5) - 1
    real_image = (real_image / 127.5) - 1
    return input_image, real_image

def random_jitter(input_image, real_image):
    """Apply random jitter (resize, crop, flip)"""
    # Resize to 286x286 then randomly crop to 256x256
    input_image, real_image = resize(input_image, real_image, 286, 286)
    stacked_image = tf.stack([input_image, real_image], axis=0)
    cropped_image = tf.image.random_crop(stacked_image, size=[2, 256, 256, 3])
    input_image, real_image = cropped_image[0], cropped_image[1]

    # Randomly flip the images horizontally
    if tf.random.uniform(()) > 0.5:
        input_image = tf.image.flip_left_right(input_image)
        real_image = tf.image.flip_left_right(real_image)

    return input_image, real_image

def load_image_train(image_file):
    """Preprocess the image for training (including random jitter)"""
    input_image, real_image = load_image(image_file)
    input_image, real_image = random_jitter(input_image, real_image)
    input_image, real_image = normalize(input_image, real_image)
    return input_image, real_image

def load_image_test(image_file):
    """Preprocess the image for testing (without random jitter)"""
    input_image, real_image = load_image(image_file)
    input_image, real_image = resize(input_image, real_image, 256, 256)
    input_image, real_image = normalize(input_image, real_image)
    return input_image, real_image

def load_dataset(train_path, test_path, batch_size=1):
    """Load the training and testing datasets"""
    # Load and preprocess the training dataset
    train_dataset = tf.data.Dataset.list_files(train_path + '/*.jpg')
    train_dataset = train_dataset.map(load_image_train, num_parallel_calls=AUTOTUNE)
    train_dataset = train_dataset.shuffle(400)
    train_dataset = train_dataset.batch(batch_size)

    # Load and preprocess the testing dataset
    test_dataset = tf.data.Dataset.list_files(test_path + '/*.jpg')
    test_dataset = test_dataset.map(load_image_test)
    test_dataset = test_dataset.batch(batch_size)

    return train_dataset, test_dataset