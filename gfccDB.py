import numpy as np
import sqlite3
import essentia.streaming as ess
import essentia
import librosa

db_conn = sqlite3.connect("data.db")
db_cursor = db_conn.cursor()


names = ['blues','classical','country','disco','hiphop','jazz','metal','pop','reggae','rock']


for name in names:

    for i in range(10):
        song_name = name + '.' + '0000' + str(i) + '.au'
        print(song_name)
        loader = ess.MonoLoader(filename="genres/"+name+"/"+song_name)
        framecutter = ess.FrameCutter(frameSize=4096, hopSize=2048, silentFrames='noise')
        windowing = ess.Windowing(type='blackmanharris62')
        spectrum = ess.Spectrum(size=2048)
        pow_spectrum = ess.PowerSpectrum()
        spectralpeaks = ess.SpectralPeaks(orderBy='magnitude',
                                          magnitudeThreshold=0.00001,
                                          minFrequency=20,
                                          maxFrequency=3500,
                                          maxPeaks=60)



        # Use default HPCP parameters
        gfcc = ess.GFCC()

        # Use pool to store data
        pool = essentia.Pool()
        pool2 = essentia.Pool()

        # Connect streaming algorithms

        loader.audio >> framecutter.signal
        framecutter.frame >> windowing.frame >> spectrum.frame
        spectrum.spectrum >> gfcc.spectrum
        gfcc.gfcc >> (pool, 'gfcc.vector')
        gfcc.bands >> (pool2, 'bands.vector')

        """
        loader.audio >> pow_spectrum.signal
        pow_spectrum.powerSpectrum >> gfcc.spectrum
        gfcc.gfcc >> (pool, 'gfcc.vector')
        gfcc.bands >> (pool2, 'bands.vector')
        """
        # Run streaming network
        essentia.run(loader)


        arr = np.array(pool['gfcc.vector'])
        gfcc_vector = np.average(arr,axis=0)

        for i in range(1,14):
            sql = ""
            db_cursor.execute("UPDATE songs SET avg_hpcp_1=? WHERE song_name=?",(float(hpcp_profile[0]),song_name))
            db_conn.commit()






    for i in range(10,100):
        song_name = name + '.' + '000' + str(i) + '.au'
        print(song_name)
        loader = ess.MonoLoader(filename="genres/"+name+"/"+song_name)
        framecutter = ess.FrameCutter(frameSize=4096, hopSize=2048, silentFrames='noise')
        windowing = ess.Windowing(type='blackmanharris62')
        spectrum = ess.Spectrum(size=2048)
        pow_spectrum = ess.PowerSpectrum()
        spectralpeaks = ess.SpectralPeaks(orderBy='magnitude',
                                          magnitudeThreshold=0.00001,
                                          minFrequency=20,
                                          maxFrequency=3500,
                                          maxPeaks=60)



        # Use default HPCP parameters
        gfcc = ess.GFCC()

        # Use pool to store data
        pool = essentia.Pool()
        pool2 = essentia.Pool()

        # Connect streaming algorithms

        loader.audio >> framecutter.signal
        framecutter.frame >> windowing.frame >> spectrum.frame
        spectrum.spectrum >> gfcc.spectrum
        gfcc.gfcc >> (pool, 'gfcc.vector')
        gfcc.bands >> (pool2, 'bands.vector')

        """
        loader.audio >> pow_spectrum.signal
        pow_spectrum.powerSpectrum >> gfcc.spectrum
        gfcc.gfcc >> (pool, 'gfcc.vector')
        gfcc.bands >> (pool2, 'bands.vector')
        """
        # Run streaming network
        essentia.run(loader)


        arr = np.array(pool['gfcc.vector'])
        gfcc_vector = np.average(arr,axis=0)








db_conn.close()
