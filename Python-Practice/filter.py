#filter (func, collection) = retuurn all elemnts that passs a condition
import numpy as np
grades = [78,87,90,95,93]

pass_grade =  filter(lambda grade: grade>=90, grades)

for gr in pass_grade:
    print(gr)
