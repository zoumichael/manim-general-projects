from manim import *

myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
standard_font_size = 20
standard_para_width = 4

HOME = "C:/Users/zoumi/Documents/GitHub/manim-general-projects/CalcImage"


def string_to_tex(string, my_font_size=standard_font_size, paragraph_width=standard_para_width, my_color=WHITE):
    return Tex(
            "\\justifying \parbox{FILLERin}{STRING}".replace("FILLER", str(paragraph_width)).replace("STRING", string),
            tex_template=myTemplate,
            font_size=my_font_size,
            color=my_color)


class ZenoAnimation(Scene):
    def __init__(self, is_explain, location_object = None):
        # VGroup
        self.zeno_group = VGroup()
        if location_object is not None:
            self.zeno_group.move_to(location_object, DOWN)

        # Colors
        colors = [RED, YELLOW, GREEN, WHITE]
        self.dots = [[8, 17],
                [12, 25],
                [14, 29],
                [15, 31]]

        self.TPoints = []
        self.APoints = []
        for count in range(4):
            self.TPoints.append(Tex("$T_{" + str(count) + "}$", color=colors[count]))
            self.APoints.append(Tex("$A_{" + str(count) + "}$", color=colors[count]))
        self.zeno_group.add(*self.TPoints)
        self.zeno_group.add(*self.APoints)

        # Grid
        self.all_dots = VGroup()
        for count in range(0, 34):
            self.all_dots.add(Dot())

        self.all_dots.arrange_in_grid(
            rows=2,
            cols=17,
            buff=(0.75, 2)
        )

        self.t_line = Line(self.all_dots[0].get_center(), self.all_dots[16].get_center())
        self.a_line = Line(self.all_dots[17].get_center(), self.all_dots[33].get_center())
        self.zeno_group.add(self.t_line, self.a_line)

        self.tort = Dot(point=self.all_dots[8].points)
        self.ach = Dot(point=self.all_dots[17].points)
        self.zeno_group.add(self.tort, self.ach)

        for count in range(4):
            self.all_dots[self.dots[count][0]].set_color(colors[count])
            self.all_dots[self.dots[count][1]].set_color(colors[count])
            self.zeno_group.add(self.all_dots[self.dots[count][0]], self.all_dots[self.dots[count][1]])

        self.t_lines = [Line(self.all_dots[8].get_center(), self.all_dots[12].get_center(), color=RED),
                        Line(self.all_dots[12].get_center(), self.all_dots[14].get_center(), color=YELLOW),
                        Line(self.all_dots[14].get_center(), self.all_dots[15].get_center(), color=GREEN)]
        self.zeno_group.add(*self.t_lines)
        self.a_lines = [Line(self.all_dots[17].get_center(), self.all_dots[25].get_center(), color=RED),
                        Line(self.all_dots[25].get_center(), self.all_dots[29].get_center(), color=YELLOW),
                        Line(self.all_dots[29].get_center(), self.all_dots[31].get_center(), color=GREEN)]
        self.zeno_group.add(*self.a_lines)


        self.a_braces = []
        self.t_braces = []
        self.a_times = []
        self.a_distances = []
        self.t_times = []
        self.t_distances = []
        if is_explain:
            for index in range(len(self.a_lines)):
                self.a_braces.append(BraceBetweenPoints(self.a_lines[index].get_start(), self.a_lines[index].get_end()))

            self.zeno_group.add(*self.a_braces)

            for index in range(len(self.t_lines)):
                self.t_braces.append(BraceBetweenPoints(self.t_lines[index].get_start(), self.t_lines[index].get_end(), direction=UP))
            self.zeno_group.add(*self.t_braces)

            for index in range(len(self.a_lines)):
                self.a_times.append(Tex(r"$t_0=\frac{100}{v_A}=10$"+str(index)))
                self.a_distances.append(Tex(r"$s_1=t_0v_T$"+str(index)))
                self.t_times.append(Tex(r"$t_1=\frac{s_1}{v_A}$" + str(index)))
                self.t_distances.append(Tex(r"$t_2=\frac{t_1v_T}{v_A}=t_0(\frac{v_T}{v_A})^2$" + str(index)))
                self.a_times[index].next_to(self.a_lines[index], UP)
                self.a_distances[index].next_to(self.a_braces[index], DOWN)
                self.t_times[index].next_to(self.t_lines[index], UP)
                self.t_distances[index].next_to(self.t_braces[index], DOWN)
            self.zeno_group.add(*self.a_times, *self.t_times, *self.t_distances, *self.a_distances)


        for count in range(4):
            self.TPoints[count].next_to(self.all_dots[self.dots[count][0]], UP)
            self.APoints[count].next_to(self.all_dots[self.dots[count][1]], DOWN)


    def get_t_line(self):
        return self.t_line

    def get_t_lines_len(self):
        return len(self.t_lines)

    def get_t_lines_at(self, index):
        return self.t_lines[index]

    def get_t_points_at(self, index):
        return self.TPoints[index]

    def get_a_line(self):
        return self.a_line

    def get_a_lines_len(self):
        return len(self.a_lines)

    def get_a_lines_at(self, index):
        return self.a_lines[index]

    def get_a_points_at(self, index):
        return self.APoints[index]

    def get_d_at(self, index):
        return self.all_dots[index]

    def get_tort(self):
        return self.tort

    def get_ach(self):
        return self.ach

    def get_zeno_group(self):
        return self.zeno_group

    def get_dot_index_at(self, r, c):
        return self.dots[r][c]

    def get_t_braces_at(self, index):
        return self.t_braces[index]

    def get_a_braces_at(self, index):
        return self.a_braces[index]

    def get_a_distances_at(self, index):
        return self.a_distances[index]

    def get_t_distances_at(self, index):
        return self.t_distances[index]

    def get_a_times_at(self, index):
        return self.a_times[index]

    def get_t_times_at(self, index):
        return self.t_times[index]


'''
class ZenoParadox(Scene):
    def construct(self):

        with_no = True

        times = []
        times.append(Tex(r"$\frac{100}{V_A}$"))

        distances = []
        distances.append(Tex(r"$100$"))

        # VGroup
        zeno_group = VGroup()

        # Colors
        colors = [RED, YELLOW, GREEN, WHITE]
        dots = [[8, 17],
                [12, 25],
                [14, 29],
                [15, 31]]

        # Text
        paradox = "Achilles ($A$), the fleet-footed hero of the Trojan War, is engaged in a race with a tortoise (" \
                  "$T$), which has been granted a head start. He shall never catch the tortoise since each time he " \
                  "reaches to the previous position of the tortoise, the tortoise has moved forward to a new position " \
                  "ahead of him."

        paradox_tex = string_to_tex(paradox)
        paradox_tex.to_edge(UP, buff=0.5)

        T = []
        A = []
        for count in range(4):
            T.append(Tex("$T_{" + str(count) + "}$", color=colors[count]))
            A.append(Tex("$A_{" + str(count) + "}$", color=colors[count]))
        zeno_group.add(*T)
        zeno_group.add(*A)

        # Grid
        d = VGroup()
        for count in range(0, 34):
            d.add(Dot())

        d.arrange_in_grid(
            rows=2,
            cols=17,
            buff=(0.5, 1)
        )

        t_line = Line(d[0].get_center(), d[16].get_center())
        a_line = Line(d[17].get_center(), d[33].get_center())
        zeno_group.add(t_line, a_line)

        tort = Dot(point=d[8].points)
        ach = Dot(point=d[17].points)
        zeno_group.add(tort, ach)

        for count in range(4):
            d[dots[count][0]].set_color(colors[count])
            d[dots[count][1]].set_color(colors[count])
            zeno_group.add(d[dots[count][0]], d[dots[count][1]])

        t_lines = [Line(d[8].get_center(), d[12].get_center(), color=RED),
                   Line(d[12].get_center(), d[14].get_center(), color=YELLOW),
                   Line(d[14].get_center(), d[15].get_center(), color=GREEN)]
        zeno_group.add(*t_lines)
        a_lines = [Line(d[17].get_center(), d[25].get_center(), color=RED),
                   Line(d[25].get_center(), d[29].get_center(), color=YELLOW),
                   Line(d[29].get_center(), d[31].get_center(), color=GREEN)]
        zeno_group.add(*a_lines)




        for count in range(4):
            T[count].next_to(d[dots[count][0]], UP)
            A[count].next_to(d[dots[count][1]], DOWN)


        T1 = ["It is absurd and yet sounds logical.", 1]
        T2 = ["It is a paradox, isn't it? You have to admire ancient Greeks for their passions and curiosities in seeking the knowledge.", 0]
        T3 = ["To get some insights, let us be more quantitative and assume that $A$ runs and $T$ moves at speed $v_A =10m/s$ and $v_T=1m/s$", 0]

        TLines = [T1, T2, T3]

        TTex = []
        for i in range(len(TLines)):
            if TLines[i][1] == 0:
                TTex.append(string_to_tex(TLines[i][0], my_color=BLUE))
            else:
                TTex.append(string_to_tex(TLines[i][0], my_color=RED))
            if i == 0:
                TTex[i].next_to(zeno_group, DOWN)
                if TLines[i][1] == 0:
                    TTex[i].to_edge(LEFT, buff=0.5)
                else:
                    TTex[i].to_edge(RIGHT, buff=0.5)
            else:
                TTex[i].next_to(TTex[i - 1], DOWN)
                if TLines[i][1] == 0:
                    TTex[i].to_edge(LEFT, buff=0.5)
                else:
                    TTex[i].to_edge(RIGHT, buff=0.5)

        g = VGroup(*TTex)

        # PLAY THE ANIMATION

        self.play(FadeIn(paradox_tex))

        self.add(t_line)
        self.add(a_line)

        self.add(d[8], d[17])
        self.add_foreground_mobjects(ach, tort)

        self.add(T[0], A[0])

        for index in range(len(t_lines)):
            self.play(
                Create(t_lines[index]),
                Create(a_lines[index]),
                MoveAlongPath(tort, t_lines[index]),
                MoveAlongPath(ach, a_lines[index])
            )
            self.add(d[dots[index+1][0]], d[dots[index+1][1]])
            self.add(T[index+1], A[index+1])

            if with_no:
                self.wait(1)

                if index == 0:
                    brace = BraceBetweenPoints(a_lines[index].get_start(), a_lines[index].get_end())
                    self.add(times[0])

                    times[0].next_to(a_lines[index], UP)
                    distances[0].next_to(brace, DOWN)
                    self.add(brace, distances[0])
            else:
                self.wait(1)

        self.play(FadeOut(paradox_tex), zeno_group.animate.shift(UP*2))

        for i in range(len(TTex)):
            self.play(FadeIn(TTex[i]))
            self.wait(1)
'''
