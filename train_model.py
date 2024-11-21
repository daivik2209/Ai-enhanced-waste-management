import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

# Load dataset
datagen = ImageDataGenerator(validation_split=0.2, rescale=1.0 / 255)
train_gen = datagen.flow_from_directory('data/waste', subset='training', target_size=(224, 224), batch_size=32)
val_gen = datagen.flow_from_directory('data/waste', subset='validation', target_size=(224, 224), batch_size=32)

# Load pre-trained model
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False  # Freeze the base model

# Add custom layers
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
predictions = Dense(train_gen.num_classes, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=predictions)

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_gen, validation_data=val_gen, epochs=5)

# Save the trained model
model.save('waste_classifier.h5')