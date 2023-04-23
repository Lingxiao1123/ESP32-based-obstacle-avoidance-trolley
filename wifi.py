import network
import time
import wheelmotor
from machine import Pin
import socket

#配置网络模块
net = network.WLAN(network.STA_IF)
if not net.isconnected():
    net.active(True)
    #连接无线网络，设立wifi id 和密码
    net.connect('ATT 201','ibib776j+mx8')
print(net.ifconfig())

html = """<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv = "Content-Type" content = "text/html;charset = UTF-8">
        <title>GUIIII</title>
    </head>
    <body>
        <h1>Current State: %s</h1>
        <br><br>
        <a href = "/Front""><button>Move Forward</button></a>
        <a href = "/Back""><button>Move Backward</button></a>
        <a href = "/Left""><button>Turn Left</button></a>
        <a href = "/Right""><button>Turn Right</button></a>
        <a href = "/STOP""><button>Stop </button></a>
    </body>
</html>
"""
#create socket object
s = socket.socket()
s.bind(('0.0.0.0','80'))
#listen 80 port
s.listen(1)

State = "Initialization"

while True:
    #socket阻塞外部连接
    cl,addr = s.accept()
    #拿到客户端IP地址
    print('Client connected from',addr)
    #拦截客户端请求
    request = cl.recv(1024)
    if request.decode()[:100].find("Front") != -1:
        wheelmotor.moveFront()
        State = "move front"
    elif request.decode()[:100].find("Back") != -1:
        wheelmotor.moveBack()
        State = "move back"
    elif request.decode()[:100].find("Left") != -1:
        wheelmotor.turnLeft()
        State = "turn left"
    elif request.decode()[:100].find("Right") != -1:
        wheelmotor.turnRight()
        State = "turn right"
    elif request.decode()[:100].find("STOP") != -1:
        wheelmotor.stop()
        State = "Stop"
    response = html%State
    cl.send(response)
    cl.close()
    
        
    
    
    
    


