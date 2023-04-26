import network
import time
from time import sleep
import wheelmotor
from machine import Pin
import socket
import ultra_Action

#配置网络模块
net = network.WLAN(network.STA_IF)
if not net.isconnected():
    net.active(True)
    #连接无线网络，设立wifi id 和密码
#     net.connect('ATT 201','ibib776j+mx8')
    net.connect('Berkeley-IoT','fc!N7$27')
print(net.ifconfig())

html = """<!DOCTYPE html>
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <title>GUIIII</title>
    <style>
      body {
        background-color: #222222;
      }

      .controller {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-rows: 1fr 1fr 1fr;
        gap: 10px;
        justify-items: center;
        align-items: center;
        padding: 50px;
        border: 5px solid white;
        border-radius: 20px;
      }

      .button {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 80px;
        height: 80px;
        font-size: 20px;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        text-decoration: none;
        border: none;
        border-radius: 50%;
      }

      .button:hover {
        background-color: #3e8e41;
      }

      .button:active {
        background-color: #3e8e41;
        box-shadow: 0 5px #666;
        transform: translateY(4px);
      }

      .up {
        grid-area: 1 / 2 / 2 / 3;
      }

      .down {
        grid-area: 3 / 2 / 4 / 3;
      }

      .left {
        grid-area: 2 / 1 / 3 / 2;
      }

      .right {
        grid-area: 2 / 3 / 3 / 4;
      }

      .stop {
        position: absolute;
        top: 50%;
        right: 50px;
        transform: translateY(-50%);
        width: 150px;
        height: 150px;
        font-size: 30px;
        background-color: red;
        color: white;
        text-align: center;
        text-decoration: none;
        border: none;
        border-radius: 50%;
        box-shadow: 0 5px #666;
      }

      .stop:hover {
        background-color: #cc0000;
      }

      .stop:active {
        background-color: #990000;
        box-shadow: 0 2px #666;
        transform: translateY(-46%);
      }
    </style>
  </head>
  <body>
    <h1 style="color: white">Current State: %s</h1>
    <div class="controller">
      <div></div>
      <a href="/Front" class="button up"><span>^</span></a>
      <div></div>
      <a href="/Left" class="button left"><span style="transform: rotate(-90deg)">^</span></a>
      <a href="/STOP" class="button stop"><b>STOP</b></a>
      <a href="/Right" class="button right"><span style="transform: rotate(90deg)">^</span></a>
      <div></div>
      <a href="/Back" class="button down"><span style="transform: rotate(180deg)>^</span></a>
      <div></div>
    </div>
  </body>
</html>

"""
#create socket object
s = socket.socket()
s.bind(('0.0.0.0','80'))
#listen 80 port
s.listen(1)

def connectWeb():
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
            sleep(1.5)
            wheelmotor.stop()
        elif request.decode()[:100].find("Right") != -1:
            wheelmotor.turnRight()
            State = "turn right"
            sleep(1.5)
            wheelmotor.stop()
        elif request.decode()[:100].find("STOP") != -1:
            wheelmotor.stop()
            State = "Stop"
        response = html%State
        cl.send(response)
        cl.close()
          
    
        
    
    
    
    


