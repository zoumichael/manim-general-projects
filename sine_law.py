
from ChangingDecimalText import *
from Grid import *
from ArcBetweenVectors import *
from LabelFromArc import *
from Polygon import *

class SinInterface(VGroup):
    CONFIG = {
        "x_size": 16,
        "y_size": 6,
        "axes_config": {
            "x_min": -7,
            "x_max": 7,
            "y_min": -2.5,
            "y_max": 2.5,
            "axis_config": {
                "color": GREY,
                "include_tip": False,
                "exclude_zero_from_default_numbers": False,
                "decimal_number_config": {
                    "num_decimal_places": 1,
                },
            },
            "x_axis_config": {
                "unit_size": 0.8,
            },
            "y_axis_config": {
                "label_direction": LEFT,
                "unit_size": 0.8,
                # "x_min": -2.5,
                # "x_max": 2.5,
            },
            "center_point": ORIGIN,
        },
        "margin": 1,
        "x_margin": 1.2,
        "y_margin": None,
        "grid_kwargs": {
            "stroke_width": 0.5
        }
    }

    def __init__(self, **kwargs):
        #digest_config(self, kwargs)
        super().__init__(**kwargs)
        if self.x_size != None:
            self.axes_config["x_max"] = self.x_size / 2
            self.axes_config["x_min"] = -self.x_size / 2
        if self.y_size != None:
            self.axes_config["y_max"] = self.y_size / 2
            self.axes_config["y_min"] = -self.y_size / 2
        axes = Axes(**self.axes_config)
        inner_margin = RoundedRectangle(
            width=axes.get_width(),
            height=axes.get_height(),
            fill_opacity=1,
            fill_color=BLACK,
            stroke_width=0,
            stroke_color=WHITE,
        )
        if self.x_margin == None:
            self.x_margin = self.margin
        if self.y_margin == None:
            self.y_margin = self.margin
        # print(self.y_margin)
        outer_margin = Rectangle(
            width=axes.get_width() + self.x_margin,
            height=axes.get_height() + self.y_margin,
            fill_opacity=1,
            fill_color="#AAAAAA",
            stroke_width=0,
            stroke_color=WHITE,
        )
        axes[0].add_numbers()
        axes[1].add_numbers()
        axes[0][-1].remove(axes[0][-1][0])
        axes[0][-1].set_y((inner_margin.get_bottom()[1] + outer_margin.get_bottom()[1]) / 2)
        axes[1][-1].remove(axes[1][-1][0])
        axes[1][-1].set_x((inner_margin.get_left()[0] + outer_margin.get_left()[0]) / 2)
        # left_side = axes[1][-1].get_right()
        # for n in axes[1][-1]:
        #     n[:].align_to(inner_margin,RIGHT)
        VGroup(axes[0][-1], axes[1][-1]).set_color(BLACK)
        for i in [*axes[0][-1], *axes[1][-1]]:
            i.scale(0.5)
        columns = self.x_size
        rows = self.y_size
        grid = Grid(rows, columns, width=self.x_size, height=self.y_size, line_kwargs=self.grid_kwargs)
        grid.set_width(inner_margin.get_width())
        grid.move_to(inner_margin)
        self.axes = axes
        self.add(outer_margin, inner_margin, grid, axes)


class SinFunctionInterface(Scene):
    def construct(self):
        A_COLOR = YELLOW
        K_COLOR = RED
        W_COLOR = TEAL
        PHI_COLOR = BLUE
        X_COLOR = PURPLE
        T_COLOR = GREEN
        interface = SinInterface()
        interface.to_edge(DOWN, buff=0.2)
        axes = interface.axes
        # f(x,t) = A * sin(k*x + w*t + s)
        A = ValueTracker(1)
        k = ValueTracker(1)
        w = ValueTracker(1)
        s = ValueTracker(0)
        t = ValueTracker(0)
        graph = axes.get_graph(lambda t: np.sin(t), color=RED)
        graph.add_updater(lambda mob: mob.become(
            axes.get_graph(
                lambda x: A.get_value() * np.sin(
                    k.get_value() * x + w.get_value() * t.get_value() + s.get_value()
                ),
                color=RED)
        ))
        graph.t_offset = 0

        labels = VGroup(
            self.get_range_line(-2, 2, A, "A", A_COLOR),
            self.get_range_line(-2, 2, s, "\\phi", PHI_COLOR),
            self.get_range_line(-2, 2, k, "k", K_COLOR),
            self.get_range_line(-2, 2, w, "\\omega", W_COLOR),
        )
        max_tex_width = max(*[l[1].get_width() for l in labels])
        for l in range(len(labels)):
            line = labels[l][0]
            line.align_to(labels[l], LEFT)
            line.shift(RIGHT * max_tex_width + 0.2 * RIGHT)
            labels[l][-1].next_to(labels[l][0], RIGHT, 0.3)

        labels.scale(0.8)
        labels.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        labels.to_edge(UP, buff=0.1)
        labels.to_edge(LEFT)
        # -----------------
        t_tex = Tex("t", color=T_COLOR)
        t_dig = DecimalTextNumber(0, num_decimal_places=3)
        t_dig.add_updater(lambda mob: mob.set_value(t.get_value()))
        tg = VGroup(t_tex, t_dig).arrange(RIGHT, buff=0.6)
        tg_r = Rectangle(width=tg.get_width() + 0.3, height=tg.get_height() + 0.3)
        tg.add(tg_r)
        tg.next_to(interface, UP)
        tg_l = Line(tg.get_corner(UL), tg.get_corner(DL))
        tg_l.next_to(t_tex, RIGHT, buff=abs(tg.get_left() - t_tex.get_left())[0])
        tg.add(tg_l)
        tg.shift(RIGHT * interface.get_width() / 4)
        # -------------------
        formula = Tex(
            "y(x,t)=A\\ \\!{\\rm sin}(kx+\\omega t+\\phi)",
            tex_to_color_map={
                "A": A_COLOR, "k": K_COLOR, "\\omega": W_COLOR, "\\phi": PHI_COLOR,
                "x": X_COLOR, "t": T_COLOR
            },
        )
        formula.next_to(tg, UP)
        self.play(Write(interface))
        self.play(Write(labels), Write(graph))
        self.play(Write(tg), Write(formula))
        self.add(interface, graph, tg, formula, *labels)
        self.wait()
        # self.play(ChangeDecimalToValueText(t,1),run_time=2)
        RUN_TIME = 4
        self.play(A.set_value, 1.9, run_time=RUN_TIME)
        self.wait(4)
        self.play(s.set_value, 0.5, run_time=RUN_TIME)
        self.wait(4)
        self.play(s.set_value, -1.5, run_time=RUN_TIME)
        self.wait(4)
        self.play(k.set_value, -0.4, run_time=RUN_TIME)
        self.wait(4)
        self.play(k.set_value, 1.7, run_time=RUN_TIME)
        self.wait(4)
        self.play(Indicate(t_tex), FocusOn(t_tex.get_center()))
        self.wait(0.5)

        def update_t(mob, dt):
            graph.t_offset += dt * 0.3
            mob.set_value(graph.t_offset)

        t.add_updater(update_t)
        self.add(t)
        self.wait(8)
        self.play(w.set_value, 2, run_time=RUN_TIME)
        self.wait(7)
        self.play(w.set_value, -1.1, run_time=RUN_TIME)
        self.wait(7)
        self.play(
            A.set_value, -1.7,
            k.set_value, 0.8,
            run_time=RUN_TIME,
        )
        self.wait(7)

    def get_range_line(self,
                       start,
                       end,
                       vt,
                       tex="\\alpha",
                       color=WHITE,
                       tex_config={},
                       line_config={}
                       ):
        line_config["numbers_with_elongated_ticks"] = []
        line = NumberLine(x_min=start, x_max=end, **line_config)
        tex_ = Tex(tex, **tex_config)
        tex_.next_to(line, LEFT)
        dot = Dot()
        dot.add_updater(lambda mob: mob.move_to(line.n2p(vt.get_value())))
        digital = DecimalTextNumber(0, num_decimal_places=3, include_sign=True)
        digital.add_updater(lambda mob: mob.set_value(vt.get_value()))
        digital.next_to(line, RIGHT)
        VGroup(line, tex_, digital).set_color(color)
        return VGroup(line, tex_, dot, digital)


class sine_law(Scene):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.triangle_config = {
            "color": RED,
            "stroke_width": 8,
        }
        self.tex_map = {
            "tex_to_color_map": {
                "$\\alpha$": RED_A,
                "$\\beta$": TEAL_A,
                "$\\gamma$": PURPLE_A,
                "A": RED_A,
                "B": TEAL_A,
                "C": PURPLE_A,
                "x": GREEN_A,
                "h_1": YELLOW_B,
                "h_2": BLUE_B,
            }
        }
        self.__dict__.update(kwargs)

    def construct(self):
        du = UP * 1.5
        d1 = Dot(LEFT * 4 + du)
        d2 = Dot(RIGHT * 2 + du)
        d3 = Dot(RIGHT * 4 + UP * 2 + du)

        triangle = Polygon(
            d1.get_center(), d2.get_center(), d3.get_center(), **self.triangle_config
        )

        def frac_string(n, d):
            return ["{", n, "\\over", d, "}"]

        def frac_strings(n, d):
            return ["{", *n, "\\over", *d, "}"]

        sina_t = ["{\\rm sin}", "\\alpha"]
        sinb_t = ["{\\rm sin}", "\\beta"]
        sinc_t = ["{\\rm sin}", "\\gamma"]
        cosa_t = ["{\\rm cos}", "\\alpha"]
        cosb_t = ["{\\rm cos}", "\\beta"]
        cosc_t = ["{\\rm cos}", "\\gamma"]
        formulas_sine_string_1 = [
            [*sinb_t, "=", *frac_string("h_1", "C")],
            [*sinc_t, "=", *frac_string("h_1", "B")],
            ["C", "\\,", *sinb_t, "=", "h_1"],
            ["B", "\\,", *sinc_t, "=", "h_1"],
            ["C", "\\,", *sinb_t, "=", "B", "\\,", *sinc_t],
            [*frac_strings(["C"], sinc_t), "=", *frac_strings(["B"], sinb_t)]
        ]
        formulas_sine_string_2 = [
            [*sina_t, "=", *frac_string("h_2", "B")],
            [*sinb_t, "=", *frac_string("h_2", "A")],
            ["B", "\\,", *sina_t, "=", "h_2"],
            ["A", "\\,", *sinb_t, "=", "h_2"],
            ["B", "\\,", *sina_t, "=", "A", "\\,", *sinb_t],
            [*frac_strings(["B"], sinb_t), "=", *frac_strings(["A"], sina_t)]
        ]
        sine_law = MathTex(*[
            *frac_strings(["C"], sinc_t), "=", *frac_strings(["B"], sinb_t), "=", *frac_strings(["A"], sina_t),
        ], **self.tex_map).scale(0.9)
        formulas_sine_1 = VGroup(*[
            MathTex(*f, **self.tex_map) for f in formulas_sine_string_1
        ])
        # formulas_sine.arrange_in_grid(None,2)
        formulas_sine_arrange_1 = VGroup(
            formulas_sine_1[:2].arrange(RIGHT, buff=1),
            formulas_sine_1[2:4].arrange(RIGHT, buff=1),
            formulas_sine_1[4:].arrange(DOWN),
        ).arrange(DOWN, buff=0.7).scale(0.9)
        formulas_sine_2 = VGroup(*[
            MathTex(*f, **self.tex_map) for f in formulas_sine_string_2
        ])
        # formulas_sine.arrange_in_grid(None,2)
        formulas_sine_arrange_2 = VGroup(
            formulas_sine_2[:2].arrange(RIGHT, buff=1),
            formulas_sine_2[2:4].arrange(RIGHT, buff=1),
            formulas_sine_2[4:].arrange(DOWN),
        ).arrange(DOWN, buff=0.7).scale(0.9)
        formulas_sine_arrange_1.to_edge(DOWN, buff=0.3)
        formulas_sine_arrange_1.to_edge(LEFT, buff=1)
        formulas_sine_arrange_2.to_edge(DOWN, buff=0.3)
        formulas_sine_arrange_2.to_edge(RIGHT, buff=1)
        sine_law.align_to(formulas_sine_arrange_1, DOWN)
        triangle.set_x(0)
        center_vertices = triangle.get_center_of_edges()
        labels = VGroup(*[
            Tex(label, **self.tex_map).move_to(point) for label, point in zip(["C", "B", "A"], center_vertices)
        ])
        fs1 = formulas_sine_1
        fs2 = formulas_sine_2
        # ------------------------------
        h1 = MathTex("h_1", **self.tex_map)
        h2 = MathTex("h_2", **self.tex_map)
        x = MathTex("x", **self.tex_map)
        h1_line = self.get_h(d2, d1, d3)
        h2_line = DashedLine(d3.get_center() + RIGHT * 0.09, [d3.get_x() + 0.09, d2.get_y() - 0.09, 0])
        h3_line = DashedLine(d2.get_center() + RIGHT * 0.09, h2_line.get_end())
        rec_1 = Square().set_width(0.25)
        rec_1 = VMobject().set_points_as_corners([rec_1.get_corner(v) for v in [UR, UL, DL]])
        rec_2 = rec_1.copy()
        rec_1.next_to(h2_line.get_end(), UL, buff=0)
        rec_2.rotate(h1_line.get_angle())
        rec_2.next_to(h1_line.get_end(), DL, buff=0)
        rec_2.shift(DOWN * 0.1 + RIGHT * 0.05)
        x.next_to(h3_line, DOWN, 0.1)
        h1.next_to(h1_line, RIGHT, 0.1)
        h1.shift(LEFT * 0.15)
        h2.next_to(h2_line, RIGHT, 0.1)
        # h2_line.rotate(PI,about_point=h2_line.get_start())
        # ------------------------------
        alpha_arc = ArcBetweenVectors(radius=0.3, d1=d1, d2=d3, center=d2)
        beta_arc = ArcBetweenVectors(radius=1.7, d1=d2, d2=d3, center=d1)
        gamma_arc = ArcBetweenVectors(radius=1, d1=d1, d2=d2, center=d3)
        alpha_p_arc = ArcBetweenVectors(radius=0.4, d1=Dot(h2_line.get_end()), d2=d3, center=d2)
        gamma_arc.rotate(gamma_arc.get_angle() * 0.9, about_point=gamma_arc.get_arc_center())


        alpha = LabelFromArc(alpha_arc, labels[0].get_width() * 0.7, "$\\alpha$", distance_proportion=1.9, **self.tex_map)
        beta = LabelFromArc(beta_arc, labels[0].get_width() * 1.1, "$\\beta$", distance_proportion=1.9, **self.tex_map)
        gamma = LabelFromArc(gamma_arc, labels[0].get_width() * 1.1, "$\\gamma$", distance_proportion=1.9, **self.tex_map)
        alpha_p = LabelFromArc(alpha_p_arc, labels[0].get_width() * 1.1, "$\\alpha'$", distance_proportion=1.9, **self.tex_map)

        alpha.shift(LEFT * 0.25 + DOWN * 0.1)
        but = MathTex("{\\rm sin}(\\pi-\\alpha)={\\rm sin}(\\alpha)", **self.tex_map)
        but.to_corner(UL)

        t1 = Polygon(
            d1.get_center(), d2.get_center(), h1_line.get_end(),
            color=ORANGE, stroke_width=0, fill_opacity=0
        )
        t2 = Polygon(
            d2.get_center(), d3.get_center(), h1_line.get_end(),
            color=ORANGE, stroke_width=0, fill_opacity=0
        )
        t3 = Polygon(
            d2.get_center(), h3_line.get_end(), h2_line.get_start(),
            color=ORANGE, stroke_width=0, fill_opacity=0
        )
        t4 = Polygon(
            d1.get_center(), h3_line.get_end(), h2_line.get_start(),
            color=ORANGE, stroke_width=0, fill_opacity=0
        )

        def show_triange(t):
            t.set_fill(None, 0.3)
            return t

        def hide_triange(t):
            t.set_fill(None, 0)
            return t

        self.add(t1, t2, t3, t4)
        # - SHOW CREATIONS
        self.add_foreground_mobject(triangle)
        self.play(
            Create(triangle, rate_func=linear),
            LaggedStart(*list(map(Write, labels)), lag_ratio=0.8),
            run_time=2.5
        )
        self.wait()
        self.play(
            LaggedStart(*[
                TransformFromCopy(m1, m2)
                for m1, m2 in zip(labels[::-1], [alpha, beta, gamma])
            ], lag_ratio=0.7),
            LaggedStart(*list(map(Create, [alpha_arc, beta_arc, gamma_arc])), lag_ratio=0.7),
            run_time=3.5
        )
        self.wait()
        self.play(LaggedStart(*list(map(Write, [h1_line, h1, rec_2])), lag_ratio=0.5))
        # - TRANSFORMATIONS
        C, B, A = labels
        self.play(ApplyFunction(show_triange, t1))
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(beta[0], fs1[0][1]),
                TransformFromCopy(h1[0], fs1[0][-4]),
                TransformFromCopy(C[0], fs1[0][-2]),
                lag_ratio=0.7
            ),
            LaggedStart(*[Write(fs1[0][i]) for i in [0, 2, -3]]),
            run_time=5
        )
        self.wait()
        self.play(ApplyFunction(hide_triange, t1))
        self.wait()
        self.play(ApplyFunction(show_triange, t2))
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(gamma[0], fs1[1][1]),
                TransformFromCopy(h1[0], fs1[1][-4]),
                TransformFromCopy(B[0], fs1[1][-2]),
                lag_ratio=0.7
            ),
            LaggedStart(*[Write(fs1[1][i]) for i in [0, 2, -3]]),
            run_time=5
        )
        self.wait()
        self.play(ApplyFunction(hide_triange, t2))
        #  - - - - - - - -
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(fs1[0][-2], fs1[2][0]),
                AnimationGroup(
                    TransformFromCopy(fs1[0][0], fs1[2][2]),
                    TransformFromCopy(fs1[0][1], fs1[2][3]),
                    lag_ratio=0
                ),
                TransformFromCopy(fs1[0][2], fs1[2][4]),
                TransformFromCopy(fs1[0][-4], fs1[2][-1]),
                lag_ratio=0.3
            ),
            # LaggedStart(*[Write(fs1[1][i]) for i in [0,2,-3]]),
            run_time=5
        )
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(fs1[1][-2], fs1[3][0]),
                AnimationGroup(
                    TransformFromCopy(fs1[1][0], fs1[3][2]),
                    TransformFromCopy(fs1[1][1], fs1[3][3]),
                    lag_ratio=0
                ),
                TransformFromCopy(fs1[1][2], fs1[3][4]),
                TransformFromCopy(fs1[1][-4], fs1[3][-1]),
                lag_ratio=0.3
            ),
            # LaggedStart(*[Write(fs1[1][i]) for i in [0,2,-3]]),
            run_time=5
        )
        self.wait()
        self.play(
            TransformFromCopy(fs1[2][:4], fs1[4][:4]),
            TransformFromCopy(fs1[3][:4], fs1[4][-4:]),
            Write(fs1[4][4]),
            run_time=5
        )
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(fs1[4][0], fs1[5][1]),
                TransformFromCopy(fs1[4][-2:], fs1[5][3:5]),
                TransformFromCopy(fs1[4][-4], fs1[5][-5]),
                TransformFromCopy(fs1[4][2:4], fs1[5][-3:-1]),
                lag_ratio=0.5
            ),
            # TransformFromCopy(fs1[4][-2:],fs1[5][3:5]),
            # TransformFromCopy(fs1[3][:4],fs1[4][-4:]),
            LaggedStart(
                Write(fs1[5][2]),
                Write(fs1[5][-4]),
                Write(fs1[5][6]),
                lag_ratio=0.5
            ),
            run_time=5
        )
        self.wait()
        # ------------------------------
        self.play(LaggedStart(*list(map(Write, [h2_line, h2, h3_line, x, rec_1])), lag_ratio=0.5))
        self.wait()
        self.play(Write(alpha_p), Write(alpha_p_arc))
        self.wait()
        self.play(Write(but))
        self.wait()
        self.play(Indicate(but), Indicate(alpha_p), Indicate(alpha_p_arc), run_time=3)
        self.wait()
        self.play(ApplyFunction(show_triange, t3))
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(alpha_p[0], fs2[0][1]),
                TransformFromCopy(h2[0], fs2[0][-4]),
                TransformFromCopy(B[0], fs2[0][-2]),
                lag_ratio=0.7
            ),
            LaggedStart(*[Write(fs2[0][i]) for i in [0, 2, -3]]),
            run_time=5
        )
        self.wait()
        self.play(ApplyFunction(hide_triange, t3))
        self.wait()
        self.play(ApplyFunction(show_triange, t4))
        self.wait()
        self.play(
            LaggedStart(
                TransformFromCopy(beta[0], fs2[1][1]),
                TransformFromCopy(h2[0], fs2[1][-4]),
                TransformFromCopy(A[0], fs2[1][-2]),
                lag_ratio=0.7
            ),
            LaggedStart(*[Write(fs2[1][i]) for i in [0, 2, -3]]),
            run_time=5
        )
        self.wait()
        self.play(ApplyFunction(hide_triange, t4))
        self.play(
            LaggedStart(*[FadeIn(f) for f in fs2[2:]], lag_ratio=0.5),
            run_time=8
        )
        self.wait()
        # self.add(sine_law)
        self.play(
            ReplacementTransform(fs1[-1], sine_law[:len(fs1[-1])]),
            ReplacementTransform(fs2[-1], sine_law[-len(fs2[-1]):]),
            run_time=2.5
        )
        sine_law.save_state()
        self.wait()
        self.play(
            Succession(
                FadeToColor(sine_law, YELLOW),
                Restore(sine_law)
            ),
            AnimationGroup(
                ShowPassingFlash(sine_law.copy()),
                ShowPassingFlash(sine_law.copy()),
                lag_ratio=1
            )
        )
        self.wait()

    def get_h(self, dot, d1, d2, invert=True):
        line = Line(d1.get_center(), d2.get_center())
        vector = line.get_unit_vector()
        sign = 1 if invert else -1
        normal_vector = rotate_vector(vector, sign * PI / 2)

        def get_distance_point_line(line, dot):
            x_0, y_0, z_0 = dot.get_center()
            X_0 = line.point_from_proportion(0)
            X_1 = line.point_from_proportion(1)
            x_1, y_1, z_1 = X_0
            x_2, y_2, z_2 = X_1
            return np.abs((x_2 - x_1) * (y_1 - y_0) - (x_1 - x_0) * (y_2 - y_1) / np.linalg.norm(line.get_vector()))

        distance = get_distance_point_line(line, dot)
        return DashedLine(dot.get_center(), dot.get_center() + distance * normal_vector)


with tempconfig({"quality": "medium_quality"}):
    scene = sine_law()
    scene.render()