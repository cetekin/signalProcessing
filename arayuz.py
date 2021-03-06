# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuzV2_backup.ui'
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
        self.start_genre_classification.setGeometry(QtCore.QRect(450, 610, 151, 31))
        self.start_genre_classification.setStyleSheet("QPushButton{\n"
"background-color: rgb(142, 157, 255);\n"
"font-weight: bold;\n"
"}")
        self.start_genre_classification.setObjectName("start_genre_classification")
        self.genre_label = QtWidgets.QLabel(self.tab_screen_2)
        self.genre_label.setGeometry(QtCore.QRect(380, 700, 271, 71))
        self.genre_label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"background-color:rgb(0, 0, 255);\n"
"font-weight: bold;\n"
"}")
        self.genre_label.setAlignment(QtCore.Qt.AlignCenter)
        self.genre_label.setObjectName("genre_label")
        self.genre_music_name_label = QtWidgets.QLabel(self.tab_screen_2)
        self.genre_music_name_label.setGeometry(QtCore.QRect(340, 480, 371, 31))
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
        self.label_9.setGeometry(QtCore.QRect(430, 660, 271, 31))
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
        self.select_music_file.setGeometry(QtCore.QRect(450, 420, 151, 31))
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
        self.play_button.setGeometry(QtCore.QRect(370, 520, 151, 31))
        self.play_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 255, 0);\n"
"font-weight: bold;\n"
"}")
        self.play_button.setObjectName("play_button")
        self.stop_button = QtWidgets.QPushButton(self.tab_screen_2)
        self.stop_button.setGeometry(QtCore.QRect(530, 520, 151, 31))
        self.stop_button.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"font-weight: bold;\n"
"}")
        self.stop_button.setObjectName("stop_button")
        self.loading_wid = QtWidgets.QWidget(self.tab_screen_2)
        self.loading_wid.setGeometry(QtCore.QRect(310, 480, 431, 111))
        self.loading_wid.setObjectName("loading_wid")
        self.prog_load = QtWidgets.QProgressBar(self.loading_wid)
        self.prog_load.setGeometry(QtCore.QRect(100, 70, 221, 25))
        self.prog_load.setProperty("value", 24)
        self.prog_load.setObjectName("prog_load")
        self.label = QtWidgets.QLabel(self.loading_wid)
        self.label.setGeometry(QtCore.QRect(-20, 30, 452, 22))
        self.label.setObjectName("label")
        self.estimate_wid = QtWidgets.QWidget(self.tab_screen_2)
        self.estimate_wid.setGeometry(QtCore.QRect(330, 660, 401, 111))
        self.estimate_wid.setObjectName("estimate_wid")
        self.label_15 = QtWidgets.QLabel(self.estimate_wid)
        self.label_15.setGeometry(QtCore.QRect(-40, 20, 452, 22))
        self.label_15.setObjectName("label_15")
        self.prog_load_3 = QtWidgets.QProgressBar(self.estimate_wid)
        self.prog_load_3.setGeometry(QtCore.QRect(80, 60, 221, 25))
        self.prog_load_3.setProperty("value", 24)
        self.prog_load_3.setObjectName("prog_load_3")
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Loading the music file. Please wait!</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Estimating the music genre. Please wait!</span></p></body></html>"))
        self.tab_screen.setTabText(self.tab_screen.indexOf(self.tab_screen_2), _translate("MainWindow", "Genre Estimation"))
        self.import_file.setText(_translate("MainWindow", "Import Music"))
        self.actionZero_Crossing_Rate.setText(_translate("MainWindow", "Zero Crossing Rate"))
        self.import_music_file_action.setText(_translate("MainWindow", "Import Music File/s"))
        self.actionImport_Multiple_Music_Files.setText(_translate("MainWindow", "Import Multiple Music Files"))
        self.use_existing_db_action.setText(_translate("MainWindow", "Use Existing Database (Default)"))
        self.create_new_db_action.setText(_translate("MainWindow", "Create a New Database"))

