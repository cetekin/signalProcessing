import sqlite3
import essentia
import essentia.standard as es
import librosa
import numpy as np


db_conn = sqlite3.connect("data.db")
db_cursor = db_conn.cursor()


names = ['blues','classical','country','disco','hiphop','jazz','metal','pop','reggae','rock']


for name in names:

    for i in range(10):
        song_name = name + '.' + '0000' + str(i) + '.au'
        print(song_name)
        # Compute all features, aggregate only 'mean' and 'stdev' statistics for all low-level, rhythm and tonal frame features
        y,sr = librosa.load("genres/"+name+"/"+song_name)

        #mfcc var
        tmp_mfcc=librosa.feature.mfcc(y,sr)
        tmpp=[None]*20
        for i in range(20):
            tmpp[i]=np.var(tmp_mfcc[i])


        tmpp = np.array(tmpp)


        for i in range(1,21):
            sql = "UPDATE songs SET var_mfcc_" + str(i) + "=? WHERE song_name=?"
            db_cursor.execute(sql,(float(tmpp[i-1]),song_name))
            db_conn.commit()


        #chroma stft var
        tmp_chroma_stft=librosa.feature.chroma_stft(y,sr)
        tmpp=[None]*12
        for i in range(12):
            tmpp[i]=np.var(tmp_chroma_stft[i])


        tmpp = np.array(tmpp)

        for i in range(1,13):
            sql = "UPDATE songs SET var_chroma_stft_" + str(i) + "=? WHERE song_name=?"
            db_cursor.execute(sql,(float(tmpp[i-1]),song_name))
            db_conn.commit()



        #avg-var mfcc derivative

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


        mfcc_derivative_avgs_stds = np.array(mfcc_derivative_avgs_stds)

        j = 0

        for i in range(1,21):
            sql = "UPDATE songs SET avg_mfcc_derivative_" + str(i) + "=? WHERE song_name=?"
            db_cursor.execute(sql,(float(mfcc_derivative_avgs_stds[j]),song_name))
            db_conn.commit()


            sql = "UPDATE songs SET var_mfcc_derivative_" + str(i) + "=? WHERE song_name=?"
            db_cursor.execute(sql,(float(mfcc_derivative_avgs_stds[j+1]),song_name))
            db_conn.commit()

            j=j+2





    for i in range(10,100):
        song_name = name + '.' + '000' + str(i) + '.au'
        print(song_name)

        y,sr = librosa.load("genres/"+name+"/"+song_name)



        #mfcc var
        tmp_mfcc=librosa.feature.mfcc(y,sr)
        tmpp=[None]*20
        for i in range(20):
            tmpp[i]=np.var(tmp_mfcc[i])


        tmpp = np.array(tmpp)


        for i in range(1,21):
            sql = "UPDATE songs SET var_mfcc_" + str(i) + "=? WHERE song_name=?"
            db_cursor.execute(sql,(float(tmpp[i-1]),song_name))
            db_conn.commit()


        #chroma stft var
        tmp_chroma_stft=librosa.feature.chroma_stft(y,sr)
        tmpp=[None]*12
        for i in range(12):
            tmpp[i]=np.var(tmp_chroma_stft[i])


        tmpp = np.array(tmpp)

        for i in range(1,13):
            sql = "UPDATE songs SET var_chroma_stft_" + str(i) + "=? WHERE song_name=?"
            db_cursor.execute(sql,(float(tmpp[i-1]),song_name))
            db_conn.commit()



        #avg-var mfcc derivative

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


        mfcc_derivative_avgs_stds = np.array(mfcc_derivative_avgs_stds)

        j = 0

        for i in range(1,21):
            sql = "UPDATE songs SET avg_mfcc_derivative_" + str(i) + "=? WHERE song_name=?"
            db_cursor.execute(sql,(float(mfcc_derivative_avgs_stds[j]),song_name))
            db_conn.commit()


            sql = "UPDATE songs SET var_mfcc_derivative_" + str(i) + "=? WHERE song_name=?"
            db_cursor.execute(sql,(float(mfcc_derivative_avgs_stds[j+1]),song_name))
            db_conn.commit()

            j=j+2




db_conn.close()
