from manim import *

class Polygon(Polygon):
    def get_center_of_edges(self, buff=SMALL_BUFF * 3):
        vertices = self.get_vertices()
        coords_vertices = []
        for i in range(len(vertices)):
            if i < len(vertices) - 1:
                p1, p2 = [vertices[i], vertices[i + 1]]
            else:
                p1, p2 = [vertices[-1], vertices[0]]
            guide_line = Line(p1, p2)
            side = guide_line.get_center()
            normal_direction = guide_line.copy()
            normal_direction.rotate(-PI / 2)
            vector_normal_direction = normal_direction.get_unit_vector()
            direction = Dot(side).shift(vector_normal_direction * buff).get_center()
            coords_vertices.append(direction)

        return coords_vertices

