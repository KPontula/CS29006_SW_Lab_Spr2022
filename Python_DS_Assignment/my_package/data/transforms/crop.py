import PIL
from random import randrange

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''

        self.shape = shape
        self.crop_type = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        h, w = self.shape
        W, H = image.size
        if(self.crop_type == 'center'):
            return image.crop((int(W/2 - w/2), int(H/2 - h/2), int(W/2 + w/2), int(H/2 + h/2)))
        elif(self.crop_type == 'random'):
            x = randrange(int(W/2 - w/2), int(W/2 + w/2))
            y = randrange(int(H/2 - h/2), int(H/2 + h/2))
            return image.crop((int(x - w/2), int(y - h/2), int(x + w/2), int(y + h/2)))
        

 