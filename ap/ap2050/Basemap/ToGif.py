'''
20210617 This code shows how to read a series of jpg files to make a gif animation.
'''

from PIL import Image
import numpy as np

image_frames = []

days = np.arange(1,160)

for k in days:
    new_frame = Image.open(r'jpeg/'+str(k)+'.jpg')
    image_frames.append(new_frame)

image_frames[0].save('temperature_timelapse.gif', format = 'gif',
                     append_images = image_frames[1:],
                     save_all = True, duration = 150,
                     loop = 0 )