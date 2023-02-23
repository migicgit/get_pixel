from time import sleep

import pyautogui

print("本程序目标是统计某像素点 RGB 的浮动范围, 每次约历时30秒, 请在期间尽情奔跑.")
print("建议将目标窗口移动到左上减少人工计算, 使用截图软件确定窗口纯画面位于左上(0,0), 以及确定需要截取的像素坐标.这个我不管.\n")

while True:
    print("--- 请输入横纵坐标(x,y) ---")
    input_x = int(input("输入x: "))
    input_y = int(input("输入y: "))

    print('请手动切换窗口, 4秒后获取像素.')
    pyautogui.sleep(4)

    L = input_x - 1
    T = input_y - 1
    R = input_x + 2
    B = input_y + 2

    times = 100

    red = []
    green = []
    blue = []

    for i in range(0, times):
        # img = pyautogui.screenshot(imageFilename='get_pixel.png', region=(L, T, 3, 3))
        pix = pyautogui.pixel(input_x, input_y)
        red.append(pix[0])
        green.append(pix[1])
        blue.append(pix[2])
        # red[i], green[i], blue[i] = pyautogui.pixel(input_x, input_y)
        sleep(0.2)


    # r_mean = int(sum(red) / len(red))
    r_max = max(red)
    r_min = min(red)
    r_mean = int((r_max + r_min) / 2)
    r_mean_probability = red.count(r_mean) / times * 100
    r_tolerance = r_max - r_mean + 1

    # g_mean = int(sum(green) / len(green))
    g_max = max(green)
    g_min = min(green)
    g_mean = int((g_max + g_min) / 2)
    g_mean_probability = green.count(g_mean) / times * 100
    g_tolerance = g_max - g_mean + 1

    # b_mean = int(sum(blue) / len(blue))
    b_max = max(blue)
    b_min = min(blue)
    b_mean = int((b_max + b_min) / 2)
    b_mean_probability = blue.count(b_mean) / times * 100
    b_tolerance = b_max - b_mean + 1

    print('Red最大:', r_max, '最小:', r_min, '均值:', r_mean, '均值概率:', str(r_mean_probability) + '%, 建议容差:', r_tolerance)
    print('Green最大:', g_max, '最小:', g_min, '均值:', g_mean, '均值概率:', str(g_mean_probability) + '%, 建议容差:', g_tolerance)
    print('Blue最大:', b_max, '最小:', b_min, '均值:', b_mean, '均值概率:', str(b_mean_probability) + '&, 建议容差:', b_tolerance)

    w, h = pyautogui.size()
    h = 1080

    tolerance = max(r_tolerance, g_tolerance, b_tolerance)
    print('中心点属性: [[' + str(input_x) + '/' + str(w) + ', ' + str(input_y-31) + '/' + str(h) + '], [' + str(
        r_mean) + ', ' + str(g_mean) + ', ' + str(b_mean) + '], ' + str(tolerance) + ', \'注释内容\']')
    print('自行确认xy坐标和纯画面分辨率！y已经减去标题栏高度(31)')

    print('-' * 60, '\n')


