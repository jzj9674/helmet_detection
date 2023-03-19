# coding=utf-8
import tkinter
import tkinter.filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os

# 检测结果图片
tkImage = None


def show_detection_image(win):
    """
    显示图片检测结果
    :param win: 创建句柄
    :return: null
    """
    global tkImage
    path, shotname, extension = selectPath()
    print(path)
    print(shotname)
    exec_parms = """
       python detect.py --cfg cfg/yolov3-tiny3-final.cfg --weights weights/best260.pt --source """ + path + " --name data/template.names --device cpu"
    # print(exec_parms)
    messagebox.showinfo('稍等...', '稍等...')
    os.system(exec_parms)
    output_path = "./output/" + shotname + extension
    print(output_path)
    pilImage = Image.open(output_path)
    img = pilImage.resize((600, 500), Image.ANTIALIAS)
    tkImage = ImageTk.PhotoImage(image=img)
    label = tkinter.Label(win, image=tkImage, width=600, height=500)
    label.place(x=120, y=20)


def show_detection_camera():
    """
    摄像头目标检测
    :return:
    """
    exec_parms = """
           python detect.py --cfg cfg/yolov3-tiny3-final.cfg --weights weights/best260.pt --source 0 --name data/template.names --device cpu"""
    # print(exec_parms)
    messagebox.showinfo('稍等...', '稍等...')
    os.system(exec_parms)


def init_component(win):
    """
     初始化组件
    :param win: 窗口句柄
    :return: null
    """
    btn_dete_image = tkinter.Button(win, text='打开 图片', width=10, height=2, command=lambda: show_detection_image(win))
    btn_dete_camera = tkinter.Button(win, text='打开摄像头', width=10, height=2, command=show_detection_camera)
    btn_dete_vedio = tkinter.Button(win, text='打开 视频', width=10, height=2, command=show_detection_vedio)
    btn_dete_image.place(x=20, y=100)
    btn_dete_camera.place(x=20, y=200)
    btn_dete_vedio.place(x=20, y=300)


def show_detection_vedio():
    # print(selectPath())
    file = selectPath()
    print(file)
    if file[0] is "":
        return ;
    path = file[0]
    vedio = os.getcwd() + "\\output\\" + file[1] + file[2];
    print(vedio)
    path1 = "python detect.py --cfg cfg/yolov3-tiny3-final.cfg --weights weights/best260.pt --name data/template.names --source ";
    result_path = path1 + path
    print(result_path)
    messagebox.showinfo('稍等...', '稍等... cmd 窗口 显示执行结果 执行完成显示视频检测结果')
    os.system(result_path)
    messagebox.showinfo('稍等...', '稍等... 即将显示视频执行结果')
    os.system("start " + vedio)


def init_win():
    """
        初始化窗口
    :return:null
    """
    win = tkinter.Tk()
    win.title("安全帽检测")
    mw, mh = win.maxsize()
    win.geometry('800x500+%d+%d' % ((mw - 800) / 2, (mh - 500) / 2))  # 窗口居中
    init_component(win)
    win.resizable(False, False)
    win.protocol("WM_DELETE_WINDOW", lambda: sys.exit(0));
    win.mainloop()


def selectPath():
    """
    选择路径
    :return:
    """
    # 选择文件path_接收文件地址
    path_ = tkinter.filedialog.askopenfilename()

    # 注意：\\转义后为\，所以\\\\转义后为\\
    path_ = path_.replace("/", "\\")
    filepath, tmpfilename = os.path.split(path_)
    shotname, extension = os.path.splitext(tmpfilename)
    return path_, shotname, extension


if __name__ == "__main__":
    init_win()
