from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from keras.models import load_model # type: ignore

test_dir = 'test'  # update this path
img_size = (500, 500)

# Normalize pixel values
test_datagen = ImageDataGenerator(rescale=1./255)

# Load test data
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=img_size,
    color_mode='grayscale',
    batch_size=32,
    class_mode='binary',
    shuffle=False
)
model = load_model('models/pneu_cnn_model.h5')
loss, accuracy = model.evaluate(test_generator)
print(f"Test Accuracy: {accuracy*100:.2f}%")

