from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
def CNN_BULDMODEL():
    classifier = Sequential()
    # Convolution and Max pooling
    classifier.add(Conv2D(32, (6, 6), input_shape=(128, 128, 3), activation='relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    classifier.add(Conv2D(64, (6, 6), activation='relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2), data_format="channels_first"))
    classifier.add(Conv2D(128, (6, 6), activation='relu'))
    classifier.add(MaxPooling2D(pool_size=(2, 2), data_format="channels_first"))
    # Flatten
    classifier.add(Flatten())
    # Full connection
    classifier.add(Dense(128, activation='relu'))
    classifier.add(Dense(6, activation='softmax'))
    # Compile classifier
    classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Fitting CNN to the images
    train_datagen = ImageDataGenerator(rescale=1. / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
    test_datagen = ImageDataGenerator(rescale=1. / 255)
    training_set = train_datagen.flow_from_directory('../GarbargeClassification/dataset/train', target_size=(128, 128), batch_size=32,
                                                     class_mode='categorical')
    test_set = test_datagen.flow_from_directory('../GarbargeClassification/dataset/valid', target_size=(128, 128), batch_size=32,
                                                class_mode='categorical')
    classifier.fit_generator(training_set, steps_per_epoch=30, epochs=50, validation_data=test_set,validation_steps=20)

    # save model
    classifier.save('cnn_model.h5')
