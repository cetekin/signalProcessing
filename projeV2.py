# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton, QFileDialog, QDialog
import librosa
import librosa.display
import numpy as np
import sqlite3
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import winsound


#qt designer baslangic
class Ui_MainWindow(object):
    music_directory={}
    db_name = "data.db"
    test_music_path = ""

    def setupUi(self, MainWindow):
        self.mainwindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 830)
        MainWindow.setMinimumSize(QtCore.QSize(1032, 830))
        MainWindow.setMaximumSize(QtCore.QSize(1032, 830))
        MainWindow.setStyleSheet("QMainWindow {\n"
"background-color: rgb(222, 249, 255);\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 40, 361, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.music_list = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.music_list.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(181, 146, 186, 255), stop:1 rgba(255, 255, 255, 255))\n"
"\n"
"\n"
"")
        self.music_list.setObjectName("music_list")
        self.gridLayout.addWidget(self.music_list, 0, 0, 1, 1)
        self.start_classification_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_classification_button.setGeometry(QtCore.QRect(390, 430, 141, 31))
        self.start_classification_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(142, 157, 255);\n"
"font-weight: bold;\n"
"}")
        self.start_classification_button.setObjectName("start_classification_button")
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setGeometry(QtCore.QRect(10, 410, 161, 31))
        self.play_button.setStyleSheet("QPushButton{\n"
"font-weight: bold;\n"
"background-color: rgb(57, 255, 47)\n"
"}")
        self.play_button.setObjectName("play_button")
        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setGeometry(QtCore.QRect(190, 410, 161, 31))
        self.pause_button.setStyleSheet("QPushButton{\n"
"font-weight: bold;\n"
"background-color: rgb(255, 83, 83);\n"
"}")
        self.pause_button.setObjectName("pause_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 91, 31))
        self.label_2.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.feature_table = QtWidgets.QTableWidget(self.centralwidget)
        self.feature_table.setGeometry(QtCore.QRect(10, 570, 1011, 251))
        self.feature_table.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(181, 146, 186, 255), stop:1 rgba(255, 255, 255, 255))")
        self.feature_table.setObjectName("feature_table")
        self.feature_table.setColumnCount(45)
        self.feature_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(32, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(33, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(34, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(35, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(36, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(37, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(38, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(39, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(40, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(41, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(42, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(43, item)
        item = QtWidgets.QTableWidgetItem()
        self.feature_table.setHorizontalHeaderItem(44, item)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 530, 101, 41))
        self.label_3.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(400, 50, 141, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(400, 110, 131, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(400, 90, 141, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(400, 70, 131, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(400, 150, 81, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(400, 130, 111, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(400, 170, 81, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(400, 190, 111, 20))
        self.checkBox_8.setObjectName("checkBox_8")
        self.tab_screen = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_screen.setGeometry(QtCore.QRect(600, 10, 411, 531))
        self.tab_screen.setStyleSheet("background-color:qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(181, 146, 186, 255), stop:1 rgba(255, 255, 255, 255))\n"
"")
        self.tab_screen.setObjectName("tab_screen")
        self.tab_screen_1 = QtWidgets.QWidget()
        self.tab_screen_1.setObjectName("tab_screen_1")
        self.tab_screen.addTab(self.tab_screen_1, "")
        self.tab_screen_2 = QtWidgets.QWidget()
        self.tab_screen_2.setObjectName("tab_screen_2")
        self.waveplot_label = QtWidgets.QLabel(self.tab_screen_2)
        self.waveplot_label.setGeometry(QtCore.QRect(20, 10, 386, 278))
        self.waveplot_label.setMinimumSize(QtCore.QSize(386, 278))
        self.waveplot_label.setMaximumSize(QtCore.QSize(386, 278))
        self.waveplot_label.setText("")
        self.waveplot_label.setObjectName("waveplot_label")
        self.start_genre_classification = QtWidgets.QPushButton(self.tab_screen_2)
        self.start_genre_classification.setGeometry(QtCore.QRect(130, 320, 151, 31))
        self.start_genre_classification.setStyleSheet("QPushButton{\n"
"background-color: rgb(142, 157, 255);\n"
"font-weight: bold;\n"
"}")
        self.start_genre_classification.setObjectName("start_genre_classification")
        self.genre_label = QtWidgets.QLabel(self.tab_screen_2)
        self.genre_label.setGeometry(QtCore.QRect(130, 470, 161, 20))
        self.genre_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"font-weight: bold;\n"
"}")
        self.genre_label.setObjectName("genre_label")
        self.genre_play_button = QtWidgets.QPushButton(self.tab_screen_2)
        self.genre_play_button.setGeometry(QtCore.QRect(120, 410, 81, 31))
        self.genre_play_button.setStyleSheet("QPushButton{\n"
"font-weight: bold;\n"
"background-color: rgb(57, 255, 47)\n"
"}")
        self.genre_play_button.setObjectName("genre_play_button")
        self.genre_pause_button = QtWidgets.QPushButton(self.tab_screen_2)
        self.genre_pause_button.setGeometry(QtCore.QRect(210, 410, 81, 31))
        self.genre_pause_button.setStyleSheet("QPushButton{\n"
"font-weight: bold;\n"
"background-color: rgb(255, 83, 83);\n"
"}")
        self.genre_pause_button.setObjectName("genre_pause_button")
        self.genre_music_name_label = QtWidgets.QLabel(self.tab_screen_2)
        self.genre_music_name_label.setGeometry(QtCore.QRect(20, 370, 371, 20))
        self.genre_music_name_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"}")
        self.genre_music_name_label.setObjectName("genre_music_name_label")
        self.tab_screen.addTab(self.tab_screen_2, "")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 10, 91, 31))
        self.label_4.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(410, 230, 91, 31))
        self.label_5.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(400, 270, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(400, 290, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(400, 310, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(400, 350, 131, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(400, 370, 141, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(400, 330, 121, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(400, 390, 95, 20))
        self.radioButton_7.setObjectName("radioButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1032, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuImport_music = QtWidgets.QMenu(self.menuBar)
        self.menuImport_music.setObjectName("menuImport_music")
        self.menuDatabase_Preferences = QtWidgets.QMenu(self.menuImport_music)
        self.menuDatabase_Preferences.setObjectName("menuDatabase_Preferences")
        MainWindow.setMenuBar(self.menuBar)
        self.import_file = QtWidgets.QAction(MainWindow)
        self.import_file.setObjectName("import_file")
        self.actionZero_Crossing_Rate = QtWidgets.QAction(MainWindow)
        self.actionZero_Crossing_Rate.setObjectName("actionZero_Crossing_Rate")
        self.import_music_file_action = QtWidgets.QAction(MainWindow)
        self.import_music_file_action.setObjectName("import_music_file_action")
        self.actionImport_Multiple_Music_Files = QtWidgets.QAction(MainWindow)
        self.actionImport_Multiple_Music_Files.setObjectName("actionImport_Multiple_Music_Files")
        self.use_existing_db_action = QtWidgets.QAction(MainWindow)
        self.use_existing_db_action.setObjectName("use_existing_db_action")
        self.create_new_db_action = QtWidgets.QAction(MainWindow)
        self.create_new_db_action.setCheckable(False)
        self.create_new_db_action.setObjectName("create_new_db_action")
        self.menuDatabase_Preferences.addSeparator()
        self.menuDatabase_Preferences.addAction(self.use_existing_db_action)
        self.menuDatabase_Preferences.addAction(self.create_new_db_action)
        self.menuImport_music.addAction(self.import_music_file_action)
        self.menuImport_music.addAction(self.menuDatabase_Preferences.menuAction())
        self.menuBar.addAction(self.menuImport_music.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_screen.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Genre Classification"))
        self.start_classification_button.setText(_translate("MainWindow", "Start Classification"))
        self.play_button.setText(_translate("MainWindow", "PLAY"))
        self.pause_button.setText(_translate("MainWindow", "STOP"))
        self.label_2.setText(_translate("MainWindow", "MUSIC FILES"))
        item = self.feature_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "song_name"))
        item = self.feature_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "avg_zero_crs_rate"))
        item = self.feature_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "var_zero_crs_rate"))
        item = self.feature_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "avg_spec_centroid"))
        item = self.feature_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "var_spec_centroid"))
        item = self.feature_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "avg_spec_bandwidth"))
        item = self.feature_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "var_spec_bandwidth"))
        item = self.feature_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "avg_spec_contrast"))
        item = self.feature_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "var_spec_contrast"))
        item = self.feature_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "avg_spec_rolloff"))
        item = self.feature_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "var_spec_rolloff"))
        item = self.feature_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "avg_rmse"))
        item = self.feature_table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "var_rmse"))
        item = self.feature_table.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "avg_mfcc_1"))
        item = self.feature_table.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "avg_mfcc_2"))
        item = self.feature_table.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "avg_mfcc_3"))
        item = self.feature_table.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "avg_mfcc_4"))
        item = self.feature_table.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "avg_mfcc_5"))
        item = self.feature_table.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "avg_mfcc_6"))
        item = self.feature_table.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "avg_mfcc_7"))
        item = self.feature_table.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "avg_mfcc_8"))
        item = self.feature_table.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "avg_mfcc_9"))
        item = self.feature_table.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "avg_mfcc_10"))
        item = self.feature_table.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "avg_mfcc_11"))
        item = self.feature_table.horizontalHeaderItem(24)
        item.setText(_translate("MainWindow", "avg_mfcc_12"))
        item = self.feature_table.horizontalHeaderItem(25)
        item.setText(_translate("MainWindow", "avg_mfcc_13"))
        item = self.feature_table.horizontalHeaderItem(26)
        item.setText(_translate("MainWindow", "avg_mfcc_14"))
        item = self.feature_table.horizontalHeaderItem(27)
        item.setText(_translate("MainWindow", "avg_mfcc_15"))
        item = self.feature_table.horizontalHeaderItem(28)
        item.setText(_translate("MainWindow", "avg_mfcc_16"))
        item = self.feature_table.horizontalHeaderItem(29)
        item.setText(_translate("MainWindow", "avg_mfcc_17"))
        item = self.feature_table.horizontalHeaderItem(30)
        item.setText(_translate("MainWindow", "avg_mfcc_18"))
        item = self.feature_table.horizontalHeaderItem(31)
        item.setText(_translate("MainWindow", "avg_mfcc_19"))
        item = self.feature_table.horizontalHeaderItem(32)
        item.setText(_translate("MainWindow", "avg_mfcc_20"))
        item = self.feature_table.horizontalHeaderItem(33)
        item.setText(_translate("MainWindow", "avg_chroma_stft_1"))
        item = self.feature_table.horizontalHeaderItem(34)
        item.setText(_translate("MainWindow", "avg_chroma_stft_2"))
        item = self.feature_table.horizontalHeaderItem(35)
        item.setText(_translate("MainWindow", "avg_chroma_stft_3"))
        item = self.feature_table.horizontalHeaderItem(36)
        item.setText(_translate("MainWindow", "avg_chroma_stft_4"))
        item = self.feature_table.horizontalHeaderItem(37)
        item.setText(_translate("MainWindow", "avg_chroma_stft_5"))
        item = self.feature_table.horizontalHeaderItem(38)
        item.setText(_translate("MainWindow", "avg_chroma_stft_6"))
        item = self.feature_table.horizontalHeaderItem(39)
        item.setText(_translate("MainWindow", "avg_chroma_stft_7"))
        item = self.feature_table.horizontalHeaderItem(40)
        item.setText(_translate("MainWindow", "avg_chroma_stft_8"))
        item = self.feature_table.horizontalHeaderItem(41)
        item.setText(_translate("MainWindow", "avg_chroma_stft_9"))
        item = self.feature_table.horizontalHeaderItem(42)
        item.setText(_translate("MainWindow", "avg_chroma_stft_10"))
        item = self.feature_table.horizontalHeaderItem(43)
        item.setText(_translate("MainWindow", "avg_chroma_stft_11"))
        item = self.feature_table.horizontalHeaderItem(44)
        item.setText(_translate("MainWindow", "avg_chroma_stft_12"))
        self.label_3.setText(_translate("MainWindow", "FEATURE TABLE"))
        self.checkBox.setText(_translate("MainWindow", "Zero Crossing Rate"))
        self.checkBox_2.setText(_translate("MainWindow", "Spectral Contrast"))
        self.checkBox_3.setText(_translate("MainWindow", "Spectral Bandwidth"))
        self.checkBox_4.setText(_translate("MainWindow", "Spectral Centroid"))
        self.checkBox_5.setText(_translate("MainWindow", "RMSE"))
        self.checkBox_6.setText(_translate("MainWindow", "Spectral Rollof"))
        self.checkBox_7.setText(_translate("MainWindow", "MFCC"))
        self.checkBox_8.setText(_translate("MainWindow", "Chroma STFT"))
        self.tab_screen.setTabText(self.tab_screen.indexOf(self.tab_screen_1), _translate("MainWindow", "Classification Results"))
        self.start_genre_classification.setText(_translate("MainWindow", "Import Music File"))
        self.genre_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">ESTIMATED GENRE</span></p></body></html>"))
        self.genre_play_button.setText(_translate("MainWindow", "PLAY"))
        self.genre_pause_button.setText(_translate("MainWindow", "STOP"))
        self.genre_music_name_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">NAME OF THE MUSIC</p></body></html>"))
        self.tab_screen.setTabText(self.tab_screen.indexOf(self.tab_screen_2), _translate("MainWindow", "Genre Estimation"))
        self.label_4.setText(_translate("MainWindow", "FEATURES"))
        self.label_5.setText(_translate("MainWindow", "CLASSIFIER"))
        self.radioButton.setText(_translate("MainWindow", "K-NN"))
        self.radioButton_2.setText(_translate("MainWindow", "Naive Bayes"))
        self.radioButton_3.setText(_translate("MainWindow", "SVM"))
        self.radioButton_4.setText(_translate("MainWindow", "Neural Network"))
        self.radioButton_5.setText(_translate("MainWindow", "Logistic Regression"))
        self.radioButton_6.setText(_translate("MainWindow", "Random Forest"))
        self.radioButton_7.setText(_translate("MainWindow", "LDA"))
        self.menuImport_music.setTitle(_translate("MainWindow", "Actions"))
        self.menuDatabase_Preferences.setTitle(_translate("MainWindow", "Database Preferences"))
        self.import_file.setText(_translate("MainWindow", "Import Music"))
        self.actionZero_Crossing_Rate.setText(_translate("MainWindow", "Zero Crossing Rate"))
        self.import_music_file_action.setText(_translate("MainWindow", "Import Music File/s"))
        self.actionImport_Multiple_Music_Files.setText(_translate("MainWindow", "Import Multiple Music Files"))
        self.use_existing_db_action.setText(_translate("MainWindow", "Use Existing Database (Default)"))
        self.create_new_db_action.setText(_translate("MainWindow", "Create a New Database"))

        #qt designer bitis

        self.import_music_file_action.triggered.connect(self.import_music)
        self.create_new_db_action.triggered.connect(self.create_db_table)
        self.use_existing_db_action.triggered.connect(self.use_existing_table)
        self.play_button.setEnabled(False)
        self.pause_button.setEnabled(False)
        self.music_list.itemClicked.connect(self.enable_button)
        self.play_button.clicked.connect(self.play_music)
        self.pause_button.clicked.connect(self.pause_music)
        self.start_genre_classification.clicked.connect(self.estimate_music_genre)
        self.genre_play_button.clicked.connect(self.genre_play_music)
        self.genre_pause_button.clicked.connect(self.pause_music)


    def import_music(self):
        options = QFileDialog.Options()
        fname,ok = QFileDialog.getOpenFileNames(self.mainwindow, 'Import music file','', 'Music files (*.mp3 *.wav *.au)',options=options)

        if ok:
            db_conn = sqlite3.connect(self.db_name)
            for i in range(len(fname)):
                #getting name of the music
                url = QUrl.fromLocalFile(fname[i])
                music_name = url.fileName()
                #directory of the music is put in the music_directory dictionary
                self.music_directory[music_name] = fname[i]
                self.music_list.addItem(music_name)

                y,sr = librosa.load(fname[i])
                print(y)
                feature_list=feature_extract(y,sr)
                self.write_features_to_database(feature_list,music_name,db_conn)
                self.write_features_to_feature_table(feature_list,music_name)
            db_conn.close()



    def enable_button(self):
        self.play_button.setEnabled(True)
        self.pause_button.setEnabled(True)



    def play_music(self):
        directory = self.music_directory[self.music_list.currentItem().text()]
        winsound.PlaySound(directory,winsound.SND_ASYNC)


    def pause_music(self):
        winsound.PlaySound(None, winsound.SND_PURGE)



    def write_features_to_feature_table(self,feature_list,music_name):
        numRows = self.feature_table.rowCount()
        self.feature_table.insertRow(numRows)
        self.feature_table.setItem(numRows, 0, QtWidgets.QTableWidgetItem(music_name))
        for i in range(44):
            self.feature_table.setItem(numRows, i+1, QtWidgets.QTableWidgetItem(str(feature_list[i]) ) )




    def create_db_table(self):
        db_name, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Create New Database", "", "Database (*.db)")
        self.db_name = db_name
        db_conn = sqlite3.connect(db_name)
        db_cursor = db_conn.cursor()

        db_cursor.execute('''
        CREATE TABLE songs(
        song_name VARCHAR(200),
        avg_zero_crs_rate REAL,
        var_zero_crs_rate REAL,
        avg_spec_centroid REAL,
        var_spec_centroid REAL,
        avg_spec_bandwidth REAL,
        var_spec_bandwidth REAL,
        avg_spec_contrast REAL,
        var_spec_contrast REAL,
        avg_spec_rolloff REAL,
        var_spec_rolloff REAL,
        avg_rmse REAL,
        var_rmse REAL,
        avg_mfcc_1 REAL,
        avg_mfcc_2 REAL,
        avg_mfcc_3 REAL,
        avg_mfcc_4 REAL,
        avg_mfcc_5 REAL,
        avg_mfcc_6 REAL,
        avg_mfcc_7 REAL,
        avg_mfcc_8 REAL,
        avg_mfcc_9 REAL,
        avg_mfcc_10 REAL,
        avg_mfcc_11 REAL,
        avg_mfcc_12 REAL,
        avg_mfcc_13 REAL,
        avg_mfcc_14 REAL,
        avg_mfcc_15 REAL,
        avg_mfcc_16 REAL,
        avg_mfcc_17 REAL,
        avg_mfcc_18 REAL,
        avg_mfcc_19 REAL,
        avg_mfcc_20 REAL,
        avg_chroma_stft_1 REAL,
        avg_chroma_stft_2 REAL,
        avg_chroma_stft_3 REAL,
        avg_chroma_stft_4 REAL,
        avg_chroma_stft_5 REAL,
        avg_chroma_stft_6 REAL,
        avg_chroma_stft_7 REAL,
        avg_chroma_stft_8 REAL,
        avg_chroma_stft_9 REAL,
        avg_chroma_stft_10 REAL,
        avg_chroma_stft_11 REAL,
        avg_chroma_stft_12 REAL
        )
        ''')

        db_conn.commit()
        db_conn.close()


    def genre_play_music(self):
        winsound.PlaySound(self.test_music_path,winsound.SND_ASYNC)


    def estimate_music_genre(self):
        options = QFileDialog.Options()
        fname,ok = QFileDialog.getOpenFileName(self.mainwindow, 'Import music file','', 'Music files (*.mp3 *.wav *.au)',options=options)
        self.test_music_path = fname
        if ok:
            #Music name display
            url = QUrl.fromLocalFile(fname)
            music_name = url.fileName()
            self.genre_music_name_label.setText(music_name)
            #Waveplot drawing
            y, sr = librosa.load(fname)
            plt.figure()
            librosa.display.waveplot(y, sr=sr)
            plt.title('Waveplot of the Song')
            plt.savefig('fig2.png', bbox_inches="tight", pad_inches=0.3)
            self.waveplot_label.setPixmap(QtGui.QPixmap('fig2.png').scaled(371, 181, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation))
            plt.clf()

    def write_features_to_database(self,feature_list,s_name,db_conn): #Write given feature list of a specific song to the database
        db_cursor = db_conn.cursor()

        db_cursor.execute('''
        INSERT INTO songs (
        song_name,
        avg_zero_crs_rate,
        var_zero_crs_rate,
        avg_spec_centroid,
        var_spec_centroid,
        avg_spec_bandwidth,
        var_spec_bandwidth,
        avg_spec_contrast,
        var_spec_contrast,
        avg_spec_rolloff,
        var_spec_rolloff,
        avg_rmse,
        var_rmse,
        avg_mfcc_1,
        avg_mfcc_2,
        avg_mfcc_3,
        avg_mfcc_4,
        avg_mfcc_5,
        avg_mfcc_6,
        avg_mfcc_7,
        avg_mfcc_8,
        avg_mfcc_9,
        avg_mfcc_10,
        avg_mfcc_11,
        avg_mfcc_12,
        avg_mfcc_13,
        avg_mfcc_14,
        avg_mfcc_15,
        avg_mfcc_16,
        avg_mfcc_17,
        avg_mfcc_18,
        avg_mfcc_19,
        avg_mfcc_20,
        avg_chroma_stft_1,
        avg_chroma_stft_2,
        avg_chroma_stft_3,
        avg_chroma_stft_4,
        avg_chroma_stft_5,
        avg_chroma_stft_6,
        avg_chroma_stft_7,
        avg_chroma_stft_8,
        avg_chroma_stft_9,
        avg_chroma_stft_10,
        avg_chroma_stft_11,
        avg_chroma_stft_12
        ) VALUES (
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?,
        ?
        )
        ''',
        (s_name,
        *feature_list
        )
        )
        db_conn.commit()


    def use_existing_table(self):
        self.db_name = "data.db"




######################################################################################################################################

def feature_extract(y,sr):
    features = [np.average(librosa.feature.zero_crossing_rate(y)),np.var(librosa.feature.zero_crossing_rate(y)),
           np.average(librosa.feature.spectral_centroid(y,sr)),np.var(librosa.feature.spectral_centroid(y,sr)),
                     np.average(librosa.feature.spectral_bandwidth(y,sr)),np.var(librosa.feature.spectral_bandwidth(y,sr)),
                               np.average(librosa.feature.spectral_contrast(y,sr)),np.var(librosa.feature.spectral_contrast(y,sr)),
                                         np.average(librosa.feature.spectral_rolloff(y,sr)),np.var(librosa.feature.spectral_rolloff(y,sr)),
                                                   np.average(librosa.feature.rmse(y)),np.var(librosa.feature.rmse(y))]

    #calculate and add mfcc
    tmp=librosa.feature.mfcc(y,sr)
    tmpp=[None]*20
    for i in range(20):
        tmpp[i]=np.average(tmp[i])
    features=np.append(features,tmpp)
    #calculate and add chroma_stft
    tmp=librosa.feature.chroma_stft(y,sr)
    tmpp=[None]*12
    for i in range(12):
        tmpp[i]=np.average(tmp[i])
    features=np.append(features,tmpp)

    return features







if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)


    MainWindow.show()
    sys.exit(app.exec_())
