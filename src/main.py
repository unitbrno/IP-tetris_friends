#!/usr/bin/python3
# -*- coding: UTF8 -*-

import sys
import cv2 #TEMP
from csv_handler import CsvHandler
from image_convertor import ImageConvertor
from elipse_draw import ElipseDraw

class Main:

    """
    Is responsible for launching everything (it's a main...)
    """

    def __init__(self):
        """
        args[1..n-1] == tiff
        args[last] == csv
        """

        # Arg check (it's pathetic)
        if len(sys.argv) == 1:
            print("Wrong args, try again lul")
            exit(1)

        self.args = sys.argv
        self.csv_file = self.args[len(sys.argv)-1]
        # self.tester()

        # CSV SETUP
        csv = CsvHandler(self.csv_file)
        csv.create_heading()

        # ELIPSEDRAW SETUP
        ed = ElipseDraw()

        # Loop goes through all the file arguments, this is where
        # the magic happens.
        for i in range(1, len(sys.argv)-1):
            
            # File names
            img_name = self.args[i]
            # img_name_work = img_name[:-5] + "_WORK.tiff"
            # img_name_res = img_name[:-5] + "_RES.tiff"

            # File modifications so we can work with it
            workable_img = ImageConvertor().convert_image(img_name)
            cv2.imwrite(img_name, workable_img) # Outputing workable image, optional

            final_img = ed.draw_elipse(img_name)

            # cv2.imwrite(img_name, final_img) # Outputing workable image, optional

            final_img = [img_name] + final_img # Pridani jmena souboru
            
            csv.append_row(final_img)

if __name__ == "__main__":
    Main()
