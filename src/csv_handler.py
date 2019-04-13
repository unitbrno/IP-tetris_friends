#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import csv

class CsvHandler:

    """
    This is responsible for working with CSV files
    """

    def __init__(self, file):
        self.file = file

    def create_heading(self):
        """
        Creates a heading for the CSV file
        """
        fields = ["filename", "ellipse_center_x", "ellipse_center_y",
                  "ellipse_majoraxis", "ellipse_minoraxis",
                  "ellipse_angle", "elapsed_time"] # Header, do not change

        with open(self.file, 'w+') as csv_file:

            # sniffer = csv.Sniffer()
            # has_header = sniffer.has_header(csv_file.read(2048))
            # csv_file.seek(0)

            # if not has_header:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(fields)

    def append_row(self, data):
        """
        Appends a row to the CSV
        fil  =  filename
        ecx  =  ellipse_center_x
        ecy  =  ellipse_center_y
        ema  =  ellipse_majoraxis
        emi  =  ellipse_minoraxis
        ean  =  ellipse_angle
        eti  =  elapsed_time
        """

        with open(self.file, 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)
