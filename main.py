import tkinter as tk
import numpy as np


'''
TODO: 
Colour
Redraw
 
'''


def find_next_square(number):  # returns the square root of the next biggest square number
    sqrt = np.sqrt(number)
    next_square = int(np.ceil(sqrt))
    return next_square


class ShapeCanvas(tk.Canvas):
    def __init__(self, master, shape, num_shapes=1, gap_width=10, canvas_size=500):
        super().__init__(master, width=canvas_size, height=canvas_size, borderwidth=0, highlightthickness=0)
        self._shape = shape
        self._shape_border_width = 20
        self._gap_width = gap_width
        self._next_square = find_next_square(num_shapes)
        self._canvas_size = canvas_size
        self._shape_size = (canvas_size / self._next_square) - self._gap_width - self._shape_border_width - ((self._gap_width) / self._next_square)
        self._number_of_shapes = num_shapes
        self._shapes = []

        self.draw_shapes()

        self.fill_shapes_up_to(3)

    def draw_shapes(self):
        shape_count = 0
        for j in range(self._next_square):
            y0 = self._canvas_size - self._gap_width - self._shape_border_width/2 - j * (self._shape_size + self._gap_width + self._shape_border_width)
            y1 = y0 - self._shape_size
            for i in range(self._next_square):
                x0 = self._gap_width + self._shape_border_width/2 + i * (self._shape_size + self._gap_width + self._shape_border_width)
                x1 = x0 + self._shape_size
                if self._shape == "square":
                    shape = self.create_rectangle(x0, y0, x1, y1, outline="black", width=self._shape_border_width,
                                                  fill="")
                else:
                    shape = self.create_oval(x0, y0, x1, y1, outline="black", width=self._shape_border_width,
                                             fill="")
                self._shapes.append(shape)
                shape_count += 1
                if shape_count >= self._number_of_shapes:
                    break
            if shape_count >= self._number_of_shapes:
                break

    def empty_shape(self, shape_number):
        self.itemconfig(shape_number, fill="")

    def empty_shapes_up_to(self, shape_number):
        for i in range(1, shape_number + 1):
            self.empty_shape(i)

    def fill_shape(self, shape_number, colour="black"):
        self.itemconfig(shape_number, fill=colour)

    def fill_shapes_up_to(self, shape_number, colour="black"):
        for i in range(1, shape_number + 1):
            self.fill_shape(i, colour)


class ShapeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shape Canvas")

        self.square_canvas = ShapeCanvas(self, "square", num_shapes=20)
        self.circle_canvas = ShapeCanvas(self, "circle", num_shapes=7)

        self.square_canvas.grid(row=0, column=0)
        self.circle_canvas.grid(row=0, column=1)


if __name__ == "__main__":
    app = ShapeApp()
    app.mainloop()
