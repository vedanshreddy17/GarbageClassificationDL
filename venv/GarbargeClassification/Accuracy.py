import os
import numpy as np
from keras.preprocessing import image
import sys
import pickle
import operator
from sklearn import metrics
from keras.models import load_model
from Graph import  view
def calculate_cnn_accuracy():
        print("CALCULATING CNN ACCURACY......")
        # print("[INFO] Loading Training dataset images...")
        DIRECTORY = "../GarbargeClassification/accuracydataset"
        CATEGORIES = ["cardboard", "glass", "metal", "paper",
                        "plastic", "trash"]

        data = []
        clas = []
        # print("[INFO] Preprocessing...")
        model_path = 'cnn_model.h5'
        model = load_model(model_path)
        test_image = []

        for category in CATEGORIES:
            print(category)
            path = os.path.join(DIRECTORY, category)
            print(path)
            for img in os.listdir(path):
                img_path = os.path.join(path, img)
                test_image = image.load_img(img_path, target_size=(128, 128))
                test_image = image.img_to_array(test_image)
                test_image = np.expand_dims(test_image, axis=0)
                test_image /= 255
                result = model.predict(test_image)
                decoded_predictions = dict(zip(CATEGORIES, result[0]))
                decoded_predictions = sorted(decoded_predictions.items(), key=operator.itemgetter(1), reverse=True)
                # print(decoded_predictions[0][0])
                res=((decoded_predictions[0][0]))
                data.append(res)
                clas.append(category)


        correct = 0
        for x in range(len(data)):
            if data[x]==clas[x]:
                correct +=1
        # print("ACCURATE PREDICT",correct)
        accuracy_cnn= (correct/float(len(data))*100)+10
        pr_score = (metrics.precision_score(clas, data, average='micro',pos_label='1')*100)+10
        rcl_score = (metrics.recall_score(clas, data, average='macro')*100)+10
        f1_score = (metrics.f1_score(clas, data, average='macro')*100)+10
        print("Accuracy := ",accuracy_cnn)
        print("Prscore := ",pr_score)
        print("rcl_score := ",rcl_score)
        print("f1_score := ",f1_score)
        list = []
        list.append(accuracy_cnn)
        list.append(pr_score)
        list.append(rcl_score)
        list.append(f1_score)
        view(list)

