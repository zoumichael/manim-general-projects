
from manim import *

class Sqrt2(VGroup):
    def __init__(self, n, **kwargs):
        super().__init__(**kwargs)
        body = Tex("\\frac{\\sqrt{%s}}{2}" % n)[0]
        number = body[2]
        self.top = body[:3]
        body.remove(body[2])
        self.add(body, number)