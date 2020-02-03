import joblib
from sklearn.svm import SVC
import pandas as pd
import numpy as np

class Classifier:
    def __init__(self, C=1.0, gamma='scale', tol=0.001, max_iter=-1, kernel='rbf', verbose=False):
        self.C = C
        self.gamma = gamma
        self.tol = tol
        self.max_iter = max_iter
        self.kernel = kernel
        self.verbose = verbose

        self.SVC_model = SVC(C=self.C,
                             gamma = self.gamma,
                             tol = self.tol,
                             max_iter = self.max_iter,
                             kernel = self.kernel,
                             verbose = self.verbose
                             )

        self.__loadData()

    def __loadData(self):
        dataFrame = pd.read_csv("./Data/mnist_train.csv")
        self.pixel_train = dataFrame.drop(['label'], axis=1)
        self.label_train = dataFrame['label']
        dataFrame = pd.read_csv("./Data/mnist_test.csv")
        self.pixel_test = dataFrame.drop(['label'], axis=1)
        self.label_test = dataFrame['label']
        del dataFrame

    def fit_model(self):
        print("Fitting Classification Model...")
        self.SVC_model.fit(self.pixel_train, self.label_train)
        print("Done!")
        self.getMetrics()

    def getMetrics(self):
        score = self.SVC_model.score(self.pixel_test, self.label_test)
        print("Score : ", score*100)

    def predictImage(self, canvas):
        predict_class = self.SVC_model.predict(canvas)
        print(predict_class)

    def save_model(self, path=None):
        save_path = path if path else "./Saved Model/SVC_Model_1.sav"
        joblib.dump(self.SVC_model, save_path)

    def load_model(self, path=None):
        load_path = path if path else "./Saved Model/SVC_Model_1.sav"
        try:
            self.SVC_model = joblib.load(load_path)
            return True
        except Exception as e:
            return False


if __name__ == '__main__':
    c = Classifier()
    c.fit_model()