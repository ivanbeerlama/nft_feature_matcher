from argparse import ArgumentParser
import cv2
import numpy as np
import os

parser = ArgumentParser()
parser.add_argument("-i", "--image", dest="image", help="Image file")
parser.add_argument("-p", "--path", dest="path", help="Image dir path")
parser.add_argument("-o", "--output", dest="output", help="Output csv file")

args = parser.parse_args()

# Load base image
image = cv2.imread(args.image)

cv2.namedWindow("Input image", 2)

print("Draw box around feature and press ENTER...")

roi = cv2.selectROI("Input image", image)

 ## Display the roi
if roi is not None:

  cv2.namedWindow("Mask",2)
  cv2.namedWindow("Feature",2)

  x,y,w,h = roi
  mask = np.zeros_like(image, np.uint8)
  cv2.rectangle(mask, (x,y), (x+w, y+h), (255,255,255), -1)
  
  feature = image[y:y+h, x:x+w]

  cv2.imshow("Mask", mask)
  cv2.imshow("Feature", feature)

  print("Press ENTER to start matching...")
  
  cv2.waitKey()

  cv2.namedWindow("Feature matching",2)

  result_list = []
  
  for filename in os.listdir(args.path):
    f = os.path.join(args.path, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print("Checking " + filename + "... ", end='')
        
        image2 = cv2.imread(f)
        
        result = cv2.matchTemplate(image2, feature, cv2.TM_CCOEFF_NORMED, mask)

        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        
        threshold = 0.8
        flag = False
        y = 0.0;

        if np.amax(result) > y:
            y = np.amax(result)
        if np.amax(result) > threshold:
            flag = True

        if flag:
          top_left = max_loc
          bottom_right = (top_left[0] + w, top_left[1] + h)

          cv2.rectangle(image2, top_left, bottom_right, (0, 255, 0), int(image2.shape[0] / 100))
        
        print(str(y) + " -> " + str(flag))

        result_list.append([y,flag,filename])
        
        cv2.imshow("Feature matching", image2)

        cv2.waitKey(10)

  csv = open(args.output, "w")
  csv.write("filename,has_feature,score\n")

  print("***** Results: *****")

  sorted_list = sorted(result_list, reverse=True)

  for f in sorted_list:
    line_str = str(f[2]) + "," + str(f[1]) + "," + str(f[0]) + "\n"
    csv.write(line_str)

  print("********************")

  csv.close()

        
  print("Done, press ENTER to exit...")

  cv2.waitKey()


print(args)
