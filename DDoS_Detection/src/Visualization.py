'''
Created on Apr 6, 2018

@author: animesh
'''
import matplotlib.pyplot as plt
import numpy as np

xAxis = np.arange(1,29)

# Information Gain
IG_NByAxis = [76.68390804,78.52776052,19.94537724,19.94537724,19.94537724,19.94537724,19.94537724,19.87776864,77.03146462,
         33.04903431,37.07950146,37.10217256,37.3215969,37.30803459,37.09569504,41.2115202,41.30665804,41.32001777,41.27811668,41.27811666,
         41.42041862,41.76696346,45.03464493,98.36099847,98.40755524,96.50886191,95.84632453,76.60600997]
IG_SVMyAxis = [77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,
            77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,56.94247376,99.43001,99.28001,99.28001,99.28001,
            99.28001,99.28001]
IG_DTyAxis = [80.30906492,80.30906492,80.30906492,80.24995799,80.34044018,80.49104086,81.15457654,81.87296813,84.04898924,84.08522207,
           84.19331395,84.27994981,84.84328413,85.24974384,86.18492756,86.20597924,89.88962569,93.64083814,93.65379313,93.92240189,
           97.38981358,97.41511606,99.64697869,99.6919159,99.70689472,99.69191579,99.72855358,99.78583869]
IG_RFyAxis = [80.30906492,80.30906492,80.30906492,80.22951348,80.33234334,80.44225741,81.18615398,81.86628859,84.03380761,
           84.07874457,84.16133129,84.26051726,84.88720933,85.24427839,86.19079765,86.18452259,89.89023294,93.64306435,
           93.70945842,93.99061709,97.42280801,97.43090484,99.68786778,99.72207633,99.7710621,99.77288412,99.78685105,99.81640469]

# Chi-Squared
Chi2_NByAxis = [80.30906492, 80.28639318,76.27481497,76.27785129,34.92709601,41.51535503,41.56960384,41.45361564,41.29208372,41.18824177,
                41.58822591,41.59369138,41.56899602,41.51677137,41.71089269,41.65522692,41.69206751,41.70137882,41.72465723,42.72259257,
                42.71287633,42.72279496,42.70579161,46.43256401,98.3769896,98.38387195,77.46225052,76.60600997]
Chi2_SVMyAxis = [77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,77.86001,
                 77.86001,77.86001,77.76036482,99.67007996,99.68007996,99.68007996,99.69001,99.69001,99.69001,99.69001,99.69001,
                 99.28001,99.28001,99.28001,99.28001]
Chi2_DTyAxis = [85.18435927,85.15844946,85.81591235,85.87947254,87.9391047,88.12634309,88.54879566,88.4915105,88.71680499,88.92873983,
                89.17670473,89.24957596,89.62243224,89.93011067,89.94853077,99.39598048,99.49091559,99.47897136,99.57653683,99.69495207,
                99.72956585,99.71984961,99.71843309,99.68685522,99.75952506,99.77632598,99.78664889,99.7771346]
Chi2_RFyAxis = [85.18435927,85.16472445,85.80599372,85.88028221,87.91623117,88.11419785,88.54636659,88.54231815,88.80506053,88.9078904,
                89.21759332,89.2805461,89.64753238,89.93942206,89.91654856,99.36379584,99.4688516,99.48868748,99.64029897,99.71053856,
                99.77774225,99.7431282,99.77753982,99.78644647,99.7807786,99.78604124,99.80466432,99.8202505]

#ReliefF
ReliefF_NByAxis = [76.1540052,76.29832988,76.27444422,76.2040018,76.20420423,76.20420423,76.22262453,76.4446803,76.44427546,76.44609725,
                   76.45156262,76.45156262,75.58236721,75.58236721,75.58236721,75.58358173,75.58580837,76.58293398,76.58374366,76.58597029,
                   76.58597029,76.58597029,76.60115187,76.60094944,76.60600997,76.60600997,76.60600997,76.60600997]
ReliefF_SVMyAxis = [99.52001,99.52001,99.52001,99.42001,99.42001,99.42001,99.42001,99.28001,99.28001,99.28001,99.28001,99.28001,99.28001,
                    99.28001,99.28001,99.28001,99.28001,99.28001,99.28001,99.28001,99.28001,99.28001,99.28001,99.28001,99.28001,
                    99.28001,99.28001,99.28001]
ReliefF_DTyAxis = [84.96712074,98.6083573,98.80875341,99.80122344,99.81316629,99.75709568,99.76114397,99.71458721,99.71620667,99.72045744,
                   99.76782407,99.77450397,99.75952479,99.79373396,99.78199355,99.78502981,99.76903917,99.77328999,99.75770363,
                   99.76033511,99.79009063,99.76013272,99.73219858,99.74069982,99.74535592,99.75345236,99.74252163,99.76114375]
ReliefF_RFyAxis = [84.70134203,98.63102842,98.75328997,99.71114616,99.71418238,99.70223954,99.71701619,99.76053671,99.74333098,
                   99.74920125,99.74069947,99.76802627,99.74818902,99.79292411,99.74636739,99.78867361,99.75486959,99.8238943,
                   99.80365219,99.78604157,99.83583702,99.83259903,99.80891522,99.81154668,99.81741673,99.81276113,99.80506908,99.85365003]


#*******************************************
# Plot the Graphs
#*******************************************
#Line Chart for Information Gain
f = plt.figure(1)
plt.title('Information Gain')
plt.plot(xAxis, IG_NByAxis)
plt.plot(xAxis, IG_SVMyAxis)
plt.plot(xAxis, IG_DTyAxis)
plt.plot(xAxis, IG_RFyAxis)
plt.legend(['Naive Bayes', 'SVM', 'Decision Tree', 'Random Forest'], loc='upper left')
plt.xlabel('# Features')
plt.ylabel('Accuracy')
plt.grid(True)
f.show()

#Line Chart for Chi-Squared
g = plt.figure(2)
plt.title('Chi-Squared')
plt.plot(xAxis, Chi2_NByAxis)
plt.plot(xAxis, Chi2_SVMyAxis)
plt.plot(xAxis, Chi2_DTyAxis)
plt.plot(xAxis, Chi2_RFyAxis)
plt.legend(['Naive Bayes', 'SVM', 'Decision Tree', 'Random Forest'], loc='upper left')
plt.xlabel('# Features')
plt.ylabel('Accuracy')
plt.grid(True)
g.show()

#Line Chart for ReliefF
g = plt.figure(3)
plt.title('ReliefF')
plt.plot(xAxis, ReliefF_NByAxis)
plt.plot(xAxis, ReliefF_SVMyAxis)
plt.plot(xAxis, ReliefF_DTyAxis)
plt.plot(xAxis, ReliefF_RFyAxis)
plt.legend(['Naive Bayes', 'SVM', 'Decision Tree', 'Random Forest'], loc='upper left')
plt.xlabel('# Features')
plt.ylabel('Accuracy')
plt.grid(True)
g.show()


plt.show()
