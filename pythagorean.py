from re import A
from typing import final
from manim import *
from math import sin, cos, atan, sqrt

class pythagorean(Scene):
    def construct(self):
        # Variables for scaling/moving the image.
        scale = 2
        x_shift = 0.0
        y_shift = -1.75
        rangle_size = 0.2
        angle_size = 0.4
        angle_size_2 = 0.5

        initial_equation_coor = LEFT * 6 + UP * 2
        equation_font_size = 32

        os_coor = [
            ORIGIN * scale + UP * y_shift + RIGHT * x_shift,                    # Lower Left (A)
            (RIGHT * 2) * scale + UP * y_shift + RIGHT * x_shift,               # Lower Right (B)
            (UP * 2) * scale + UP * y_shift + RIGHT * x_shift,                  # Upper Left (D)
            (UP * 2 + RIGHT * 2) * scale + UP * y_shift + RIGHT * x_shift       # Upper Right (E)
        ]
        is_coor = [
            (UP / 2 + RIGHT * sqrt(3) / 2) * scale + UP * y_shift + RIGHT * x_shift,            # Bottom
            (UP * (2 - sqrt(3) / 2) + RIGHT / 2) * scale + UP * y_shift + RIGHT * x_shift,      # Left
            (3 / 2 * UP + (2 - sqrt(3) / 2) * RIGHT) * scale + UP *  y_shift + RIGHT * x_shift,  # Up
            (sqrt(3) / 2 * UP + 3 / 2 * RIGHT) * scale + UP * y_shift + RIGHT * x_shift         # Right (C)
        ]

        # Lines of the triangle

        tri_line = [
            Line(os_coor[1], is_coor[3]),
            Line(is_coor[3], os_coor[0]),
            Line(os_coor[0], os_coor[1])
        ]

        rangle = RightAngle(tri_line[0], tri_line[1], length=rangle_size, quadrant=(-1, 1))

        os_line = [
            Line(os_coor[1], os_coor[3], color=RED),  # RIGHT
            Line(os_coor[3], os_coor[2], color=RED),  # UP
            Line(os_coor[2], os_coor[0], color=RED)   # LEFT
        ]

        squ_rangle = [
            RightAngle(tri_line[2], os_line[0], length=rangle_size, quadrant=(-1, 1), color=RED),
            RightAngle(os_line[0], os_line[1], length=rangle_size, quadrant=(-1, 1), color=RED),
            RightAngle(os_line[1], os_line[2], length=rangle_size, quadrant=(-1, 1), color=RED),
            RightAngle(os_line[2], tri_line[2], length=rangle_size, quadrant=(-1, 1), color=RED),
        ]

        extra_lines = [
            Line(os_coor[2], is_coor[0], color=RED_E),
            Line(os_coor[3], is_coor[1], color=RED_E),
            Line(is_coor[3], is_coor[2], color=RED_E)
        ]

        extra_rangle = [
            RightAngle(extra_lines[0], tri_line[1], length=rangle_size, quadrant=(-1, 1), color=RED),
            RightAngle(extra_lines[1], extra_lines[0], length=rangle_size, quadrant=(-1, -1), color=RED),
            RightAngle(extra_lines[2], extra_lines[1], length=rangle_size, quadrant=(-1, -1), color=RED)
        ]

        theta = Angle(tri_line[2], tri_line[1], radius=angle_size, quadrant=(1, -1), color=YELLOW)
        ninty_theta = Angle(tri_line[0], tri_line[2], radius=angle_size_2, quadrant=(1, -1), color=BLUE)

        extra_theta = [
            Angle(os_line[0], tri_line[0], radius=angle_size, quadrant=(1, 1), color=YELLOW),
            Angle(os_line[1], extra_lines[1], radius=angle_size, quadrant=(1, 1), color=YELLOW),
            Angle(os_line[2], extra_lines[0], radius=angle_size, quadrant=(1, 1), color=YELLOW)
        ]

        extra_ninty_theta = [
            Angle(extra_lines[1], os_line[0], radius=angle_size_2, quadrant=(1, -1), color=BLUE),
            Angle(extra_lines[0], os_line[1], radius=angle_size_2, quadrant=(1, -1), color=BLUE),
            Angle(tri_line[1], os_line[2], radius=angle_size_2, quadrant=(-1, -1), color=BLUE)
        ]

        side_font_size = 24
        tri_line_tex = [
            MathTex("a", font_size=side_font_size),
            MathTex("b", font_size=side_font_size),
            MathTex("c", font_size=side_font_size)
        ]
        point_font_size = 24
        tri_point_tex = [ 
            MathTex("A", font_size=point_font_size),
            MathTex("B", font_size=point_font_size),
            MathTex("C", font_size=point_font_size)
        ]
        tri_point_tex[0].next_to(os_coor[0], DL, buff=SMALL_BUFF)
        tri_point_tex[1].next_to(os_coor[1], DR, buff=SMALL_BUFF)
        tri_point_tex[2].next_to(is_coor[3], RIGHT, buff=SMALL_BUFF)
        os_point_tex = [
            MathTex("D", font_size=point_font_size),
            MathTex("E", font_size=point_font_size) 
        ]
        os_point_tex[0].next_to(os_coor[3], UR, buff=SMALL_BUFF)
        os_point_tex[1].next_to(os_coor[2], UL, buff=SMALL_BUFF)
        is_point_tex = [ 
            MathTex("F", font_size=point_font_size),
            MathTex("G", font_size=point_font_size),
            MathTex("H", font_size=point_font_size)
        ]
        is_point_tex[0].next_to(is_coor[0], DOWN, buff=SMALL_BUFF)
        is_point_tex[1].next_to(is_coor[1], LEFT, buff=SMALL_BUFF)
        is_point_tex[2].next_to(is_coor[2], UP, buff=SMALL_BUFF)
        os_line_tex = [
            MathTex("c", font_size=side_font_size),
            MathTex("c", font_size=side_font_size),
            MathTex("c", font_size=side_font_size)
        ]
        for i in range(3):
            tri_line_tex[i].shift(tri_line[i].get_center())
            guide_line = tri_line[i].copy()
            guide_line.rotate(-PI/2)
            vector_normal = guide_line.get_unit_vector()
            tri_line_tex[i].shift(vector_normal * 0.2)

            os_line_tex[i].shift(os_line[i].get_center())
            guide_line = os_line[i].copy()
            guide_line.rotate(-PI/2)
            vector_normal = guide_line.get_unit_vector()
            os_line_tex[i].shift(vector_normal * 0.2)

        theta_font_size = 32
        theta_distance = 0.7
        theta_tex = [
            MathTex("\\theta", font_size=theta_font_size, color=YELLOW),
            MathTex("\\theta", font_size=theta_font_size, color=YELLOW),
            MathTex("\\theta", font_size=theta_font_size, color=YELLOW),
            MathTex("\\theta", font_size=theta_font_size, color=YELLOW) 
        ]
        for i in range(4):
            theta_tex[i].shift(os_coor[i])
        theta_tex[0].shift((sin(PI/12) * UP + cos(PI/12) * RIGHT) * theta_distance)
        theta_tex[1].shift((sin(PI/12) * LEFT + cos(PI/12) * UP) * theta_distance)
        theta_tex[2].shift((sin(PI/12) * RIGHT + cos(PI/12) * DOWN) * theta_distance)
        theta_tex[3].shift((sin(PI/12) * DOWN + cos(PI/12) * LEFT) * theta_distance)
        theta_90_font_size = 32
        theta_90_distance = 1.0
        theta_90_tex = [ 
            MathTex(r"{\pi \over 2}", r"- \theta", font_size=theta_90_font_size, color=BLUE),
            MathTex(r"{\pi \over 2}", r"- \theta", font_size=theta_90_font_size, color=BLUE),
            MathTex(r"{\pi \over 2}", r"- \theta", font_size=theta_90_font_size, color=BLUE),
            MathTex(r"{\pi \over 2}", r"- \theta", font_size=theta_90_font_size, color=BLUE)
        ]
        for i in range(4):
            theta_90_tex[i].shift(os_coor[i])
        theta_90_tex[0].shift((sin(PI/6) * RIGHT + cos(PI/6) * UP) * theta_90_distance)
        theta_90_tex[1].shift((sin(PI/6) * UP + cos(PI/6) * LEFT) * theta_90_distance)
        theta_90_tex[2].shift((sin(PI/6) * DOWN + cos(PI/6) * RIGHT) * theta_90_distance)
        theta_90_tex[3].shift((sin(PI/6) * LEFT + cos(PI/6) * DOWN) * theta_90_distance)

        congruent_triangles_equation = [ 
            MathTex(r"\Delta ABC", font_size=equation_font_size).set_color(YELLOW),
            MathTex(r"\cong", font_size=equation_font_size),
            MathTex(r"\Delta BDH", font_size=equation_font_size).set_color(BLUE),
            MathTex(r"\cong", font_size=equation_font_size),
            MathTex(r"\Delta DEG", font_size=equation_font_size).set_color(GREEN),
            MathTex(r"\cong", font_size=equation_font_size),
            MathTex(r"\Delta EAF", font_size=equation_font_size).set_color(PURPLE)
        ]

        for i in range(7):
            if i == 0:
                congruent_triangles_equation[i].shift(initial_equation_coor)
            elif i > 0:
                congruent_triangles_equation[i].next_to(congruent_triangles_equation[i-1], RIGHT, buff=SMALL_BUFF)

        triangles = [ 
            Polygon(os_coor[0], os_coor[1], is_coor[3]),
            Polygon(os_coor[1], os_coor[3], is_coor[2]),
            Polygon(os_coor[3], os_coor[2], is_coor[1]),
            Polygon(os_coor[2], os_coor[0], is_coor[0])
        ]
        for poly in triangles:
            poly.set_stroke(BLUE, width=0.0)
        triangles[0].set_fill(YELLOW, opacity=0.5)
        triangles[1].set_fill(BLUE, opacity=0.5)
        triangles[2].set_fill(GREEN, opacity=0.5)
        triangles[3].set_fill(PURPLE, opacity=0.5)

        Line_AF = Line(os_coor[0], is_coor[0], color=PURPLE)
        Line_AF_tex = MathTex(r"a", font_size=side_font_size)
        Line_AF_tex.shift(Line_AF.get_center())
        guide_line = Line_AF.copy()
        guide_line.rotate(-PI/2)
        vector_normal = guide_line.get_unit_vector()
        Line_AF_tex.shift(vector_normal * 0.3)

        Line_FC = Line(is_coor[0], is_coor[3], color=RED)
        Line_FC_tex = MathTex(r"b-a", font_size=side_font_size)
        Line_FC_tex.shift(Line_FC.get_center())
        guide_line = Line_FC.copy()
        guide_line.rotate(-PI/2)
        vector_normal = guide_line.get_unit_vector()
        Line_FC_tex.shift(vector_normal * 0.3)

        o_square = Polygon(os_coor[0], os_coor[1], os_coor[3], os_coor[2])
        o_square.set_fill(RED, opacity=0.5)
        o_square.set_stroke(BLUE, width=0.0)
        i_square = Polygon(is_coor[0], is_coor[1], is_coor[2], is_coor[3])
        i_square.set_fill(PINK, opacity=0.5)
        i_square.set_stroke(BLUE, width=0.0)


        final_equation_line_one = [ 
            MathTex(r"c^2", font_size=equation_font_size).set_color(RED),
            MathTex(r"=", font_size=equation_font_size),
            MathTex(r"{ab \over 2}}", font_size=equation_font_size).set_color(YELLOW),
            MathTex(r"+", font_size=equation_font_size),
            MathTex(r"{ab \over 2}}", font_size=equation_font_size).set_color(BLUE),
            MathTex(r"+", font_size=equation_font_size),
            MathTex(r"{ab \over 2}}", font_size=equation_font_size).set_color(GREEN),
            MathTex(r"+", font_size=equation_font_size),
            MathTex(r"{ab \over 2}}", font_size=equation_font_size).set_color(PURPLE),
            MathTex(r"+", font_size=equation_font_size),
            MathTex(r"(b-a)^2}", font_size=equation_font_size).set_color(PINK)
        ]
        final_equation_line_one[0].next_to(congruent_triangles_equation[0], DOWN, buff=LARGE_BUFF)
        final_equation_line_one[0].align_to(congruent_triangles_equation[0], LEFT)
        for i in range(11):
            if i != 0:
                final_equation_line_one[i].next_to(final_equation_line_one[i-1], RIGHT, buff=SMALL_BUFF)

        final_equation_line_two = [ 
            MathTex(r"=", font_size=equation_font_size),
            MathTex(r"2 ab", font_size=equation_font_size),
            MathTex(r"+", font_size=equation_font_size),
            MathTex(r"b^2 - 2ab + a^2}", font_size=equation_font_size).set_color(PINK)
        ]
        for i in range(4):
            if i == 0:
                final_equation_line_two[0].next_to(final_equation_line_one[1], DOWN, buff=LARGE_BUFF)
                final_equation_line_two[0].align_to(final_equation_line_one[1], LEFT)
            else:
                final_equation_line_two[i].next_to(final_equation_line_two[i-1], RIGHT, buff=SMALL_BUFF)

        final_equation_line_three = [ 
            MathTex(r"=", font_size=equation_font_size),
            MathTex(r"a^2 + b^2}", font_size=equation_font_size)
        ]
        final_equation_line_three[0].next_to(final_equation_line_two[0], DOWN, buff=LARGE_BUFF)
        final_equation_line_three[0].align_to(final_equation_line_two[0], LEFT)
        final_equation_line_three[1].next_to(final_equation_line_three[0], RIGHT, buff=SMALL_BUFF)


        for num in range(3):
            self.play(Create(tri_line[num]), Write(tri_line_tex[num]))

        self.play(Create(rangle))
        self.play(Write(tri_point_tex[0]), Write(tri_point_tex[1]), Write(tri_point_tex[2]))

        self.play(FadeOut(tri_line_tex[0]), FadeOut(tri_line_tex[1]))

        self.play(Create(squ_rangle[0]))
        for i in range(3):
            #self.play(Create(os_line[i]), Create(squ_rangle[i+1]))
            self.play(Create(os_line[i]), Write(os_line_tex[i]))
            if i < 2:
                self.play(Write(os_point_tex[i]))
            self.play(Create(squ_rangle[i+1]))

        for i in range(3):
            self.play(Create(extra_lines[i]))
            self.play(Create(extra_rangle[i]))
            self.play(Write(is_point_tex[i]))

        self.play(FadeOut(extra_rangle[0]), FadeOut(extra_rangle[1]), FadeOut(extra_rangle[2]))
        self.play(FadeOut(squ_rangle[0]), FadeOut(squ_rangle[1]), FadeOut(squ_rangle[2]), FadeOut(squ_rangle[3]))

        self.play(Create(theta), Write(theta_tex[0]))
        self.play(Create(ninty_theta), Write(theta_90_tex[1]))
        self.play(Create(extra_theta[0]), Write(theta_tex[1]))
        self.play(Create(extra_ninty_theta[0]), Write(theta_90_tex[3]))
        self.play(Create(extra_theta[1]), Write(theta_tex[3]))
        self.play(Create(extra_ninty_theta[1]), Write(theta_90_tex[2]))
        self.play(Create(extra_theta[2]), Write(theta_tex[2]))
        self.play(Create(extra_ninty_theta[2]), Write(theta_90_tex[0]))

        for i in range(7):
            if i % 2 == 0:
                self.bring_to_back(triangles[int(i/2)])
                self.play(Write(congruent_triangles_equation[i]), Create(triangles[int(i/2)]))
            else:
                self.play(Write(congruent_triangles_equation[i]))
            

        self.play(  FadeOut(theta), FadeOut(theta_tex[0]),
                    FadeOut(ninty_theta), FadeOut(theta_90_tex[1]),
                    FadeOut(extra_theta[0]), FadeOut(theta_tex[1]),
                    FadeOut(extra_ninty_theta[0]), FadeOut(theta_90_tex[3]),
                    FadeOut(extra_theta[1]), FadeOut(theta_tex[3]),
                    FadeOut(extra_ninty_theta[1]), FadeOut(theta_90_tex[2]),
                    FadeOut(extra_theta[2]), FadeOut(theta_tex[2]),
                    FadeOut(extra_ninty_theta[2]), FadeOut(theta_90_tex[0]))


        self.play(Write(tri_line_tex[0]), Write(tri_line_tex[1]))

        self.play(Create(Line_AF), Write(Line_AF_tex))
        self.play(Create(Line_FC), Write(Line_FC_tex))
        
        for i in range(11):
            if i == 0:
                self.bring_to_back(o_square)
                self.play(Write(final_equation_line_one[i]), Create(o_square))
                self.play(FadeOut(o_square))
            elif i == 10:
                self.bring_to_back(i_square)
                self.play(Write(final_equation_line_one[i]), Create(i_square))
            else:
                self.play(Write(final_equation_line_one[i]))

        for i in range(4):
            self.play(Write(final_equation_line_two[i]))

        for i in range(2):
            self.play(Write(final_equation_line_three[i]))

    def shift_tex_to_line(self, tex, line, direction=True, shift_distance=0.4):
        tex.shift(line.get_center)
        guide_line = line.copy()
        guide_line.rotate(-PI/2)
        vector_normal = guide_line.get_unit_vector()
        if(direction):
            tex.shift(vector_normal * shift_distance)
        else:
            tex.shift(vector_normal * shift_distance * -1)

with tempconfig({"quality": "medium_quality"}):
    #scene = UsingBraces()
    scene = pythagorean()
    scene.render()