# nft_feature_matcher
Template matching tool to find treat similarities in image collections. This scripts allows the user to draw a bounding box around a certain treat. Correction score is calculated over the whole collection with the assumption the feature occurs on the same place in all image.

## Dependancies

- python3
- requests
- opencv-python
- numpy

## Usage

### download.py

Adjust the file to point to the correct input .csv file, output directory and file extension and run:

`python3 download.py`

### match.py

Input arguments:

- -i --image: Path of input image to be used to select ROI to use as template for template matching
- -p --path: Path to directory containing the image collection
- -o --output: Output csv file with the result

Activating threshold (0.8) can be adjusted in match.py or can be ignored if post-processing is done based on correlation score. You choose yout own threshold manually after processing. Run the following command:

`python3 match.py -i [image_path] -p [collection_path] -o [results.csv]`

1. A image is show in which a rectangular bounding box can be drawn around a feature. Press ENTER if the box is drawn
2. Next, the image mask and cropped feature is shown, press ENTER to start matching
3. Matching takes a while, intermediate results are displayed on the screen. Activated areas are highlighted in green.
4. After matching results are written to the output.csv

