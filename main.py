import tkinter as tk
import numpy as np


def find_next_square(number):  # returns the square root of the next biggest square number
    sqrt = np.sqrt(number)
    next_square = int(np.ceil(sqrt))
    return next_square


class ShapeCanvas(tk.Canvas):
    def __init__(self, master, shape, gap_width=5, canvas_size=500, num_shapes=11):
        super().__init__(master, width=canvas_size, height=canvas_size, borderwidth=0, highlightthickness=0)
        self.shape = shape
        self.next_square = find_next_square(num_shapes)
        self.canvas_size = canvas_size
        self.shape_size = (canvas_size / self.next_square) - gap_width - (gap_width / self.next_square)
        self.number_of_shapes = num_shapes
        self.gap_width = gap_width
        self.shapes = [False] * num_shapes

        self.draw_shapes()

    def draw_shapes(self):
        shape_count = 0
        for j in range(self.next_square):
            y0 = self.canvas_size - self.gap_width - j * (self.shape_size + self.gap_width)
            y1 = y0 - self.shape_size
            for i in range(self.next_square):
                x0 = self.gap_width + i * (self.shape_size + self.gap_width)
                x1 = x0 + self.shape_size
                if self.shape == "square":
                    self.create_rectangle(x0, y0, x1, y1, outline="black", width=3, fill="")
                elif self.shape == "circle":
                    self.create_oval(x0, y0, x1, y1, outline="black", width=3, fill="")
                shape_count += 1
                if shape_count >= self.number_of_shapes:
                    break
            if shape_count >= self.number_of_shapes:
                break


class ShapeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shape Canvas")

        self.square_canvas = ShapeCanvas(self, "square")
        self.circle_canvas = ShapeCanvas(self, "circle")

        self.square_canvas.grid(row=0, column=0)
        self.circle_canvas.grid(row=0, column=1)


if __name__ == "__main__":
    app = ShapeApp()
    app.mainloop()