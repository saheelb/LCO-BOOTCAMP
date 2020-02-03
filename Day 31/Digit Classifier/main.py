import svm_classifier, canvas
import cv2

from svm_classifier import Classifier

def main():
    # Train Classifier...
    classifier_obj = Classifier()
    if not classifier_obj.load_model():
        print("Saved Model NOT Found, Creating one...")
        classifier_obj.fit_model()
        classifier_obj.save_model()
    # Calling a live Canvas...
    canvas.Canvas(classifier=classifier_obj).loop_canvas()

if __name__ == '__main__':
    main()