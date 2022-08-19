import os
dirname = '//home//dmitriy//airflow_hw//data//models'
files = os.listdir(dirname)
files.sort()
pred = files[-1].split('_')[-1].split('.')[0]
print(pred)