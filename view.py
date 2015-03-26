from tkinter import *
import math


class View:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cellWidth = 20     # px
        self.lineColor = "#000000"
        self.lineWidth = 2
        self.backgroundColor = "#FFFFFF"
        self.markSize = 0.5
        self.markWidth = 3
        self.playerColors = ["#FF0000", "#0000FF"];
        self.width = self.cols * self.cellWidth + (self.cols - 1) * self.lineWidth
        self.height = self.rows * self.cellWidth + (self.rows - 1) * self.lineWidth
        self.top = 50;
        self.master = Tk()
        self.canvas = Canvas(self.master, width=self.width, height=self.height+self.top)
        self.canvas.pack()
        self.canvas.bind('<Button>', self.click)

        self.controller_click = lambda x : 0

    def click(self, event):
        x = event.x
        y = event.y - self.top
        x = math.floor(x / (self.cellWidth + self.lineWidth))
        y = math.floor(y / (self.cellWidth + self.lineWidth))

        print(x)
        print(y)
        if hasattr(self.controller_click, '__call__'):
            try:
                self.controller_click(x, y, 1)
            finally:
                pass

    def set_callback(self, func):
        self.controller_click = func

    def render(self, data):
        self.render_background()
        self.render_grid()

        for x in range(0, len(data)):
            for y in range(0, len(data[x])):
                if data[x][y] != 0:
                    self.render_mark(x, y, data[x][y])

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

    def render_mark(self, u, v, type):
        x = (u) * (self.cellWidth + self.lineWidth) + self.cellWidth / 2;
        y = self.top + (v) * (self.cellWidth + self.lineWidth) + self.cellWidth / 2;

        if(type == 1):
            self.canvas.create_line(x - self.markSize / 2 * self.cellWidth, y - self.markSize / 2 * self.cellWidth, x + self.markSize / 2 * self.cellWidth, y + self.markSize / 2 * self.cellWidth, fill=self.playerColors[type - 1], width=self.markWidth)
            self.canvas.create_line(x + self.markSize / 2 * self.cellWidth, y - self.markSize / 2 * self.cellWidth, x - self.markSize / 2 * self.cellWidth, y + self.markSize / 2 * self.cellWidth, fill=self.playerColors[type - 1], width=self.markWidth)
        else:
            self.canvas.create_oval(x - self.markSize / 2 * self.cellWidth, y - self.markSize / 2 * self.cellWidth, x + self.markSize / 2 * self.cellWidth, y + self.markSize / 2 * self.cellWidth, outline=self.playerColors[type - 1], width=self.markWidth)