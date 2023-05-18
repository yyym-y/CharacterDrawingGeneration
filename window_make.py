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
