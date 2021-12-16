# coding:utf-8
import time
import pyautogui
import unittest
import cv2
import numpy as np
import pyautogui as auto


# @unittest.skip("skipping")
class testOPlayer(unittest.TestCase):

    def login(self):
        # 移至应用程序桌面图标，双击打开运行应用程序
        pyautogui.moveTo(952, 540, duration=1)
        pyautogui.doubleClick()
        time.sleep(10)
        # 移至登录输入框，输入账号和密码
        pyautogui.moveTo(590, 432, duration=1)
        pyautogui.doubleClick()
        pyautogui.typewrite('110028893', interval=0.25)
        pyautogui.moveTo(611, 506, duration=1)
        pyautogui.doubleClick()
        pyautogui.typewrite('110016117', interval=0.25)
        login_button = auto.locateOnScreen('../source_photoes/login/login_button.png')  # 传入登录按钮的图片
        time.sleep(3)
        auto.screenshot('../photoes/login/login_button.png', region=(531, 647, 368, 60))  # 校对图片位置
        auto.click(login_button)  # 点击登录按钮

    # 编辑公告
    # @unittest.skip("skipping")
    def testRoom01(self):
        # self.login()
        edit_affiche = auto.locateOnScreen('../source_photoes/room/edit_affiche.png')
        auto.click(edit_affiche)
        time.sleep(1)
        pyautogui.typewrite('huanyinglaidaolvsezhibojian1')
        save = auto.locateOnScreen('../source_photoes/room/save.png')
        auto.click(save)
        time.sleep(3)
        audit = auto.locateOnScreen('../source_photoes/room/audit.png')
        print(audit)
        time.sleep(1)
        auto.screenshot('../photoes/room/audit.png', region=(831, 436, 258, 145))
        time.sleep(3)
        roger = auto.locateOnScreen('../source_photoes/room/roger.png')
        auto.click(roger)

        # 图片断言
        image1 = cv2.imread("../source_photoes/room/audit.png")
        image2 = cv2.imread("../photoes/room/audit.png")
        difference = cv2.subtract(image1, image2)
        result = not np.any(difference)
        self.assertTrue(result, "图片飞走了~")



if __name__ == '__main__':
    unittest.main()  # unittest 的执行
