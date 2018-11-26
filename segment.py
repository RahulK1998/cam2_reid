import cv2
import numpy as np
import argparse
import os
import time

#directory must exist

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", help="path to the image files")
ap.add_argument("-s", "--save", help="path to save image files")
args = vars(ap.parse_args())


# if the video argument is None, then we are reading from webcam
if args.get("folder", None) is None:
    path = os.getcwd()
    time.sleep(2.0)
else:
    path = args["folder"]

if args.get("save", None) is None:
    path2 = path
    time.sleep(2.0)
else:
    path2 = args["save"]


directory = os.fsencode(path)


for file in os.listdir(directory):
    filename = os.fsdecode(file)

    if filename.endswith(".jpg") or filename.endswith(".jpeg")or filename.endswith(".png") or filename.endswith(".PNG") or filename.endswith(".JPG") :
        name, file_extension = os.path.splitext(filename)
        top_name = path2+"\\"+name+"_TOP"+file_extension
        mid_name = path2+"\\"+name+"_MID"+file_extension
        bot_name = path2+"\\"+name+"_BOT"+file_extension

        image_loc = path+"\\"+filename

        image = cv2.imread(image_loc)
        #cv2.imshow("Original Image", image)
        #cv2.waitKey(0)

        height, width = image.shape[:2]
        # print(image.shape)

        start_row, start_col = int(0), int(0)
        # Let's get the ending pixel coordinates (bottom right of cropped top)
        end_row, end_col = int(height * .2), int(width)
        cropped_top = image[start_row:end_row , start_col:end_col]

        # print(start_row, end_row)
        # print(start_col, end_col)
        cv2.imwrite(top_name, cropped_top)

        # cv2.imshow("Cropped head", cropped_top)
        # cv2.waitKey(0)

        start_row, start_col = int(height * .2), int(0)
        # Let's get the ending pixel coordinates (bottom right of cropped bottom)
        end_row, end_col = int(height * .65), int(width)
        cropped_mid = image[start_row:end_row , start_col:end_col]
        # print(start_row, end_row)
        # print(start_col, end_col)

        cv2.imwrite(mid_name, cropped_mid)

        # cv2.imshow("Cropped mid", cropped_mid)
        # cv2.waitKey(0)

        # Let's get the starting pixel coordiantes (top left of cropped bottom)
        start_row, start_col = int(height * .65), int(0)
        # Let's get the ending pixel coordinates (bottom right of cropped bottom)
        end_row, end_col = int(height), int(width)
        cropped_bot = image[start_row:end_row , start_col:end_col]
        # print(start_row, end_row)
        # print(start_col, end_col)
        #
        cv2.imwrite(bot_name, cropped_bot)

        # cv2.imshow("Cropped Bot", cropped_bot)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    else:
        continue
