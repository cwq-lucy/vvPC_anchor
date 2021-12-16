# coding:utf-8
import time
import pyautogui
import unittest
import cv2
import numpy as np
import pyautogui as auto


#
# 问题：鼠标点击无响应问题（需要管理员身份进行运行才能触发点击效果）
#

# @unittest.skip("skipping")
class testLogin(unittest.TestCase):
    # 手机号登录
    #@unittest.skip("skipping")
    def testLogin01(self):
        # 移至应用程序桌面图标，双击打开运行应用程序
        pyautogui.moveTo(1025, 541, duration=1)
        pyautogui.doubleClick()
        time.sleep(10)

        pyautogui.doubleClick(906, 551)
        time.sleep(1)
        pyautogui.write("15112378424")
        time.sleep(3)
        pyautogui.doubleClick(910, 608)
        time.sleep(1)
        pyautogui.write("110016117")
        time.sleep(3)
        pyautogui.click(1023, 648)
        time.sleep(3)
        pyautogui.click(953, 692)

    # 用户账号不存在
    # @unittest.skip("skipping")
    def testLogin02(self):
        time.sleep(10)
        # 移至应用程序桌面图标，双击打开运行应用程序
        pyautogui.moveTo(1025, 541, duration=1)
        pyautogui.doubleClick()
        time.sleep(10)

        pyautogui.doubleClick(906, 551)
        time.sleep(1)
        pyautogui.write("110000000")
        time.sleep(3)
        pyautogui.doubleClick(910, 608)
        time.sleep(1)
        pyautogui.write("110016117")
        time.sleep(3)
        pyautogui.click(953, 692)

    # 密码错误
    @unittest.skip("skipping")
    def testLogin03(self):
        # 移至应用程序桌面图标，双击打开运行应用程序
        pyautogui.moveTo(1025, 541, duration=1)
        pyautogui.doubleClick()
        time.sleep(10)

        pyautogui.doubleClick(906, 551)
        time.sleep(1)
        pyautogui.write("15112378424")
        time.sleep(3)
        pyautogui.doubleClick(910, 608)
        time.sleep(1)
        pyautogui.write("cuowumima1")
        time.sleep(3)
        pyautogui.click(953, 692)


    #@unittest.skip("skipping")
    def testLogin04(self):
        time.sleep(10)
        # 移至应用程序桌面图标，双击打开运行应用程序
        pyautogui.moveTo(1025, 541, duration=1)
        pyautogui.doubleClick()
        time.sleep(10)

        pyautogui.doubleClick(906, 551)
        time.sleep(1)
        pyautogui.write("110013889")
        time.sleep(3)
        pyautogui.doubleClick(910, 608)
        time.sleep(1)
        pyautogui.write("110016117")
        time.sleep(3)
        pyautogui.click(1023, 648)
        time.sleep(3)
        pyautogui.click(953, 692)


if __name__ == '__main__':
    unittest.main()  # unittest 的执行
