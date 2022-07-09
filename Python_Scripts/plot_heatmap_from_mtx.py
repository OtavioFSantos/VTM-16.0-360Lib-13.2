import numpy as np
import matplotlib.pyplot as plt
import sys

# inputFile = sys.argv[1]

data_ISP = np.genfromtxt('Rate_ISP_4x4.csv', delimiter=',')
data_MRL = np.genfromtxt('Rate_MRL_4x4.csv', delimiter=',')
data_MIP = np.genfromtxt('Rate_MIP_4x4.csv', delimiter=',')
data_NORMAL = np.genfromtxt('Rate_Normal_4x4.csv', delimiter=',')

data_NORMAL_ANGULAR = np.genfromtxt('Rate_Normal_Angular_4x4.csv', delimiter=',')
data_NORMAL_PLANAR = np.genfromtxt('Rate_Normal_Planar_4x4.csv', delimiter=',')
data_NORMAL_DC = np.genfromtxt('Rate_Normal_DC_4x4.csv', delimiter=',')

data_soma = np.genfromtxt('Rate_MRL+ISP+MIP+Normal_4x4.csv', delimiter=',')

fig = plt.figure()

ax1 = fig.add_subplot(241) 
ax2 = fig.add_subplot(242) 
ax3 = fig.add_subplot(243) 
ax4 = fig.add_subplot(244) 
ax5 = fig.add_subplot(245) 
ax6 = fig.add_subplot(246) 
ax7 = fig.add_subplot(247) 
ax8 = fig.add_subplot(248) 

# plt.imshow(data, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')#, title='sys.argv[1]')
ax1.imshow(data_ISP, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')#, title='sys.argv[1]')
ax1.title.set_text('ISP')

ax2.imshow(data_MRL, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')#, title='sys.argv[1]')
ax2.title.set_text('MRL')

ax3.imshow(data_MIP, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')#, title='sys.argv[1]')
ax3.title.set_text('MIP')

ax4.imshow(data_NORMAL, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')#, title='sys.argv[1]')
ax4.title.set_text('NORMAL')

ax5.imshow(data_NORMAL_ANGULAR, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')#, title='sys.argv[1]')
ax5.title.set_text('ANGULAR in NORMAL')

ax6.imshow(data_NORMAL_PLANAR, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')#, title='sys.argv[1]')
ax6.title.set_text('PLANAR in NORMAL')

ax7.imshow(data_NORMAL_DC, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')#, title='sys.argv[1]')
ax7.title.set_text('DC in NORMAL')

ax8.imshow(data_soma, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')#, title='sys.argv[1]')
ax8.title.set_text('ISP+MRL+MIP+NORMAL')

plt.show()