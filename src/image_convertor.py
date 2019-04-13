#!/bin/python3
# -*- coding: UTF-8 -*-

import cv2


class ImageConvertor:

    def convert_image(self, path):
        img = cv2.imread(path, -1) # load image as is
        normalized_img = img # copy H, W of image
        normalized_img = cv2.normalize(img, normalized_img, 0,
                                       255, cv2.NORM_MINMAX) # normalize image
        return normalized_img * 255 # make image great again
