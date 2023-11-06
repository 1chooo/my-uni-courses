'''
第一區 X:0.3 Y:0.65 ,X:0 Y:0.35
第二區 X:0.65 Y:0.35, X:0.35 Y:0.05
範圍是0.3 *0.3 兩個平面中心點分別是0.5 0.2 跟 0.15 0.5
0.8 * 0.8
'''

def capture_image():
    '''
    __summary__ : the api will return the frame raw byte
    params : N/A
    return [640 x 640 x 3]
    '''
    # Dummy data
    # data = random.randint(0, 255)
    image = [[[1 for _ in range(3)] for _ in range(640)] for _ in range(640)]
    return image