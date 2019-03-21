from os import path
import numpy as np
from cv2 import imread, floodFill, imwrite, cvtColor, COLOR_BGR2RGB
from PIL.ImageColor import getrgb

percentiles = [10, 30, 50, 70, 90]

def read_line_frame(file_name):
    original_pic = imread(path.join(path.dirname(__file__), file_name), flags=8)
    pic = original_pic.copy()
    return pic

def read_value(file_name):
    num = np.loadtxt(path.join(path.dirname(__file__), file_name), dtype=int, delimiter=',', skiprows=1)
    return num

def mapping_area(num):
    positions = [eval(s) for s in ('19,19 40,13 51,11 60,23 74,22 '
    '40,34 45,34 50,34 55,34 8,46 13,46 18,46 23,46 28,46 33,46 61,46 89,46').split()]
    area_num = np.append(num, positions, axis=1)
    return area_num

def assign_heat_coor(area_num):
    percentiles_results = []
    area_colors = []

    for i in percentiles:
        percentiles_results.append(np.percentile(area_num[:,1],i))

    for i in area_num[:,1]:
        if percentiles_results[0] > i:
            area_colors.append('#c6ffff')
        elif percentiles_results[0] < i and i <= percentiles_results[1]:
            area_colors.append('#8fd0ff')
        elif percentiles_results[1] < i and i <= percentiles_results[2]:
            area_colors.append('#589fef')
        elif percentiles_results[2] < i and i <= percentiles_results[3]:
            area_colors.append('#0071bc')
        elif percentiles_results[3] < i and i <= percentiles_results[4]:
            area_colors.append('#00468b')
        elif percentiles_results[4] < i:
            area_colors.append('#00215d')
    
    return area_colors

def heatmap(area_num, pic, area_colors):
    for index, row in enumerate(area_num):
        heat_color = getrgb(area_colors[index])
        floodFill(pic, None, (row[2]*10,row[3]*10), newVal=heat_color)
        imwrite('test.png', cvtColor(pic, COLOR_BGR2RGB))

    return heatmap

if __name__ == '__main__':
    pic = read_line_frame('nurinuri.png')
    area_num = mapping_area(read_value('area_number.csv'))
    area_colors = assign_heat_coor(area_num)

    heatmap(area_num, pic, area_colors)