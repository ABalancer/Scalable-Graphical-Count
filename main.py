import tkinter as tk


class ShapeCanvas(tk.Canvas):
    def __init__(self, master, shape, gap_width=5, shape_size=50, num_shapes=5):
        super().__init__(master, width=((shape_size + gap_width) * num_shapes) + gap_width + 1,
                         height=shape_size + (2 * gap_width) + 1,
                         borderwidth=0, highlightthickness=0)
        self.shape = shape
        self.shape_size = shape_size
        self.num_shapes = num_shapes
        self.gap_width = gap_width
        self.shapes = [False] * num_shapes

        self.draw_shapes()

        self.bind("<Button-1>", self.toggle_shape)

    def draw_shapes(self):
        for i in range(self.num_shapes):
            x0 = self.gap_width + i * (self.shape_size + self.gap_width)
            y0 = self.gap_width
            x1 = x0 + self.shape_size
            y1 = y0 + self.shape_size
            if self.shape == "square":
                self.create_rectangle(x0, y0, x1, y1, outline="black", width=3, fill="")
            elif self.shape == "circle":
                self.create_oval(x0, y0, x1, y1, outline="black", width=3, fill="")

    def toggle_shape(self, event):
        index = event.x // self.shape_size
        if index < self.num_shapes:
            self.shapes[index] = not self.shapes[index]
            self.redraw_shapes()

    def redraw_shapes(self):
        self.delete("shape")
        for i, filled in enumerate(self.shapes):
            if filled:
                x0 = self.gap_width + i * (self.shape_size + self.gap_width)
                y0 = self.gap_width
                x1 = x0 + self.shape_size
                y1 = y0 + self.shape_size
                if self.shape == "square":
                    self.create_rectangle(x0, y0, x1, y1, outline="black", width=3, fill="blue", tags="shape")
                elif self.shape == "circle":
                    self.create_oval(x0, y0, x1, y1, outline="black", width=3, fill="blue", tags="shape")


class ShapeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shape Canvas")

        self.square_canvas = ShapeCanvas(self, "square")
        self.circle_canvas = ShapeCanvas(self, "circle")

        self.square_canvas.pack(pady=5)
        self.circle_canvas.pack(pady=5)


if __name__ == "__main__":
    app = ShapeApp()
    app.mainloop()