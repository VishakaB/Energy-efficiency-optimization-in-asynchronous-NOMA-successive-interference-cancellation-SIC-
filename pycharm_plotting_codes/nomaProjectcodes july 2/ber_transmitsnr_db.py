import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

time = (60,62,64,66,68,70,72,74,78,81,83.85,87,89,91,93,95,97,100,101,102)#transmit, snr db

conv= (
0.01004619519,
0.007692783452,
0.005857125514,
4.14E-03,
2.80E-03,
1.77E-03,
1.06E-03,
5.82E-04,
2.97E-04,
1.38E-04,
5.80E-05,
2.14E-05,
6.83E-06,
1.78E-06,
3.63E-07,
5.57E-08,
1.29E-08,
5.86E-09,
3.94E-09,
3.81E-09)

proposed = (
0.01004619519,
0.007474622234,
5.55E-03,
3.77E-03,
2.44E-03,
1.45E-03,
8.01E-04,
4.02E-04,
1.83E-04,
7.30E-05,
2.52E-05,
7.09E-06,
1.53E-06,
2.14E-07,
3.63E-08,
9.75E-09,
3.93E-09,
2.65E-09,
2.39E-09,
2.48E-09)

convi= (
0.0205,
0.01643333333,
0.01288,
0.00954,
0.00674,
0.0045,
0.00286,
0.00174,
0.00104,
0.00064,
0.00042,
0.0003,
0.00024,
0.00022,
0.0002,
0.0002,
0.0002,
0.0002,
0.0002,
0.0002)

proposedi = (
0.02053440782,
0.01613388642,
0.01245988659,
0.0090178282,
0.006211247779,
0.004008745987,
0.002425945451,
0.001369020846,
0.0007301044748,
3.75E-04,
1.93E-04,
1.08E-04,
7.04E-05,
5.18E-05,
4.27E-05,
3.78E-05,
3.49E-05,
3.28E-05,
3.10E-05,
2.95E-05)

convw= (
0.11525,
0.112775,
0.110275,
0.109025,
0.107775,
0.106375,
0.1060125,
0.1051875,
0.103625,
0.1010625,
0.0976625,
0.093375,
0.0886875,
0.0841125,
0.0802,
0.07705,
0.075,
0.073825,
0.073025,
0.073
)

proposedw = (
0.1125,
0.09797916667,
0.0871975,
0.0768425,
0.0678875,
0.06024,
0.054055,
0.049175,
0.045415,
0.04242,
0.0398625,
0.03757,
0.03548,
0.03364,
0.032285,
0.0313975,
0.03091,
0.030725,
0.030725,
0.030725)

convee= (
11.44204,
11.44204,
11.44204,
11.44204,
11.43188,
11.3372,
11.17008,
10.97798,
10.7892,
10.63044,
10.5102,
10.42876,
10.37978,
10.35444,
10.34284,
10.33864,
10.3377,
10.3377,
10.3377,
10.3377)

proposedee = (
12.5255,
13.91856667,
15.35436,
16.7637,
18.13404,
19.41154,
20.52678,
21.43176,
22.10852,
22.56394,
22.8274,
22.9618,
23.01788,
23.03364,
23.0348,
23.0348,
23.0348,
23.0348,
23.0348,
23.0348)

f, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.set_yscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
#strongest user
lns1 = ax1.plot(time, proposed, color="black",marker=".", markersize=3, label=r'sequential T-SIC (nearest user)')
lns2 = ax1.plot(time, conv,color="peru",marker=".",linestyle='dashed', markersize=3,  label=r'conv T-SIC (nearest user)')

#intermediate user
lns3 = ax1.plot(time, proposedi, color="black",marker="x", markersize=5, label=r'sequential T-SIC (intermediate user)')
lns4 = ax1.plot(time, convi,color="peru",marker="x",linestyle='dashed', markersize=5,  label=r'conv T-SIC (intermediate user)')

#weakest user
lns5 = ax1.plot(time, proposedw, color="black",marker="p", markersize=5, label=r'sequential T-SIC (farthest user)')
lns6= ax1.plot(time, convw,color="peru",marker="p",linestyle='dashed', markersize=5,  label=r'conv T-SIC (farthest user)')

#EE analysis
lns7 = ax2.plot(time, proposedee, color="darkblue",marker=".", markersize=3, label=r'sequential T-SIC')
lns8 = ax2.plot(time, convee,color="brown",marker=".",linestyle='dashed', markersize=3,  label=r'conv T-SIC')

lns = lns1+lns2+lns3+lns4+lns5+lns6+lns7+lns8
labs = [l.get_label() for l in lns]


ax2.legend(lns, labs, loc=[0.15,0.20],prop={'size':8})
font = font_manager.FontProperties(family='Arial', style='normal', size=12)


d = .015  # how big to make the diagonal lines in axes coordinates

ax1.set_ylim(1e-9,1.35)  # most of the data
ax2.set_ylim(9,24)  # most of the data
ax1.set_xlim(60, 103.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")
plt.text(7,0.5e-2,'Received power ratio: 5',fontsize=13,fontname="Arial")
ax1.set_xlabel(r"Transmit SNR (dB)",fontname="Arial",fontsize=14)
ax1.set_ylabel(r"Average bit error rate ($BER$)",fontname="Arial",fontsize=14)
ax2.set_ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
