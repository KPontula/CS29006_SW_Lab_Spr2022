import PIL
from random import randrange


class BlurImage(object):
    '''
        Applies Gaussian Blur on the image.
    '''

    def __init__(self, radius):
        '''
            Arguments:
            radius (int): radius to blur
        '''

        self.radius = radius

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL Image)

            Returns:
            image (numpy array or PIL Image)
        '''

        return image.filter(PIL.ImageFilter.GaussianBlur(self.radius))


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


class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''

        self.flip_type = flip_type

        
    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        if (self.flip_type == 'horizontal'):
            return image.transpose(method=PIL.Image.FLIP_LEFT_RIGHT)
        elif (self.flip_type == 'vertical'):
            return image.transpose(method=PIL.Image.FLIP_TOP_BOTTOM)
        else:
            return None


class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''

        self.output_size = output_size

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        if (isinstance(self.output_size, tuple)):
            return image.resize(self.output_size)
        elif (isinstance(self.output_size, int)):
            w, h = image.size
            if(w >= h):
                return image.resize((int(w*self.output_size/h), self.output_size))
            else:
                return image.resize((self.output_size,int(h*self.output_size/w)))


class RotateImage(object):
    '''
        Rotates the image about the centre of the image.
    '''

    def __init__(self, degrees):
        '''
            Arguments:
            degrees: rotation degree.
        '''
        
        self.degrees = degrees

    def __call__(self, sample):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        return sample.rotate(self.degrees)