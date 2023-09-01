import network
import time
import wheelmotor
from machine import Pin
import socket
import uasyncio as asyncio

# 配置网络模块
net = network.WLAN(network.STA_IF)
if not net.isconnected():
    net.active(True)
    # 连接无线网络，设立 wifi id 和密码
    net.connect('ATT 201', 'ibib776j+mx8')
#     net.connect('Berkeley-IoT', 'fc!N7$27')
print(net.ifconfig())

html = """<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF -8" />
    <title>GUIIII</title>
    <style>
      button {{
        font-size: 35px;
        background-color: lightgray;
        border-radius: 12px;
      }}
      button:hover {{
        box-shadow: 0 12px 16px 0 rgba(0, 0, 0, 0.24),
          0 17px 50px 0 rgba(0, 0, 0, 0.19);
      }}
      .border {{
        border-width: 10px;
        border-radius: 25px;
        padding: 50px;
        border: 3px solid gray;
        box-sizing: border-box;
      }}
      .front {{
        position: relative;
        left: 50%;
      }}
      .middle {{
        position: relative;
      }}
      .left {{
        position: relative;
        left: 47%;
      }}
      .right {{
        position: absolute;
        left: 53%;
      }}
      .back {{
        position: relative;
        left: 50%;
      }}
      .stop {{
        position: relative;
        left: 40%;
      }}
    </style>
  </head>
  <body>
    <h1>Current State: {}</h1>
    <div class="border">
      <div class="front">
        <a href="/Front"><button>↑</button></a>
      </div>
      <div class="middle">
        <span class="left">
          <a href="/Left"><button>←</button></a>
        </span>
        <span class="right">
          <a href="/Right"><button>→</button></a>
        </span>
      </div>
      <div class="back">
        <a href="/Back"><button>↓</button></a>
      </div>
      <div class="stop">
        <a href="/STOP"><button>Stop</button></a>
      </div>
    </div>
  </body>
</html>
"""

async def connectWeb():
    # 创建 socket 对象
    s = socket.socket()
    s.bind(('0.0.0.0', '80'))
    # 监听 80 端口
    s.listen(1)
    State = "Initialization"
    while True:
        # socket 阻塞外部连接
        cl, addr = s.accept()
        # 拿到客户端 IP 地址
        print('Client connected from', addr)
        # 拦截客户端请求
        request = cl.recv(1024)
        if request.decode()[:100].find("Front") != -1:
            wheelmotor.moveFront()
            State = "move front"
            await asyncio.sleep(2.6)
            wheelmotor.stop()
        elif request.decode()[:100].find("Back") != -1:
            wheelmotor.moveBack()
            State = "move back"
            await asyncio.sleep(2.6)
            wheelmotor.stop()
        elif request.decode()[:100].find("Left") != -1:
            wheelmotor.turnLeft()
            State = "turn left"
            await asyncio.sleep(1.5)
            wheelmotor.stop()
        elif request.decode()[:100].find("Right") != -1:
            wheelmotor.turnRight()
            State = "turn right"
            await asyncio.sleep(1.5)
            wheelmotor.stop()
        elif request.decode()[:100].find("STOP") != -1:
            wheelmotor.stop()
            State = "Stop"
        response = html.format(State)
        cl.send(response)
        cl.close()


#编辑异步任务
def runTask():
    
    #create event loop
    loop = asyncio.get_event_loop()
    loop.create_task(connectWeb())
    loop.run_forever()

# runTask()

