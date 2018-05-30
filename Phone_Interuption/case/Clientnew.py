import os
from time import *
from socket import *
import threading

# addr = '127.0.0.1'
# port = 9999

# client = socket(AF_INET, SOCK_STREAM)
# client.connect((addr, port))


class ClientTransmit(object):
    '''
    1.RunSend(data),创建新线程来发送数据，每次发送结束后关闭线程，data是需要发送的数据;
    2.RunRecv(),创建新线程来接收数据，一直到接收到"#"，退出接收
    Canoe 发送字符a-z,可自定义；py根据接收的字符进行相应动作；
    py发送数字给Canoe，Canoe根据接收的字符进行相应动作；
    '''
    def __init__(self):
        self.addr = '127.0.0.1'
        self.port = 9999
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((self.addr,self.port))

    def CLSend(self,data):

        #global client
        cmd = str(data)
        self.client.send(cmd.encode("utf-8"))
        print("Send>>"+cmd)

    def CLRecv(self):

        #global client

        while True:
            received_data = self.client.recv(4)
            cmd_res_size = len(received_data)

            print("Receive<<"+received_data.decode())
 
            if received_data.decode() == '#\000':

                break

    def Close(self):
        #global client
        self.client.close()

    def RunRecv(self):
        # 创建新线程来接收数据，一直到接收到"#"，退出接收
        #t1 = threading.Thread(target=ClientTransmit.CLRecv, args=(naddr, nport))
        t1 = threading.Thread(target=self.CLRecv)
        t1.start()

    def RunSend(self,data):

        # 创建新线程来发送数据，每次发送结束后关闭线程
        t2 = threading.Thread(target=self.CLSend,args=(data))
        t2.start()
        t2.join()


if __name__ == '__main__':

    #for Test
    TestClient = ClientTransmit()
    TestClient.RunRecv()
    TestClient.CLSend(99)
    sleep(5)
    TestClient.CLSend(2)