# extract frame every one second. So a 1-minute video will give 60 frames(images).
#       python3 app2.py --pathIn /home/t/Downloads/bees_pics/b12.mp4 --pathOut /home/t/Pyth/extract_pics_from_video/extracted_img/
# python3 app2.py --pathIn /home/t/Downloads/bees_pics_and_videos/videos/4.mp4 --pathOut /home/t/Pyth/Bees_data/all_bees_new_dataset_main/img_from_videos/
import sys
import argparse

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*200))    # 1000 = 1 second
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        cv2.imwrite( pathOut + "frame%d.jpg" % count, image)     # save frame as JPG file with given name
        count = count + 1

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut)
