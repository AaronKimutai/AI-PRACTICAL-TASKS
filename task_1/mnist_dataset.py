import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Download and load the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize pixel values to be between 0 and 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# 2. Build a Neural Network to distinguish digits 0-9
model = models.Sequential([
    layers.Input(shape=(28, 28)),   # improved modern way (fixes warning)
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')  # 10 output units for digits 0-9
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
print("Training the model...")
model.fit(x_train, y_train, epochs=5)

# Evaluate the model
print("\nEvaluating on test data:")
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)

print(f"\nFinal Test Accuracy: {test_acc:.4f}")
print("Model trained successfully on MNIST dataset.")