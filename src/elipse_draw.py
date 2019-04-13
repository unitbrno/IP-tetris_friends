#!/bin/python3

import time
import math
import cv2


class ElipseDraw:

    def draw_elipse(self, image_dir):

        # Timer
        start_time = time.time()

        img = cv2.imread(image_dir)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray, (5, 5), 1, 1, 0)
        # blur = cv2.blur(gray, (5, 5))

        _, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
        # _, thresh = cv2.threshold(blur, 127, 255, cv2.ADAPTIVE_THRESH_MEAN_C)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        for cnt in contours:
            try:
                (x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
            except:
                print(image_dir)
                return []

        # cv2.ellipse(img, ((x, y), (MA, ma), angle), (0,0,255), 2, cv2.LINE_AA)

        end_time = time.time()
        total_time = end_time - start_time

        data = [x, y, ma/2, MA/2, angle, total_time]
        end_data = ['%.2f' % elem for elem in data]

        # cv2.imwrite(image_dir, img)
        return end_data
