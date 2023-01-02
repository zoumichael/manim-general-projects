from manim import *

class LabelFromArc(Tex):
    '''
    CONFIG = {
        "distance_proportion": 1.2
    }
    '''

    def __init__(self, arc, tex_height,  *tex_strings, distance_proportion=1.2, **kwargs):
        super().__init__(*tex_strings, **kwargs)
        self.set_height(tex_height)
        center = arc.get_arc_center()

        self.distance_proportion = distance_proportion
        max_size = max(self.get_width(), self.get_height()) * self.distance_proportion / 2
        vector = Line(center, arc.point_from_proportion(0.5)).get_vector()
        end_coord = center + vector + normalize(vector) * max_size
        self.move_to(end_coord)
        self.__dict__.update(kwargs)
