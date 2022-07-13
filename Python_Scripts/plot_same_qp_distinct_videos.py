import numpy as np
import matplotlib.pyplot as plt
import sys

# inputFile = sys.argv[1]

# -----
folderName1 = "chairqp22"
folderName2 = "harborqp22"
folderName3 = "kiteqp22"
folderName4 = "trolleyqp22"

Bloco_X = 4
Bloco_Y = 4

blockSize = "%dx%d" % (Bloco_X, Bloco_Y)
# -----

# chair video data
data_ISP_chair = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                               folderName1+'/Rate_ISP_'+blockSize+'.csv', delimiter=',')
data_MRL_chair = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                               folderName1+'/Rate_MRL_'+blockSize+'.csv', delimiter=',')
data_MIP_chair = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                               folderName1+'/Rate_MIP_'+blockSize+'.csv', delimiter=',')
data_NORMAL_chair = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                  folderName1+'/Rate_Normal_'+blockSize+'.csv', delimiter=',')
data_NORMAL_ANGULAR_chair = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName1+'/Rate_Normal_Angular_'+blockSize+'.csv', delimiter=',')
data_NORMAL_PLANAR_chair = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName1+'/Rate_Normal_Planar_'+blockSize+'.csv', delimiter=',')
data_NORMAL_DC_chair = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName1+'/Rate_Normal_DC_'+blockSize+'.csv', delimiter=',')
data_soma_chair = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                folderName1+'/Rate_MRL+ISP+MIP+Normal_'+blockSize+'.csv', delimiter=',')

# harbor video data
data_ISP_harbor = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                folderName2+'/Rate_ISP_'+blockSize+'.csv', delimiter=',')
data_MRL_harbor = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                folderName2+'/Rate_MRL_'+blockSize+'.csv', delimiter=',')
data_MIP_harbor = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                folderName2+'/Rate_MIP_'+blockSize+'.csv', delimiter=',')
data_NORMAL_harbor = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName2+'/Rate_Normal_'+blockSize+'.csv', delimiter=',')
data_NORMAL_ANGULAR_harbor = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName2+'/Rate_Normal_Angular_'+blockSize+'.csv', delimiter=',')
data_NORMAL_PLANAR_harbor = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName2+'/Rate_Normal_Planar_'+blockSize+'.csv', delimiter=',')
data_NORMAL_DC_harbor = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName2+'/Rate_Normal_DC_'+blockSize+'.csv', delimiter=',')
data_soma_harbor = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                 folderName2+'/Rate_MRL+ISP+MIP+Normal_'+blockSize+'.csv', delimiter=',')

# kite video data
data_ISP_kite = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                              folderName3+'/Rate_ISP_'+blockSize+'.csv', delimiter=',')
data_MRL_kite = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                              folderName3+'/Rate_MRL_'+blockSize+'.csv', delimiter=',')
data_MIP_kite = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                              folderName3+'/Rate_MIP_'+blockSize+'.csv', delimiter=',')
data_NORMAL_kite = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                 folderName3+'/Rate_Normal_'+blockSize+'.csv', delimiter=',')
data_NORMAL_ANGULAR_kite = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName3+'/Rate_Normal_Angular_'+blockSize+'.csv', delimiter=',')
data_NORMAL_PLANAR_kite = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName3+'/Rate_Normal_Planar_'+blockSize+'.csv', delimiter=',')
data_NORMAL_DC_kite = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                    folderName3+'/Rate_Normal_DC_'+blockSize+'.csv', delimiter=',')
data_soma_kite = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                               folderName3+'/Rate_MRL+ISP+MIP+Normal_'+blockSize+'.csv', delimiter=',')

# trolley video data
data_ISP_trolley = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                 folderName4+'/Rate_ISP_'+blockSize+'.csv', delimiter=',')
data_MRL_trolley = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                 folderName4+'/Rate_MRL_'+blockSize+'.csv', delimiter=',')
data_MIP_trolley = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                 folderName4+'/Rate_MIP_'+blockSize+'.csv', delimiter=',')
data_NORMAL_trolley = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName4+'/Rate_Normal_'+blockSize+'.csv', delimiter=',')
data_NORMAL_ANGULAR_trolley = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName4+'/Rate_Normal_Angular_'+blockSize+'.csv', delimiter=',')
data_NORMAL_PLANAR_trolley = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName4+'/Rate_Normal_Planar_'+blockSize+'.csv', delimiter=',')
data_NORMAL_DC_trolley = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName4+'/Rate_Normal_DC_'+blockSize+'.csv', delimiter=',')
data_soma_trolley = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                  folderName4+'/Rate_MRL+ISP+MIP+Normal_'+blockSize+'.csv', delimiter=',')

data_ISP = np.zeros((2048, 4096))
data_MRL = np.zeros((2048, 4096))
data_MIP = np.zeros((2048, 4096))
data_NORMAL = np.zeros((2048, 4096))
data_NORMAL_ANGULAR = np.zeros((2048, 4096))
data_NORMAL_PLANAR = np.zeros((2048, 4096))
data_NORMAL_DC = np.zeros((2048, 4096))
data_soma = np.zeros((2048, 4096))

# PREENCHIMENTO DAS MATRIZES
for i in range(2048):
    for j in range(4096):
        data_ISP[i][j] = (data_ISP_chair[i][j] + data_ISP_harbor[i]
                       [j] + data_ISP_kite[i][j] + data_ISP_trolley[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_MRL[i][j] = (data_MRL_chair[i][j] + data_MRL_harbor[i]
                       [j] + data_MRL_kite[i][j] + data_MRL_trolley[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_MIP[i][j] = (data_MIP_chair[i][j] + data_MIP_harbor[i]
                       [j] + data_MIP_kite[i][j] + data_MIP_trolley[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_NORMAL[i][j] = (data_NORMAL_chair[i][j] + data_NORMAL_harbor[i]
                       [j] + data_NORMAL_kite[i][j] + data_NORMAL_trolley[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_NORMAL_ANGULAR[i][j] = (data_NORMAL_ANGULAR_chair[i][j] + data_NORMAL_ANGULAR_harbor[i]
                       [j] + data_NORMAL_ANGULAR_kite[i][j] + data_NORMAL_ANGULAR_trolley[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_NORMAL_PLANAR[i][j] = (data_NORMAL_PLANAR_chair[i][j] + data_NORMAL_PLANAR_harbor[i]
                       [j] + data_NORMAL_PLANAR_kite[i][j] + data_NORMAL_PLANAR_trolley[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_NORMAL_DC[i][j] = (data_NORMAL_DC_chair[i][j] + data_NORMAL_DC_harbor[i]
                       [j] + data_NORMAL_DC_kite[i][j] + data_NORMAL_DC_trolley[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_soma[i][j] = (data_soma_chair[i][j] + data_soma_harbor[i]
                       [j] + data_soma_kite[i][j] + data_soma_trolley[i][j]) / 4


fig = plt.figure()

ax1 = fig.add_subplot(241)
ax2 = fig.add_subplot(242)
ax3 = fig.add_subplot(243)
ax4 = fig.add_subplot(244)
ax5 = fig.add_subplot(245)
ax6 = fig.add_subplot(246)
ax7 = fig.add_subplot(247)
ax8 = fig.add_subplot(248)

##
# cmap = plt.cm.jet
# cmap.set_bad('white',1.)
##

# plt.imshow(data, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')#, title='sys.argv[1]')
ax1.imshow(data_ISP, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap=cmap)#, title='sys.argv[1]')
ax1.title.set_text('ISP')

ax2.imshow(data_MRL, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap=cmap)#, title='sys.argv[1]')
ax2.title.set_text('MRL')

ax3.imshow(data_MIP, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap=cmap)#, title='sys.argv[1]')
ax3.title.set_text('MIP')

ax4.imshow(data_NORMAL, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap=cmap)#, title='sys.argv[1]')
ax4.title.set_text('NORMAL')

ax5.imshow(data_NORMAL_ANGULAR, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap=cmap)#, title='sys.argv[1]')
ax5.title.set_text('ANGULAR in NORMAL')

ax6.imshow(data_NORMAL_PLANAR, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap=cmap)#, title='sys.argv[1]')
ax6.title.set_text('PLANAR in NORMAL')

ax7.imshow(data_NORMAL_DC, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap=cmap)#, title='sys.argv[1]')
ax7.title.set_text('DC in NORMAL')

ax8.imshow(data_soma, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap=cmap)#, title='sys.argv[1]')
ax8.title.set_text('ISP+MRL+MIP+NORMAL')

plt.show()
