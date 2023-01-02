from manim import *

inner_line_config = PURPLE_A
outer_line_config = TEAL_A
inner_arc_config = PURPLE_A
outer_arc_config = TEAL_A
tex_1_config = TEAL_A
tex_2_config = PURPLE_A

class CircleWithAngles(VGroup):
    CONFIG = {
        "inner_line_config": {"color": PURPLE_A},
        "outer_line_config": {"color": TEAL_A},
        "inner_arc_config": {"color": PURPLE_A},
        "outer_arc_config": {"color": TEAL_A},
        "tex_1_config": {"color": TEAL_A},
        "tex_2_config": {"color": PURPLE_A},
    }

    def __init__(self, radius=3, ang1=30, ang2=130, ang3=260, small_radius=0.4, **kwargs):
        #digest_config(self, kwargs)
        super().__init__(**kwargs)


        circle = Circle(radius=radius)
        vt_1 = ValueTracker(ang1)
        vt_2 = ValueTracker(ang2)
        vt_3 = ValueTracker(ang3)
        p1 = Dot(circle.point_at_angle(ang1 * DEGREES))
        p2 = Dot(circle.point_at_angle(ang2 * DEGREES))
        p3 = Dot(circle.point_at_angle(ang3 * DEGREES))
        in_lines = VMobject(inner_line_config)
        # ------------- LINES
        out_lines = VMobject(outer_line_config)
        # ------------- ANGLES
        out_arc = self.get_arc_between_lines(small_radius, p1, p2, p3)
        in_arc = self.get_inner_angle(small_radius, p1, p2, p3, circle)
        # ------------- LABELS
        theta_2 = Tex("$2\\theta$", fill_color=tex_2_config)
        theta_1 = Tex("$\\theta$", fill_color=tex_1_config)
        # ------------- Equals
        theta_1_val = DecimalNumber(number=0, unit="deg", num_decimal_places=3, fill_color=tex_1_config)
        theta_2_val = DecimalNumber(number=0, unit="deg", num_decimal_places=3, fill_color=tex_2_config)
        # theta_1_val = DecimalTextNumber(number=0, unit="deg", num_decimal_places=3, fill_color=tex_1_config)
        # theta_2_val = DecimalTextNumber(number=0, unit="deg", num_decimal_places=3, fill_color=tex_2_config)
        equal = Text("= 2 * ", font="Digital-7")
        theta_eq = VGroup(theta_1_val, equal, theta_2_val)
        theta_eq_temp = VGroup(theta_1_val, equal, theta_2_val)
        theta_eq.arrange(RIGHT, buff=0.6, aligned_edge=DOWN)
        theta_2_val.shift(LEFT * max(*[f.get_width() for f in theta_2_val]) * 1)
        rectangle = Rectangle(width=theta_eq.get_width() + 0.2, height=theta_eq.get_height() + 0.2)
        rectangle.move_to(theta_eq)
        theta_eq.add(rectangle)
        # UPDATERS
        p1.add_updater(lambda mob: mob.move_to(circle.point_at_angle(vt_1.get_value() * DEGREES)))
        p2.add_updater(lambda mob: mob.move_to(circle.point_at_angle(vt_2.get_value() * DEGREES)))
        p3.add_updater(lambda mob: mob.move_to(circle.point_at_angle(vt_3.get_value() * DEGREES)))
        in_lines.add_updater(lambda mob: mob.set_points_as_corners([
            p1.get_center(), circle.get_center(), p2.get_center()
        ]))
        out_lines.add_updater(lambda mob: mob.set_points_as_corners([
            p1.get_center(), p3.get_center(), p2.get_center()
        ]))
        out_arc.add_updater(lambda mob: mob.become(self.get_arc_between_lines(small_radius, p1, p2, p3)))
        in_arc.add_updater(lambda mob: mob.become(self.get_inner_angle(small_radius, p1, p2, p3, circle)))
        theta_1.add_updater(
            lambda mob: mob.move_to(
                p3.get_center() + Line(p3.get_center(), out_arc.point_from_proportion(0.5)).get_vector() * 1.7)
        )
        theta_2.add_updater(
            lambda mob: mob.move_to(
                circle.get_center() + Line(circle.get_center(), in_arc.point_from_proportion(0.5)).get_vector() * 1.7)
        )
        theta_1_val.add_updater(
            lambda mob: mob.set_value(self.get_inner_angle(1, p1, p2, p3, circle, False) * 180 / PI))
        theta_2_val.add_updater(lambda mob: mob.set_value(self.get_arc_between_lines(1, p1, p2, p3, False) * 180 / PI))
        rectangle.max_width = rectangle.get_width()

        def rect_up(mob):
            line = Line(theta_eq_temp.get_left() + LEFT * 0.2, theta_eq_temp.get_right() + RIGHT * 0.2)
            if line.get_width() > mob.max_width:
                mob.max_width = line.get_width()
            mob.set_width(mob.max_width)
            # mob.move_to(line)
            mob.align_to(theta_1_val, LEFT)
            mob.shift(LEFT * 0.1)

        rectangle.add_updater(rect_up)
        # ------------- Groups
        dots = VGroup(p1, p2, p3)
        vts = Group(vt_1, vt_2, vt_3)
        self.vts = vts
        self.add(
            circle, dots,
            in_lines, out_lines,
            in_arc, out_arc,
            theta_1, theta_2,
            theta_eq,
        )

    def get_arc_between_lines(self, radius, d1, d2, center, mob=True):
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
        arc = Arc(start_angle=start_angle, angle=angle, radius=radius, arc_center=center.get_center(), stroke_color=outer_arc_config)
        if mob:
            return arc
        else:
            return angle

    def get_inner_angle(self, radius, d1, d2, out_center, in_center, mob=True):
        line1 = Line(out_center.get_center(), d1.get_center())
        line2 = Line(out_center.get_center(), d2.get_center())
        h = Line(out_center.get_center(), out_center.get_center() + RIGHT)
        angle = angle_between_vectors(line1.get_unit_vector(), line2.get_unit_vector())
        v1 = Line(in_center.get_center(), d1.get_center())
        start_angle = angle_between_vectors(h.get_unit_vector(), v1.get_unit_vector())
        arc = Arc(start_angle=start_angle, angle=angle * 2, radius=radius, arc_center=in_center.get_center(), stroke_color=inner_arc_config)
        if mob:
            return arc
        else:
            return angle * 2
