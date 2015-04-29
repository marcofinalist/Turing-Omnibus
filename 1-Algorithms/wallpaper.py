#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack()

        self.refresh = tk.Button(self)
        self.refresh['command'] = self.draw
        self.refresh['text'] = 'Refresh'
        self.refresh.pack()

        self.input = tk.Entry()
        self.value = tk.IntVar()
        self.value.set(100)
        self.input['textvariable'] = self.value
        self.input.pack()


    def draw(self):
        self.canvas.delete("all")
        corna, cornb, side = 0, 0, self.value.get()

        for i in range(0, 100):
            for j in range(0, 100):
                x = corna + i * side / 100.0
                y = cornb + j * side / 100.0
                c = int(x * x + y * y)

                if c % 3 == 0:
                    self.draw_pixel(canvas=self.canvas, x=x+corna, y=y+cornb, fill='')
                elif c % 3 == 1:
                    self.draw_pixel(canvas=self.canvas, x=x+corna, y=y+cornb, fill='gray')
                elif c % 3 == 2:
                    self.draw_pixel(canvas=self.canvas, x=x+corna, y=y+cornb, fill='black')

    def draw_pixel(self, canvas, x, y, fill):
        outline = ''
        factor = 5
        x *= factor
        y *= factor
        canvas.create_rectangle(x, y, x+factor, y+factor, fill=fill, outline=outline)

root = tk.Tk()
app = Application(master=root)
app.mainloop()