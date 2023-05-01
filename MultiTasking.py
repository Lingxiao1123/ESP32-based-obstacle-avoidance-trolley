import ultra_Action
import uasyncio as asyncio
import wifi


async def task1():
    # 异步任务1
    ultra_Action.run()
    await asyncio.sleep(1)
    print("Task 1 done")
    
async def task2():
    # 异步任务2
    wifi.runTask()
    await asyncio.sleep(2)
    print("Task 2 done")

async def main():
    # 主函数
    await asyncio.gather(task1(), task2())
    
asyncio.run(main())