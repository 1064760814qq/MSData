import paramiko
import time
from threading import Thread
#这是跟随人模式
def ssh1():
    sum = 1
    sshClient = paramiko.SSHClient()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient.connect(hostname = "192.168.123.213", port = 22, username = "firefly", password = "firefly")

    shell = sshClient.invoke_shell()
    shell.sendall("roslaunch rikirobot bringup.launch\n")
    # shell.sendall("ls\n")
    shell.sendall("exit\n")

    while True:
        # shell.sendall("^c\n")
        data = shell.recv(2048).decode()
        result = str(data)
        with open('result_people.txt','a') as file:
            file.write("{}\n".format(result))
        time.sleep(0.4)
        sum = sum + 1
        if (sum==30):
            break
        # if  0xff == ord('q'):
            # break
        print(data, end = "")

    # sshClient.close()
def ssh2():
    # time.sleep(12)
    sum2 = 1
    sshClient2 = paramiko.SSHClient()
    sshClient2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient2.connect(hostname="192.168.123.213", port=22, username="firefly", password="firefly")

    shell2 = sshClient2.invoke_shell()
    shell2.sendall("roslaunch riki_follower follower.launch\n")
    # shell2.sendall("roslaunch openni2_launch openni2.launch\n")
    shell2.sendall("exit\n")
    while True:
        data2 = shell2.recv(2048).decode()
        result2 = str(data2)
        with open('result_people2.txt','a') as file2:
            file2.write("{}\n".format(result2))
        time.sleep(0.3)
        sum2 = sum2+1
        # if 0xff == ord('q'):
        #     print('ooo')
        #     break
        if sum2 == 30:
            print("quit now")
            break
        print(data2, end="")
    sshClient2.close()

def main1():
    t1 = Thread(target=ssh1())
    t2 = Thread(target=ssh2())
    t1.start()
    t2.start()
    print('开始')
