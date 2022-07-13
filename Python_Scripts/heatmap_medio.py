# -*- Coding: UTF-8 -*-
#coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
fid1 = open('/home/otavio/Downloads/VTM_16/Python_Scripts/TangoQP37/saida16x4.md','r')
fid2 = open('/home/otavio/Downloads/VTM_16/Python_Scripts/TangoQP32/saida16x4.md','r')
fid3 = open('/home/otavio/Downloads/VTM_16/Python_Scripts/TangoQP27/saida16x4.md','r')
fid4 = open('/home/otavio/Downloads/VTM_16/Python_Scripts/TangoQP22/saida16x4.md','r')

Bloco_X = 16
Bloco_Y = 4

FLAG_MIP = 0
FLAG_ISP = 0
FLAG_MRL = 0
FLAG_PLANAR = 1
FLAG_DC = 0

CU_TESTA_1 = np.zeros((2048, 4096))
CU_TESTA_2 = np.zeros((2048, 4096))
CU_TESTA_3 = np.zeros((2048, 4096))
CU_TESTA_4 = np.zeros((2048, 4096))
if(FLAG_MIP):
	BEST_MIP_1 = np.zeros((2048, 4096))
	MIP_RATE_1 = np.zeros((2048, 4096))
	BEST_MIP_2 = np.zeros((2048, 4096))
	MIP_RATE_2 = np.zeros((2048, 4096))
	BEST_MIP_3 = np.zeros((2048, 4096))
	MIP_RATE_3 = np.zeros((2048, 4096))
	BEST_MIP_4 = np.zeros((2048, 4096))
	MIP_RATE_4 = np.zeros((2048, 4096))
	MIP_RATE = np.zeros((2048, 4096))
if(FLAG_ISP):
	BEST_ISP_1 = np.zeros((2048, 4096))
	ISP_RATE_1 = np.zeros((2048, 4096))
	BEST_ISP_2 = np.zeros((2048, 4096))
	ISP_RATE_2 = np.zeros((2048, 4096))
	BEST_ISP_3 = np.zeros((2048, 4096))
	ISP_RATE_3 = np.zeros((2048, 4096))
	BEST_ISP_4 = np.zeros((2048, 4096))
	ISP_RATE_4 = np.zeros((2048, 4096))
	ISP_RATE = np.zeros((2048, 4096))
if(FLAG_MRL):
	BEST_MRL_1 = np.zeros((2048, 4096))
	MRL_RATE_1 = np.zeros((2048, 4096))
	BEST_MRL_2 = np.zeros((2048, 4096))
	MRL_RATE_2 = np.zeros((2048, 4096))
	BEST_MRL_3 = np.zeros((2048, 4096))
	MRL_RATE_3 = np.zeros((2048, 4096))
	BEST_MRL_4 = np.zeros((2048, 4096))
	MRL_RATE_4 = np.zeros((2048, 4096))
	MRL_RATE = np.zeros((2048, 4096))
if(FLAG_PLANAR):
	BEST_PLANAR_1 = np.zeros((2048, 4096))
	PLANAR_RATE_1 = np.zeros((2048, 4096))
	BEST_PLANAR_2 = np.zeros((2048, 4096))
	PLANAR_RATE_2 = np.zeros((2048, 4096))
	BEST_PLANAR_3 = np.zeros((2048, 4096))
	PLANAR_RATE_3 = np.zeros((2048, 4096))
	BEST_PLANAR_4 = np.zeros((2048, 4096))
	PLANAR_RATE_4 = np.zeros((2048, 4096))
	PLANAR_RATE = np.zeros((2048, 4096))
if(FLAG_DC):
	BEST_DC_1 = np.zeros((2048, 4096))
	DC_RATE_1 = np.zeros((2048, 4096))
	BEST_DC_2 = np.zeros((2048, 4096))
	DC_RATE_2 = np.zeros((2048, 4096))
	BEST_DC_3 = np.zeros((2048, 4096))
	DC_RATE_3 = np.zeros((2048, 4096))
	BEST_DC_4 = np.zeros((2048, 4096))
	DC_RATE_4 = np.zeros((2048, 4096))
	DC_RATE = np.zeros((2048, 4096))

prevline = ""
for line in fid1:
	if "Posicao " in prevline:
		posX = line.split(',')[1]
		posY = line.split(',')[2]
	if "Best " in prevline:
		MIPFlag = line.split(',')[2] # 0 ou 1
		ISPFlag = line.split(',')[4] # 0 ou 1 ou 2
		MRLFlag = line.split(',')[5] # 0 ou 1
		DCFlag = line.split(',')[6] # Qualquer coisa [0,66]
		PLANARFlag = line.split(',')[6] # Qualquer coisa [0,66]
		
		# Testa a CU
		for i in range(Bloco_Y):
			for j in range(Bloco_X):
				CU_TESTA_1[int(posY)+i][int(posX)+j] = CU_TESTA_1[int(posY)+i][int(posX)+j] + 1
		
		# MIP FLAG / DC / PLANAR
		if(FLAG_MIP):
			if(int(MIPFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_MIP_1[int(posY)+i][int(posX)+j] = BEST_MIP_1[int(posY)+i][int(posX)+j] + 1		
		if(FLAG_DC):
			if(int(MIPFlag) <= 0):
				if(int(DCFlag) == 1):
					for i in range(Bloco_Y):
						for j in range(Bloco_X):
							BEST_DC_1[int(posY)+i][int(posX)+j] = BEST_DC_1[int(posY)+i][int(posX)+j] + 1
		if(FLAG_PLANAR):
			if(int(MIPFlag) <= 0):		
				if(int(PLANARFlag) == 0):
					for i in range(Bloco_Y):
						for j in range(Bloco_X):
							BEST_PLANAR_1[int(posY)+i][int(posX)+j] = BEST_PLANAR_1[int(posY)+i][int(posX)+j] + 1
	
		# ISP FLAG
		if(FLAG_ISP):
			if(int(ISPFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_ISP_1[int(posY)+i][int(posX)+j] = BEST_ISP_1[int(posY)+i][int(posX)+j] + 1

		# MRL FLAG
		if(FLAG_MRL):
			if(int(MRLFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_MRL_1[int(posY)+i][int(posX)+j] = BEST_MRL_1[int(posY)+i][int(posX)+j] + 1

	prevline = line
for line in fid2:
	if "Posicao " in prevline:
		posX = line.split(',')[1]
		posY = line.split(',')[2]
	if "Best " in prevline:
		MIPFlag = line.split(',')[2] # 0 ou 1
		ISPFlag = line.split(',')[4] # 0 ou 1 ou 2
		MRLFlag = line.split(',')[5] # 0 ou 1
		DCFlag = line.split(',')[6] # Qualquer coisa [0,66]
		PLANARFlag = line.split(',')[6] # Qualquer coisa [0,66]
		
		# Testa a CU
		for i in range(Bloco_Y):
			for j in range(Bloco_X):
				CU_TESTA_2[int(posY)+i][int(posX)+j] = CU_TESTA_2[int(posY)+i][int(posX)+j] + 1
		
		# MIP FLAG / DC / PLANAR
		if(FLAG_MIP):
			if(int(MIPFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_MIP_2[int(posY)+i][int(posX)+j] = BEST_MIP_2[int(posY)+i][int(posX)+j] + 1		
		if(FLAG_DC):
			if(int(MIPFlag) <= 0):
				if(int(DCFlag) == 1):
					for i in range(Bloco_Y):
						for j in range(Bloco_X):
							BEST_DC_2[int(posY)+i][int(posX)+j] = BEST_DC_2[int(posY)+i][int(posX)+j] + 1
		if(FLAG_PLANAR):
			if(int(MIPFlag) <= 0):		
				if(int(PLANARFlag) == 0):
					for i in range(Bloco_Y):
						for j in range(Bloco_X):
							BEST_PLANAR_2[int(posY)+i][int(posX)+j] = BEST_PLANAR_2[int(posY)+i][int(posX)+j] + 1
	
		# ISP FLAG
		if(FLAG_ISP):
			if(int(ISPFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_ISP_2[int(posY)+i][int(posX)+j] = BEST_ISP_2[int(posY)+i][int(posX)+j] + 1

		# MRL FLAG
		if(FLAG_MRL):
			if(int(MRLFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_MRL_2[int(posY)+i][int(posX)+j] = BEST_MRL_2[int(posY)+i][int(posX)+j] + 1

	prevline = line
for line in fid3:
	if "Posicao " in prevline:
		posX = line.split(',')[1]
		posY = line.split(',')[2]
	if "Best " in prevline:
		MIPFlag = line.split(',')[2] # 0 ou 1
		ISPFlag = line.split(',')[4] # 0 ou 1 ou 2
		MRLFlag = line.split(',')[5] # 0 ou 1
		DCFlag = line.split(',')[6] # Qualquer coisa [0,66]
		PLANARFlag = line.split(',')[6] # Qualquer coisa [0,66]
		
		# Testa a CU
		for i in range(Bloco_Y):
			for j in range(Bloco_X):
				CU_TESTA_3[int(posY)+i][int(posX)+j] = CU_TESTA_3[int(posY)+i][int(posX)+j] + 1
		
		# MIP FLAG / DC / PLANAR
		if(FLAG_MIP):
			if(int(MIPFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_MIP_3[int(posY)+i][int(posX)+j] = BEST_MIP_3[int(posY)+i][int(posX)+j] + 1		
		if(FLAG_DC):
			if(int(MIPFlag) <= 0):
				if(int(DCFlag) == 1):
					for i in range(Bloco_Y):
						for j in range(Bloco_X):
							BEST_DC_3[int(posY)+i][int(posX)+j] = BEST_DC_3[int(posY)+i][int(posX)+j] + 1
		if(FLAG_PLANAR):
			if(int(MIPFlag) <= 0):		
				if(int(PLANARFlag) == 0):
					for i in range(Bloco_Y):
						for j in range(Bloco_X):
							BEST_PLANAR_3[int(posY)+i][int(posX)+j] = BEST_PLANAR_3[int(posY)+i][int(posX)+j] + 1
	
		# ISP FLAG
		if(FLAG_ISP):
			if(int(ISPFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_ISP_3[int(posY)+i][int(posX)+j] = BEST_ISP_3[int(posY)+i][int(posX)+j] + 1

		# MRL FLAG
		if(FLAG_MRL):
			if(int(MRLFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_MRL_3[int(posY)+i][int(posX)+j] = BEST_MRL_3[int(posY)+i][int(posX)+j] + 1

	prevline = line
for line in fid4:
	if "Posicao " in prevline:
		posX = line.split(',')[1]
		posY = line.split(',')[2]
	if "Best " in prevline:
		MIPFlag = line.split(',')[2] # 0 ou 1
		ISPFlag = line.split(',')[4] # 0 ou 1 ou 2
		MRLFlag = line.split(',')[5] # 0 ou 1
		DCFlag = line.split(',')[6] # Qualquer coisa [0,66]
		PLANARFlag = line.split(',')[6] # Qualquer coisa [0,66]
		
		# Testa a CU
		for i in range(Bloco_Y):
			for j in range(Bloco_X):
				CU_TESTA_4[int(posY)+i][int(posX)+j] = CU_TESTA_4[int(posY)+i][int(posX)+j] + 1
		
		# MIP FLAG / DC / PLANAR
		if(FLAG_MIP):
			if(int(MIPFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_MIP_4[int(posY)+i][int(posX)+j] = BEST_MIP_4[int(posY)+i][int(posX)+j] + 1		
		if(FLAG_DC):
			if(int(MIPFlag) <= 0):
				if(int(DCFlag) == 1):
					for i in range(Bloco_Y):
						for j in range(Bloco_X):
							BEST_DC_4[int(posY)+i][int(posX)+j] = BEST_DC_4[int(posY)+i][int(posX)+j] + 1
		if(FLAG_PLANAR):
			if(int(MIPFlag) <= 0):		
				if(int(PLANARFlag) == 0):
					for i in range(Bloco_Y):
						for j in range(Bloco_X):
							BEST_PLANAR_4[int(posY)+i][int(posX)+j] = BEST_PLANAR_4[int(posY)+i][int(posX)+j] + 1
	
		# ISP FLAG
		if(FLAG_ISP):
			if(int(ISPFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_ISP_4[int(posY)+i][int(posX)+j] = BEST_ISP_4[int(posY)+i][int(posX)+j] + 1

		# MRL FLAG
		if(FLAG_MRL):
			if(int(MRLFlag) > 0):
				for i in range(Bloco_Y):
					for j in range(Bloco_X):
						BEST_MRL_4[int(posY)+i][int(posX)+j] = BEST_MRL_4[int(posY)+i][int(posX)+j] + 1

	prevline = line

# MIP RATE
if(FLAG_MIP):
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_1[i][j] == 0):
				MIP_RATE_1[i][j] = 0
			else:
				MIP_RATE_1[i][j] = BEST_MIP_1[i][j]/CU_TESTA_1[i][j]
	
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_2[i][j] == 0):
				MIP_RATE_2[i][j] = 0
			else:
				MIP_RATE_2[i][j] = BEST_MIP_2[i][j]/CU_TESTA_2[i][j] 

	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_3[i][j] == 0):
				MIP_RATE_3[i][j] = 0
			else:
				MIP_RATE_3[i][j] = BEST_MIP_3[i][j]/CU_TESTA_3[i][j] 
	
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_4[i][j] == 0):
				MIP_RATE_4[i][j] = 0
			else:
				MIP_RATE_4[i][j] = BEST_MIP_4[i][j]/CU_TESTA_4[i][j] 
	
	for i in range(2048):
		for j in range(4096):
			MIP_RATE[i][j] = (MIP_RATE_1[i][j] + MIP_RATE_2[i][j] + MIP_RATE_3[i][j] + MIP_RATE_4[i][j])/4

# ISP RATE
if(FLAG_ISP):
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_1[i][j] == 0):
				ISP_RATE_1[i][j] = 0
			else:
				ISP_RATE_1[i][j] = BEST_ISP_1[i][j]/CU_TESTA_1[i][j]
	
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_2[i][j] == 0):
				ISP_RATE_2[i][j] = 0
			else:
				ISP_RATE_2[i][j] = BEST_ISP_2[i][j]/CU_TESTA_2[i][j] 
	
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_3[i][j] == 0):
				ISP_RATE_3[i][j] = 0
			else:
				ISP_RATE_3[i][j] = BEST_ISP_3[i][j]/CU_TESTA_3[i][j] 
	
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_4[i][j] == 0):
				ISP_RATE_4[i][j] = 0
			else:
				ISP_RATE_4[i][j] = BEST_ISP_4[i][j]/CU_TESTA_4[i][j] 
	
	for i in range(2048):
		for j in range(4096):
			ISP_RATE[i][j] = (ISP_RATE_1[i][j] + ISP_RATE_2[i][j] + ISP_RATE_3[i][j] + ISP_RATE_4[i][j])/4

# MRL RATE
if(FLAG_MRL):
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_1[i][j] == 0):
				MRL_RATE_1[i][j] = 0
			else:
				MRL_RATE_1[i][j] = BEST_MRL_1[i][j]/CU_TESTA_1[i][j] 

	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_2[i][j] == 0):
				MRL_RATE_2[i][j] = 0
			else:
				MRL_RATE_2[i][j] = BEST_MRL_2[i][j]/CU_TESTA_2[i][j] 
	
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_3[i][j] == 0):
				MRL_RATE_3[i][j] = 0
			else:
				MRL_RATE_3[i][j] = BEST_MRL_3[i][j]/CU_TESTA_3[i][j] 
	
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_4[i][j] == 0):
				MRL_RATE_4[i][j] = 0
			else:
				MRL_RATE_4[i][j] = BEST_MRL_4[i][j]/CU_TESTA_4[i][j] 
	
	for i in range(2048):
		for j in range(4096):
			MRL_RATE[i][j] = (MRL_RATE_1[i][j] + MRL_RATE_2[i][j] + MRL_RATE_3[i][j] + MRL_RATE_4[i][j])/4

# PLANAR RATE
if(FLAG_PLANAR):
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_1[i][j] == 0):
				PLANAR_RATE_1[i][j] = 0
			else:
				PLANAR_RATE_1[i][j] = BEST_PLANAR_1[i][j]/CU_TESTA_1[i][j]

	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_2[i][j] == 0):
				PLANAR_RATE_2[i][j] = 0
			else:
				PLANAR_RATE_2[i][j] = BEST_PLANAR_2[i][j]/CU_TESTA_2[i][j]

	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_3[i][j] == 0):
				PLANAR_RATE_3[i][j] = 0
			else:
				PLANAR_RATE_3[i][j] = BEST_PLANAR_3[i][j]/CU_TESTA_3[i][j]

	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_4[i][j] == 0):
				PLANAR_RATE_4[i][j] = 0
			else:
				PLANAR_RATE_4[i][j] = BEST_PLANAR_4[i][j]/CU_TESTA_4[i][j]

	for i in range(2048):
		for j in range(4096):
			PLANAR_RATE[i][j] = (PLANAR_RATE_1[i][j] + PLANAR_RATE_2[i][j] + PLANAR_RATE_3[i][j] + PLANAR_RATE_4[i][j])/4

# DC RATE
if(FLAG_DC):
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_1[i][j] == 0):
				DC_RATE_1[i][j] = 0
			else:
				DC_RATE_1[i][j] = BEST_DC_1[i][j]/CU_TESTA_1[i][j] 
	
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_2[i][j] == 0):
				DC_RATE_2[i][j] = 0
			else:
				DC_RATE_2[i][j] = BEST_DC_2[i][j]/CU_TESTA_2[i][j]
	
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_3[i][j] == 0):
				DC_RATE_3[i][j] = 0
			else:
				DC_RATE_3[i][j] = BEST_DC_3[i][j]/CU_TESTA_3[i][j]
	
	for i in range(2048):
		for j in range(4096):
			if(CU_TESTA_4[i][j] == 0):
				DC_RATE_4[i][j] = 0
			else:
				DC_RATE_4[i][j] = BEST_DC_4[i][j]/CU_TESTA_4[i][j]

	for i in range(2048):
		for j in range(4096):
			DC_RATE[i][j] = (DC_RATE_1[i][j] + DC_RATE_2[i][j] + DC_RATE_3[i][j] + DC_RATE_4[i][j])/4

# MAPA DE CALOR
if(FLAG_MIP):
	plt.imshow(MIP_RATE, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')
if(FLAG_ISP):
	plt.imshow(ISP_RATE, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')
if(FLAG_MRL):
	plt.imshow(MRL_RATE, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')
if(FLAG_PLANAR):
	plt.imshow(PLANAR_RATE, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')
if(FLAG_DC):
	plt.imshow(DC_RATE, vmin=0, vmax=1, cmap='jet', interpolation='nearest', aspect='auto')

plt.colorbar()
plt.show()

fid1.close()
fid2.close()
fid3.close()
fid4.close()