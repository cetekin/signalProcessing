# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\arayuzV2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        self.rb_knn.setGeometry(QtCore.QRect(200, 70, 95, 20))
        self.rb_knn.setObjectName("rb_knn")
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
        self.cb_gfcc = QtWidgets.QCheckBox(self.tab_screen_1)
        self.cb_gfcc.setGeometry(QtCore.QRect(710, 340, 111, 20))
        self.cb_gfcc.setObjectName("cb_gfcc")
        self.rb_decision_tree = QtWidgets.QRadioButton(self.tab_screen_1)
        self.rb_decision_tree.setGeometry(QtCore.QRect(200, 190, 121, 20))
        self.rb_decision_tree.setObjectName("rb_decision_tree")
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
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>CONFUSION MATRIX</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>AVG ACCURACY</p></body></html>"))
        self.max_accuracy_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; text-decoration: underline;\">ACCURACY</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>MAX ACCURACY</p></body></html>"))
        self.start_classification_button.setText(_translate("MainWindow", "Start Classification"))
        self.cb_hpcp.setText(_translate("MainWindow", "HPCP"))
        self.cb_gfcc.setText(_translate("MainWindow", "GFCC"))
        self.rb_decision_tree.setText(_translate("MainWindow", "Decision Tree"))
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

