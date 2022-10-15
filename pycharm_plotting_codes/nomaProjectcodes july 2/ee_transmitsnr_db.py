import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

time = (60,62,64,66,68,70,72,74,78,81,83.85,87,89,91,93,95,97,100,101,102)#transmit, snr db

convee= (
12.5437,
12.6436,
12.675,
12.6962,
12.6727,
12.6187,
12.5291,
12.4072,
12.2509,
12.0613,
11.8447,
11.6173,
11.4059,
11.2473,
11.177,
11.2325,
11.4168,
11.761,
12.157,
12.7621,)

proposedee = (
61.766,
65.536,
68.5176,
71.3981,
73.8086,
75.9609,
77.8688,
79.6442,
81.3143,
82.886,
84.3239,
85.5834,
86.6281,
87.4467,
88.051,
88.4689,
88.7454,
88.9128,
89.036,
89.0757)

# convi= (
# 0.884,
# 0.8388,
# 0.7958,
# 0.7532,
# 0.7119,
# 0.6715,
# 0.6317,
# 0.592,
# 0.5521,
# 0.5117,
# 0.4724,
# 0.436,
# 0.4044,
# 0.3794,
# 0.3626,
# 0.3526,
# 0.3476,
# 0.346,
# 0.346,
# 0.346)
#
# proposedi = (
# 0.8840348737,
# 0.759026398,
# 0.6359729509,
# 0.5126822807,
# 0.4008497892,
# 0.3100166306,
# 0.2241853661,
# 0.1725350602,
# 0.1352971264,
# 0.1068306913,
# 0.09101741577,
# 0.08080537748,
# 0.07871213907,
# 0.07661890066,
# 0.07412566225,
# 0.07092566225,
# 0.06692566225,
# 0.06372566225,
# 0.06025899558,
# 0.05892566225)
#
# convw= (
# 0.922,
# 0.9022,
# 0.8822,
# 0.8722,
# 0.8622,
# 0.851,
# 0.8481,
# 0.8415,
# 0.829,
# 0.8085,
# 0.7813,
# 0.747,
# 0.7095,
# 0.6729,
# 0.6416,
# 0.6164,
# 0.6,
# 0.5906,
# 0.5842,
# 0.584
# )
#
# proposedw = (
# 0.9,
# 0.78,
# 0.69758,
# 0.61474,
# 0.5431,
# 0.48192,
# 0.43244,
# 0.3934,
# 0.36332,
# 0.33936,
# 0.3189,
# 0.30056,
# 0.28384,
# 0.26912,
# 0.25828,
# 0.25118,
# 0.24728,
# 0.2458,
# 0.2458,
# 0.2458)

f, ax1 = plt.subplots()
# ax1.set_yscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
#strongest user
lns1 = ax1.plot(time, proposed, color="black",marker=".", markersize=3, label=r'sequential T-SIC')
lns2 = ax1.plot(time, conv,color="peru",marker=".",linestyle='dashed', markersize=3,  label=r'conv T-SIC')

# #intermediate user
# lns1 = ax1.plot(time, proposedi, color="black",marker="x", markersize=5, label=r'sequential T-SIC (intermediate user)')
# lns2 = ax1.plot(time, convi,color="peru",marker="x",linestyle='dashed', markersize=5,  label=r'conv T-SIC (intermediate user)')
#
# #weakest user
# lns1 = ax1.plot(time, proposedw, color="black",marker="p", markersize=5, label=r'sequential T-SIC (farthest user)')
# lns2 = ax1.plot(time, convw,color="peru",marker="p",linestyle='dashed', markersize=5,  label=r'conv T-SIC (farthest user)')

lns = lns1
labs = [l.get_label() for l in lns]

ax1.legend(loc=2, fontsize=10)

font = font_manager.FontProperties(family='Arial', style='normal', size=12)
ax1.legend(prop=font)

d = .015  # how big to make the diagonal lines in axes coordinates

ax1.set_ylim(10,90)  # most of the data
ax1.set_xlim(60, 103.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")
plt.text(7,0.5e-2,'Received power ratio: 5',fontsize=13,fontname="Arial")
plt.xlabel(r"Transmit SNR (dB)",fontname="Arial",fontsize=14)
plt.ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
