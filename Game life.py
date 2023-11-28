import tkinter
from time import time

master = tkinter.Tk()
canvas = tkinter.Canvas(master, bg='white', height=500, width=500)
for i in range(50):
    canvas.create_line((0, i * 10), (1000, i * 10))

for i in range(50):
    canvas.create_line((0, i * 10)[::-1], (1000, i * 10)[::-1])

d = []
for i in range(50):
    s1 = []
    for j in range(50):
        s1.append([j * 10, i * 10, j * 10 + 10, i * 10 + 10, 0, 0])  # [координаты, нужно ли изменять, состояние]
    d.append(s1)


def change(d):
    matrix = []
    for i in range(len(d)):
        s1 = []
        for j in range(len(d[i])):
            s1.append(d[i][j][-1])
        matrix.append(s1)
    key = lambda x: x == 1
    s = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    y = len(matrix) - 1  # в данном случае это i
    x = len(matrix[1]) - 1  # в данном случае это j
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == y and j == x:
                s[i][j] += int(key(matrix[0][0]))
                s[i][j] += int(key(matrix[0][j]))
                s[i][j] += int(key(matrix[i][0]))
                s[i][j] += int(key(matrix[i][j - 1]))
                s[i][j] += int(key(matrix[0][j - 1]))
                s[i][j] += int(key(matrix[i - 1][0]))
                s[i][j] += int(key(matrix[i - 1][j - 1]))
                s[i][j] += int(key(matrix[i - 1][j]))
            elif i == y:
                s[i][j] += int(key(matrix[0][j + 1]))
                s[i][j] += int(key(matrix[0][j]))
                s[i][j] += int(key(matrix[i][j + 1]))
                s[i][j] += int(key(matrix[i][j - 1]))
                s[i][j] += int(key(matrix[0][j - 1]))
                s[i][j] += int(key(matrix[i - 1][j + 1]))
                s[i][j] += int(key(matrix[i - 1][j - 1]))
                s[i][j] += int(key(matrix[i - 1][j]))
            elif j == x:
                s[i][j] += int(key(matrix[i + 1][0]))
                s[i][j] += int(key(matrix[i + 1][j]))
                s[i][j] += int(key(matrix[i][0]))
                s[i][j] += int(key(matrix[i][j - 1]))
                s[i][j] += int(key(matrix[i + 1][j - 1]))
                s[i][j] += int(key(matrix[i - 1][0]))
                s[i][j] += int(key(matrix[i - 1][j - 1]))
                s[i][j] += int(key(matrix[i - 1][j]))
            else:
                s[i][j] += int(key(matrix[i + 1][j + 1]))
                s[i][j] += int(key(matrix[i + 1][j]))
                s[i][j] += int(key(matrix[i][j + 1]))
                s[i][j] += int(key(matrix[i][j - 1]))
                s[i][j] += int(key(matrix[i + 1][j - 1]))
                s[i][j] += int(key(matrix[i - 1][j + 1]))
                s[i][j] += int(key(matrix[i - 1][j - 1]))
                s[i][j] += int(key(matrix[i - 1][j]))
            if s[i][j] == 3:
                s[i][j] = 1
            elif s[i][j] == 2 and d[i][j][-1] == 1:
                s[i][j] = 1
            else:
                s[i][j] = 0
            if d[i][j][-1] == s[i][j]:
                pass
            else:
                d[i][j][-1] = s[i][j]
                d[i][j][-2] = 1
            if d[i][j][-2] != 0:
                d[i][j][-1] = d[i][j][-1] % 2
                if d[i][j][-1] == 1:
                    canvas.create_rectangle(d[i][j][0] + 1, d[i][j][1] + 1, d[i][j][2] - 1, d[i][j][3] - 1,
                                            outline="red", fill="red")
                    d[i][j][-2] = 0
                elif d[i][j][-1] == 0:
                    canvas.create_rectangle(d[i][j][0] + 1, d[i][j][1] + 1, d[i][j][2] - 1, d[i][j][3] - 1,
                                            outline="white", fill="white")
                    d[i][j][-2] = 0
    return d


def game_life():
    global d, glag, st
    st = time()
    d = change(d)
    master.after(50, wait)


def show(d):
    for i in range(len(d)):
        for j in range(len(d[i])):
            print(d[i][j][-1], end='')
        print()


st = 0
text = 'pause'
glag = 0


def wait():  # ждёт
    global glag, st
    if time() - st > 1:
        master.destroy()
    print(time() - st)
    if glag == 1:
        game_life()
    else:
        return None


def click(event):  # кнопка мыши
    global d
    if glag == 1:
        return
    x = event.x
    y = event.y
    for i in range(len(d)):
        for j in range(len(d[i])):
            if x > d[i][j][0] and x < d[i][j][2] and y > d[i][j][1] and y < d[i][j][3]:
                d[i][j][-1] += 1
                d[i][j][-2] += 1
    check(d)


def check(d):  # рисует новую матрицу
    global glag
    for i in range(len(d)):
        for j in range(len(d[i])):
            if d[i][j][-2] != 0:
                d[i][j][-1] = d[i][j][-1] % 2
                if d[i][j][-1] == 1:
                    canvas.create_rectangle(d[i][j][0] + 1, d[i][j][1] + 1, d[i][j][2] - 1, d[i][j][3] - 1,
                                            outline="red", fill="red")
                    d[i][j][-2] = 0
                elif d[i][j][-1] == 0:
                    canvas.create_rectangle(d[i][j][0] + 1, d[i][j][1] + 1, d[i][j][2] - 1, d[i][j][3] - 1,
                                            outline="white", fill="white")
                    d[i][j][-2] = 0


def click_button():  # кнопка старт/пауза
    global text, glag, d
    glag += 1
    glag = glag % 2
    if glag == 0:
        text = 'pause'
    else:
        text = 'start'
    btn.configure(text=text)
    if glag == 1:
        game_life()


check(d)
canvas.bind('<Button-1>', click)

btn = tkinter.Button(text=text, background="#555", foreground="#ccc",
                     padx="8", pady="8", font="16", command=click_button)
canvas.create_rectangle(-10, -20, -30, -40, outline='blue', fill='blue')

btn.pack()
canvas.pack()
master.mainloop()
