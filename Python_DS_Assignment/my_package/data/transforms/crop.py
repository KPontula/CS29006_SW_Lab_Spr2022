import PIL

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
        if(self.crop_type == 'center'):
            h, w = self.shape
            w0, h0 = image.size
            return image.crop((int(w0/2 - w/2), int(h0/2 - h/2), int(w0/2 + w/2), int(h0/2 + h/2)))
        elif(self.crop_type == 'random'):
            pass
        

 