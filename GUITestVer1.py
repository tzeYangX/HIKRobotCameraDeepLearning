# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestGUI1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Camera_SDK.CamOperation_class import CameraOperation
from MvCameraControl_class import *
from MvErrorDefine_const import *
from CameraParams_header import *
import cv2, imutils, threading
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QTimer
from mmcv import Config
from mmcv.runner import load_checkpoint
from mmdet.apis import inference_detector, show_result_pyplot
from mmdet.models import build_detector
import numpy as np
from model import detect_center
import time


def TxtWrapBy(start_str, end, all):
    start = all.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = all.find(end, start)
        if end >= 0:
            return all[start:end].strip()


def ToHexStr(num):
    chaDic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    hexStr = ""
    if num < 0:
        num = num + 2 ** 32
    while num >= 16:
        digit = num % 16
        hexStr = chaDic.get(digit, str(digit)) + hexStr
        num //= 16
    hexStr = chaDic.get(num, str(num)) + hexStr
    return hexStr


global deviceList
deviceList = MV_CC_DEVICE_INFO_LIST()
global cam
cam = MvCamera()
global nSelCamIndex
nSelCamIndex = 0
global obj_cam_operation
obj_cam_operation = 0
global isOpen
isOpen = False
global isGrabbing
isGrabbing = False
global isCalibMode  # CalibMode check
isCalibMode = True

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1339, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 771, 551))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(260, 200, 63, 20))
        self.label.setText("")
        self.label.setObjectName("label")
        self.displayLabel = QtWidgets.QLabel(self.groupBox)
        self.displayLabel.setGeometry(QtCore.QRect(10, 20, 741, 511))
        self.displayLabel.setText("")
        self.displayLabel.setObjectName("displayLabel")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(800, 10, 261, 551))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboDevices = QtWidgets.QComboBox(self.groupBox_2)
        self.comboDevices.setGeometry(QtCore.QRect(20, 30, 231, 31))
        self.comboDevices.setObjectName("comboDevices")
        self.btnEnum = QtWidgets.QPushButton(self.groupBox_2)
        self.btnEnum.setGeometry(QtCore.QRect(20, 70, 231, 31))
        self.btnEnum.setObjectName("btnEnum")
        self.btnOpen = QtWidgets.QPushButton(self.groupBox_2)
        self.btnOpen.setGeometry(QtCore.QRect(20, 110, 101, 31))
        self.btnOpen.setObjectName("btnOpen")
        self.btnClose = QtWidgets.QPushButton(self.groupBox_2)
        self.btnClose.setGeometry(QtCore.QRect(150, 110, 101, 31))
        self.btnClose.setObjectName("btnClose")
        self.radioContinueMode = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioContinueMode.setGeometry(QtCore.QRect(20, 150, 110, 24))
        self.radioContinueMode.setObjectName("radioContinueMode")
        self.radioTriggerMode = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioTriggerMode.setGeometry(QtCore.QRect(160, 150, 110, 24))
        self.radioTriggerMode.setObjectName("radioTriggerMode")
        self.bnStart = QtWidgets.QPushButton(self.groupBox_2)
        self.bnStart.setGeometry(QtCore.QRect(20, 220, 101, 29))
        self.bnStart.setObjectName("bnStart")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 101, 21))
        self.label_2.setObjectName("label_2")
        self.editTimeTrigger = QtWidgets.QTextEdit(self.groupBox_2)
        self.editTimeTrigger.setGeometry(QtCore.QRect(150, 180, 101, 31))
        self.editTimeTrigger.setObjectName("editTimeTrigger")
        self.bnStop = QtWidgets.QPushButton(self.groupBox_2)
        self.bnStop.setGeometry(QtCore.QRect(152, 220, 101, 29))
        self.bnStop.setObjectName("bnStop")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 360, 261, 181))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 120, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnGetParam = QtWidgets.QPushButton(self.groupBox_3)
        self.btnGetParam.setGeometry(QtCore.QRect(20, 150, 101, 29))
        self.btnGetParam.setObjectName("btnGetParam")
        self.btnSetParam = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSetParam.setGeometry(QtCore.QRect(152, 150, 101, 29))
        self.btnSetParam.setObjectName("btnSetParam")
        self.edtExposureTime = QtWidgets.QTextEdit(self.groupBox_3)
        self.edtExposureTime.setGeometry(QtCore.QRect(150, 30, 101, 31))
        self.edtExposureTime.setObjectName("edtExposureTime")
        self.edtGain = QtWidgets.QTextEdit(self.groupBox_3)
        self.edtGain.setGeometry(QtCore.QRect(150, 70, 101, 31))
        self.edtGain.setObjectName("edtGain")
        self.edtFrameRate = QtWidgets.QTextEdit(self.groupBox_3)
        self.edtFrameRate.setGeometry(QtCore.QRect(150, 110, 101, 31))
        self.edtFrameRate.setObjectName("edtFrameRate")
        self.Combo_model = QtWidgets.QGroupBox(self.centralwidget)
        self.Combo_model.setGeometry(QtCore.QRect(1070, 10, 241, 261))
        self.Combo_model.setObjectName("Combo_model")
        self.label_13 = QtWidgets.QLabel(self.Combo_model)
        self.label_13.setGeometry(QtCore.QRect(10, 40, 63, 20))
        self.label_13.setObjectName("label_13")
        self.comboModels = QtWidgets.QComboBox(self.Combo_model)
        self.comboModels.setGeometry(QtCore.QRect(80, 30, 151, 31))
        self.comboModels.setObjectName("comboModels")
        self.comboModels.addItem("")
        self.comboModels.addItem("")
        self.comboModels.addItem("")
        self.btnLoadCheckpoint = QtWidgets.QPushButton(self.Combo_model)
        self.btnLoadCheckpoint.setGeometry(QtCore.QRect(10, 70, 221, 31))
        self.btnLoadCheckpoint.setObjectName("btnLoadCheckpoint")
        self.label_18 = QtWidgets.QLabel(self.Combo_model)
        self.label_18.setGeometry(QtCore.QRect(10, 120, 63, 20))
        self.label_18.setObjectName("label_18")
        self.editInferenceTime = QtWidgets.QTextEdit(self.Combo_model)
        self.editInferenceTime.setGeometry(QtCore.QRect(100, 120, 131, 31))
        self.editInferenceTime.setObjectName("editInferenceTime")
        self.label_19 = QtWidgets.QLabel(self.Combo_model)
        self.label_19.setGeometry(QtCore.QRect(10, 170, 71, 21))
        self.label_19.setObjectName("label_19")
        self.editScoreThreshold = QtWidgets.QTextEdit(self.Combo_model)
        self.editScoreThreshold.setGeometry(QtCore.QRect(100, 170, 131, 31))
        self.editScoreThreshold.setObjectName("editScoreThreshold")
        self.btnRunInferenceVideo = QtWidgets.QPushButton(self.Combo_model)
        self.btnRunInferenceVideo.setGeometry(QtCore.QRect(10, 210, 93, 29))
        self.btnRunInferenceVideo.setObjectName("btnRunInferenceVideo")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(1070, 270, 241, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(10, 30, 81, 20))
        self.label_20.setObjectName("label_20")
        self.btnRunCalib = QtWidgets.QPushButton(self.groupBox_4)
        self.btnRunCalib.setGeometry(QtCore.QRect(10, 60, 91, 31))
        self.btnRunCalib.setObjectName("btnRunCalib")
        self.btnLoadCalib = QtWidgets.QPushButton(self.groupBox_4)
        self.btnLoadCalib.setGeometry(QtCore.QRect(130, 60, 101, 31))
        self.btnLoadCalib.setObjectName("btnLoadCalib")
        self.editLoadedCalib = QtWidgets.QTextEdit(self.groupBox_4)
        self.editLoadedCalib.setGeometry(QtCore.QRect(100, 20, 131, 31))
        self.editLoadedCalib.setObjectName("editLoadedCalib")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(1070, 370, 241, 191))
        self.groupBox_5.setObjectName("groupBox_5")
        self.btnRunInference = QtWidgets.QPushButton(self.groupBox_5)
        self.btnRunInference.setGeometry(QtCore.QRect(10, 60, 91, 31))
        self.btnRunInference.setObjectName("btnRunInference")
        self.btnLoadImage = QtWidgets.QPushButton(self.groupBox_5)
        self.btnLoadImage.setGeometry(QtCore.QRect(130, 60, 101, 31))
        self.btnLoadImage.setObjectName("btnLoadImage")
        self.label_21 = QtWidgets.QLabel(self.groupBox_5)
        self.label_21.setGeometry(QtCore.QRect(20, 110, 63, 20))
        self.label_21.setObjectName("label_21")
        self.editInferenceTimeImage = QtWidgets.QTextEdit(self.groupBox_5)
        self.editInferenceTimeImage.setGeometry(QtCore.QRect(100, 110, 131, 31))
        self.editInferenceTimeImage.setObjectName("editInferenceTimeImage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1339, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.model_name = 'solov2' # Default model
        self.run = False
        self.Timer = QTimer()
        self.Timer.timeout.connect(self.trigger_once)

        """
        Connections Connections Connections Connections Connections
        """
        self.retranslateUi(MainWindow)
        self.btnEnum.clicked.connect(self.enum_devices)
        self.btnOpen.clicked.connect(self.open_device)
        self.btnClose.clicked.connect(self.close_device)
        self.bnStart.clicked.connect(self.start_grabbing)
        self.bnStop.clicked.connect(self.stop_grabbing)
        self.btnGetParam.clicked.connect(self.get_param)
        self.btnSetParam.clicked.connect(self.set_param)
        self.radioContinueMode.clicked.connect(self.set_continue_mode)
        self.radioTriggerMode.clicked.connect(self.set_software_trigger_mode)
        self.btnLoadCheckpoint.clicked.connect(self.load_model)
        self.btnRunInferenceVideo.clicked.connect(self.run_model)
        self.btnRunCalib.clicked.connect(self.displayLabel.clear)
        self.btnLoadCalib.clicked.connect(self.displayLabel.clear)
        self.btnRunInference.clicked.connect(self.displayLabel.clear)
        self.btnLoadImage.clicked.connect(self.displayLabel.clear)
        self.comboModels.currentIndexChanged.connect(self.select_model)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    """
    Define functions
    """

    def select_model(self, i):
        if i == 0:
            self.model_name = 'solov2'

    def load_model(self):
        checkpoint = QFileDialog.getOpenFileName()[0]
        cfg = Config.fromfile('mmdetection/configs/solov2/solov2_light_r18_fpn_3x_coco.py')
        cfg.model.mask_head.num_classes = 1

        model = build_detector(cfg.model)
        checkpoint = load_checkpoint(model, checkpoint, map_location='cpu')
        model.CLASSES = checkpoint['meta']['CLASSES']
        model.cfg = cfg
        model.to('cuda')
        model.eval()
        self.model = model


    def run_model(self):
        self.run = True



    def detect(self, image, score_thr_value, center=True):

        self.time_start = time.time()

        result = inference_detector(self.model, image)
        img_show = self.model.show_result(
            image,
            result,
            score_thr=score_thr_value,
            show=False,
            wait_time=0,
            win_name='result',
            bbox_color=None,
            text_color=(200, 200, 200),
            mask_color=None,
            out_file=None)
        if center:
            center_list = detect_center(img_show, result, score_thr_value)
            for center_point in center_list:
                img_show = cv2.circle(img_show, center_point, 10, (255, 0, 0), -1)

        self.time_detect = time.time() - self.time_start
        self.editInferenceTime.setText(str(self.time_detect))

        return img_show


    def set_img_show(self,image):
        """ This function will take image input and resize it
            only for display purpose and convert it to QImage
            to set at the label.
        """
        self.tmp = image
        if image is not None:
            image = imutils.resize(image,width=640)
            frame = image
            # frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
            self.displayLabel.setPixmap(QtGui.QPixmap.fromImage(image))


    def xFunc(event):
        global nSelCamIndex
        nSelCamIndex = TxtWrapBy("[", "]", ui.comboDevices.itemData(ui.comboDevices.currentIndex()))

        # ch:枚举相机 | en:enum devices


    def enum_devices(self):
        global deviceList
        global obj_cam_operation

        deviceList = MV_CC_DEVICE_INFO_LIST()
        ret = MvCamera.MV_CC_EnumDevices(MV_GIGE_DEVICE | MV_USB_DEVICE, deviceList)
        if ret != 0:
            strError = "Enum devices fail! ret = :" + ToHexStr(ret)
            QMessageBox.warning(QMainWindow(), "Error", strError, QMessageBox.Ok)
            return ret

        if deviceList.nDeviceNum == 0:
            QMessageBox.warning(QMainWindow(), "Info", "Find no device", QMessageBox.Ok)
            return ret
        print("Find %d devices!" % deviceList.nDeviceNum)

        devList = []
        for i in range(0, deviceList.nDeviceNum):
            mvcc_dev_info = cast(deviceList.pDeviceInfo[i], POINTER(MV_CC_DEVICE_INFO)).contents
            if mvcc_dev_info.nTLayerType == MV_GIGE_DEVICE:
                print("\ngige device: [%d]" % i)
                chUserDefinedName = ""
                for per in mvcc_dev_info.SpecialInfo.stGigEInfo.chUserDefinedName:
                    if 0 == per:
                        break
                    chUserDefinedName = chUserDefinedName + chr(per)
                print("device user define name: %s" % chUserDefinedName)

                chModelName = ""
                for per in mvcc_dev_info.SpecialInfo.stGigEInfo.chModelName:
                    if 0 == per:
                        break
                    chModelName = chModelName + chr(per)

                print("device model name: %s" % chModelName)

                nip1 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0xff000000) >> 24)
                nip2 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x00ff0000) >> 16)
                nip3 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x0000ff00) >> 8)
                nip4 = (mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x000000ff)
                print("current ip: %d.%d.%d.%d\n" % (nip1, nip2, nip3, nip4))
                devList.append(
                    "[" + str(i) + "]GigE: " + chUserDefinedName + " " + chModelName + "(" + str(nip1) + "." + str(
                        nip2) + "." + str(nip3) + "." + str(nip4) + ")")
            elif mvcc_dev_info.nTLayerType == MV_USB_DEVICE:
                print("\nu3v device: [%d]" % i)
                chUserDefinedName = ""
                for per in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chUserDefinedName:
                    if per == 0:
                        break
                    chUserDefinedName = chUserDefinedName + chr(per)
                print("device user define name: %s" % chUserDefinedName)

                chModelName = ""
                for per in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chModelName:
                    if 0 == per:
                        break
                    chModelName = chModelName + chr(per)
                print("device model name: %s" % chModelName)

                strSerialNumber = ""
                for per in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chSerialNumber:
                    if per == 0:
                        break
                    strSerialNumber = strSerialNumber + chr(per)
                print("user serial number: %s" % strSerialNumber)
                devList.append("[" + str(i) + "]USB: " + chUserDefinedName + " " + chModelName
                               + "(" + str(strSerialNumber) + ")")

        self.comboDevices.clear()
        self.comboDevices.addItems(devList)
        self.comboDevices.setCurrentIndex(0)

        # en:open device


    def open_device(self):
        global deviceList
        global nSelCamIndex
        global obj_cam_operation
        global isOpen
        if isOpen:
            QMessageBox.warning(QMainWindow(), "Error", 'Camera is Running!', QMessageBox.Ok)
            return MV_E_CALLORDER

        nSelCamIndex = ui.comboDevices.currentIndex()
        if nSelCamIndex < 0:
            QMessageBox.warning(QMainWindow(), "Error", 'Please select a camera!', QMessageBox.Ok)
            return MV_E_CALLORDER

        obj_cam_operation = CameraOperation(cam, deviceList, nSelCamIndex)
        ret = obj_cam_operation.Open_device()
        if 0 != ret:
            strError = "Open device failed ret:" + ToHexStr(ret)
            QMessageBox.warning(QMainWindow(), "Error", strError, QMessageBox.Ok)
            isOpen = False
        else:
            self.set_software_trigger_mode()

            self.get_param()

            isOpen = True
            self.enable_controls()

        # ch:开始取流 | en:Start grab image


    def start_grabbing(self):
        global obj_cam_operation
        global isGrabbing
        global cam
        # ret = obj_cam_operation.Start_grabbing(ui.widgetDisplay.winId())
        # ret = cam.MV_CC_StartGrabbing()
        # if ret != 0:
        #     strError = "Start grabbing failed ret:" + ToHexStr(ret)
        #     QMessageBox.warning(mainWindow, "Error", strError, QMessageBox.Ok)
        # else:
        if self.radioTriggerMode.isChecked():
            print(self.editTimeTrigger.toPlainText())
            isGrabbing = True
            self.enable_controls()
            self.Timer.start(int(self.editTimeTrigger.toPlainText()))
        theard = threading.Thread(target=self.thread)
        theard.start()


    def thread(self):
        global obj_cam_operation
        while True:
            img = obj_cam_operation.get_np_image()

            if self.run:
                score_thr = float(self.editScoreThreshold.toPlainText())
                img = self.detect(img, score_thr)
            self.set_img_show(img)
            if isGrabbing == False:
                break

        # en:Stop grab image


    def stop_grabbing(self):
        global obj_cam_operation
        global isGrabbing
        ret = obj_cam_operation.Stop_grabbing()
        print(ret)
        isGrabbing = False
        self.thread()
        self.Timer.stop()
        self.enable_controls()
        print('Camera stopped')
        # if ret != 0:
        #     strError = "Stop grabbing failed ret:" + ToHexStr(ret)
        #     QMessageBox.warning(QMainWindow(), "Error", strError, QMessageBox.Ok)
        # else:
        #     self.Timer.stop()
        #     isGrabbing = False
        #     self.enable_controls()
        #     print('here2')

        # ch:关闭设备 | Close device

    def close_device(self):
        global isOpen
        global isGrabbing
        global obj_cam_operation

        if isOpen:
            obj_cam_operation.Close_device()
            isOpen = False

        isGrabbing = False

        self.enable_controls()

        # ch:设置触发模式 | en:set trigger mode

    def set_continue_mode(self):
        global is_trigger_mode
        strError = None

        ret = obj_cam_operation.Set_trigger_mode(False)
        if ret != 0:
            strError = "Set continue mode failed ret:" + ToHexStr(ret) + " mode is " + str(is_trigger_mode)
            QMessageBox.warning(QMainWindow(), "Error", strError, QMessageBox.Ok)
        else:
            self.radioContinueMode.setChecked(True)
            self.radioTriggerMode.setChecked(False)
            # ui.bnSoftwareTrigger.setEnabled(False)

        # ch:设置软触发模式 | en:set software trigger mode


    def set_software_trigger_mode(self):
        global isOpen
        global isGrabbing
        global obj_cam_operation


        ret = obj_cam_operation.Set_trigger_mode(True)
        if ret != 0:
            strError = "Set trigger mode failed ret:" + ToHexStr(ret)
            QMessageBox.warning(QMainWindow(), "Error", strError, QMessageBox.Ok)
        else:

            self.radioContinueMode.setChecked(False)
            self.radioTriggerMode.setChecked(True)
            # ui.bnSoftwareTrigger.setEnabled(isGrabbing)

        # ch:设置触发命令 | en:set trigger software


    def trigger_once(self):
        ret = obj_cam_operation.Trigger_once()
        if ret != 0:
            # strError = "TriggerSoftware failed ret:" + ToHexStr(ret)
            # QMessageBox.warning(QMainWindow(), "Error", strError, QMessageBox.Ok)
            print('TriggerSoffware failed ret:' + ToHexStr(ret))

        # ch:存图 | en:save image


    def save_bmp(self):
        ret = obj_cam_operation.Save_Bmp()
        if ret != MV_OK:
            strError = "Save BMP failed ret:" + ToHexStr(ret)
            QMessageBox.warning(QMainWindow(), "Error", strError, QMessageBox.Ok)
        else:
            print("Save image success")

        # ch: 获取参数 | en:get param


    def get_param(self):
        ret = obj_cam_operation.Get_parameter()
        if ret != MV_OK:
            strError = "Get param failed ret:" + ToHexStr(ret)
            QMessageBox.warning(QMainWindow(), "Error", strError, QMessageBox.Ok)
        else:
            self.edtExposureTime.setText("{0:.2f}".format(obj_cam_operation.exposure_time))
            self.edtGain.setText("{0:.2f}".format(obj_cam_operation.gain))
            self.edtFrameRate.setText("{0:.2f}".format(obj_cam_operation.frame_rate))

        # ch: 设置参数 | en:set param


    def set_param(self):
        frame_rate = self.edtFrameRate.toPlainText()
        exposure = self.edtExposureTime.toPlainText()
        gain = self.edtGain.toPlainText()
        ret = obj_cam_operation.Set_parameter(frame_rate, exposure, gain)
        if ret != MV_OK:
            strError = "Set param failed ret:" + ToHexStr(ret)
            QMessageBox.warning(QMainWindow(), "Error", strError, QMessageBox.Ok)

        return MV_OK


    def get_image(self):
        global obj_cam_operation
        img = obj_cam_operation.get_np_image()
        return img

        # ch: 设置控件状态 | en:set enable status


    def enable_controls(self):
        global isGrabbing
        global isOpen

        # 先设置group的状态，再单独设置各控件状态
        # ui.groupGrab.setEnabled(isOpen)
        # ui.groupParam.setEnabled(isOpen)

        self.btnOpen.setEnabled(not isOpen)
        self.btnClose.setEnabled(isOpen)

        self.bnStart.setEnabled(isOpen and (not isGrabbing))
        self.bnStop.setEnabled(isOpen and isGrabbing)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "DISPLAY"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Camera setting"))
        self.btnEnum.setText(_translate("MainWindow", "Enum"))
        self.btnOpen.setText(_translate("MainWindow", "Open"))
        self.btnClose.setText(_translate("MainWindow", "Close"))
        self.radioContinueMode.setText(_translate("MainWindow", "Continue"))
        self.radioTriggerMode.setText(_translate("MainWindow", "Trigger"))
        self.bnStart.setText(_translate("MainWindow", "Start"))
        self.label_2.setText(_translate("MainWindow", "Time trigger(s):"))
        self.bnStop.setText(_translate("MainWindow", "Stop"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Parameters"))
        self.label_3.setText(_translate("MainWindow", "ExposureTime:"))
        self.label_4.setText(_translate("MainWindow", "Gain:"))
        self.label_5.setText(_translate("MainWindow", "FrameRate:"))
        self.btnGetParam.setText(_translate("MainWindow", "GetParam"))
        self.btnSetParam.setText(_translate("MainWindow", "SetParam"))
        self.Combo_model.setTitle(_translate("MainWindow", "Deep learning"))
        self.label_13.setText(_translate("MainWindow", "Model:"))
        self.comboModels.setItemText(0, _translate("MainWindow", "Solov2"))
        self.comboModels.setItemText(1, _translate("MainWindow", "Faster_RCNN"))
        self.comboModels.setItemText(2, _translate("MainWindow", "YOLOX-s"))
        self.btnLoadCheckpoint.setText(_translate("MainWindow", "Load"))
        self.label_18.setText(_translate("MainWindow", "Time:(s): "))
        self.label_19.setText(_translate("MainWindow", "Threshold"))
        self.btnRunInferenceVideo.setText(_translate("MainWindow", "Run"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Calib Camera"))
        self.label_20.setText(_translate("MainWindow", "Calib File:"))
        self.btnRunCalib.setText(_translate("MainWindow", "Run"))
        self.btnLoadCalib.setText(_translate("MainWindow", "Load"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Single Image Inference"))
        self.btnRunInference.setText(_translate("MainWindow", "Run"))
        self.btnLoadImage.setText(_translate("MainWindow", "Load"))
        self.label_21.setText(_translate("MainWindow", "Time:(s): "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())