import time
import datetime
import os
import threading
import json
import pandas as pd
def open_calc():
    sum = 0
    epoch_total = 0
    dict = {}
    with open('result_line.txt', 'r', encoding='utf-8') as f:
        flag = 0
        login_time = []
        con_times = []
        info = []
        flag1 = 1
        for line in f.readlines():
            epoch_total += 1
            # data = line.split(' ')
            if 'Welcome' in line:
                flag += 1
            if 'Last login' in line:
                    sum = sum+1
                    login_time.append(line)
            if '[INFO]' in line:
                # print(line)
                info.append(line)
            if(flag > flag1):
                con_times.append(sum)
                writer = open('car_info.csv', 'a+',encoding='utf-8')
                cpu = ['ARM+FPGA']
                RAM = ['1GB']
                Moter =['RIKIBOT-X4（STM32F103RC）']
                start_time = datetime.datetime.now()
                # Start_time.append(start_time)
                print(start_time)
                # follower_people.main1()
                # time.sleep(3)
                # end_time = datetime.datetime.now()
                # print(end_time.second - start_time.second, '秒')
                # time1 = end_time.second-start_time.second
                time1 = epoch_total*0.04
                print(time1)
                Total_time = []
                second = '秒'
                Total_time.append((time1, second))
                id = '智能车1号'
                # print(Total_time[0][0])
                dict['CPU'] = cpu
                dict['内存'] = RAM
                dict['运行时间'] = Total_time
                dict['电机驱动板'] = Moter
                dict['login_time'] = login_time
                dict['ID'] = id
                dict['连接次数'] = con_times
                dict['INFO'] = info
                str_data = json.dumps(dict, ensure_ascii=False)
                writer.write(str_data + "\n")
                login_time = []
                con_times = []
                info = []

                print("epoch_total", epoch_total)
                epoch_total = 0
                flag1 += 1
                writer.close()
        con_times.append(sum)
        writer = open('car_info.csv', 'a+', encoding='utf-8')
        cpu = ['ARM+FPGA']
        RAM = ['1GB']
        Moter = ['RIKIBOT-X4（STM32F103RC）']
        start_time = datetime.datetime.now()
        # Start_time.append(start_time)
        print(start_time)
        # follower_people.main1()
        # time.sleep(3)
        # end_time = datetime.datetime.now()
        # print(end_time.second - start_time.second, '秒')
        # time1 = end_time.second-start_time.second
        time1 = epoch_total * 0.04
        print(time1)
        Total_time = []
        second = '秒'
        Total_time.append((time1, second))
        id = '智能车1号'
        # print(Total_time[0][0])
        dict['CPU'] = cpu
        dict['内存'] = RAM
        dict['运行时间'] = Total_time
        dict['电机驱动板'] = Moter
        dict['login_time'] = login_time
        dict['ID'] = id
        dict['连接次数'] = con_times
        dict['INFO'] = info
        str_data = json.dumps(dict, ensure_ascii=False)
        writer.write(str_data + "\n")
        print("epoch_total", epoch_total)
        flag1 += 1
        writer.close()



if __name__ == '__main__':
    open_calc()
#     # 使用threading模块，threading.Thread()创建线程，其中target参数值为需要调用的方法，同样将其他多个线程放在一个列表中，遍历这个列表就能同时执行里面的函数了
#     threads = [threading.Thread(target=open_calc),
#                threading.Thread(target=open_mstsc)]
#     for t in threads:
#         # 启动线程
#         t.start()