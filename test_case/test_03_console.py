# coding:utf-8
import time
import pyautogui
import unittest
import cv2
import numpy as np
import pyautogui as auto


# @unittest.skip("skipping")
class testConsole(unittest.TestCase):

    # 查看潜力用户列表
    def testConsole01(self):
        time.sleep(3)
        pyautogui.click(1742, 156)
        time.sleep(3)
        pyautogui.click(1629, 199)
        time.sleep(3)
        pyautogui.click(1697, 198)
        time.sleep(3)
        pyautogui.click(1867, 195)
        time.sleep(3)
        pyautogui.click(1859, 219)
        time.sleep(3)
        pyautogui.click(1773, 195)
        time.sleep(3)
        pyautogui.click(1867, 195)
        time.sleep(3)
        pyautogui.click(1859, 219)

    # 查看联系人：陌生人列表、好友列表、亲密好友
    def testConsole02(self):
        time.sleep(3)
        pyautogui.click(1630, 159)
        time.sleep(3)
        pyautogui.click(1604, 260)
        time.sleep(3)
        pyautogui.click(1604, 260)
        time.sleep(3)
        pyautogui.click(1615, 299)
        time.sleep(3)
        pyautogui.click(1615, 299)
        time.sleep(3)
        pyautogui.click(1618, 341)
        time.sleep(3)
        pyautogui.click(1618, 341)

    # 查看消息列表
    def testConsole03(self):
        time.sleep(3)
        pyautogui.click(1844, 159)
        time.sleep(3)
        pyautogui.doubleClick(1679, 212)
        time.sleep(3)
        pyautogui.click(1164, 304)
        time.sleep(3)
        pyautogui.doubleClick(1717, 272)
        time.sleep(3)
        pyautogui.click(1167, 307)

    # 加好友：找人、找主播
    def testConsole04(self):
        time.sleep(3)
        pyautogui.click(1628, 158)
        time.sleep(3)
        pyautogui.click(1661, 749)
        time.sleep(3)
        pyautogui.click(789, 351)
        time.sleep(3)
        pyautogui.write("11")
        time.sleep(3)
        pyautogui.click(1179, 351)
        time.sleep(3)
        pyautogui.click(1180, 417)
        time.sleep(3)
        pyautogui.click(958, 584)

        time.sleep(3)
        pyautogui.click(858, 299)
        time.sleep(3)
        pyautogui.click(1177, 350)
        time.sleep(3)
        pyautogui.click(1173, 417)
        time.sleep(3)
        pyautogui.click(957, 579)
        time.sleep(3)
        pyautogui.click(1202, 292)

    #连麦
    def testConsole05(self):
        time.sleep(3)
        pyautogui.click(1815, 750)
        time.sleep(3)
        pyautogui.click(803, 351)
        time.sleep(3)
        pyautogui.write("11")
        time.sleep(3)
        pyautogui.click(1181, 353)
        time.sleep(3)
        pyautogui.click(904, 417)
        time.sleep(3)
        pyautogui.click()


if __name__ == '__main__':
    unittest.main()  # unittest 的执行
