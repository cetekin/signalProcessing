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
import pandas as pd
from sklearn import model_selection, preprocessing, metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


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
        self.tab_screen = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_screen.setGeometry(QtCore.QRect(0, 0, 1051, 931))
        self.tab_screen.setStyleSheet("background-color: rgb(222, 249, 255);")
        self.tab_screen.setObjectName("tab_screen")
        self.tab_screen_1 = QtWidgets.QWidget()
        self.tab_screen_1.setObjectName("tab_screen_1")
        self.rb_lda = QtWidgets.QRadioButton(self.tab_screen_1)
        self.rb_lda.setGeometry(QtCore.QRect(200, 250, 95, 20))
        self.rb_lda.setObjectName("rb_lda")
        self.rb_knn = QtWidgets.QRadioButton(self.tab_screen_1)
        self.rb_knn.setGeometry(QtCore.QRect(200, 70, 95, 20))
        self.rb_knn.setObjectName("rb_knn")
        self.rb_log_reg = QtWidgets.QRadioButton(self.tab_screen_1)
        self.rb_log_reg.setGeometry(QtCore.QRect(200, 220, 141, 20))
        self.rb_log_reg.setObjectName("rb_log_reg")
        self.rb_naive_bayes = QtWidgets.QRadioButton(self.tab_screen_1)
        self.rb_naive_bayes.setGeometry(QtCore.QRect(200, 100, 95, 20))
        self.rb_naive_bayes.setObjectName("rb_naive_bayes")
        self.label_5 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_5.setGeometry(QtCore.QRect(200, 30, 91, 31))
        self.label_5.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.rb_random_forest = QtWidgets.QRadioButton(self.tab_screen_1)
        self.rb_random_forest.setGeometry(QtCore.QRect(200, 160, 121, 20))
        self.rb_random_forest.setObjectName("rb_random_forest")
        self.rb_neu_network = QtWidgets.QRadioButton(self.tab_screen_1)
        self.rb_neu_network.setGeometry(QtCore.QRect(200, 190, 131, 20))
        self.rb_neu_network.setObjectName("rb_neu_network")
        self.rb_svm = QtWidgets.QRadioButton(self.tab_screen_1)
        self.rb_svm.setGeometry(QtCore.QRect(200, 130, 95, 20))
        self.rb_svm.setObjectName("rb_svm")
        self.label_4 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_4.setGeometry(QtCore.QRect(710, 30, 91, 31))
        self.label_4.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.cb_zcr = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_zcr.setGeometry(QtCore.QRect(710, 70, 141, 20))
        self.cb_zcr.setObjectName("cb_zcr")
        self.cb_spec_cen = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_spec_cen.setGeometry(QtCore.QRect(710, 100, 131, 20))
        self.cb_spec_cen.setObjectName("cb_spec_cen")
        self.cb_rmse = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_rmse.setGeometry(QtCore.QRect(710, 220, 81, 20))
        self.cb_rmse.setObjectName("cb_rmse")
        self.cb_spec_con = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_spec_con.setGeometry(QtCore.QRect(710, 160, 131, 20))
        self.cb_spec_con.setObjectName("cb_spec_con")
        self.cb_spec_ban = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_spec_ban.setGeometry(QtCore.QRect(710, 130, 141, 20))
        self.cb_spec_ban.setObjectName("cb_spec_ban")
        self.cb_chroma_stft = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_chroma_stft.setGeometry(QtCore.QRect(710, 280, 111, 20))
        self.cb_chroma_stft.setObjectName("cb_chroma_stft")
        self.cb_spec_rollof = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_spec_rollof.setGeometry(QtCore.QRect(710, 190, 111, 20))
        self.cb_spec_rollof.setObjectName("cb_spec_rollof")
        self.cb_mfcc = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_mfcc.setGeometry(QtCore.QRect(710, 250, 81, 20))
        self.cb_mfcc.setObjectName("cb_mfcc")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_screen_1)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 2, 2))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.avg_accuracy_label = QtWidgets.QLabel(self.tab_screen_1)
        self.avg_accuracy_label.setGeometry(QtCore.QRect(110, 480, 271, 71))
        self.avg_accuracy_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"font-weight: bold;\n"
"}")
        self.avg_accuracy_label.setObjectName("avg_accuracy_label")
        self.con_matrix_label = QtWidgets.QLabel(self.tab_screen_1)
        self.con_matrix_label.setGeometry(QtCore.QRect(600, 450, 347, 297))
        self.con_matrix_label.setMinimumSize(QtCore.QSize(347, 297))
        self.con_matrix_label.setMaximumSize(QtCore.QSize(444, 397))
        self.con_matrix_label.setText("")
        self.con_matrix_label.setObjectName("con_matrix_label")
        self.label_6 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_6.setGeometry(QtCore.QRect(710, 400, 131, 31))
        self.label_6.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_7.setGeometry(QtCore.QRect(190, 440, 131, 31))
        self.label_7.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_7.setObjectName("label_7")
        self.max_accuracy_label = QtWidgets.QLabel(self.tab_screen_1)
        self.max_accuracy_label.setGeometry(QtCore.QRect(110, 650, 271, 71))
        self.max_accuracy_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"font-weight: bold;\n"
"}")
        self.max_accuracy_label.setObjectName("max_accuracy_label")
        self.label_8 = QtWidgets.QLabel(self.tab_screen_1)
        self.label_8.setGeometry(QtCore.QRect(190, 610, 131, 31))
        self.label_8.setStyleSheet("QLabel {\n"
"color: black;\n"
"font-weight: bold;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.start_classification_button = QtWidgets.QPushButton(self.tab_screen_1)
        self.start_classification_button.setGeometry(QtCore.QRect(420, 270, 151, 51))
        self.start_classification_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(142, 157, 255);\n"
"font-weight: bold;\n"
"}")
        self.start_classification_button.setObjectName("start_classification_button")
        self.cb_hpcp = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_hpcp.setGeometry(QtCore.QRect(710, 310, 111, 20))
        self.cb_hpcp.setObjectName("cb_hpcp")
        self.tab_screen.addTab(self.tab_screen_1, "")
        self.tab_screen_2 = QtWidgets.QWidget()
        self.tab_screen_2.setObjectName("tab_screen_2")
        self.waveplot_label = QtWidgets.QLabel(self.tab_screen_2)
        self.waveplot_label.setGeometry(QtCore.QRect(320, 110, 386, 278))
        self.waveplot_label.setMinimumSize(QtCore.QSize(386, 278))
        self.waveplot_label.setMaximumSize(QtCore.QSize(386, 278))
        self.waveplot_label.setText("")
        self.waveplot_label.setObjectName("waveplot_label")
        self.start_genre_classification = QtWidgets.QPushButton(self.tab_screen_2)
        self.start_genre_classification.setGeometry(QtCore.QRect(430, 60, 151, 31))
        self.start_genre_classification.setStyleSheet("QPushButton{\n"
"background-color: rgb(142, 157, 255);\n"
"font-weight: bold;\n"
"}")
        self.start_genre_classification.setObjectName("start_genre_classification")
        self.genre_label = QtWidgets.QLabel(self.tab_screen_2)
        self.genre_label.setGeometry(QtCore.QRect(380, 590, 271, 71))
        self.genre_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"font-weight: bold;\n"
"}")
        self.genre_label.setObjectName("genre_label")
        self.genre_play_button = QtWidgets.QPushButton(self.tab_screen_2)
        self.genre_play_button.setGeometry(QtCore.QRect(430, 450, 81, 31))
        self.genre_play_button.setStyleSheet("QPushButton{\n"
"font-weight: bold;\n"
"background-color: rgb(57, 255, 47)\n"
"}")
        self.genre_play_button.setObjectName("genre_play_button")
        self.genre_pause_button = QtWidgets.QPushButton(self.tab_screen_2)
        self.genre_pause_button.setGeometry(QtCore.QRect(530, 450, 81, 31))
        self.genre_pause_button.setStyleSheet("QPushButton{\n"
"font-weight: bold;\n"
"background-color: rgb(255, 83, 83);\n"
"}")
        self.genre_pause_button.setObjectName("genre_pause_button")
        self.genre_music_name_label = QtWidgets.QLabel(self.tab_screen_2)
        self.genre_music_name_label.setGeometry(QtCore.QRect(340, 410, 371, 20))
        self.genre_music_name_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"}")
        self.genre_music_name_label.setObjectName("genre_music_name_label")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rb_lda.setText(_translate("MainWindow", "LDA"))
        self.rb_knn.setText(_translate("MainWindow", "K-NN"))
        self.rb_log_reg.setText(_translate("MainWindow", "Logistic Regression"))
        self.rb_naive_bayes.setText(_translate("MainWindow", "Naive Bayes"))
        self.label_5.setText(_translate("MainWindow", "CLASSIFIER"))
        self.rb_random_forest.setText(_translate("MainWindow", "Random Forest"))
        self.rb_neu_network.setText(_translate("MainWindow", "Neural Network"))
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
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>CONFUSION MATRIX</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>AVG ACCURACY</p></body></html>"))
        self.max_accuracy_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline;\">ACCURACY</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>MAX ACCURACY</p></body></html>"))
        self.start_classification_button.setText(_translate("MainWindow", "Start Classification"))
        self.cb_hpcp.setText(_translate("MainWindow", "HPCP"))
        self.tab_screen.setTabText(self.tab_screen.indexOf(self.tab_screen_1), _translate("MainWindow", "Classification Results"))
        self.start_genre_classification.setText(_translate("MainWindow", "Import Music File"))
        self.genre_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline;\">ESTIMATED GENRE</span></p></body></html>"))
        self.genre_play_button.setText(_translate("MainWindow", "PLAY"))
        self.genre_pause_button.setText(_translate("MainWindow", "STOP"))
        self.genre_music_name_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">NAME OF THE MUSIC</p></body></html>"))
        self.tab_screen.setTabText(self.tab_screen.indexOf(self.tab_screen_2), _translate("MainWindow", "Genre Estimation"))
        self.import_file.setText(_translate("MainWindow", "Import Music"))
        self.actionZero_Crossing_Rate.setText(_translate("MainWindow", "Zero Crossing Rate"))
        self.import_music_file_action.setText(_translate("MainWindow", "Import Music File/s"))
        self.actionImport_Multiple_Music_Files.setText(_translate("MainWindow", "Import Multiple Music Files"))
        self.use_existing_db_action.setText(_translate("MainWindow", "Use Existing Database (Default)"))
        self.create_new_db_action.setText(_translate("MainWindow", "Create a New Database"))

        #qt designer bitis


        self.start_classification_button.clicked.connect(self.start_classification)
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




    def play_music(self):
        directory = self.music_directory[self.music_list.currentItem().text()]
        winsound.PlaySound(directory,winsound.SND_ASYNC)


    def pause_music(self):
        winsound.PlaySound(None, winsound.SND_PURGE)


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

        #genre labels are encoded to integer values
        tmp = []

        for song in database_features.song_name:
            if "blues" in song:
                tmp.append(1)
            if "classical" in song:
                tmp.append(2)
            if "country" in song:
                tmp.append(3)
            if "disco" in song:
                tmp.append(4)
            if "hiphop" in song:
                tmp.append(5)
            if "jazz" in song:
                tmp.append(6)
            if "metal" in song:
                tmp.append(7)
            if "pop" in song:
                tmp.append(8)
            if "reggae" in song:
                tmp.append(9)
            if "rock" in song:
                tmp.append(10)



        y_data = np.array(tmp, dtype=int)
        x = database_features.drop(["song_name"],axis=1)


        #min-max normalization
        x_data = ( (x - np.min(x)) / (np.max(x) - np.min(x)) )

        knn = SVC(kernel='linear', random_state=42)

        for i in range(10):

            x_train,x_test,y_train,y_test =train_test_split(x_data,y_data,test_size=0.1,random_state=42)

            knn.fit(x_train,y_train)
            y_pred = knn.predict(x_test)
            acc = metrics.accuracy_score(y_test, y_pred)*100

            print(acc)









        nb = GaussianNB()
        nb.fit(x_train,y_train)

        #print(nb.score(x_test,y_test))












    def get_user_selected_features(self):
        db_con = sqlite3.connect("data.db")

        cols = "song_name,"

        if self.cb_zcr.isChecked() == True:
            cols = cols + "avg_zero_crs_rate,var_zero_crs_rate,med_zero_crs_rate,"
        if self.cb_spec_cen.isChecked() == True:
            cols = cols + "avg_spec_centroid,var_spec_centroid,med_spec_centroid,"
        if self.cb_spec_ban.isChecked() == True:
            cols = cols + "avg_spec_bandwidth,var_spec_bandwidth,med_spec_bandwidth,"
        if self.cb_spec_con.isChecked() == True:
            cols = cols + "avg_spec_contrast,var_spec_contrast,med_spec_contrast,"
        if self.cb_spec_rollof.isChecked() == True:
            cols = cols + "avg_spec_rolloff,var_spec_rolloff,med_spec_rolloff,"
        if self.cb_rmse.isChecked() == True:
            cols = cols + "avg_rmse,var_rmse,med_rmse,"

        if self.cb_mfcc.isChecked() == True:
            for i in range(1,21):
                cols = cols + "avg_mfcc_" + str(i) + ","

        if self.cb_chroma_stft.isChecked() == True:
            for i in range(1,13):
                cols = cols + "avg_chroma_stft_" + str(i) + ","

        if self.cb_hpcp.isChecked() == True:
            for i in range(1,13):
                cols = cols + "avg_hpcp_" + str(i) + ","

        cols = cols[0:-1]

        query = "SELECT " + cols + " FROM songs"
        database_features = pd.read_sql(sql=query, con=db_con)


        #print(database_features)
        db_con.close()
        return database_features






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
