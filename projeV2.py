# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import multiprocessing
multiprocessing.freeze_support()

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton, QFileDialog, QDialog, QMessageBox
import librosa
#import essentia
#import essentia.standard as es
import librosa.display
import numpy as np
import sqlite3
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import itertools
import winsound
import pandas as pd
from sklearn import model_selection, preprocessing, metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score




#qt designer baslangic
class Ui_MainWindow(object):
    music_directory={}
    db_name = "data.db"
    test_music_path = ""

    def setupUi(self, MainWindow):
        self.mainwindow = MainWindow
        self.error_msg = QMessageBox()
        self.import_info_msg = QMessageBox()
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
        self.tab_screen = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_screen.setGeometry(QtCore.QRect(0, 0, 1051, 931))
        self.tab_screen.setStyleSheet("background-color: rgb(222, 249, 255);")
        self.tab_screen.setObjectName("tab_screen")
        self.tab_screen_1 = QtWidgets.QWidget()
        self.tab_screen_1.setObjectName("tab_screen_1")
        self.rb_knn = QtWidgets.QRadioButton(self.tab_screen_1)
        self.rb_knn.setGeometry(QtCore.QRect(30, 70, 111, 20))
        self.rb_knn.setObjectName("rb_knn")
        self.rb_naive_bayes = QtWidgets.QRadioButton(self.tab_screen_1)
        self.rb_naive_bayes.setGeometry(QtCore.QRect(30, 100, 121, 20))
        self.rb_naive_bayes.setObjectName("rb_naive_bayes")
        self.label_5 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 131, 31))
        self.label_5.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.rb_random_forest = QtWidgets.QRadioButton(self.tab_screen_1)
        self.rb_random_forest.setGeometry(QtCore.QRect(30, 160, 141, 20))
        self.rb_random_forest.setObjectName("rb_random_forest")
        self.rb_svm = QtWidgets.QRadioButton(self.tab_screen_1)
        self.rb_svm.setGeometry(QtCore.QRect(30, 130, 111, 20))
        self.rb_svm.setObjectName("rb_svm")
        self.label_4 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_4.setGeometry(QtCore.QRect(270, 30, 141, 31))
        self.label_4.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.cb_zcr = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_zcr.setGeometry(QtCore.QRect(270, 70, 171, 20))
        self.cb_zcr.setObjectName("cb_zcr")
        self.cb_spec_cen = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_spec_cen.setGeometry(QtCore.QRect(270, 100, 171, 20))
        self.cb_spec_cen.setObjectName("cb_spec_cen")
        self.cb_rmse = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_rmse.setGeometry(QtCore.QRect(270, 220, 121, 20))
        self.cb_rmse.setObjectName("cb_rmse")
        self.cb_spec_con = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_spec_con.setGeometry(QtCore.QRect(270, 160, 181, 20))
        self.cb_spec_con.setObjectName("cb_spec_con")
        self.cb_spec_ban = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_spec_ban.setGeometry(QtCore.QRect(270, 130, 191, 20))
        self.cb_spec_ban.setObjectName("cb_spec_ban")
        self.cb_chroma_stft = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_chroma_stft.setGeometry(QtCore.QRect(270, 310, 151, 20))
        self.cb_chroma_stft.setObjectName("cb_chroma_stft")
        self.cb_spec_rollof = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_spec_rollof.setGeometry(QtCore.QRect(270, 190, 161, 20))
        self.cb_spec_rollof.setObjectName("cb_spec_rollof")
        self.cb_mfcc = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_mfcc.setGeometry(QtCore.QRect(270, 250, 121, 20))
        self.cb_mfcc.setObjectName("cb_mfcc")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_screen_1)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 2, 2))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.avg_accuracy_label = QtWidgets.QLabel(self.tab_screen_1)
        self.avg_accuracy_label.setGeometry(QtCore.QRect(480, 750, 161, 41))
        self.avg_accuracy_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"font-weight: bold;\n"
"}")
        self.avg_accuracy_label.setAlignment(QtCore.Qt.AlignCenter)
        self.avg_accuracy_label.setObjectName("avg_accuracy_label")
        self.con_matrix_label = QtWidgets.QLabel(self.tab_screen_1)
        self.con_matrix_label.setGeometry(QtCore.QRect(510, 90, 441, 351))
        self.con_matrix_label.setMinimumSize(QtCore.QSize(347, 297))
        self.con_matrix_label.setMaximumSize(QtCore.QSize(444, 397))
        self.con_matrix_label.setText("")
        self.con_matrix_label.setObjectName("con_matrix_label")
        self.label_6 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_6.setGeometry(QtCore.QRect(660, 30, 231, 31))
        self.label_6.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_7.setGeometry(QtCore.QRect(500, 720, 151, 31))
        self.label_7.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.max_accuracy_label = QtWidgets.QLabel(self.tab_screen_1)
        self.max_accuracy_label.setGeometry(QtCore.QRect(480, 550, 161, 41))
        self.max_accuracy_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"font-weight: bold;\n"
"}")
        self.max_accuracy_label.setAlignment(QtCore.Qt.AlignCenter)
        self.max_accuracy_label.setObjectName("max_accuracy_label")
        self.label_8 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_8.setGeometry(QtCore.QRect(500, 520, 151, 31))
        self.label_8.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.start_classification_button = QtWidgets.QPushButton(self.tab_screen_1)
        self.start_classification_button.setGeometry(QtCore.QRect(50, 690, 151, 51))
        self.start_classification_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(142, 157, 255);\n"
"font-weight: bold;\n"
"}")
        self.start_classification_button.setObjectName("start_classification_button")
        self.cb_hpcp = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_hpcp.setGeometry(QtCore.QRect(270, 340, 151, 20))
        self.cb_hpcp.setObjectName("cb_hpcp")
        self.cb_gfcc = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_gfcc.setGeometry(QtCore.QRect(270, 370, 141, 20))
        self.cb_gfcc.setObjectName("cb_gfcc")
        self.rb_decision_tree = QtWidgets.QRadioButton(self.tab_screen_1)
        self.rb_decision_tree.setGeometry(QtCore.QRect(30, 190, 151, 20))
        self.rb_decision_tree.setObjectName("rb_decision_tree")
        self.label_2 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_2.setGeometry(QtCore.QRect(60, 530, 391, 16))
        self.label_2.setObjectName("label_2")
        self.le_kfold = QtWidgets.QLineEdit(self.tab_screen_1)
        self.le_kfold.setGeometry(QtCore.QRect(60, 570, 113, 22))
        self.le_kfold.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.le_kfold.setObjectName("le_kfold")
        self.pb_select_all_features = QtWidgets.QPushButton(self.tab_screen_1)
        self.pb_select_all_features.setGeometry(QtCore.QRect(260, 410, 131, 31))
        self.pb_select_all_features.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 85, 0);\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.pb_select_all_features.setObjectName("pb_select_all_features")
        self.cb_mfcc_derivative = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_mfcc_derivative.setGeometry(QtCore.QRect(270, 280, 171, 20))
        self.cb_mfcc_derivative.setObjectName("cb_mfcc_derivative")
        self.fscore_label = QtWidgets.QLabel(self.tab_screen_1)
        self.fscore_label.setGeometry(QtCore.QRect(810, 550, 161, 41))
        self.fscore_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"font-weight: bold;\n"
"}")
        self.fscore_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fscore_label.setObjectName("fscore_label")
        self.recall_label = QtWidgets.QLabel(self.tab_screen_1)
        self.recall_label.setGeometry(QtCore.QRect(810, 650, 161, 41))
        self.recall_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"font-weight: bold;\n"
"}")
        self.recall_label.setAlignment(QtCore.Qt.AlignCenter)
        self.recall_label.setObjectName("recall_label")
        self.label_10 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_10.setGeometry(QtCore.QRect(850, 520, 151, 31))
        self.label_10.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_11.setGeometry(QtCore.QRect(850, 620, 151, 31))
        self.label_11.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.min_accuracy_label = QtWidgets.QLabel(self.tab_screen_1)
        self.min_accuracy_label.setGeometry(QtCore.QRect(480, 650, 161, 41))
        self.min_accuracy_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"font-weight: bold;\n"
"}")
        self.min_accuracy_label.setAlignment(QtCore.Qt.AlignCenter)
        self.min_accuracy_label.setObjectName("min_accuracy_label")
        self.label_12 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_12.setGeometry(QtCore.QRect(500, 620, 151, 31))
        self.label_12.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_12.setObjectName("label_12")
        self.precision_label = QtWidgets.QLabel(self.tab_screen_1)
        self.precision_label.setGeometry(QtCore.QRect(810, 750, 161, 41))
        self.precision_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"font-weight: bold;\n"
"}")
        self.precision_label.setAlignment(QtCore.Qt.AlignCenter)
        self.precision_label.setObjectName("precision_label")
        self.label_13 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_13.setGeometry(QtCore.QRect(840, 720, 151, 31))
        self.label_13.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_13.setObjectName("label_13")
        self.knn_sb = QtWidgets.QSpinBox(self.tab_screen_1)
        self.knn_sb.setGeometry(QtCore.QRect(150, 65, 48, 31))
        self.knn_sb.setObjectName("knn_sb")
        self.knn_label = QtWidgets.QLabel(self.tab_screen_1)
        self.knn_label.setGeometry(QtCore.QRect(130, 70, 16, 21))
        self.knn_label.setObjectName("knn_label")
        self.tab_screen.addTab(self.tab_screen_1, "")
        self.tab_screen_2 = QtWidgets.QWidget()
        self.tab_screen_2.setObjectName("tab_screen_2")
        self.waveplot_label = QtWidgets.QLabel(self.tab_screen_2)
        self.waveplot_label.setGeometry(QtCore.QRect(330, 110, 386, 278))
        self.waveplot_label.setMinimumSize(QtCore.QSize(386, 278))
        self.waveplot_label.setMaximumSize(QtCore.QSize(386, 278))
        self.waveplot_label.setText("")
        self.waveplot_label.setObjectName("waveplot_label")
        self.start_genre_classification = QtWidgets.QPushButton(self.tab_screen_2)
        self.start_genre_classification.setGeometry(QtCore.QRect(450, 570, 151, 31))
        self.start_genre_classification.setStyleSheet("QPushButton{\n"
"background-color: rgb(142, 157, 255);\n"
"font-weight: bold;\n"
"}")
        self.start_genre_classification.setObjectName("start_genre_classification")
        self.genre_label = QtWidgets.QLabel(self.tab_screen_2)
        self.genre_label.setGeometry(QtCore.QRect(380, 680, 271, 71))
        self.genre_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"font-weight: bold;\n"
"}")
        self.genre_label.setAlignment(QtCore.Qt.AlignCenter)
        self.genre_label.setObjectName("genre_label")
        self.genre_music_name_label = QtWidgets.QLabel(self.tab_screen_2)
        self.genre_music_name_label.setGeometry(QtCore.QRect(340, 410, 371, 41))
        self.genre_music_name_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"}")
        self.genre_music_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.genre_music_name_label.setObjectName("genre_music_name_label")
        self.label_3 = QtWidgets.QLabel(self.tab_screen_2)
        self.label_3.setGeometry(QtCore.QRect(460, 30, 191, 51))
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.tab_screen_2)
        self.label_9.setGeometry(QtCore.QRect(400, 640, 271, 31))
        self.label_9.setObjectName("label_9")
        self.rb_naive_bayes_4 = QtWidgets.QRadioButton(self.tab_screen_2)
        self.rb_naive_bayes_4.setGeometry(QtCore.QRect(50, 110, 121, 20))
        self.rb_naive_bayes_4.setObjectName("rb_naive_bayes_4")
        self.rb_svm_4 = QtWidgets.QRadioButton(self.tab_screen_2)
        self.rb_svm_4.setGeometry(QtCore.QRect(50, 140, 111, 20))
        self.rb_svm_4.setObjectName("rb_svm_4")
        self.rb_random_forest_4 = QtWidgets.QRadioButton(self.tab_screen_2)
        self.rb_random_forest_4.setGeometry(QtCore.QRect(50, 170, 141, 20))
        self.rb_random_forest_4.setObjectName("rb_random_forest_4")
        self.label_40 = QtWidgets.QLabel(self.tab_screen_2)
        self.label_40.setGeometry(QtCore.QRect(50, 40, 131, 31))
        self.label_40.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_40.setObjectName("label_40")
        self.rb_decision_tree_4 = QtWidgets.QRadioButton(self.tab_screen_2)
        self.rb_decision_tree_4.setGeometry(QtCore.QRect(50, 200, 151, 20))
        self.rb_decision_tree_4.setObjectName("rb_decision_tree_4")
        self.rb_knn_4 = QtWidgets.QRadioButton(self.tab_screen_2)
        self.rb_knn_4.setGeometry(QtCore.QRect(50, 80, 111, 20))
        self.rb_knn_4.setObjectName("rb_knn_4")
        self.cb_chroma_stft_4 = QtWidgets.QCheckBox(self.tab_screen_2)
        self.cb_chroma_stft_4.setGeometry(QtCore.QRect(40, 550, 151, 20))
        self.cb_chroma_stft_4.setObjectName("cb_chroma_stft_4")
        self.cb_spec_cen_4 = QtWidgets.QCheckBox(self.tab_screen_2)
        self.cb_spec_cen_4.setGeometry(QtCore.QRect(40, 340, 171, 20))
        self.cb_spec_cen_4.setObjectName("cb_spec_cen_4")
        self.cb_spec_ban_4 = QtWidgets.QCheckBox(self.tab_screen_2)
        self.cb_spec_ban_4.setGeometry(QtCore.QRect(40, 370, 191, 20))
        self.cb_spec_ban_4.setObjectName("cb_spec_ban_4")
        self.cb_gfcc_4 = QtWidgets.QCheckBox(self.tab_screen_2)
        self.cb_gfcc_4.setGeometry(QtCore.QRect(40, 610, 141, 20))
        self.cb_gfcc_4.setObjectName("cb_gfcc_4")
        self.label_41 = QtWidgets.QLabel(self.tab_screen_2)
        self.label_41.setGeometry(QtCore.QRect(40, 270, 141, 31))
        self.label_41.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_41.setObjectName("label_41")
        self.cb_zcr_4 = QtWidgets.QCheckBox(self.tab_screen_2)
        self.cb_zcr_4.setGeometry(QtCore.QRect(40, 310, 171, 20))
        self.cb_zcr_4.setObjectName("cb_zcr_4")
        self.cb_mfcc_4 = QtWidgets.QCheckBox(self.tab_screen_2)
        self.cb_mfcc_4.setGeometry(QtCore.QRect(40, 490, 121, 20))
        self.cb_mfcc_4.setObjectName("cb_mfcc_4")
        self.cb_mfcc_derivative_4 = QtWidgets.QCheckBox(self.tab_screen_2)
        self.cb_mfcc_derivative_4.setGeometry(QtCore.QRect(40, 520, 171, 20))
        self.cb_mfcc_derivative_4.setObjectName("cb_mfcc_derivative_4")
        self.cb_hpcp_4 = QtWidgets.QCheckBox(self.tab_screen_2)
        self.cb_hpcp_4.setGeometry(QtCore.QRect(40, 580, 151, 20))
        self.cb_hpcp_4.setObjectName("cb_hpcp_4")
        self.cb_rmse_4 = QtWidgets.QCheckBox(self.tab_screen_2)
        self.cb_rmse_4.setGeometry(QtCore.QRect(40, 460, 121, 20))
        self.cb_rmse_4.setObjectName("cb_rmse_4")
        self.pb_select_all_features_4 = QtWidgets.QPushButton(self.tab_screen_2)
        self.pb_select_all_features_4.setGeometry(QtCore.QRect(30, 650, 131, 31))
        self.pb_select_all_features_4.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 85, 0);\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255)\n"
"}")
        self.pb_select_all_features_4.setObjectName("pb_select_all_features_4")
        self.cb_spec_con_4 = QtWidgets.QCheckBox(self.tab_screen_2)
        self.cb_spec_con_4.setGeometry(QtCore.QRect(40, 400, 181, 20))
        self.cb_spec_con_4.setObjectName("cb_spec_con_4")
        self.cb_spec_rollof_4 = QtWidgets.QCheckBox(self.tab_screen_2)
        self.cb_spec_rollof_4.setGeometry(QtCore.QRect(40, 430, 161, 20))
        self.cb_spec_rollof_4.setObjectName("cb_spec_rollof_4")
        self.select_music_file = QtWidgets.QPushButton(self.tab_screen_2)
        self.select_music_file.setGeometry(QtCore.QRect(450, 530, 151, 31))
        self.select_music_file.setStyleSheet("QPushButton{\n"
"background-color: rgb(142, 157, 255);\n"
"font-weight: bold;\n"
"}")
        self.select_music_file.setObjectName("select_music_file")
        self.knn_label_4 = QtWidgets.QLabel(self.tab_screen_2)
        self.knn_label_4.setGeometry(QtCore.QRect(150, 80, 16, 21))
        self.knn_label_4.setObjectName("knn_label_4")
        self.knn_sb_4 = QtWidgets.QSpinBox(self.tab_screen_2)
        self.knn_sb_4.setGeometry(QtCore.QRect(170, 75, 48, 31))
        self.knn_sb_4.setObjectName("knn_sb_4")
        self.play_button = QtWidgets.QPushButton(self.tab_screen_2)
        self.play_button.setGeometry(QtCore.QRect(370, 460, 151, 31))
        self.play_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 255, 0);\n"
"font-weight: bold;\n"
"}")
        self.play_button.setObjectName("play_button")
        self.stop_button = QtWidgets.QPushButton(self.tab_screen_2)
        self.stop_button.setGeometry(QtCore.QRect(530, 460, 151, 31))
        self.stop_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"font-weight: bold;\n"
"}")
        self.stop_button.setObjectName("stop_button")
        self.tab_screen.addTab(self.tab_screen_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
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

        self.retranslateUi(MainWindow)
        self.tab_screen.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Genre Classification"))
        self.rb_knn.setText(_translate("MainWindow", "K-NN"))
        self.rb_naive_bayes.setText(_translate("MainWindow", "Naive Bayes"))
        self.label_5.setText(_translate("MainWindow", "CLASSIFIER"))
        self.rb_random_forest.setText(_translate("MainWindow", "Random Forest"))
        self.rb_svm.setText(_translate("MainWindow", "SVM"))
        self.label_4.setText(_translate("MainWindow", "FEATURES"))
        self.cb_zcr.setText(_translate("MainWindow", "Zero Crossing Rate"))
        self.cb_spec_cen.setText(_translate("MainWindow", "Spectral Centroid"))
        self.cb_rmse.setText(_translate("MainWindow", "RMSE"))
        self.cb_spec_con.setText(_translate("MainWindow", "Spectral Contrast"))
        self.cb_spec_ban.setText(_translate("MainWindow", "Spectral Bandwidth"))
        self.cb_chroma_stft.setText(_translate("MainWindow", "Chroma STFT"))
        self.cb_spec_rollof.setText(_translate("MainWindow", "Spectral Rollof"))
        self.cb_mfcc.setText(_translate("MainWindow", "MFCC"))
        self.avg_accuracy_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline;\">ACCURACY</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>AVG CONFUSION MATRIX</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>AVG ACCURACY</p></body></html>"))
        self.max_accuracy_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline;\">ACCURACY</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>MAX ACCURACY</p></body></html>"))
        self.start_classification_button.setText(_translate("MainWindow", "Start Classification"))
        self.cb_hpcp.setText(_translate("MainWindow", "HPCP"))
        self.cb_gfcc.setText(_translate("MainWindow", "GFCC"))
        self.rb_decision_tree.setText(_translate("MainWindow", "Decision Tree"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">K Fold Cross Validation number of splits selection</span></p></body></html>"))
        self.le_kfold.setText(_translate("MainWindow", "10"))
        self.pb_select_all_features.setText(_translate("MainWindow", "Select all features"))
        self.cb_mfcc_derivative.setText(_translate("MainWindow", "MFCC Derivative"))
        self.fscore_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline;\">F-SCORE</span></p></body></html>"))
        self.recall_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline;\">RECALL</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>AVG F-SCORE</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>AVG RECALL</p></body></html>"))
        self.min_accuracy_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline;\">ACCURACY</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p>MIN ACCURACY</p></body></html>"))
        self.precision_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline;\">PRECISION</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p>AVG PRECISION</p></body></html>"))
        self.knn_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">K: </span></p></body></html>"))
        self.tab_screen.setTabText(self.tab_screen.indexOf(self.tab_screen_1), _translate("MainWindow", "Classification Results"))
        self.start_genre_classification.setText(_translate("MainWindow", "Estimate Genre"))
        self.genre_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline;\">ESTIMATED GENRE</span></p></body></html>"))
        self.genre_music_name_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">NAME OF THE MUSIC</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Waveplot</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Estimated Genre</span></p></body></html>"))
        self.rb_naive_bayes_4.setText(_translate("MainWindow", "Naive Bayes"))
        self.rb_svm_4.setText(_translate("MainWindow", "SVM"))
        self.rb_random_forest_4.setText(_translate("MainWindow", "Random Forest"))
        self.label_40.setText(_translate("MainWindow", "CLASSIFIER"))
        self.rb_decision_tree_4.setText(_translate("MainWindow", "Decision Tree"))
        self.rb_knn_4.setText(_translate("MainWindow", "K-NN"))
        self.cb_chroma_stft_4.setText(_translate("MainWindow", "Chroma STFT"))
        self.cb_spec_cen_4.setText(_translate("MainWindow", "Spectral Centroid"))
        self.cb_spec_ban_4.setText(_translate("MainWindow", "Spectral Bandwidth"))
        self.cb_gfcc_4.setText(_translate("MainWindow", "GFCC"))
        self.label_41.setText(_translate("MainWindow", "FEATURES"))
        self.cb_zcr_4.setText(_translate("MainWindow", "Zero Crossing Rate"))
        self.cb_mfcc_4.setText(_translate("MainWindow", "MFCC"))
        self.cb_mfcc_derivative_4.setText(_translate("MainWindow", "MFCC Derivative"))
        self.cb_hpcp_4.setText(_translate("MainWindow", "HPCP"))
        self.cb_rmse_4.setText(_translate("MainWindow", "RMSE"))
        self.pb_select_all_features_4.setText(_translate("MainWindow", "Select all features"))
        self.cb_spec_con_4.setText(_translate("MainWindow", "Spectral Contrast"))
        self.cb_spec_rollof_4.setText(_translate("MainWindow", "Spectral Rollof"))
        self.select_music_file.setText(_translate("MainWindow", "Select Music File"))
        self.knn_label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">K: </span></p></body></html>"))
        self.play_button.setText(_translate("MainWindow", "PLAY"))
        self.stop_button.setText(_translate("MainWindow", "STOP"))
        self.tab_screen.setTabText(self.tab_screen.indexOf(self.tab_screen_2), _translate("MainWindow", "Genre Estimation"))
        self.import_file.setText(_translate("MainWindow", "Import Music"))
        self.actionZero_Crossing_Rate.setText(_translate("MainWindow", "Zero Crossing Rate"))
        self.import_music_file_action.setText(_translate("MainWindow", "Import Music File/s"))
        self.actionImport_Multiple_Music_Files.setText(_translate("MainWindow", "Import Multiple Music Files"))
        self.use_existing_db_action.setText(_translate("MainWindow", "Use Existing Database (Default)"))
        self.create_new_db_action.setText(_translate("MainWindow", "Create a New Database"))

        #qt designer bitis


        self.start_classification_button.clicked.connect(self.start_classification)
        self.pb_select_all_features.clicked.connect(self.select_all_features)
        self.pb_select_all_features_4.clicked.connect(self.select_all_features_genretab)
        self.select_music_file.clicked.connect(self.import_music)
        self.start_genre_classification.clicked.connect(self.estimate_music_genre)
        self.knn_label.setVisible(False)
        self.knn_sb.setVisible(False)
        self.knn_sb.setValue(1)
        self.knn_label_4.setVisible(False)
        self.knn_sb_4.setVisible(False)
        self.knn_sb_4.setValue(1)
        self.play_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        self.start_genre_classification.setEnabled(False)
        self.rb_knn.toggled.connect(self.manage_hidden_sb)
        self.rb_knn_4.toggled.connect(self.manage_hidden_sb)
        self.play_button.clicked.connect(self.genre_play_music)
        self.stop_button.clicked.connect(self.genre_stop_music)





    def manage_hidden_sb(self):

        if self.rb_knn.isChecked() == True:
            self.knn_label.setVisible(True)
            self.knn_sb.setVisible(True)


        else:
            self.knn_label.setVisible(False)
            self.knn_sb.setVisible(False)



        if self.rb_knn_4.isChecked() == True:
            self.knn_label_4.setVisible(True)
            self.knn_sb_4.setVisible(True)


        else:
            self.knn_label_4.setVisible(False)
            self.knn_sb_4.setVisible(False)




    def import_music(self):
        options = QFileDialog.Options()
        fname,ok = QFileDialog.getOpenFileName(self.mainwindow, 'Import music file','', 'Music files (*.mp3 *.wav *.au)',options=options)
        self.test_music_path = fname
        if ok:
            #Music name display
            url = QUrl.fromLocalFile(fname)
            music_name = url.fileName()
            self.test_music_name = music_name
            self.genre_music_name_label.setText(music_name)
            self.genre_music_name_label.setStyleSheet("QLabel {font: 20pt;color: rgb(255, 255, 255);background-color:rgb(0, 0, 255);text-align: center}")


            #Waveplot drawing
            y, sr = librosa.load(fname)
            plt.figure()
            librosa.display.waveplot(y, sr=sr)
            plt.title('Waveplot of the Song')
            plt.savefig('fig2.png', bbox_inches="tight", pad_inches=0.3)
            self.waveplot_label.setPixmap(QtGui.QPixmap('fig2.png').scaled(371, 181, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation))
            plt.clf()

            self.start_genre_classification.setEnabled(True)
            self.play_button.setEnabled(True)
            self.stop_button.setEnabled(True)

            self.import_info_msg.setIcon(QMessageBox.Information)
            self.import_info_msg.setWindowTitle("Music Import Information")

            self.import_info_msg.setText("The music file is successfully loaded!")
            self.import_info_msg.show()




    def select_all_features(self):
        self.cb_zcr.setChecked(True)
        self.cb_hpcp.setChecked(True)
        self.cb_mfcc.setChecked(True)
        self.cb_rmse.setChecked(True)
        self.cb_gfcc.setChecked(True)
        self.cb_spec_cen.setChecked(True)
        self.cb_spec_ban.setChecked(True)
        self.cb_spec_con.setChecked(True)
        self.cb_spec_rollof.setChecked(True)
        self.cb_chroma_stft.setChecked(True)
        self.cb_mfcc_derivative.setChecked(True)


    def select_all_features_genretab(self):
        self.cb_zcr_4.setChecked(True)
        self.cb_hpcp_4.setChecked(True)
        self.cb_mfcc_4.setChecked(True)
        self.cb_rmse_4.setChecked(True)
        self.cb_gfcc_4.setChecked(True)
        self.cb_spec_cen_4.setChecked(True)
        self.cb_spec_ban_4.setChecked(True)
        self.cb_spec_con_4.setChecked(True)
        self.cb_spec_rollof_4.setChecked(True)
        self.cb_chroma_stft_4.setChecked(True)
        self.cb_mfcc_derivative_4.setChecked(True)


    """
    def write_features_to_feature_table(self,feature_list,music_name):
        numRows = self.feature_table.rowCount()
        self.feature_table.insertRow(numRows)
        self.feature_table.setItem(numRows, 0, QtWidgets.QTableWidgetItem(music_name))
        for i in range(44):
            self.feature_table.setItem(numRows, i+1, QtWidgets.QTableWidgetItem(str(feature_list[i]) ) )
    """



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


    def genre_stop_music(self):
        winsound.PlaySound(None, winsound.SND_PURGE)



    #Write given feature list of a specific song to the database
    def write_features_to_database(self,feature_list,s_name,db_conn):
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


    def start_classification(self):
        database_features = self.get_user_selected_features()

        if self.feature_flag == 1  and self.knn_sb.value() != 0 and self.le_kfold.text() != "":

            #genre labels are encoded to integer values
            tmp = []

            for song in database_features.song_name:
                if "blues" in song:
                    tmp.append(0)
                if "classical" in song:
                    tmp.append(1)
                if "country" in song:
                    tmp.append(2)
                if "disco" in song:
                    tmp.append(3)
                if "hiphop" in song:
                    tmp.append(4)
                if "jazz" in song:
                    tmp.append(5)
                if "metal" in song:
                    tmp.append(6)
                if "pop" in song:
                    tmp.append(7)
                if "reggae" in song:
                    tmp.append(8)
                if "rock" in song:
                    tmp.append(9)



            y_data = np.array(tmp, dtype=int)
            #drop np.array dondurur mu?
            x = database_features.drop(["song_name"],axis=1)


            #min-max normalization (0,1)
            #x_data = ( (x - np.min(x)) / (np.max(x) - np.min(x)) )

            #min-max normalization (-1,1)
            normalizer = preprocessing.MinMaxScaler((-1,1))
            normalizer.fit(x)
            self.normalizer = normalizer
            x_data = normalizer.transform(x.values)

            #default model selection
            classifier = KNeighborsClassifier(n_neighbors=self.knn_sb.value(), weights='distance')




            if self.rb_knn.isChecked() == True:
                classifier = KNeighborsClassifier(n_neighbors=self.knn_sb.value(), weights='distance')

            if self.rb_svm.isChecked() == True:
                classifier = SVC(kernel='linear', random_state=42)#, gamma=1/25)

            if self.rb_naive_bayes.isChecked() == True:
                classifier = GaussianNB()

            if self.rb_decision_tree.isChecked() == True:
                classifier = DecisionTreeClassifier()

            if self.rb_random_forest.isChecked() == True:
                classifier = RandomForestClassifier(criterion='entropy', random_state=42)



            self.classifier = classifier

            #K fold cross validation
            cross_validator = model_selection.KFold(n_splits=int(self.le_kfold.text()), shuffle=True, random_state=42)
            total_acc = 0
            init_flag = 0
            max_acc = 0
            min_acc = 1.0
            resulting_cm = []  #resulting confusion matrix will be calculated cumulatively as k fold cross validation advances
            precision = 0
            recall = 0
            f1 = 0


            for train_index,test_index in cross_validator.split(x_data):
                x_train, x_test = x_data[train_index], x_data[test_index]
                y_train, y_test = y_data[train_index], y_data[test_index]

                classifier.fit(x_train,y_train)
                acc = classifier.score(x_test,y_test)
                y_pred = classifier.predict(x_test)
                total_acc += acc

                if acc > max_acc:
                    max_acc = acc

                elif acc < min_acc:
                    min_acc = acc

                cm = confusion_matrix(y_test,y_pred)
                precision += precision_score(y_test, y_pred, average='macro')
                recall += recall_score(y_test, y_pred, average='macro')
                f1 += f1_score(y_test, y_pred, average='macro')

                if init_flag == 0:
                    resulting_cm = cm
                    init_flag = 1
                else:
                    resulting_cm = resulting_cm + cm





            #print("precision:",100*(precision/int(self.le_kfold.text()))) #degisecek
            #print("recall:",100*(recall/int(self.le_kfold.text()))) #degisecek
	    #print("f1_score:",100*(recall/int(self.le_kfold.text()))) #degisecek


            avg_acc = total_acc / int(self.le_kfold.text())
            avg_acc *= 100
            #Avg acc
            self.avg_accuracy_label.setScaledContents(True)
            self.avg_accuracy_label.setText(("%%%.2f" % avg_acc))
            self.avg_accuracy_label.setStyleSheet("QLabel {font: 20pt;color: rgb(255, 255, 255);background-color:rgb(0, 0, 255);text-align: center}")

            #Max acc
            max_acc *= 100
            self.max_accuracy_label.setScaledContents(True)
            self.max_accuracy_label.setText(("%%%.2f" % max_acc))
            self.max_accuracy_label.setStyleSheet("QLabel {font: 20pt;color: rgb(255, 255, 255);background-color:rgb(0, 0, 255);text-align: center}")

            #Min acc
            min_acc *= 100
            self.min_accuracy_label.setScaledContents(True)
            self.min_accuracy_label.setText(("%%%.2f" % min_acc))
            self.min_accuracy_label.setStyleSheet("QLabel {font: 20pt;color: rgb(255, 255, 255);background-color:rgb(0, 0, 255);text-align: center}")

            #Precision showing
            precision = 100*(precision/int(self.le_kfold.text()))
            self.precision_label.setScaledContents(True)
            self.precision_label.setText(("%%%.2f" % precision))
            self.precision_label.setStyleSheet("QLabel {font: 20pt;color: rgb(255, 255, 255);background-color:rgb(0, 0, 255);text-align: center}")

            #Recall showing
            recall = 100*(recall/int(self.le_kfold.text()))
            self.recall_label.setScaledContents(True)
            self.recall_label.setText(("%%%.2f" % recall))
            self.recall_label.setStyleSheet("QLabel {font: 20pt;color: rgb(255, 255, 255);background-color:rgb(0, 0, 255);text-align: center}")

            #F-score showing
            f1 = 100*(f1/int(self.le_kfold.text()))
            self.fscore_label.setScaledContents(True)
            self.fscore_label.setText(("%%%.2f" % f1))
            self.fscore_label.setStyleSheet("QLabel {font: 20pt;color: rgb(255, 255, 255);background-color:rgb(0, 0, 255);text-align: center}")


            self.plot_confusion_matrix(resulting_cm, classes=["blues", "classical", "country", "disco", "hiphop", "jazz", "metal", "pop", "reggae", "rock"])
            self.con_matrix_label.setScaledContents(True)
            self.con_matrix_label.setPixmap(QtGui.QPixmap('fig.png'))

        else:

            self.error_msg.setIcon(QMessageBox.Critical)
            self.error_msg.setWindowTitle("Error")

            if self.feature_flag == 0:
                self.error_msg.setText("Please select at least one feature from features!")


            elif self.knn_sb.value() == 0:
                self.error_msg.setText("K value for K-NN classification cannot be 0!")


            elif self.le_kfold.text() == "":
                self.error_msg.setText("Number of splits value for K fold cross validation cannot be empty!")


            self.error_msg.show()




    def get_user_selected_features(self):
        db_con = sqlite3.connect("data.db")

        cols = "song_name,"
        self.feature_flag = 0

        if self.cb_zcr.isChecked() == True:
            self.feature_flag = 1
            cols = cols + "avg_zero_crs_rate,var_zero_crs_rate,med_zero_crs_rate,"
        if self.cb_spec_cen.isChecked() == True:
            self.feature_flag = 1
            cols = cols + "avg_spec_centroid,var_spec_centroid,med_spec_centroid,"
        if self.cb_spec_ban.isChecked() == True:
            self.feature_flag = 1
            cols = cols + "avg_spec_bandwidth,var_spec_bandwidth,med_spec_bandwidth,"
        if self.cb_spec_con.isChecked() == True:
            self.feature_flag = 1
            cols = cols + "avg_spec_contrast,var_spec_contrast,med_spec_contrast,"
        if self.cb_spec_rollof.isChecked() == True:
            self.feature_flag = 1
            cols = cols + "avg_spec_rolloff,var_spec_rolloff,med_spec_rolloff,"
        if self.cb_rmse.isChecked() == True:
            self.feature_flag = 1
            cols = cols + "avg_rmse,var_rmse,med_rmse,"

        if self.cb_mfcc.isChecked() == True:
            self.feature_flag = 1
            for i in range(1,21):
                cols = cols + "avg_mfcc_" + str(i) + ","
            for i in range(1,21):
                cols = cols + "var_mfcc_" + str(i) + ","

        if self.cb_chroma_stft.isChecked() == True:
            self.feature_flag = 1
            for i in range(1,13):
                cols = cols + "avg_chroma_stft_" + str(i) + ","
            for i in range(1,13):
                cols = cols + "var_chroma_stft_" + str(i) + ","


        if self.cb_gfcc.isChecked() == True:
            self.feature_flag = 1
            for i in range(1,14):
                cols = cols + "avg_gfcc_" + str(i) + ","



        if self.cb_hpcp.isChecked() == True:
            self.feature_flag = 1
            for i in range(1,37):
                cols = cols + "avg_hpcp_" + str(i) + ","




        if self.cb_mfcc_derivative.isChecked() == True:
            self.feature_flag = 1
            for i in range(1,21):
                cols = cols + "avg_mfcc_derivative_" + str(i) + ","
                cols = cols + "var_mfcc_derivative_" + str(i) + ","





        cols = cols[0:-1]


        query = "SELECT " + cols + " FROM songs"
        database_features = pd.read_sql(sql=query, con=db_con)


        #print(database_features)
        db_con.close()
        return database_features



    #The function at sklearn confusion matrix page is used
    def plot_confusion_matrix(self,cm, classes,
                              normalize=False,
                              title=' Confusion Matrix',
                              cmap=plt.cm.Blues):


        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
            print("Normalized confusion matrix")
        else:
            print('Confusion matrix, without normalization')

        print(cm)

        plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
        plt.title('Confusion Matrix')
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)

        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], 'd'),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

        plt.xlabel('Predicted Label')
        plt.ylabel('True Label')
        plt.tight_layout()
        plt.savefig('fig.png', bbox_inches="tight", pad_inches=0.5)
        plt.clf()


    def estimate_music_genre(self):

        db_con = sqlite3.connect("data.db")
        feature_flag = 0

        cols = "song_name,"

        if self.cb_zcr_4.isChecked() == True:
            feature_flag = 1
            cols = cols + "avg_zero_crs_rate,var_zero_crs_rate,med_zero_crs_rate,"
        if self.cb_spec_cen_4.isChecked() == True:
            feature_flag = 1
            cols = cols + "avg_spec_centroid,var_spec_centroid,med_spec_centroid,"
        if self.cb_spec_ban_4.isChecked() == True:
            feature_flag = 1
            cols = cols + "avg_spec_bandwidth,var_spec_bandwidth,med_spec_bandwidth,"
        if self.cb_spec_con_4.isChecked() == True:
            feature_flag = 1
            cols = cols + "avg_spec_contrast,var_spec_contrast,med_spec_contrast,"
        if self.cb_spec_rollof_4.isChecked() == True:
            feature_flag = 1
            cols = cols + "avg_spec_rolloff,var_spec_rolloff,med_spec_rolloff,"
        if self.cb_rmse_4.isChecked() == True:
            feature_flag = 1
            cols = cols + "avg_rmse,var_rmse,med_rmse,"

        if self.cb_mfcc_4.isChecked() == True:
            feature_flag = 1
            for i in range(1,21):
                cols = cols + "avg_mfcc_" + str(i) + ","
            for i in range(1,21):
                cols = cols + "var_mfcc_" + str(i) + ","

        if self.cb_chroma_stft_4.isChecked() == True:
            feature_flag = 1
            for i in range(1,13):
                cols = cols + "avg_chroma_stft_" + str(i) + ","
            for i in range(1,13):
                cols = cols + "var_chroma_stft_" + str(i) + ","


        if self.cb_gfcc_4.isChecked() == True:
            feature_flag = 1
            for i in range(1,14):
                cols = cols + "avg_gfcc_" + str(i) + ","



        if self.cb_hpcp_4.isChecked() == True:
            feature_flag = 1
            for i in range(1,37):
                cols = cols + "avg_hpcp_" + str(i) + ","


        if self.cb_mfcc_derivative_4.isChecked() == True:
            feature_flag = 1
            for i in range(1,21):
                cols = cols + "avg_mfcc_derivative_" + str(i) + ","
                cols = cols + "var_mfcc_derivative_" + str(i) + ","





        cols = cols[0:-1]

        query = "SELECT " + cols + " FROM songs"
        database_features = pd.read_sql(sql=query, con=db_con)



        if feature_flag == 1  and self.knn_sb_4.value() != 0:

            #genre labels are encoded to integer values
            tmp = []

            for song in database_features.song_name:
                if "blues" in song:
                    tmp.append(0)
                if "classical" in song:
                    tmp.append(1)
                if "country" in song:
                    tmp.append(2)
                if "disco" in song:
                    tmp.append(3)
                if "hiphop" in song:
                    tmp.append(4)
                if "jazz" in song:
                    tmp.append(5)
                if "metal" in song:
                    tmp.append(6)
                if "pop" in song:
                    tmp.append(7)
                if "reggae" in song:
                    tmp.append(8)
                if "rock" in song:
                    tmp.append(9)



            y_data = np.array(tmp, dtype=int)

            x = database_features.drop(["song_name"],axis=1)


            #min-max normalization (0,1)
            #x_data = ( (x - np.min(x)) / (np.max(x) - np.min(x)) )

            #min-max normalization (-1,1)
            normalizer = preprocessing.MinMaxScaler((-1,1))
            normalizer.fit(x)
            x_data = normalizer.transform(x.values)



            #default model selection
            classifier = KNeighborsClassifier(n_neighbors=self.knn_sb_4.value(), weights='distance')




            if self.rb_knn_4.isChecked() == True:
                classifier = KNeighborsClassifier(n_neighbors=self.knn_sb_4.value(), weights='distance')

            if self.rb_svm_4.isChecked() == True:
                classifier = SVC(kernel='linear', random_state=42)

            if self.rb_naive_bayes_4.isChecked() == True:
                classifier = GaussianNB()

            if self.rb_decision_tree_4.isChecked() == True:
                classifier = DecisionTreeClassifier()

            if self.rb_random_forest_4.isChecked() == True:
                classifier = RandomForestClassifier(criterion='entropy', random_state=42)



            classifier.fit(x_data,y_data)


            normalizer_test = preprocessing.MinMaxScaler((-1,1))



            test_music_name = self.test_music_name
            test_music_name = test_music_name[0:-4] # .wav silindi
            test_music_name = test_music_name + ".au" # .au uzanti eklendi


            #Secilen muzik ozellik cekimi
            
            query = "SELECT " + cols + " FROM songs WHERE song_name=?"
            test_features = pd.read_sql(sql=query, con=db_con, params=(test_music_name,))
            print(test_features)
            x = test_features.drop(["song_name"],axis=1)
            #normalizer_test.fit(x)
            x_test =  normalizer.transform(x.values)


            Y_pred = classifier.predict(x_test)


            if Y_pred == 0: self.genre_label.setText("Blues")
            if Y_pred == 1: self.genre_label.setText("Classical")
            if Y_pred == 2: self.genre_label.setText("Country")
            if Y_pred == 3: self.genre_label.setText("Disco")
            if Y_pred == 4: self.genre_label.setText("Hiphop")
            if Y_pred == 5: self.genre_label.setText("Jazz")
            if Y_pred == 6: self.genre_label.setText("Metal")
            if Y_pred == 7: self.genre_label.setText("Pop")
            if Y_pred == 8: self.genre_label.setText("Reggae")
            if Y_pred == 9: self.genre_label.setText("Rock")

            self.genre_label.setStyleSheet("QLabel {font: 30pt;color: rgb(255, 255, 255);background-color:rgb(0, 0, 255);text-align: center}")

            db_con.close()


        else:

            self.error_msg.setIcon(QMessageBox.Critical)
            self.error_msg.setWindowTitle("Error")

            if feature_flag == 0:
                self.error_msg.setText("Please select at least one feature from features!")



            self.error_msg.show()    



    #Feature extraction part
    def feature_extract(self,song_name):

        y,sr = librosa.load(song_name)

        total_features = np.array([np.average(librosa.feature.zero_crossing_rate(y)),np.var(librosa.feature.zero_crossing_rate(y)),np.median(librosa.feature.zero_crossing_rate(y)),
               np.average(librosa.feature.spectral_centroid(y,sr)),np.var(librosa.feature.spectral_centroid(y,sr)),np.median(librosa.feature.spectral_centroid(y,sr)),
                         np.average(librosa.feature.spectral_bandwidth(y,sr)),np.var(librosa.feature.spectral_bandwidth(y,sr)),np.median(librosa.feature.spectral_bandwidth(y,sr)),
                                   np.average(librosa.feature.spectral_contrast(y,sr)),np.var(librosa.feature.spectral_contrast(y,sr)),np.median(librosa.feature.spectral_contrast(y,sr)),
                                             np.average(librosa.feature.spectral_rolloff(y,sr)),np.var(librosa.feature.spectral_rolloff(y,sr)),np.median(librosa.feature.spectral_rolloff(y,sr)),
                                                       np.average(librosa.feature.rmse(y)),np.var(librosa.feature.rmse(y)),np.median(librosa.feature.rmse(y))])





        #calculate and add avg mfcc
        tmp_mfcc=librosa.feature.mfcc(y,sr)

        tmpp=[None]*20
        for i in range(20):
            tmpp[i]=np.average(tmp_mfcc[i])
        total_features=np.append(total_features,np.array(tmpp))

        #calculate and add avg chroma_stft
        tmp_chroma_stft=librosa.feature.chroma_stft(y,sr)

        tmpp=[None]*12
        for i in range(12):
            tmpp[i]=np.average(tmp_chroma_stft[i])
        total_features=np.append(total_features,np.array(tmpp))


        #essentia features
        features, features_frames = es.MusicExtractor(lowlevelStats=['mean', 'stdev'],
                                                      rhythmStats=['mean', 'stdev'],
                                                      tonalStats=['mean', 'stdev'])(song_name)




        #calculate and add avg gfcc
        avg_gfcc_vector = features["lowlevel.gfcc.mean"]
        total_features = np.append(total_features,avg_gfcc_vector)


        #calculate and add avg HPCP
        avg_hpcp_vector = features["tonal.hpcp.mean"]
        total_features = np.append(total_features,avg_hpcp_vector)



        #calculate and add std dev. mfcc
        tmpp=[None]*20
        for i in range(20):
            tmpp[i]=np.var(tmp_mfcc[i])
        total_features=np.append(total_features,np.array(tmpp))


        #calculate and add std dev. chroma stft
        tmpp=[None]*12
        for i in range(12):
            tmpp[i]=np.var(tmp_chroma_stft[i])
        total_features=np.append(total_features,tmpp)



        #MFCC derivative
        #Reference --> Bilal's code

        mfcc_col_size = len(tmp_mfcc[0])
        mfcc_derivative = np.empty([20, mfcc_col_size], dtype=float)
        #First columns initialized to 0
        for i in range(20):
            mfcc_derivative[i][0] = 0
        #Calculating derivative and filling matrix
        for i in range(20):
            for j in range(1, mfcc_col_size):
                mfcc_derivative[i][j] = tmp_mfcc[i][j] - tmp_mfcc[i][j-1]


        #add mfcc derivative avg and std
        mfcc_derivative_avgs_stds = np.empty(2*20, dtype=float)
        j=0
        for i in range(20):
            mfcc_derivative_avgs_stds[j] = np.average(mfcc_derivative[i])
            mfcc_derivative_avgs_stds[j+1] = np.var(mfcc_derivative[i])
            j = j+2
        total_features = np.append(total_features, np.array(mfcc_derivative_avgs_stds))




        return total_features




if __name__ == '__main__':

    multiprocessing.freeze_support()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
