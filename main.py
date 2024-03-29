import tkinter as tk
import numpy as np


def find_next_square(number):  # returns the square root of the next biggest square number
    sqrt = np.sqrt(number)
    next_square = int(np.ceil(sqrt))
    return next_square


def find_previous_square(number):  # returns the square root of the next biggest square number
    sqrt = np.sqrt(number)
    previous_square = int(np.floor(sqrt))
    return previous_square


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
        self._filled_shapes = filled if filled >= 0 else 0
        next_square = find_next_square(total)
        self._total_shapes = next_square * next_square
        self._shapes = [0] * self._total_shapes
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
                self._shapes[shape_count] = shape
                shape_count += 1

    def _destroy_shapes(self):
        self.delete("all")

    def get_filled_shape_count(self):
        return self._filled_shapes

    def get_unfilled_shape_count(self):
        return self._unfilled_shapes

    def _empty_shape(self, shape_number):
        self.itemconfig(self._shapes[shape_number - 1], fill="")
        self._filled_shapes -= 1

    def empty_shapes_up_to(self, shape_number):
        if shape_number < self._filled_shapes:
            for i in range(self._filled_shapes, shape_number, -1):
                square_of_next_square = find_next_square(i - 1)**2
                if (self._unfilled_shapes <= square_of_next_square == shape_number > 0) or \
                   (self._total_shapes > square_of_next_square and shape_number > 0):
                    self.draw_shapes(square_of_next_square, self._unfilled_shapes, i - 1)
                else:
                    self._empty_shape(i)

    def empty_shapes_and_colour_final_shape(self, shape_number, colour):
        self.empty_shapes_up_to(shape_number)
        self.colour_latest_filled_shape(colour)

    def _fill_shape(self, shape_number, colour="black"):
        self.itemconfig(self._shapes[shape_number - 1], fill=colour)
        self._filled_shapes += 1

    def colour_latest_filled_shape(self, colour):
        if self._filled_shapes > 0:
            self.itemconfig(self._shapes[self._filled_shapes - 1], fill=colour)

    def fill_shapes_up_to(self, shape_number, colour="black"):
        if shape_number > self._total_shapes:
            if find_next_square(shape_number)**2 > self._total_shapes + 1:
                self.draw_shapes(total=shape_number, filled=shape_number, unfilled=self._unfilled_shapes)
            else:
                self.draw_shapes(total=self._total_shapes + 1, filled=shape_number, unfilled=self._unfilled_shapes)
        else:
            for i in range(1 + self._filled_shapes, shape_number + 1):
                self._fill_shape(i, colour)

    def fill_shapes_and_colour_final_shape(self, shape_number, colour):
        self.colour_latest_filled_shape("black")
        self.fill_shapes_up_to(shape_number)
        self.colour_latest_filled_shape(colour)


class ShapeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shape Canvas")

        self.square_canvas = ShapeCanvas(self, "square")
        self.circle_canvas = ShapeCanvas(self, "circle")

        self.square_canvas.draw_shapes(1, 0, 0)
        self.circle_canvas.draw_shapes(4, 5, 0)

        self.square_canvas.grid(row=0, column=0)
        self.circle_canvas.grid(row=0, column=1)

        for i in range(1, 101):
            self.after(50 * i, self.square_canvas.fill_shapes_and_colour_final_shape, i, "#00008B")

        for i in range(99, -1, -1):
            self.after(5000 + (50 * (100 - i)), self.square_canvas.empty_shapes_and_colour_final_shape, i, "#00008B")

        self.after(2000, self.circle_canvas.fill_shapes_and_colour_final_shape, 2, "#8B0000")
        self.after(4000, self.circle_canvas.fill_shapes_and_colour_final_shape, 5, "#8B0000")
        self.after(6000, self.circle_canvas.fill_shapes_and_colour_final_shape, 6, "#8B0000")
        self.after(8000, self.circle_canvas.fill_shapes_and_colour_final_shape, 16, "#8B0000")
        self.after(10000, self.circle_canvas.fill_shapes_and_colour_final_shape, 17, "#8B0000")
        self.after(12000, self.circle_canvas.empty_shapes_and_colour_final_shape, 7, "#8B0000")


if __name__ == "__main__":
    app = ShapeApp()
    app.mainloop()
