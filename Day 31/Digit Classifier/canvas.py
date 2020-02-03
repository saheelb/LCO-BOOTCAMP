import cv2
import numpy as np

class Canvas:
    def __init__(self, classifier, name="Canvas", width=600, height=600, brush_size=15, dtype="uint8"):
        self.width = width
        self.height = height
        self.__dtype = dtype
        self.name = name
        self.brush_size = brush_size

        self.page = np.ones((self.width, self.height), dtype=self.__dtype) * 0

        self.start_point = None
        self.end_point = None
        self.is_Drawing = False

        cv2.namedWindow(self.name)
        cv2.setMouseCallback(self.name, self.__mouseEvent)
        self.Classifier_obj = classifier

    def __drawLine(self):
        cv2.line(self.page, self.start_point, self.end_point, 255, self.brush_size)

    def __mouseEvent(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.is_Drawing = True
            if self.is_Drawing:
                self.start_point = (x, y)
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.is_Drawing:
                self.end_point = (x,y)
                self.__drawLine()
                self.start_point = self.end_point
        elif event == cv2.EVENT_LBUTTONUP:
            self.is_Drawing = False

    def clear_canvas(self):
        self.page[:, :] = 0

    def show_canvas(self, timeout):
        cv2.imshow(self.name, self.page)
        return cv2.waitKey(timeout)

    def close_canvas(self):
        cv2.destroyAllWindows()

    def loop_canvas(self):
        print("Running Canvas...")
        while True:
            key = self.show_canvas(timeout=1) & 0xFF

            if key == ord('q'):
                break
            elif key == ord("c"):
                self.clear_canvas()
            elif key == ord('p'):
                self.predictCanvas()

        self.clear_canvas()

    def predictCanvas(self):
        data = cv2.resize(self.page, (28, 28)).reshape((1, -1))
        # print(data)
        self.Classifier_obj.predictImage(data)

    def getCanvasData(self):
        return self.page


if __name__ == '__main__':
    c = Canvas()
    c.loop_canvas()
