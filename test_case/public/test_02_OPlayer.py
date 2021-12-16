# coding:utf-8
import time
import pyautogui
import unittest
import cv2
import numpy as np
import pyautogui as auto

class testOplayer(unittest.TestCase):
    # 手机号登录
    #@unittest.skip("skipping")
    def testOplayer01(self):
        time.sleep(10)
        pyautogui.click(1737, 206)
        time.sleep(3)
        pyautogui.click(949, 580)
        time.sleep(3)
        pyautogui.click(940, 652)
        time.sleep(3)
        pyautogui.click(965, 878)

    # 查看潜力用户
    def testOplayer02(self):
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
