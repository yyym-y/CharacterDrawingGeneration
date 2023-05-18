import cv2, os, window_make, paint, numpy, random

path = os.getcwd()
dir_name = path + '/this is a dir'
def Create():
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

def name():
    ran = "zxcvbnm,dsakfgwa1131234567890-=vcsdhgkcqwertyuiopscdjsvzxcvbnmeywur"
    a = random.sample(ran,10)
    s = ''
    for pr in a:
        s += pr
    return s

def Remember_image():
    Create()
    image = paint.give_out()
    cv2.imwrite(dir_name + '/' + name() + '_new.jpg', image)

def Form_TXT():
    Create()
    put = paint.Remember3
    data = open(dir_name + '/' + name() + '_new.txt','a+')
    for i in range(len(put)):
        for j in range(len(put[i])):
            data.write(str(put[i][j]))
            data.write(' ')
        data.write('\n')
    data.close()




