# 基于Opencv的字符画自动生成



## **Updata**

这个项目本来是大一上的python大作业，之前发在CSDN上做纪念，下学期突发奇想想要发到GitHub上

码力非常弱，可能有许多错误，望各位打大佬指点

CSDN链接 ： [ 基于Opencv的字符画自动生成_yyym__的博客-CSDN博客](https://blog.csdn.net/weixin_73503181/article/details/128396671)

:smile:



## 简述

其实很早之前就把这个做好了，毕竟要交大作业，为此学了一个星期的Opencv.....还用上了我行将就木的tkinter.....

好吧，我的代码风格不是很好，yysy是第一次尝试类的模式编程

具体的原理就是把图像灰度读入，然后再根据灰度值选择合适的字符，不难吧....

另外，这是我今年的大作业，要抄的话please等到明年，谢谢...

还有，今年寒假学算法，欢迎某位大佬为我的算法笔记指点...

好了好了，废话不说了，说一下使用准则，顺便把答辩时的解释思维附上：



main.py文件不能在有中文的路径下执行，否则字符画的保存将受影响
这是受制于opencv的imwrite的特性
同理：
选择的图片不能在有中文的路径下
这是受制于opencv的imopen

对了，可以用pystaller来生成可执行exe文件，这样可以直接发给你的好朋友zhuang B



<img src="https://img-blog.csdnimg.cn/5fdbbe83b6fa487f89ba6bc40d21a05a.png" alt="image-20230518180557112" style="zoom:80%;" />



## main.py

![img](https://img-blog.csdnimg.cn/6552db7c41194daf90cd458eb9715304.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

```py
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
    pass
```



## window_make.py

其实我觉得我的窗口做的稀烂

![img](https://img-blog.csdnimg.cn/da8dec899c554f1d8a401cfbc1ae685f.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

```py
import tkinter as tk  # 导入tkinter
import cv2
from tkinter import filedialog  # 导入 filedialog
import paint  # 导入paint
import expand  # 导入expand
class MakeWindow(object):  # 窗口类
    def __init__(self):
        # 之后所需要的变量
        self.give = None
        self.put = None
        self.entry_text = None
        self._root = tk.Tk()  # 建立窗口
        self._root.geometry('500x400')  # 设置大小
        self.space = ['基于OpenCv的字符画自动生成及其应用','方法一:请输入想打开文件的绝对路径',
                      '方法二:选择文件（路径不要包含中文）', '开始生成']  # 所需要的文字
        self._root.title(self.space[0])

    def Label(self):
        # 标题
        introduce = tk.Label(self._root, text=self.space[0], bg='white', font=('Arial', 15), width=40, height=2)
        # 方法一
        info1 = tk.Label(self._root, text=self.space[1], bg='white',font=('Arial', 10),height=2)
        # 方法二
        info2 = tk.Label(self._root, text=self.space[2], bg='white',font=('Arial', 10),height=2)
        introduce.grid(row=0, column=0, padx=30, pady=20,columnspan=10)
        info1.grid(row=1, column=0,padx=30, pady=10, sticky='w', columnspan=5)
        info2.grid(row=3, column=0,padx=30, pady=10, sticky='w',columnspan=5)

    def Button(self):
        def get_space():  # 获取内容
            self.give = self.put.get()
            paint.Judge_form(self.give)

        def get_path():  # 获得路径
            path = filedialog.askopenfilename(title='请选择文件')
            self.entry_text.set(path)
        # 开始生成
        check = tk.Button(self._root, text=self.space[3],bg='red',height=2,width=10,command=get_space)
        # 选择路径
        Search = tk.Button(self._root, text='选择路径', command=get_path, bg='pink')
        # 保存图片
        Remember1 = tk.Button(self._root, text='保存图片', command=expand.Remember_image, bg='pink')
        # 保存为txt
        Remember2 = tk.Button(self._root, text='保存为txt', command=expand.Form_TXT, bg='pink')
        check.grid(row=5, column=4,)
        Search.grid(row=3, column=6)
        Remember1.grid(row=8, column=2,pady=5)
        Remember2.grid(row=8, column=6,pady=5)

    def Entry(self):  # 输入绝对路径
        self.entry_text = tk.StringVar()
        self.put = tk.Entry(self._root, textvariable=self.entry_text, width=50)
        self.put.grid(row=2, column=0,columnspan=10)

    def Warming(self):
        write = ["注：关闭视频时按esc退出，选择图片时路径不可有中文，视频路径无限制"]
        info2 = tk.Label(self._root, text=write, bg='white', font=('Arial', 10), height=3,width=60)
        info2.grid(row=10,column=1,sticky='w',columnspan=10)

    def Show(self):  # 展示
        self.Label()
        self.Entry()
        self.Button()
        self.Warming()
        self._root.mainloop()


if __name__ == '__main__':
    a = MakeWindow()
    a.Show()
```

## expand.py

![img](https://img-blog.csdnimg.cn/66ffc2834256468186bf6405e27f5934.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

```py
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
```



##  **main.py**

一个我觉得很多余但是还是像这样干的文件

```py
import window_make
Finally = window_make.MakeWindow()
Finally.Show()
```



## 最后的执行效果

Vedio

看我坤哥：

![img](https://img-blog.csdnimg.cn/eb4e3847abda40f4806158c23aa3020e.png)

Picture

这是一个霸屏我的VS， Wallpaper的动漫角色，虽然我不知道是谁

![img](https://img-blog.csdnimg.cn/bbee4a8e5946494ba5f94ab9d47d3775.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

 另外

再窗口设计这方面此程序还有些许不足，但是我懒的改

对了

大家玩的过程要是要啥问题可以评论，放心，绝对不会改