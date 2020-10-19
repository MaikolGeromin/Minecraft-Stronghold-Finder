import tkinter as tk
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def convert(self):
        self.y = -self.y


def result_handler():
    try:
        p1 = Point(float(X_A_text.get()), float(Z_A_text.get()))
        p2 = Point(float(X_B_text.get()), float(Z_B_text.get()))
        g1 = float(D_A_text.get())
        g2 = float(D_B_text.get())

        p1.convert()
        p2.convert()

        # from degrees (Minecraft) to slope
        s1 = 1 / (np.tan(g1 * np.pi / 180))
        s2 = 1 / (np.tan(g2 * np.pi / 180))

        q1 = p1.y - p1.x * s1
        q2 = p2.y - p2.x * s2

        xd = (q1 - q2) / (s2 - s1)
        yd = s1 * xd + q1

        pd = Point(xd, yd)
        pd.convert()  # now these are the coords for the stronghold

        result = "Result: X = " + str(int(pd.x)) + ",   Z = " + str(int(pd.y))
        lbl_result["text"] = f"{result}"

    except:
        result = "An error has occurred"
        lbl_result["text"] = f"{result}"


def reset():
    X_A_text.delete(0, tk.END)
    Z_A_text.delete(0, tk.END)
    D_A_text.delete(0, tk.END)
    X_B_text.delete(0, tk.END)
    Z_B_text.delete(0, tk.END)
    D_B_text.delete(0, tk.END)


window = tk.Tk()
window.title("Stronghold finder")

window.columnconfigure(0, weight=1, minsize=200)
window.rowconfigure([0, 1], weight=1, minsize=75)


frame_points = tk.Frame(master=window, width=200, height=100)
frame_points.grid(row=0, column=0)

frame_result = tk.Frame(master=window, width=400, height=200)
frame_result.grid(row=1, column=0)

frame_A = tk.Frame(master=frame_points, padx=20, pady=20)
frame_B = tk.Frame(master=frame_points, padx=20, pady=20)

frame_A.grid(row=0, column=0)
frame_B.grid(row=0, column=1)

lbl_A = tk.Label(master=frame_A, text="Point A", font=("Helvetica", "12"), pady=10)
lbl_A.grid(row=0, column=0, sticky=tk.W)

label_X_A = tk.Label(master=frame_A, text="X coord")
label_X_A.grid(row=1, column=0, sticky=tk.W)

label_Z_A = tk.Label(master=frame_A, text="Z coord")
label_Z_A.grid(row=2, column=0, sticky=tk.W)

direction_A = tk.Label(master=frame_A, text="Direction")
direction_A.grid(row=3, column=0, sticky=tk.W)

X_A_text = tk.Entry(master=frame_A, width=15)
X_A_text.grid(row=1, column=1)

Z_A_text = tk.Entry(master=frame_A, width=15)
Z_A_text.grid(row=2, column=1)

D_A_text = tk.Entry(master=frame_A, width=15)
D_A_text.grid(row=3, column=1)


lbl_B = tk.Label(master=frame_B, text="Point B", font=("Helvetica", "12"), pady=10)
lbl_B.grid(row=0, column=0, sticky=tk.W)

label_X_B = tk.Label(master=frame_B, text="X coord")
label_X_B.grid(row=1, column=0, sticky=tk.W)

label_Z_B = tk.Label(master=frame_B, text="Z coord")
label_Z_B.grid(row=2, column=0, sticky=tk.W)

direction_B = tk.Label(master=frame_B, text="Direction")
direction_B.grid(row=3, column=0, sticky=tk.W)

X_B_text = tk.Entry(master=frame_B, width=15)
X_B_text.grid(row=1, column=1)

Z_B_text = tk.Entry(master=frame_B, width=15)
Z_B_text.grid(row=2, column=1)

D_B_text = tk.Entry(master=frame_B, width=15)
D_B_text.grid(row=3, column=1)


btn_calc = tk.Button(master=frame_result,
                     text="calculate",
                     padx=10, pady=10,
                     command=lambda: result_handler())
btn_calc.grid(row=0, column=1)

btn_reset = tk.Button(master=frame_result,
                      text="reset",
                      padx=10, pady=10,
                      command=lambda: reset())
btn_reset.grid(row=0, column=0)

lbl_result = tk.Label(master=frame_result,
                      text="Result:",
                      pady=10,)
lbl_result.grid(row=1, column=0, sticky=tk.W, rowspan=2)


window.mainloop()


