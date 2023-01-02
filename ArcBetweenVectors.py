from manim import *


class ArcBetweenVectors(Arc):
    def __init__(self, radius, d1, d2, center, invert_angle=False, **kwargs):
        line1 = Line(center.get_center(), d1.get_center())
        line2 = Line(center.get_center(), d2.get_center())
        h = Line(center.get_center(), center.get_center() + RIGHT)
        angle = angle_between_vectors(line1.get_unit_vector(), line2.get_unit_vector())
        h1 = angle_between_vectors(h.get_unit_vector(), line1.get_unit_vector())
        h2 = angle_between_vectors(h.get_unit_vector(), line2.get_unit_vector())
        if line1.get_angle() <= line2.get_angle():
            start_angle = h1
        else:
            start_angle = h2
        if invert_angle:
            start_angle = -start_angle
        super().__init__(start_angle=start_angle, angle=angle, radius=radius, arc_center=center.get_center(), **kwargs)

    def get_angle(self):
        return self.angle

