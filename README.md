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




## window_make.py

其实我觉得我的窗口做的稀烂

![img](https://img-blog.csdnimg.cn/da8dec899c554f1d8a401cfbc1ae685f.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

## expand.py

![img](https://img-blog.csdnimg.cn/66ffc2834256468186bf6405e27f5934.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)



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
