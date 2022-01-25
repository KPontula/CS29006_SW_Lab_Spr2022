#Imports
# from my_package.model import InstanceSegmentationModel
# from my_package.data import Dataset
# from my_package.analysis import plot_visualization
# from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
# import numpy as np
from PIL import Image

from my_package.data.transforms.blur import BlurImage
from my_package.data.transforms.flip import FlipImage
from my_package.data.transforms.rotate import RotateImage
from my_package.data.transforms.rescale import RescaleImage
from my_package.data.transforms.crop import CropImage

def experiment(annotation_file, segmentor, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        segmentor: The image segmentor
        transforms: List of transformation classes
        outputs: path of the output folder to store the images
    '''
    pass
    #Create the instance of the dataset.


    #Iterate over all data items.


    #Get the predictions from the segmentor.


    #Draw the segmentation maps on the image and save them.


    #Do the required analysis experiments.
    


def main():
    # segmentor = InstanceSegmentationModel()
    # experiment('./data/annotations.jsonl', segmentor, [FlipImage(), BlurImage()], None) # Sample arguments to call experiment()

    img = Image.open(r"C:\Users\KP\Desktop\se lab\CS29006_SW_Lab_Spr2022\Python_DS_Assignment\data\imgs\3.jpg")
    rad = 50
    # Gaussian Blur
    # img2 = (BlurImage(rad))(img)

    # FLip Image
    # img2 = (FlipImage('horizontal'))(img)

    # Rotate Image
    # img2 = (RotateImage(rad))(img)

    # Rescale Image
    # img2 = (RescaleImage(200))(img)

    # Crop Image
    img2 = (CropImage((100,300),'random'))(img)
    img2.show()

if __name__ == '__main__':
    main()
