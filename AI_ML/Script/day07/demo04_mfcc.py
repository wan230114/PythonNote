"""
demo04_mfcc.py  mfcc矩阵
"""
import scipy.io.wavfile as wf
import python_speech_features as sf
import matplotlib.pyplot as mp

sample_rate, sigs = wf.read(
	'../ml_data/speeches/training/banana/banana01.wav')
mfcc = sf.mfcc(sigs, sample_rate)

mp.matshow(mfcc.T, cmap='gist_rainbow')
mp.show()