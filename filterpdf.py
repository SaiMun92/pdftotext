# -*- coding: utf-8 -*-

import os
import shutil


"""
    This program filter out the pdf in the folder "pdf" based on the text files in the "txt" folder. 
"""
input_path = r"F:\Development\pdf_downloader\combined_txt2"
input_path2 = r"F:\Development\pdf_downloader\combined"
output_path = r"F:\Development\pdf_downloader\combined_filtered"


for root, dirs, files in os.walk(input_path):
    for filename in files:
        filename = filename.replace(".txt", ".pdf")

        # copying the path from the old to the new since they all have the same name
        shutil.copy(os.path.join(input_path2, filename), os.path.join(output_path, filename))
