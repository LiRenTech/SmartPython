import asyncio


# async 意思是异步

async def f():
    # 在 def 前面加上 async之后，这个函数就是异步函数了，或者应该叫 协程函数
    # 协程函数返回的就是一个 协程对象  res = f()  只是得到协程对象，实际不会执行函数内容
    import random
    import time
    # 模拟网络请求情况，随机等待一段时间
    t = random.random() * 3 + 1
    time.sleep(t)
    print("随机时间结束", t, "s")
    ...


# 事件循环
loop = asyncio.get_event_loop()  # 先获取一个事件循环

loop.run_until_complete(f())  # 想要执行协程函数，要交给事件循环来处理

# =============以前的写法

# 现在
asyncio.run(f())  # 3.7 之后加进来的

# ============= await
# await 后面一般跟着可等待的对象
"""
res = await f()
await就是等待拿到结果之后再继续往下走
如果当前是等待的状态，那么就会先不执行，让事件循环里执行其他的事件 
"""


async def func():
    await asyncio.sleep(1)
    return "a"


async def start():
    taskList = [
        asyncio.create_task(func(), name='t1'),
        asyncio.create_task(func(), name='t2'),
    ]
    done, pending = await asyncio.wait(taskList)
    print(done)


asyncio.run(start())

# https://www.bilibili.com/video/BV1cK4y1E77y/?p=8



