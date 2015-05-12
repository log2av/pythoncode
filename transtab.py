from Tkinter import *

master = Tk()
w = Canvas(master, width=200, height=100)
w.pack()
a=[20,30,40,20,40,30,52,75,67,100]
b=[10,20,50,23,78,45,29,111,88,99]
for x in range(1,9):
    w.create_line(int(a[x]), int(b[x]), int(a[x+1]), int(b[x+1]))
#w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
#w.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()