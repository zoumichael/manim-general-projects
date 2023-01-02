from manim import *

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
        "line_kwargs": {}
    }

    def __init__(self, rows, columns, **kwargs):
        #digest_config(self, kwargs, locals())
        self.rows = rows
        self.columns = columns
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(DashedLine(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
                **self.line_kwargs
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(DashedLine(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0],
                **self.line_kwargs
            ))

