import numpy as np
import matplotlib.pyplot as plt
import sys

# inputFile = sys.argv[1]

# -----
folderName1 = "chairqp22"
folderName2 = "chairqp27"
folderName3 = "chairqp32"
folderName4 = "chairqp37"

Bloco_X = 4
Bloco_Y = 4

blockSize = "%dx%d" % (Bloco_X, Bloco_Y)
# -----

# qp22 video data
data_ISP_qp22 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                               folderName1+'/Rate_ISP_'+blockSize+'.csv', delimiter=',')
data_MRL_qp22 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                               folderName1+'/Rate_MRL_'+blockSize+'.csv', delimiter=',')
data_MIP_qp22 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                               folderName1+'/Rate_MIP_'+blockSize+'.csv', delimiter=',')
data_NORMAL_qp22 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                  folderName1+'/Rate_Normal_'+blockSize+'.csv', delimiter=',')
data_NORMAL_ANGULAR_qp22 = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName1+'/Rate_Normal_Angular_'+blockSize+'.csv', delimiter=',')
data_NORMAL_PLANAR_qp22 = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName1+'/Rate_Normal_Planar_'+blockSize+'.csv', delimiter=',')
data_NORMAL_DC_qp22 = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName1+'/Rate_Normal_DC_'+blockSize+'.csv', delimiter=',')
data_soma_qp22 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                folderName1+'/Rate_MRL+ISP+MIP+Normal_'+blockSize+'.csv', delimiter=',')

# qp27 video data
data_ISP_qp27 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                folderName2+'/Rate_ISP_'+blockSize+'.csv', delimiter=',')
data_MRL_qp27 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                folderName2+'/Rate_MRL_'+blockSize+'.csv', delimiter=',')
data_MIP_qp27 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                folderName2+'/Rate_MIP_'+blockSize+'.csv', delimiter=',')
data_NORMAL_qp27 = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName2+'/Rate_Normal_'+blockSize+'.csv', delimiter=',')
data_NORMAL_ANGULAR_qp27 = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName2+'/Rate_Normal_Angular_'+blockSize+'.csv', delimiter=',')
data_NORMAL_PLANAR_qp27 = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName2+'/Rate_Normal_Planar_'+blockSize+'.csv', delimiter=',')
data_NORMAL_DC_qp27 = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName2+'/Rate_Normal_DC_'+blockSize+'.csv', delimiter=',')
data_soma_qp27 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                 folderName2+'/Rate_MRL+ISP+MIP+Normal_'+blockSize+'.csv', delimiter=',')

# qp32 video data
data_ISP_qp32 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                              folderName3+'/Rate_ISP_'+blockSize+'.csv', delimiter=',')
data_MRL_qp32 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                              folderName3+'/Rate_MRL_'+blockSize+'.csv', delimiter=',')
data_MIP_qp32 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                              folderName3+'/Rate_MIP_'+blockSize+'.csv', delimiter=',')
data_NORMAL_qp32 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                 folderName3+'/Rate_Normal_'+blockSize+'.csv', delimiter=',')
data_NORMAL_ANGULAR_qp32 = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName3+'/Rate_Normal_Angular_'+blockSize+'.csv', delimiter=',')
data_NORMAL_PLANAR_qp32 = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName3+'/Rate_Normal_Planar_'+blockSize+'.csv', delimiter=',')
data_NORMAL_DC_qp32 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                    folderName3+'/Rate_Normal_DC_'+blockSize+'.csv', delimiter=',')
data_soma_qp32 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                               folderName3+'/Rate_MRL+ISP+MIP+Normal_'+blockSize+'.csv', delimiter=',')

# qp37 video data
data_ISP_qp37 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                 folderName4+'/Rate_ISP_'+blockSize+'.csv', delimiter=',')
data_MRL_qp37 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                 folderName4+'/Rate_MRL_'+blockSize+'.csv', delimiter=',')
data_MIP_qp37 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
                                 folderName4+'/Rate_MIP_'+blockSize+'.csv', delimiter=',')
data_NORMAL_qp37 = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName4+'/Rate_Normal_'+blockSize+'.csv', delimiter=',')
data_NORMAL_ANGULAR_qp37 = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName4+'/Rate_Normal_Angular_'+blockSize+'.csv', delimiter=',')
data_NORMAL_PLANAR_qp37 = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName4+'/Rate_Normal_Planar_'+blockSize+'.csv', delimiter=',')
data_NORMAL_DC_qp37 = np.genfromtxt(
    '/home/otavio/Downloads/VTM_16/Python_Scripts/'+folderName4+'/Rate_Normal_DC_'+blockSize+'.csv', delimiter=',')
data_soma_qp37 = np.genfromtxt('/home/otavio/Downloads/VTM_16/Python_Scripts/' +
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
        data_ISP[i][j] = (data_ISP_qp22[i][j] + data_ISP_qp27[i]
                       [j] + data_ISP_qp32[i][j] + data_ISP_qp37[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_MRL[i][j] = (data_MRL_qp22[i][j] + data_MRL_qp27[i]
                       [j] + data_MRL_qp32[i][j] + data_MRL_qp37[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_MIP[i][j] = (data_MIP_qp22[i][j] + data_MIP_qp27[i]
                       [j] + data_MIP_qp32[i][j] + data_MIP_qp37[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_NORMAL[i][j] = (data_NORMAL_qp22[i][j] + data_NORMAL_qp27[i]
                       [j] + data_NORMAL_qp32[i][j] + data_NORMAL_qp37[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_NORMAL_ANGULAR[i][j] = (data_NORMAL_ANGULAR_qp22[i][j] + data_NORMAL_ANGULAR_qp27[i]
                       [j] + data_NORMAL_ANGULAR_qp32[i][j] + data_NORMAL_ANGULAR_qp37[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_NORMAL_PLANAR[i][j] = (data_NORMAL_PLANAR_qp22[i][j] + data_NORMAL_PLANAR_qp27[i]
                       [j] + data_NORMAL_PLANAR_qp32[i][j] + data_NORMAL_PLANAR_qp37[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_NORMAL_DC[i][j] = (data_NORMAL_DC_qp22[i][j] + data_NORMAL_DC_qp27[i]
                       [j] + data_NORMAL_DC_qp32[i][j] + data_NORMAL_DC_qp37[i][j]) / 4

for i in range(2048):
    for j in range(4096):
        data_soma[i][j] = (data_soma_qp22[i][j] + data_soma_qp27[i]
                       [j] + data_soma_qp32[i][j] + data_soma_qp37[i][j]) / 4


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
ax1.imshow(data_ISP, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap='jet')#, title='sys.argv[1]')
ax1.title.set_text('ISP')

ax2.imshow(data_MRL, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap='jet')#, title='sys.argv[1]')
ax2.title.set_text('MRL')

ax3.imshow(data_MIP, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap='jet')#, title='sys.argv[1]')
ax3.title.set_text('MIP')

ax4.imshow(data_NORMAL, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap='jet')#, title='sys.argv[1]')
ax4.title.set_text('NORMAL')

ax5.imshow(data_NORMAL_ANGULAR, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap='jet')#, title='sys.argv[1]')
ax5.title.set_text('ANGULAR in NORMAL')

ax6.imshow(data_NORMAL_PLANAR, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap='jet')#, title='sys.argv[1]')
ax6.title.set_text('PLANAR in NORMAL')

ax7.imshow(data_NORMAL_DC, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap='jet')#, title='sys.argv[1]')
ax7.title.set_text('DC in NORMAL')

ax8.imshow(data_soma, vmin=0, vmax=1, interpolation='nearest', aspect='auto', cmap='jet')#, title='sys.argv[1]')
ax8.title.set_text('ISP+MRL+MIP+NORMAL')

plt.show()
