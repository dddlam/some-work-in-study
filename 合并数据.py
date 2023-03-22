import pandas as pd
import os
path = 'D:/hjl/data/2022年/1/qixiang_wurangwu/minutes_down/'  #excel表格所在文件路径
last_data = pd.read_excel('D:/hjl/data/2022年/1\整理好的/test.xls')
for c in os.listdir(path):#遍历所有站点的名字
    c_path = path + c #站点的路径
    c_data = pd.read_excel(c_path)#读取站点，为dataframe
    for i in range(1,13):#循环是为了读取所有月份的文件夹
        way = 'D:/hjl/data/2022年/'+str(i)+'/qixiang_wurangwu/minutes_down/'
        for n in os.listdir(way):#遍历每个文件夹的文件
            if c == n:#前后两次遍历文件是否匹配
                n_path = way + n#就是路径咯
                n_data = pd.read_excel(n_path)#和前面一样
                new_data = pd.concat([c_data,n_data])#合并好的中间产物，哦concat要用[]，因为里面是dataframe格式，concat貌似要用列表才能拼在一起
                last_data = pd.concat([last_data,new_data])#最后要的东西
last_data.to_csv('D:/hjl/data/2022年/1\整理好的/minutes_down.csv')

print('dones')