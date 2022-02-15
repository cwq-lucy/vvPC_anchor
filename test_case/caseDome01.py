import pyautogui as auto
import cv2
import numpy as np
import pyautogui
import time
import unittest

# try:
#     number7_location = auto.locateOnScreen('../source_photoes/login_gui.png')   #传入按钮的图片
#     print(number7_location)  # 返回屏幕所在位置
#     x,y = auto.center(number7_location)  # 转化为 x,y坐标
#     print(x,y)  #按键7的坐标是1441,582
#     auto.click(number7_location)
#     # 点击坐标，click()它是支持元组格式的坐标传入的
#
# except:
#     print("找不到图片")

###
# image图像比较
###

# @unittest.skip("skipping")
class TestPC(unittest.TestCase):
    @unittest.skip("skipping")
    def test01(self):
        image1 = cv2.imread("../source_photoes/login.png")
        image2 = cv2.imread("../Photoes/login_button.png")

        difference = cv2.subtract(image1, image2)
        print(difference)
        result = not np.any(difference)
        print(result)

        # login = auto.locateOnScreen('../source_photoes/login/login_success.png')   #获取本地图片位置
        # print(login)
        # auto.screenshot('../photoes/login/login_success.png', region=(1663, 57, 94, 27))  # 截取登录成功图片

        # # 图片断言
        # image1 = cv2.imread("../source_photoes/login/user_error.png")
        # image2 = cv2.imread("../photoes/login/user_error.png")
        # difference = cv2.subtract(image1, image2)
        # result = not np.any(difference)
        # self.assertTrue(result, "图片飞走了~")

    #定位鼠标坐标
    # @unittest.skip("skipping")
    def test02(self):
        try:
            while 1:
                time.sleep(10)
                x, y = pyautogui.position()
                print(x, y)
        except:
            pass

    #代码生成
    def test03(self):
        count = 0
        nums = 5
        while (count < nums):
            print("time.sleep(3)")
            print("pyautogui.click()")
            count = count + 1

        time.sleep(1)
        print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #针对banner图轮播，进行循环截图断言
    def test04(self):
        count = 0
        nums = 500
        while (count < nums):
            time.sleep(10)
            pyautogui.moveTo(522, 371)
            time.sleep(10)
            pyautogui.moveTo(767, 371)
            count = count + 1

        time.sleep(1)
        print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #针对视频分解为静态图
    def test05(self):
        cap = cv2.VideoCapture(r'D:\ApowerREC\test.mp4')
        isOpened = cap.isOpened()
        fps = cap.get(cv2.CAP_PROP_FPS)  # 帧率<每秒中展示多少张图片>
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取宽度
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 获取宽度
        print(fps, width, height)

        i = 0
        while (isOpened):  # 当视频被打开了
            if i == 5:
                break  # 读取10张图片就够了
            else:
                i = i + 1  # i++
                (flag, frame) = cap.read()  # 读取每一张 flag<读取是否成功> frame<内容>
                filename = r'D:\ApowerREC\test\image' + str(i) + '.jpg' #指定图片保存路径
                print(filename)
                if flag == True:  # 读取成功的话
                    cv2.imwrite(filename, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
                # 写入文件，1 文件名 2 文件内容 3 质量设置
        print("end!")


if __name__ == '__main__':
    unittest.main()  # unittest 的执行
