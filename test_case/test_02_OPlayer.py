# coding:utf-8
import time
import pyautogui
import unittest
import cv2
import numpy as np
import pyautogui as auto

class testOplayer(unittest.TestCase):

    #开播操作
    def testOplayer01(self):
        time.sleep(10)
        pyautogui.click(1737, 206)
        time.sleep(3)
        pyautogui.click(949, 580)
        time.sleep(3)
        pyautogui.click(940, 652)
        time.sleep(3)
        pyautogui.click(1266, 221)
        time.sleep(3)
        pyautogui.click(965, 878)
        time.sleep(3)
        pyautogui.click(1266, 221)

    # 查看潜力用户
    def testOplayer02(self):
        time.sleep(3)
        pyautogui.click(553, 200)
        time.sleep(3)
        pyautogui.click(810, 340)
        time.sleep(3)
        pyautogui.click(963, 335)
        time.sleep(3)
        pyautogui.click(1103, 341)
        time.sleep(3)
        pyautogui.click(1139, 372)
        time.sleep(3)
        pyautogui.click(1141, 397)
        time.sleep(3)
        pyautogui.click(1173, 280)
        time.sleep(3)

    # 查看豪客榜单
    def testOplayer03(self):
        time.sleep(3)
        pyautogui.click(515, 232)
        time.sleep(3)
        pyautogui.click(409, 317)
        time.sleep(3)
        pyautogui.click(587, 320)

    # 查看公聊发送消息
    def testOplayer04(self):
        time.sleep(3)
        pyautogui.click(1375, 130)
        time.sleep(3)
        pyautogui.click(1351, 701)
        time.sleep(3)
        pyautogui.click(1373, 645)
        time.sleep(3)
        pyautogui.write("181818")
        time.sleep(3)
        pyautogui.click(1566, 895)
        time.sleep(3)

    # 贵族气泡选择及发送消息
    def testOplayer05(self):
        time.sleep(3)
        pyautogui.click(1386, 696)
        time.sleep(3)
        pyautogui.click(901, 428)
        time.sleep(3)
        pyautogui.click(1043, 663)
        time.sleep(3)
        pyautogui.click(961, 581)
        time.sleep(3)
        pyautogui.click(1429, 748)
        time.sleep(3)
        pyautogui.write("181818")
        time.sleep(3)
        pyautogui.click(1556, 897)
        time.sleep(3)
        pyautogui.click(1384, 697)
        time.sleep(3)
        pyautogui.click(770, 429)
        time.sleep(3)
        pyautogui.click(1051, 661)
        time.sleep(3)
        pyautogui.click(965, 584)
        time.sleep(3)
        pyautogui.click(1400, 766)
        time.sleep(3)
        pyautogui.write("181818")
        time.sleep(3)
        pyautogui.click(1552, 898)

    # 查看私聊及发送消息
    def testOplayer06(self):
        time.sleep(3)
        pyautogui.click(1549, 131)
        time.sleep(3)
        pyautogui.click(412, 532)
        time.sleep(3)
        pyautogui.rightClick()
        time.sleep(3)
        pyautogui.click(454, 620)
        time.sleep(3)
        pyautogui.click(1395, 740)
        time.sleep(3)
        pyautogui.write("181818")
        time.sleep(3)
        pyautogui.click(1348, 696)
        time.sleep(3)
        pyautogui.click(1351, 482)
        time.sleep(3)
        pyautogui.click(1558, 897)

    # 添加整蛊项目
    def testOplayer07(self):
        time.sleep(3)
        pyautogui.click(1253, 894)
        time.sleep(3)
        pyautogui.click(1173, 419)
        time.sleep(3)
        pyautogui.click(1146, 359)
        time.sleep(3)
        pyautogui.click(930, 427)
        time.sleep(3)
        pyautogui.click(809, 521)
        time.sleep(3)
        pyautogui.click(1118, 764)
        time.sleep(3)
        pyautogui.click(959, 581)

    # 修改整蛊项目
    def testOplayer08(self):
        time.sleep(3)
        pyautogui.click(1255, 896)
        time.sleep(3)
        pyautogui.click(839, 438)
        time.sleep(3)
        pyautogui.click(1176, 471)
        time.sleep(3)
        pyautogui.click(1154, 361)
        time.sleep(3)
        pyautogui.click(853, 461)
        time.sleep(3)
        pyautogui.click(923, 519)
        time.sleep(3)
        pyautogui.click(796, 692)
        time.sleep(3)
        pyautogui.click(1118, 767)
        time.sleep(3)
        pyautogui.click(957, 581)
        time.sleep(3)
        pyautogui.click(1164, 748)

    # 删除整蛊项目
    def testOplayer09(self):
        time.sleep(3)
        pyautogui.click(1255, 895)
        time.sleep(3)
        pyautogui.click(827, 437)
        time.sleep(3)
        pyautogui.click(1177, 680)
        time.sleep(3)
        pyautogui.click(1210, 305)

    #送礼物
    def testOplayer10(self):
        time.sleep(3)
        pyautogui.click(1297, 895)
        time.sleep(3)
        pyautogui.click(1335, 640)
        time.sleep(3)
        pyautogui.click(1610, 857)  #发送小星星

        time.sleep(3)
        pyautogui.click(1316, 586)
        time.sleep(3)
        pyautogui.click(1333, 642)
        time.sleep(3)
        pyautogui.click(1606, 860)  #发送包裹礼物

        time.sleep(3)
        pyautogui.click(1377, 586)
        time.sleep(3)
        pyautogui.click(1335, 658)
        time.sleep(3)
        pyautogui.click(1607, 855)  #发送整蛊礼物

        time.sleep(3)
        pyautogui.click(1627, 585)
        time.sleep(3)
        pyautogui.click(1333, 633)
        time.sleep(3)
        pyautogui.click(1611, 858)  #发送盖章礼物
        pyautogui.click(1611, 1000)

    #房间大banner跳转
    def testOplayer11(self):
        count = 0
        nums = 5
        while (count < nums):
            time.sleep(1)
            tia = auto.locateOnScreen('../source_photoes/room/daojubanner.png')
            if (tia != None):
                auto.screenshot('../photoes/room/daojubanner.png', region=(1216, 714, 103, 158))
                pyautogui.click(1276, 783)
                break
            count = count + 1

    #钓鱼操作
    def testOplayer12(self):
        time.sleep(3)
        pyautogui.click(789, 509)
        time.sleep(3)
        pyautogui.scroll(-20000)
        time.sleep(3)
        pyautogui.click(1092, 332)
        time.sleep(3)
        pyautogui.click(871, 625)
        time.sleep(3)
        pyautogui.click(958, 628)
        time.sleep(3)
        pyautogui.click(1078, 816)

        time.sleep(3)
        pyautogui.click(956, 557)
        time.sleep(5)
        pyautogui.click(1151, 419)  # 单次池塘钓鱼

        time.sleep(3)
        pyautogui.click(1078, 757)
        time.sleep(3)
        pyautogui.click(956, 552)  # 十连池塘钓鱼
        time.sleep(5)
        pyautogui.click(1155, 417)

        time.sleep(3)
        pyautogui.click(1052, 329)
        time.sleep(3)
        pyautogui.click(959, 552)  # 单次海边钓鱼
        time.sleep(5)
        pyautogui.click(1153, 420)

        time.sleep(3)
        pyautogui.click(1082, 756)
        time.sleep(3)
        pyautogui.click(960, 551)  # 十连海边钓鱼
        time.sleep(5)
        pyautogui.click(1153, 302)
        time.sleep(1)
        pyautogui.click(1174, 322)  # 关闭钓鱼窗口

    #宣言操作
    def testOplayer13(self):
        self.testOplayer11()

        time.sleep(5)
        pyautogui.click(903, 509)
        pyautogui.scroll(-20000)
        time.sleep(3)
        pyautogui.click(1095, 326)
        time.sleep(3)
        pyautogui.click(872, 626)
        time.sleep(3)
        pyautogui.click(955, 629)
        time.sleep(3)
        pyautogui.click(1075, 814)  #跳转宣言界面

        time.sleep(3)
        pyautogui.click(807, 490)
        time.sleep(3)
        pyautogui.click(883, 759)
        time.sleep(3)
        pyautogui.click(920, 687)

        time.sleep(6)
        pyautogui.click(958, 491)
        time.sleep(3)
        pyautogui.click(887, 756)   #批量10个宣言

        time.sleep(6)
        pyautogui.click(1102, 493 )
        time.sleep(3)
        pyautogui.click(885, 755)   #批量50个宣言

        time.sleep(6)
        pyautogui.click(1178, 335)  #关闭宣言弹窗

    # 凤凰进化
    # 抽取蛋
    def testOplayer14(self):
        self.testOplayer11()

        time.sleep(5)
        pyautogui.click(1026, 512)
        pyautogui.scroll(-20000)
        time.sleep(3)
        pyautogui.click(1100, 354)
        time.sleep(3)
        pyautogui.click(871, 629)
        time.sleep(3)
        pyautogui.click(955, 627)
        time.sleep(3)
        pyautogui.click(1075, 814)  #跳转凤凰界面

        time.sleep(3)
        pyautogui.click(803, 560)
        time.sleep(3)
        pyautogui.click(825, 849)
        time.sleep(10)
        pyautogui.doubleClick(954, 720)
        time.sleep(3)
        pyautogui.click(954, 722)  #召唤1次吉利蛋

        time.sleep(3)
        pyautogui.click(955, 849)
        time.sleep(10)
        pyautogui.doubleClick(954, 720)
        time.sleep(3)
        pyautogui.click(954, 722)  #召唤5次吉利蛋

        time.sleep(3)
        pyautogui.click(1091, 847)
        time.sleep(10)
        pyautogui.doubleClick(954, 720)
        time.sleep(3)
        pyautogui.click(954, 722)  #召唤10次吉利蛋

    # 凤凰进化
    def testOplayer15(self):
        time.sleep(3)
        pyautogui.click(1096, 561)
        time.sleep(3)
        pyautogui.click(826, 847)
        time.sleep(10)
        pyautogui.click(948, 720)

        time.sleep(3)
        pyautogui.click(956, 849)
        time.sleep(10)
        pyautogui.click(948, 720)

        time.sleep(3)
        pyautogui.click(1085, 851)
        time.sleep(10)
        pyautogui.click(948, 720)

        time.sleep(3)
        pyautogui.click(1188, 352)

    # 购买座驾
    def testOplayer16(self):
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()  # unittest 的执行