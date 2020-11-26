import paramiko
import time
from threading import Thread
#这是跟随红线模式
def ssh1():
    sum = 1
    sshClient = paramiko.SSHClient()
    sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient.connect(hostname = "192.168.123.213", port = 22, username = "firefly", password = "firefly")

    shell = sshClient.invoke_shell()
    shell.sendall("roslaunch rikirobot bringup.launch\n")
    shell.sendall("exit\n")

    while True:

        data = shell.recv(2048).decode()
        result = str(data)
        with open('result_line.txt', 'a') as file:
            file.write("{}\n".format(result))
        time.sleep(0.4)
        sum = sum + 1
        if (sum==35):
            break
        # print(data, end="")
    # sshClient.close()
def ssh2():
    sum2 = 1
    time.sleep(14)
    sshClient2 = paramiko.SSHClient()
    sshClient2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient2.connect(hostname="192.168.123.213", port=22, username="firefly", password="firefly")
    shell2 = sshClient2.invoke_shell()
    shell2.sendall("roslaunch openni2_launch openni2.launch\n")
    shell2.sendall("exit\n")
    while True:
        data2 = shell2.recv(2048).decode()
        result2 = str(data2)
        with open('result_line2.txt','a') as file2:
            file2.write("{}\n".format(result2))
        time.sleep(0.3)
        sum2 = sum2+1
        if sum2 == 20:
            break
        # print(data2, end="")
    # sshClient2.close()

def ssh3():
    sum3 = 1
    time.sleep(25)
    sshClient3 = paramiko.SSHClient()
    sshClient3.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshClient3.connect(hostname="192.168.123.213", port=22, username="firefly", password="firefly")

    shell3 = sshClient3.invoke_shell()
    shell3.sendall("roslaunch  riki_line_follower  riki_line.launch\n")
    shell3.sendall("exit\n")
    while True:
        data3 = shell3.recv(2048).decode()
        result3 = str(data3)
        with open('result_line3.txt','a') as file3:
            file3.write("{}\n".format(result3))
        print(data3, end="")
        time.sleep(0.3)
        sum3 = sum3+1
        if sum3 == 30:
            break
    sshClient3.close()

if __name__ == '__main__':
    t1 = Thread(target=ssh1)
    t2 = Thread(target=ssh2)
    t3 = Thread(target=ssh3)
    t1.start()
    t2.start()
    t3.start()
