from manim import *
import numpy as np
import random

HOME = "C:/Users/zoumi/Documents/GitHub/manim-general-projects/images"
HOME2 = "C:/Users/zoumi/Documents/GitHub/manim-general-projects/images/SVG_Images"


def gen_plane(x3, y3, l2):
    return NumberPlane(x_range=[x3[0], x3[1], x3[2]], y_range=[y3[0], y3[1], y3[2]], x_length=l2[0],
                       y_length=l2[1]).add_coordinates()


def gen_vector(plane, ps, pe, vector_name, vector_color, vector_name_color):
    vector = Line(start=plane.coords_to_point(ps[0], ps[1]), end=plane.coords_to_point(pe[0], pe[1]),
                  stroke_color=vector_color).add_tip()
    vector_name = MathTex(vector_name).next_to(vector, RIGHT, buff=0.1).set_color(vector_name_color)
    return [vector, vector_name]


def linear_albegra_mobjects():
    x3 = [-5, 5, 1]
    y3 = [-4, 4, 1]
    l2 = [5, 4]
    plane3 = gen_plane(x3, y3, l2)
    ps_1 = [0, 0]
    pe_1 = [3, 2]
    vector_name_1 = "\\vec{v}"
    [vect1, vect1_name] = gen_vector(plane3, ps_1, pe_1, vector_name_1, YELLOW, YELLOW)
    ps_2 = [0, 0]
    pe_2 = [-2, 1]
    vector_name_2 = "\\vec{w}"
    [vect2, vect2_name] = gen_vector(plane3, ps_2, pe_2, vector_name_2, RED, RED)
    ps_3 = [3, 2]
    pe_3 = [1, 3]
    vector_name_3 = "\\vec{v} + \\vec{w}"
    [vect3, vect3_name] = gen_vector(plane3, ps_3, pe_3, vector_name_3, RED, RED)
    ps_4 = [0, 0]
    pe_4 = [1, 3]
    vector_name_4 = "\\vec{v} + \\vec{w}"
    [vect4, vect4_name] = gen_vector(plane3, ps_4, pe_4, vector_name_4, GREEN, GREEN)
    return [plane3, vect1, vect1_name, vect2, vect2_name, vect3, vect4, vect4_name]


def pendulum_objects(time): 
    # time = ValueTracker(0)
    l = 3
    g = 10
    w = np.sqrt(g / l)
    T = 2 * PI / w
    theta_max = 20 / 180 * PI
    p_x = -2
    p_y = 3
    shift_req = p_x * RIGHT + p_y * UP

    vertical_line = DashedLine(start=shift_req, end=shift_req + 3 * DOWN)

    theta = DecimalNumber().move_to(RIGHT * 10)

    # theta = DecimalNumber()
    def theta_move(x):
        x.set_value(theta_max * np.sin(w * time.get_value()))
        return x

    # theta.add_updater(lambda m: m.set_value(theta_max * np.sin(w * time.get_value())))
    theta.add_updater(theta_move)

    def get_ball(x, y):
        dot = Dot(fill_color=BLUE, fill_opacity=1).move_to(x * RIGHT + y * UP).scale(3)
        return dot

    ball = always_redraw(lambda:
                         get_ball(shift_req + l * np.sin(theta.get_value()),
                                  shift_req - l * np.cos(theta.get_value()))
                         )

    def get_string():
        line = Line(color=GREY, start=shift_req, end=ball.get_center())
        return line

    string = always_redraw(lambda: get_string())

    def get_angle(theta):
        if theta != 0:
            if theta > 0:
                angle = Angle(line1=string, line2=vertical_line, other_angle=True, radius=0.5, color=YELLOW)
            else:
                angle = VectorizedPoint()
        else:
            angle = VectorizedPoint()
        return angle

    angle = always_redraw(lambda: get_angle(theta.get_value()))
    guest_name = Tex("Manoj Dhakal").next_to(vertical_line.get_start(), RIGHT, buff=0.5)
    guest_logo = ImageMobject(f"{HOME}/guest_logo.png").set_width(2).next_to(guest_name, DOWN, buff=0.1)
    # pendulum = Group(string, ball, vertical_line, guest_name, guest_logo)
    return [string, ball, vertical_line, guest_name, guest_logo, theta, angle, T]


def fig_layout(title_left, title_right, fig_left, fig_right):
    basic_3d = Tex(title_left).scale(0.7).shift(UP * 2 + LEFT * 2)
    basic_3d_image = ImageMobject(fig_left).set_width(4).next_to(basic_3d, DOWN, buff=0.1)
    adv_3d = Tex(title_right).scale(0.7).next_to(basic_3d, RIGHT, buff=1.5)
    adv_3d_image = ImageMobject(fig_right).set_width(4).next_to(adv_3d, DOWN, buff=0.1)
    return [adv_3d, adv_3d_image, basic_3d, basic_3d_image]


class Intro(Scene):
    def construct(self):
        play_icon = VGroup(*[SVGMobject(f"{HOME2}/youtube_icon.svg") for k in range(8)]
                           ).set_height(0.75).arrange(DOWN, buff=0.2).to_edge(UL, buff=0.1)
        self.play(DrawBorderThenFill(play_icon), run_time=3)
        [flag_0, flag_1, flag_2, flag_3, flag_4, flag_5, flag_6, flag_7] = 8 * [True]

        plane_box_dot = NumberPlane(x_range=[-5, 5, 1], y_range=[-3, 3, 1]).add_coordinates()
        box = Rectangle(stroke_color=GREEN_C, stroke_opacity=0.7, fill_color=RED_B, fill_opacity=0.5, height=1, width=1)
        dot = Dot().move_to(box.get_center())
        dot.add_updater(lambda x: x.move_to(box.get_center()))
        if flag_0:
            self.add(box, dot, plane_box_dot)
            self.play(box.animate.shift(RIGHT * 2 + UP))
            self.play(box.animate.shift(UP))
            self.wait()
            animate_obj = VGroup(plane_box_dot, box, dot)
            self.play(animate_obj.animate.set_width(0.8).move_to(play_icon[0].get_center()), run_time=2)
            dot.remove_updater(dot)
            self.wait()

        x3 = [-2, 2, 1]
        y3 = [0, 2, 1]
        l2 = [6, 3]
        # plane = NumberPlane(x_range=[-2, 2, 1], y_range=[0, 2, 1], x_length=6, y_length=3).add_coordinates()
        plane = gen_plane(x3, y3, l2)

        def parabolic(x):
            return 0.5 * x ** 2

        parabolic = plane.plot(parabolic, x_range=[-2, 2], color=YELLOW)

        def cubic(x):
            return 0.1 * (x - 1) * (x + 1) * x + 1

        cubic = plane.plot(cubic, x_range=[-2, 2], color=YELLOW)
        parabolic_copy = parabolic.copy()

        stuff = VGroup(plane, parabolic)
        kk = stuff.copy()
        kk.add(
            cubic)  # cubic has been changed to parabolic, it is needed in the future,  as such it should be added here.

        if flag_1:
            self.play(LaggedStart(Write(plane), Create(cubic)), run_time=2, lag_ratio=0.5)
            self.play(Transform(cubic, parabolic_copy))
            self.wait()
            self.add(
                stuff)  # stuff is needed after following animation, so we specifically add it to screen now.  it repeats plane and parambolic already in the screen
            self.play(kk.animate.set_width(0.8).move_to(play_icon[1].get_center()), run_time=2)
            self.wait()

        s = ValueTracker(-2)  # animation on slope
        k = ValueTracker(-2)  # animation on area:  right point in x-axis of shape
        d = ValueTracker(0.4)  # animation on area:  dx value of riemann rectangle
        area = always_redraw(
            lambda: plane.get_riemann_rectangles(graph=parabolic, x_range=[-2, k.get_value()], dx=d.get_value(),
                                                 stroke_color=WHITE, stroke_width=0.1))

        slope = always_redraw(
            lambda: plane.get_secant_slope_group(x=s.get_value(), graph=parabolic, dx=0.01, secant_line_color=RED,
                                                 secant_line_length=3))

        if flag_2:
            self.add(slope)
            self.play(s.animate.set_value(1.5), run_time=3)

            self.add(area)
            self.remove(slope)
            self.play(k.animate.set_value(2), run_time=5)

            stuff.add(area)
            self.wait()
            self.play(d.animate.set_value(0.05), run_time=4)

            self.play(stuff.animate.set_width(0.8).move_to(play_icon[2].get_center()), run_time=2)
            self.wait()

        ##LINEAR ALGEBRA MOBJECTS
        [plane3, vect1, vect1_name, vect2, vect2_name, vect3, vect4, vect4_name] = linear_albegra_mobjects()

        lin_alg = VGroup(plane3, vect1, vect2, vect1_name, vect2_name, vect4_name, vect3, vect4)
        if flag_3:
            self.play(Create(plane3))
            self.play(GrowFromPoint(vect1, point=vect1.get_start()), Write(vect1_name), run_time=2)
            self.wait()
            self.play(GrowFromPoint(vect2, point=vect2.get_start()), Write(vect2_name), run_time=2)
            self.wait()
            self.play(Transform(vect2, vect3), vect2_name.animate.next_to(vect3, UP, buff=0.1), run_time=2)
            self.wait()
            self.play(LaggedStart(GrowFromPoint(vect4, point=vect4.get_start())), Write(vect4_name), run_time=3,
                      lag_ratio=1)
            self.wait()
            self.play(lin_alg.animate.set_width(0.8).move_to(play_icon[3]), run_time=2)
            self.wait()

        # MOBJECTS FOR BASIC PROBABILITY ANIMATION and put into icon [5]
        ticks = VGroup(*[SVGMobject(f"{HOME2}\\green_tick.svg").set_color(GREEN) for k in range(4)]).set_width(
            0.5).arrange(RIGHT).to_edge(UP)
        crosses = VGroup(*[SVGMobject(f"{HOME2}\\cross.svg").set_color(RED) for k in range(4)]).set_width(0.48).arrange(
            RIGHT).next_to(ticks, DOWN, buff=0.25)

        data = VGroup(*ticks, *crosses)
        title_left = "Basic 3D Scenes"
        title_right = "Advanced 3D Scenes"
        fig_left = f"{HOME}\\basic_3d.jpg"
        fig_right = f"{HOME}\\adv_3d.jpg"
        [adv_3d, adv_3d_image, basic_3d, basic_3d_image] = fig_layout(title_left, title_right, fig_left, fig_right)
        basic_3d_g = Group(basic_3d, basic_3d_image)
        adv_3d_g = Group(adv_3d, adv_3d_image)

        # Playing the 3d scene stuff
        if not flag_4 and not flag_5:
            self.play(LaggedStart(Write(basic_3d), FadeIn(basic_3d_image), run_time=3, lag_ratio=1))
            self.play(LaggedStart(Write(adv_3d), FadeIn(adv_3d_image), run_time=3, lag_ratio=1))

            self.play(adv_3d_image.animate.set_opacity(0.75), basic_3d_image.animate.set_opacity(0.75))

            self.play(basic_3d_g.animate.set_width(0.8).move_to(play_icon[4].get_center()),
                      adv_3d_g.animate.set_width(0.8).move_to(play_icon[5].get_center()),
                      run_time=2)

        # Playing the probability part
        self.play(DrawBorderThenFill(ticks), DrawBorderThenFill(crosses), run_time=3)
        self.wait()

        for y in range(2):
            a = random.sample(range(0, 8), k=4)
            # THIS IS A GROUP FOR THE RESULTS BASED ON THE DATA
            res_values = VGroup()
            # for i, res in enumerate(a):
            for i in np.arange(len(a)):
                res = data[a[i]]
                res_values.add(res)

            # THIS CALLS FOR A BOX TO SURROUND THE RESULTS FROM DATA
            boxes = VGroup()
            # for i, box in enumerate(res_values):
            for i in np.arange(len(res_values)):
                box = SurroundingRectangle(res_values[i], buff=0.1)
                boxes.add(box)

            # THIS CREATES THE SAMPLE OF SELECTED DATA
            sample = VGroup()
            # for i, res in enumerate(res_values):
            for i in np.arange(len(res_values)):
                res = VGroup(res_values[i], boxes[i])
                sample.add(res)

            moved_result = sample.copy()

            self.play(Create(boxes))
            self.play(moved_result.animate.arrange(RIGHT, buff=0.1).move_to(ORIGIN).set_width(2), run_time=2)
            self.play(FadeOut(moved_result), FadeOut(boxes))

        moved_stuff = VGroup(boxes, data)
        # self.play(Create(boxes), moved_stuff.animate.set_width(0.8).move_to(play_icon[6].get_center()), run_time=2)
        self.play(moved_stuff.animate.set_width(0.8).move_to(play_icon[6].get_center()), run_time=2)

        # MOBJECTS FOR THE PENDULUM
        time = ValueTracker(0)
        # PLAYING THE PENDULUM PART

        [string, ball, vertical_line, guest_name, guest_logo, theta, angle, T] = pendulum_objects(time)
        pendulum = Group(string, ball, vertical_line, guest_name, guest_logo)

        self.play(Create(VGroup(vertical_line, theta, ball, string, angle)))
        self.wait()
        self.play(FadeIn(guest_name), FadeIn(guest_logo))
        self.play(time.animate.set_value(2 * T), rate_func=linear, run_time=2 * T)
        self.play(pendulum.animate.set_height(0.6).move_to(play_icon[7].get_center()), run_time=2)
        self.remove(theta, angle, ball, string)
        ##PLAY THE PICTURE OF FEATURED DUDE INTO THE LAST YOUTUBE LOGO

        # Playing the final part of the intro
        discord_logo = SVGMobject(f"{HOME2}\\discord.svg")

        self.play(DrawBorderThenFill(discord_logo))
        self.play(discord_logo.animate.to_edge(UP))

        banner = ManimBanner().set_width(3).next_to(discord_logo, DOWN, buff=1)

        self.wait()
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()


