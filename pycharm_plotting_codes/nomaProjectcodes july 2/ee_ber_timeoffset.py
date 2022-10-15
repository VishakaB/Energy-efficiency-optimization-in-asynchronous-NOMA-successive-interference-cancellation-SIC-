import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

time = (0.01,
0.01736842105,
0.02473684211,
0.03210526316,
0.03947368421,
0.04684210526,
0.05421052632,
0.06157894737,
0.06894736842,
0.07631578947,
0.08368421053,
0.09105263158,
0.09842105263,
0.1057894737,
0.1131578947,
0.1205263158,
0.1278947368,
0.1352631579,
0.1426315789,
0.15)#transmit, snr db

conv= (
4.89E-05,
1.55E-04,
0.0002508024012,
0.0003404257399,
0.0004168376249,
0.0004769503324,
0.000519379168,
0.00053264,
0.00053264,
0.00053264,
0.00053264,
0.00053264,
0.00053264,
0.00053264,
0.0005302068148,
0.000532786963,
0.000532786963,
0.000532786963,
0.000532786963,
0.000532786963)

proposed = (
3.05E-05,
8.96E-05,
0.0001396832446,
0.0001866160944,
0.0002251983241,
0.0002554387567,
0.000276878624,
0.0002905588764,
0.0002980498987,
0.0003012803627,
0.00030204544,
0.000301675744,
0.000301024608,
0.000300500736,
0.000300192704,
0.0003000512,
0.0003000064,
0.0003,
0.0003,
0.0003)

convi= (
0.0019,
    0.0057,
    0.0083,
    0.0107,
    0.0122,
    0.0133,
    0.0139,
    0.0143,
    0.0145,
    0.0145,
    0.0146,
    0.0146,
    0.0146,
    0.0146,
    0.0146,
    0.0146,
    0.0146,
    0.0146,
    0.0145,
    0.0144
)

proposedi = (
0.0005,
0.0015,
0.0025,
0.0035,
0.0045,
0.005,
0.0053,
0.0054,
0.0053,
0.0053,
0.0052,
0.0052,
0.0052,
0.0052,
0.0052,
0.0052,
0.0052,
0.0051,
0.0051,
0.0051)

convw= (
0.009,
0.011775,
0.016275,
0.020325,
0.02305,
0.023775,
0.02435,
0.024475,
0.0248,
0.0248,
0.0248,
0.0248,
0.0248,
0.0248,
0.0248,
0.0248,
0.0248,
0.0248,
0.0248,
0.0248
)

proposedw = (
0.001,
0.004629221187,
0.008038904211,
0.01124613031,
0.01365129893,
0.01550768336,
0.01679859922,
0.01767969711,
0.01822708183,
0.01853094243,
0.01865281521,
0.01864488128,
0.01855620233,
0.01844535949,
0.01836520681,
0.01837714872,
0.01849663457,
0.01849663457,
0.01849663457,
0.01849663457)

convee= (
10.7113,
10.3743,
10.259,
10.1589,
10.1718,
10.2215,
10.298,
10.3616,
10.4018,
10.4138,
10.4059,
10.3879,
10.369,
10.3542,
10.345,
10.3403,
10.3384,
10.3378,
10.3377,
10.3377)

proposedee = (
12.5255,
12.97683333,
14.08876,
15.21898,
16.6376,
18.07306,
19.45786,
20.63788,
21.56106,
22.20804,
22.61864,
22.85016,
22.96462,
23.01308,
23.03002,
23.03434,
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

ax2.legend(lns, labs, loc=[0.5,0.1],prop={'size':8})

font = font_manager.FontProperties(family='Arial', style='normal', size=12)

d = .015  # how big to make the diagonal lines in axes coordinates

ax1.set_ylim(1e-7,1e-1)  # most of the data
ax2.set_ylim(9,24)  # most of the data
ax1.set_xlim(0.009, 0.15)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")
plt.text(7,0.5e-2,'Received power ratio: 5',fontsize=13,fontname="Arial")
ax1.set_xlabel(r"Time offset (% of a symbol)",fontname="Arial",fontsize=14)
ax1.set_ylabel(r"Average bit error rate ($BER$)",fontname="Arial",fontsize=14)
ax2.set_ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
