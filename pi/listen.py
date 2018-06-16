#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
建立一个python server，监听指定端口，
如果该端口被远程连接访问，则获取远程连接，然后接收数据，
并且做出相应反馈。
'''
from pyfirmata import Arduino, util
import time
import re
addrs = '/dev/ttyACM0'
board = Arduino(addrs)
path = "./config.txt"


if __name__=="__main__":
        import socket

        def analy(file,content):
            file_data=""
            with open(file,"r") as f:
                for line in f:
                    if content in line:
                        line = line.replace(content,"").split()
                        return line

        ip = analy(path,"ip=")
        port = analy(path,"port=")
        
        print("Address =" + ip[0] + ":" + port[0])

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        sock.bind((ip[0], int(port[0])))  #配置soket，绑定IP地址和端口号
        sock.listen(5) #设置最大允许连接数，各连接和server的通信遵循FIFO原则
        print("\033[0;32m%s\033[0m" % "Server is starting..")
        print("\033[0;32m%s\033[0m" % "Server is listenting port 8001, with max connection 5\n")


            
        def led_on(*arg):
            name = "LED_on"
            for n in range(len(arg)):
                pin = arg[n]
                board.digital[pin].write(0)
            print(">>" + name)
            connection.send(name)
       


        def led_off(*arg):
            name = "LED_off"
            for n in range(len(arg)):
                pin = arg[n]
                board.digital[pin].write(1)
            print(">>" + name)
            connection.send(name)
    
        def light(arr):
            name = "LIGHT_up"
            pin = arr[0]
            status = arr[1]
            board.digital[pin].write(status)
            print(">>" + name)
            connection.send(name)
            



        def int_list(str):
            con =  re.findall(r'[(](.*?)[)]', str)   
            for n in range(len(con)):
                 num = con[n].split(',')
            arr = list(map(int,num))
            return arr
                            


        while True:  #循环轮询socket状态，等待访问
                
                connection,address = sock.accept()  

                try:  
                        connection.settimeout(50)
                        #获得一个连接，然后开始循环处理这个连接发送的信息
                        '''
                        如果server要同时处理多个连接，则下面的语句块应该用多线程来处理，
                        否则server就始终在下面这个while语句块里被第一个连接所占用，
                        无法去扫描其他新连接了，但多线程会影响代码结构，所以记得在连接数大于1时
                        下面的语句要改为多线程即可。
                        '''
                        while True:
                                buf = connection.recv(1024)  
                                print(">>Get value " + buf)
                                if buf == 'off':  
                                    led_off(3,4,5,6,7,8)
                                    
                                elif buf == 'on':  
                                    led_on(3,4,5,6,7,8)
                                
                                elif buf[0:5] == "light":
                                    arg = int_list(buf)
                                    light(arg)

                                else: 
                                    print(">>close")
                                    break#退出连接监听循环
                except socket.timeout:  #如果建立连接后，该连接在设定的时间内无数据发来，则time out
                         print('time out')

                print("\033[0;31m%s\033[0m" % "closing one connection\n") #当一个连接监听循环退出后，连接可以关掉
                connection.close()  

