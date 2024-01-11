import math
import turtle as t
import pandas as pd

user_input=float(input('输入图片放大倍数：'))

mul=user_input

t.mode('standard')

t.pencolor('blue')

t.setup(width=1000 * mul, height=1500 * mul)

t.circle(1,90)

t.speed(0)

t.pensize(2)

t.setworldcoordinates(0, 0, 1000 * mul, 1500 * mul)

# 从Excel文件中读取数据，返回一个DataFrame对象
df = pd.read_excel("drawing2.xls")

# 获取第2行到36行（索引为1到35）的数据，这些是圆弧
arc_data = df.loc[1:34].values

tp_values = []

for row in arc_data:
    r, op, x, y, c, x1, y1, x2, y2 = row[2:11]  # 半径, 起点角度, 中心 X, 中心 Y, 总角度, 端点 X, 端点 Y, 起点 X, 起点 Y
    # 将所有的数变为浮点数
    x = float(x) if isinstance(x, int) else x
    y = float(y) if isinstance(y, int) else y
    x = round(x / 10000, 2)
    y = round(y / 10000, 2)
    tp_values.append([x, y])

def tp(values):
    t.penup()
    t.setpos(x*mul,y*mul)
    t.pendown()
for value in tp_values:
    tp(value)

# 定义一个空列表，用来存储所有的圆弧数据
tpc_values = []

# 遍历圆弧数据，将每一行的数据分为两个函数的参数
for row in arc_data:
    r, op, x, y, c, x1, y1, x2, y2 = row[2:11]  # 半径, 起点角度, 中心 X, 中心 Y, 总角度, 端点 X, 端点 Y, 起点 X, 起点 Y
    # 将所有的数变为浮点数
    r = float(r) if isinstance(r, int) else r
    op = float(op) if isinstance(op, int) else op
    x = float(x) if isinstance(x, int) else x
    y = float(y) if isinstance(y, int) else y
    c = float(c) if isinstance(c, int) else c
    ed = c + op
    r = round(r/10000, 2)
    x = round(x/10000, 2)
    y = round(y/10000, 2)
    tpc_values.append([x, y, r, op, ed])

# 调用tpc函数，并将返回值赋给变量

def tpc(values):
    x, y, r, op, ed = values
    rad = math.radians(op)  # 已知圆心、角度，求起笔位置
    x += r * (math.cos(rad))
    y += r * (math.sin(rad))
    t.penup()
    t.setpos(x * mul, y * mul)
    t.pendown()
    t.setheading(op + 90)
    if ed >= op:
        t.circle(r * mul, ed - op)
    else:
        t.circle(r * mul, ed + 360 - op)
for value in tpc_values:
    tpc(value)

print(tpc_values)

# 获取第37行到198行（索引为36到197）的数据，这些是直线
line_data = df.loc[36:197].values

# 定义一个空列表，用来存储所有的直线数据
line_values = []

# 遍历直线数据，将每一行的数据分为两个函数的参数
for row in line_data:
    r, op, x, y, c, x1, y1, x2, y2 = row[2:11]  # 半径, 起点角度, 中心 X, 中心 Y, 总角度, 端点 X, 端点 Y, 起点 X, 起点 Y
    # 将所有的数变为浮点数
    x1 = float(x1) if isinstance(x1, int) else x1
    y1 = float(y1) if isinstance(y1, int) else y1
    x2 = float(x2) if isinstance(x2, int) else x2
    y2 = float(y2) if isinstance(y2, int) else y2
    x1 = round(x1/10000, 2)
    x2 = round(x2/10000, 2)
    y1 = round(y1/10000, 2)
    y2 = round(y2/10000, 2)
    # 将每一行的数据添加到列表中
    line_values.append([x1, y1, x2, y2])

print(line_values)

# 调用l函数，并将返回值赋给变量
def l(values):
    x1, y1, x2, y2 = values
    t.penup()
    t.setpos(x1 * mul, y1 * mul)
    t.pendown()
    t.setpos(x2 * mul, y2 * mul)
for value in line_values:
    l(value)

