
import pyautogui

while True:
    input_x = int(input("输入x: "))
    input_y = int(input("输入y: "))

    print('请手动切换窗口, 4秒后截取.')
    pyautogui.sleep(4)

    L = input_x - 1
    T = input_y - 1
    R = input_x + 2
    B = input_y + 2
    # W = R - L
    # H = B - T

    img = pyautogui.screenshot(imageFilename='get_pixel.png', region=(L, T, 3, 3))

    point_red, point_green, point_blue = pyautogui.pixel(input_x, input_y)

    tolerance = [0, 0, 0]
    result = [0, 0, 0]
    for y in range(T, B):
        i = 0
        for x in range(L, R):
            pix = pyautogui.pixel(x, y)
            # print(pix)
            tolerance[0] = abs(pix[0] - point_red)
            tolerance[1] = abs(pix[1] - point_green)
            tolerance[2] = abs(pix[2] - point_blue)

            # print('(' + str(x) + ', ' + str(y) + ') (' + str(pix[0]) + ', ' + str(pix[1]) + ', ' + str(pix[2]) + ')', end='\t\t')
            s = '(' + str(x) + ', ' + str(y) + ') (' + str(pix[0]) + ', ' + str(pix[1]) + ', ' + str(pix[2]) + ')'
            print(f"{s:32}", end='')
            i = i + 1
            if i == 3:
                print('\n')
            for k in range(0, 3):
                if tolerance[k] > result[k]:
                    result[k] = tolerance[k]

    w, h = pyautogui.size()
    print('中心点属性: [[' + str(input_x) + '/' + str(w) + ', ' + str(input_y) + '/' + str(h) + '], [' + str(point_red) + ', ' + str(point_green) + ', ' + str(point_blue) + '], 0, \'\']')
    print('请手动修改xy坐标和纯画面分辨率！y需要减去任务栏高(一般31)，纯画面通过抓图识别一次')
    print('RGB容差分别是:', result, '取最大值即可')

    print('-' * 60)

    # pmc = pyautogui.pixelMatchesColor(x-1, y, (255, 237, 199), tolerance=6)
    # # pmc = pyautogui.pixelMatchesColor(x, y, (43, 43, 43), tolerance=0)
    # print(pmc, type(pmc))

