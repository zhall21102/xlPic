import pandas as pd
import cv2 as cv
import numpy as np
def toXlsx(file):
    img = cv.imread(file)
    lis = img.tolist()
    df = pd.DataFrame(lis)
    df.to_excel(excel_writer = "test.xlsx")
    
def toImg():
    df = pd.read_excel('test.xlsx')
    lis = df.values.tolist()
    lis2 = []
    for e in lis:
        lis2.append(e[1:]) 
    for x in range(len(lis2)):
        for y in range(len(lis2[0])):
            lis2[x][y] = (lis2[x][y].strip('][').split(', '))
    for x in range(len(lis2)):
        for y in range(len(lis2[0])):
            for z in range(len(lis2[0][0])):
                lis2[x][y][z] = int(lis2[x][y][z])
    array = np.asarray(lis2)
    cv.imwrite('test.png', array)
    
file = 'icon.png'
toXlsx(file)
print('XLSX done')
toImg()
