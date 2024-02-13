import tkinter as tk
import numpy as np

'''
TODO: 
Colour
 
'''


def find_next_square(number):  # returns the square root of the next biggest square number
    sqrt = np.sqrt(number)
    next_square = int(np.ceil(sqrt))
    return next_square


class ShapeCanvas(tk.Canvas):
    def __init__(self, master, shape, canvas_size=500, gap_width=15, border_width=15):
        super().__init__(master, width=canvas_size, height=canvas_size, borderwidth=0, highlightthickness=0)
        self._total_shapes = 0
        self._unfilled_shapes = 0
        self._filled_shapes = 0
        self._shape = shape
        self._shape_border_width = border_width
        self._gap_width = gap_width
        self._canvas_size = canvas_size
        self._shapes = []

    def draw_shapes(self, total, unfilled=0, filled=0):
        self._destroy_shapes()
        self._unfilled_shapes = unfilled
        self._filled_shapes = filled
        next_square = find_next_square(total)
        self._total_shapes = next_square
        shape_size = (self._canvas_size / next_square) - self._gap_width - self._shape_border_width - \
                     (self._gap_width / next_square)
        shape_count = 0
        outline = "black"
        fill = "black"
        for j in range(next_square):
            y0 = self._canvas_size - self._gap_width - self._shape_border_width / 2 - \
                 j * (shape_size + self._gap_width + self._shape_border_width)
            y1 = y0 - shape_size
            for i in range(next_square):
                if shape_count >= filled:
                    fill = ""
                if shape_count >= unfilled:
                    outline = ""
                x0 = self._gap_width + self._shape_border_width / 2 + \
                     i * (shape_size + self._gap_width + self._shape_border_width)
                x1 = x0 + shape_size
                if self._shape == "square":
                    shape = self.create_rectangle(x0, y0, x1, y1, outline=outline, width=self._shape_border_width,
                                                  fill=fill)
                else:
                    shape = self.create_oval(x0, y0, x1, y1, outline=outline, width=self._shape_border_width,
                                             fill=fill)
                self._shapes.append(shape)
                shape_count += 1

    def _destroy_shapes(self):
        if self._shapes:
            for shape in self._shapes:
                self.delete(shape)
            self._shapes = []

    def get_filled_shape_count(self):
        return self._filled_shapes

    def get_unfilled_shape_count(self):
        return self._unfilled_shapes

    def empty_shape(self, shape_number):
        self.itemconfig(shape_number, fill="")

    def empty_shapes_up_to(self, shape_number):
        for i in range(1, shape_number + 1):
            self.empty_shape(i)

    def fill_shape(self, shape_number, colour="black"):
        self.itemconfig(shape_number, fill=colour)

    def fill_shapes_up_to(self, shape_number, colour="black"):
        current_total = self._shapes[-1]
        if shape_number > current_total:
            self.draw_shapes(total=current_total + 1, filled=shape_number, unfilled=self._unfilled_shapes)
        else:
            for i in range(1, shape_number + 1):
                self.fill_shape(i, colour)


class ShapeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shape Canvas")

        self.square_canvas = ShapeCanvas(self, "square")
        self.circle_canvas = ShapeCanvas(self, "circle")

        self.square_canvas.draw_shapes(25, 14, 3)
        self.circle_canvas.draw_shapes(9, 7, 3)

        self.square_canvas.grid(row=0, column=0)
        self.circle_canvas.grid(row=0, column=1)

        self.after(2000, self.square_canvas.fill_shapes_up_to, 14)
        self.after(4000, self.square_canvas.fill_shapes_up_to, 29)

        self.after(2000, self.circle_canvas.fill_shapes_up_to, 9)
        self.after(4000, self.circle_canvas.fill_shapes_up_to, 15)


if __name__ == "__main__":
    app = ShapeApp()
    app.mainloop()
