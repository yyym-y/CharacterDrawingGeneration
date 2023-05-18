import cv2  # 导入opencv
import numpy as np  # 导入 numpy用于生成新画布
import matplotlib.pyplot as plt
Remember1 = None
Remember2 = None
Remember3 = []
class Info(object):  # 初始化相关信息
    def __init__(self, root):
        # 判断输入的类型，如果是视频，传入的是读取完的数据，图片则是原始路径
        if type(root) == str:  # 这里是如果输入的是图片绝对路径
            image = cv2.imread(root, cv2.IMREAD_GRAYSCALE)  # 以灰度图形读入
            length, width = image.shape[1], image.shape[0]  # 获取图片的基本信息
            rate = self.Change_size(length, width)  # 因为有些图片过于大，导致屏幕无法显示，所以这里是获取缩放的比例
            image = cv2.resize(image, (0, 0), fx=rate, fy=rate)  # 根据上面数据缩放图片
            self._height, self._width = image.shape  # 记录最后的实际长宽
            self._gray_info = image  # 将读入的图片信息保存
        else:  # 如果是视频格式， 相比之下省略了读入这一操作
            length, width = root.shape[1], root.shape[0]
            rate = self.Change_size(length, width)
            root = cv2.resize(root, (0, 0), fx=rate, fy=rate)
            self._height, self._width = root.shape
            self._gray_info = root
    @staticmethod
    def Change_size(length, width):
        mutiply_, tem1, tem2 = 1, width, length
        while tem1 > 900 or tem2 > 1900:  # 这两个参数代表如果屏幕想要完全展示的的最大边界
            mutiply_ -= 0.1  # 逐一尝试只到符合
            tem1 = mutiply_ * width
            tem2 = mutiply_ * length
        return mutiply_

class Paint(Info):  # 实际操作
    _use_char = ['.', '-', '=', '+', '#']  # 使用的字符
    @staticmethod
    def Judge(number):  # 判断用哪一个字符，灰度值为255 对其5分
        return number // 52  # 不用51来除是为了防止数组越界
    def New(self):
        Canvas = np.ndarray([self._height, self._width])  # 依据原始图片大小来生成新的画布
        return Canvas
    def Paint_Canvas(self):
        global Remember2, Remember3
        Remember3.clear()
        Canvas = self.New()
        for pr1 in range(0, self._height, 5):  # 每5步判断当前灰度值判断使用何种字符
            tem = []
            for pr2 in range(0, self._width, 5):
                char = self._use_char[self.Judge(self._gray_info[pr1][pr2])]
                tem.append(char)
                cv2.putText(Canvas, char, (pr2, pr1), cv2.FONT_HERSHEY_SIMPLEX,0.1,(255,255,255),1)
            Remember3.append(tem)
        Remember2 = Canvas
        return Canvas  # 将制作好的画布返回

class Vidio(object):  # 视频类
    def __init__(self, root):
        self.sample = cv2.VideoCapture(root, cv2.IMREAD_GRAYSCALE)  # 正常读入视频
    def Show(self):
        if_can = self.sample.isOpened()  # 判断是否可以正常打开
        while if_can:
            tem, flame = self.sample.read(cv2.IMREAD_GRAYSCALE)  # 获取每帧的图像信息
            if flame is None:  # 如果读取的图像为空，结束
                break
            else:
                flame = cv2.cvtColor(flame, cv2.COLOR_BGR2GRAY)  # 转化为灰度图
                used = Paint(flame)  # 将图片置为paint类进行转化
                image = used.Paint_Canvas()
                cv2.imshow('point esc to quit',image)  # 展示
                if cv2.waitKey(10) & 0xFF == 27:  # 等待10ms或者按下退出键结束
                    break

class Picture(Paint):  # 图片类
    def Show(self):
        global Remember1
        image = self.Paint_Canvas()  # 直接转为paint类
        Remember1 = image
        cv2.imshow('image', image)
        # 将关闭模式设为判断窗口是否存在，这样可以避免如果没有按esc关闭导致的程序卡死问题
        while True:
            if cv2.getWindowProperty('image', 0) == -1:  # 如果窗口关闭
                break
            cv2.waitKey(1)

# 判断输入的是图像还是视频
def Judge_form(root):
    vidio_ = ['mp4', 'avi', 'wmv', 'm4v', 'flv', 'f4v']  # 视频常见格式
    Picture_ = ['jpg', 'png', 'bmp']  # 图片常见格式
    root.replace('\\', '/')  # 将'\'转化为'/'，防止转义
    if root[-3:] in Picture_:  # 切片判断
        begin = Picture(root)
        begin.Show()
    elif root[-3:] in vidio_:
        begin = Vidio(root)
        begin.Show()

def give_out():
    return Remember1

if __name__ == '__main__':
    a = 0