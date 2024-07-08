import tensorflow as tf
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist
(train_images, train_labels) , (test_images, test_labels) = mnist.load_data()
# Printing the shapes
print("train_images shape: ", train_images.shape)
print("train_labels shape: ", train_labels.shape)
print("test_images shape: ", test_images.shape)
print("test_labels shape: ", test_labels.shape)
 
 
# Displaying first 9 images of dataset
fig = plt.figure(figsize=(10,10))
 
nrows=3
ncols=3
for i in range(9):
  fig.add_subplot(nrows, ncols, i+1)
  plt.imshow(train_images[i])
  plt.title("Digit: {}".format(train_labels[i]))
  plt.axis(False)
plt.show()

# COnvert image pixel values to 0 - 1
train_images = train_images / 255
test_images = test_images / 255

print("First label before convert: ")
print(train_labels[0])

# Convert labels to one-hot encoded vectors (smaller values are better used)
train_labels = tf.keras.utils.to_categorical(train_labels)
test_labels = tf.keras.utils.to_categorical(test_labels)

print("First Label after conversion:")
print(train_labels[0])

'''Creating the Model'''
# Sequential funciton repeats this set of code for every row
model = tf.keras.Sequential([
    # Flatten layers to conver to 1D array
    tf.keras.layers.Flatten(),

    # Hidden Layer with 512 units and RELU (convert to only pos #'s)
    tf.keras.layers.Dense(units=512, activation='relu'),

    # Output Layer with 10 units for 10 classes and softmax activation
    tf.keras.layers.Dense(units=10, activation='softmax')
])

'''Compiling the Model'''
model.compile(
  loss = 'categorical_crossentropy',
  optimizer = 'adam',
  metrics = ['accuracy']
)

# Train the neural network with .fit()
history = model.fit(
    x = train_images,
    y = train_labels,
    epochs = 20 # number of times the training is run
)

# Showing plot for loss
plt.plot(history.history['loss'])
plt.xlabel('epochs')
plt.legend(['loss'])
plt.show()

# Showing plot for accuracy
plt.plot(history.history['accuracy'], color='orange')
plt.xlabel('epochs')
plt.legend(['accuracy'])
plt.show()

# Evaluate the neural network based on test_images
# using the .evaluate(x,y)
test_loss, test_accuracy = model.evaluate(
    x = test_images,
    y = test_labels
)

print(test_loss)
print(test_accuracy)

predicted_probabilities = model.predict(test_images)
predicted_classes = tf.argmax(predicted_probabilities, axis=-1).numpy()

index=7

# Showing image
plt.imshow(test_images[index])

# Printing Probabilities
print("Probabilities predicted for image at index", index)
print(predicted_probabilities[index])

print()

# Printing Predicted Class
print("Probabilities class for image at index", index)
print(predicted_classes[index])