import os
import json
import matplotlib.pyplot as plt
import numpy as np

correct_list_h = []
wrong_list_h = []

correct_list_w = []
wrong_list_w = []

correct_list_c = []
wrong_list_c = []

skip_list = []

files = os.listdir("C:/Users/DSLab/Lab/DSL/ARC/data/training")
# index = 147
# f = files[index]
f = "e98196ab.json"
file_path = "C:/Users/DSLab/Lab/DSL/ARC/data/training/" + f
try:
    with open(file_path) as file:
        task = json.load(file)         
except :
    print("file open error")
print(f, " ", index + 1, "/", len(files))

truth_h = len (task["test"][0]["output"])
truth_w = len (task["test"][0]["output"][0])
truth_c = {color for row in task["test"][0]["output"] for color in row}

candi_answer_h, candi_answer_w, candi_answer_c = GridSize_pridictorr(task)
    
    
print("found ", len(candi_answer_h),len(candi_answer_w),len(candi_answer_c),"answers!")

h = 0
w = 0 
c = 0

for a in candi_answer_h:
    if a == truth_h:
        correct_list_h.append(f)
        print("h correct!")
        h = 1
        break
if h == 0:
    wrong_list_h.append(f)
    print("h wrong")

for a in candi_answer_w:
    if a == truth_w:
        correct_list_w.append(f)
        print("w correct!")
        w = 1
        break
if w == 0:
    wrong_list_w.append(f)
    print("w wrong")

for a in candi_answer_c:
    if a == truth_c:
        correct_list_c.append(f)
        print("c correct!")
        c = 1
        break
if c == 0:
    wrong_list_c.append(f)
    print("c wrong")
print("correct : ",len(correct_list_h), len(correct_list_w), len(correct_list_c), "/ wrong", len(wrong_list_h), len(wrong_list_w), len(wrong_list_c))
