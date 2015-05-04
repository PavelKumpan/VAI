from tkinter import *
from tkinter import messagebox
import math

'''
View.py
------

This module is used to render graphical user interface.
'''

class View:
    cellWidth = 30                          # pixel width of grid cell
    lineColor = "#000000"                   # color of grid line
    lineWidth = 1                           # pixel width of grid line (this width is ad to cellWidth)
    backgroundColor = "#FFFFFF"             # color of window background
    markSize = 0.5                          # width of mark in % of cell (0.5 = half of cell)
    markLineWidth = 3                       # width of mark line
    playerColors = ["#FF0000", "#0000FF"]   # colors of player marks
    top = 0

    player = 1

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.width = self.cols * self.cellWidth + (self.cols - 1) * self.lineWidth
        self.height = self.rows * self.cellWidth + (self.rows - 1) * self.lineWidth
        self.player = 1
        self.master = Tk()
        self.master.title('Pišqorky { Pavel Kumpán | 144902 | 4oMET }')
        self.controller_click = lambda x : 0

    def update(self):
        self.master.update()

    def start(self):
        self.player = 2 - messagebox.askyesno('Pišqorky', 'Vítejte v pišqorkách, chcete hrát hrát za křížky?')

        if self.player == 2:
            self.controller_click(None, None, self.player)

    def end(self):
        return not messagebox.askyesno('Pišqorky', 'Chcete hrát znovu?')

    def create_canvas(self):
        self.canvas = Canvas(self.master, width=self.width, height=self.height+self.top)
        self.canvas.pack()
        self.canvas.bind('<Button>', self.click)

    def click(self, event):
        col = event.x // (self.cellWidth + self.lineWidth)
        row = (event.y - self.top) // (self.cellWidth + self.lineWidth)

        if hasattr(self.controller_click, '__call__'):
            try:
                self.controller_click(row, col, self.player)
            finally:
                pass

    def set_callback(self, func):
        self.controller_click = func

    def close(self):
        del self.canvas

    def clear(self):
        self.render_background()
        self.render_grid()

    def render(self, data, cost, five):
        self.clear()

        for row in range(0, len(data)):
            for col in range(0, len(data[0])):
                if data[row][col] != 0:
                    self.render_mark(row, col, data[row][col])
           #     self.canvas.create_text(col * (self.cellWidth + self.lineWidth) + self.cellWidth / 2, self.top + (row) * (self.cellWidth + self.lineWidth) + self.cellWidth / 2, text=str(round(cost[row][col] * 100)))

        if len(five) != 0:
            x_prev = five[0][1] * (self.cellWidth + self.lineWidth) + self.cellWidth / 2
            y_prev = five[0][0] * (self.cellWidth + self.lineWidth) + self.cellWidth / 2
            for i in range(1, len(five)):
                x = five[i][1] * (self.cellWidth + self.lineWidth) + self.cellWidth / 2
                y = five[i][0] * (self.cellWidth + self.lineWidth) + self.cellWidth / 2
                self.canvas.create_line(x_prev, y_prev, x, y, fill="#000000", width=2)
                x_prev = x
                y_prev = y

        self.master.update()

    def c(self):
        mainloop()

    def render_background(self):
        self.canvas.create_rectangle(0, self.top, self.width, self.height + self.top, fill=self.backgroundColor, width=0)

    def render_grid(self):
        for i in range(1, self.cols):
            x = i * (self.cellWidth + self.lineWidth)
            self.canvas.create_line(x, self.top, x, self.height + self.top, fill=self.lineColor, width=self.lineWidth)

        for i in range(1, self.rows):
            y = self.top + i * (self.cellWidth + self.lineWidth)
            self.canvas.create_line(0, y, self.width, y, fill=self.lineColor, width=self.lineWidth)

    def render_mark(self, row, col, type):
        x = (col) * (self.cellWidth + self.lineWidth) + self.cellWidth / 2;
        y = self.top + (row) * (self.cellWidth + self.lineWidth) + self.cellWidth / 2;

        if(type == 1):
            self.canvas.create_line(x - self.markSize / 2 * self.cellWidth, y - self.markSize / 2 * self.cellWidth, x + self.markSize / 2 * self.cellWidth, y + self.markSize / 2 * self.cellWidth, fill=self.playerColors[type - 1], width=self.markLineWidth)
            self.canvas.create_line(x + self.markSize / 2 * self.cellWidth, y - self.markSize / 2 * self.cellWidth, x - self.markSize / 2 * self.cellWidth, y + self.markSize / 2 * self.cellWidth, fill=self.playerColors[type - 1], width=self.markLineWidth)
        else:
            self.canvas.create_oval(x - self.markSize / 2 * self.cellWidth, y - self.markSize / 2 * self.cellWidth, x + self.markSize / 2 * self.cellWidth, y + self.markSize / 2 * self.cellWidth, outline=self.playerColors[type - 1], width=self.markLineWidth)