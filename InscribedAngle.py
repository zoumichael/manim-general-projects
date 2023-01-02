from manim import *
from CircleWithAngles import *
from ArcBetweenVectors import ArcBetweenVectors
from LabelFromArc import LabelFromArc

FRAME_HEIGHT = config["frame_height"]
FRAME_WIDTH = config["frame_width"]
#FRAME_WIDTH = 200
#FRAME_HEIGHT = 300

class InscribedAngle(MovingCameraScene):
    def construct(self):
        circle_grp = CircleWithAngles()
        v1, v2, v3 = circle_grp.vts
        eq = circle_grp[-1]
        circle_grp.to_edge(LEFT, buff=1)
        eq.to_edge(RIGHT, buff=1)
        for mob in circle_grp:
            mob.suspend_updating()
            mob.update()
        self.play(Write(circle_grp))
        for mob in circle_grp:
            mob.resume_updating()
        self.wait()
        #self.play(v1.set_value, -10, run_time=3, rate_func=linear)
        self.play(v1.animate.set_value(-10), run_time=3, rate_func=linear)
        self.wait()
        #self.play(v2.set_value, 225, run_time=5, rate_func=there_and_back)
        self.play(v2.animate.set_value(255), run_time=5, rate_func=there_and_back)
        self.wait()
        self.play(
            v1.animate.set_value(47),
            v2.animate.set_value(110),
            v3.animate.set_value(335),
            run_time=3,
            rate_func=there_and_back
        )
        self.wait()
        circle_grp.remove(eq)
        self.play(
            FadeOut(eq),
            circle_grp[0].animate.scale(0.64),
            circle_grp[0].animate.move_to(ORIGIN),
            circle_grp[0].animate.to_edge(DOWN, buff=0.2)
        )
        self.wait()
        # ---------------------- Transform 2theta by varphi
        theta_2 = circle_grp[-1]
        varphi = Tex("$\\varphi$")
        varphi.match_color(theta_2)
        varphi.move_to(theta_2)
        varphi.match_updaters(theta_2)
        self.play(Transform(theta_2, varphi))
        self.wait()
        # ---------------------- Cases
        titles = VGroup(*[
            Tex(f) for f in ["Case 1", "Case 2", "Case 3"]
        ])
        titles.arrange(RIGHT, buff=3).to_edge(UP)
        # ---------------------- Case 1
        self.play(Write(titles[0]))
        self.wait()
        self.play(
            v1.animate.set_value(40),
            v2.animate.set_value(290 - 180),
            v3.animate.set_value(290),
            run_time=3,
        )
        case_1 = circle_grp.copy()
        case_1.clear_updaters()
        self.play(
            # case_1.animate.set_width(2),
            # case_1.animate.next_to(titles[0], DOWN, buff=0.2)
            case_1.animate.set_width(0.25),
            case_1.animate.to_edge(UP, buff=0.2)
        )
        self.wait()
        self.bring_to_front(case_1[1])


        # ---------------------- Case 2
        self.play(Write(titles[1]))
        self.wait()
        self.play(
            v1.animate.set_value(30),
            v2.animate.set_value(140),
            v3.animate.set_value(260),
            run_time=3,
        )
        self.wait()
        case_2 = circle_grp.copy()
        case_2.clear_updaters()
        self.play(
            case_2.animate.set_width(2),
            #case_2.next_to, titles[1], DOWN, buff=0.2
            case_2.animate.next_to(titles[1], DOWN, buff=0.2)
        )
        self.wait()
        self.bring_to_front(case_2[1])
        # ---------------------- Case 3
        self.play(Write(titles[2]))
        self.wait()
        self.play(
            v1.animate.set_value(30),
            v2.animate.set_value(90),
            v3.animate.set_value(325),
            run_time=3,
        )
        case_3 = circle_grp.copy()
        case_3.clear_updaters()
        self.bring_to_front(case_3[1])
        self.wait()
        self.play(
            case_3.animate.set_width(2),
            #case_3.next_to, titles[2], DOWN, buff=0.2
            case_3.animate.next_to(titles[2], DOWN, buff=0.2)
        )
        # ---------------------- Remove updaters
        circle_grp.clear_updaters()
        self.play(Write(circle_grp, rate_func=lambda t: smooth(1 - t), run_time=2.5))
        self.wait()
        # ------------ Case by case
        cases = VGroup(case_1, case_2, case_3)
        SCREEN = Rectangle(width=FRAME_WIDTH, height=FRAME_HEIGHT)
        grps = VGroup(*[VGroup(t, c) for t, c in zip(titles, cases)])
        grps.generate_target()
        gt = grps.target[1:]
        gp = grps.target[0]
        gt.align_to(SCREEN, UP)
        gt.shift(UP * grps.get_height())
        gp[1].set_height(6)
        gp[1].move_to(ORIGIN)
        gp[1].to_edge(DOWN)
        gp[1].to_edge(LEFT, buff=2)
        gp[0].set_x(0)
        self.play(
            MoveToTarget(grps)
        )
        self.wait()
        self.cases_group_1 = VGroup(case_1, titles[0])
        self.proof_1(case_1)

        # next case
        def next_proof(height=6, buff_down=1, buff_left=0.5):
            def func(vgr):
                tit, gr = vgr
                tit.move_to(ORIGIN)
                tit.to_edge(UP)
                gr.set_height(height)
                gr.move_to(ORIGIN)
                gr.to_edge(DOWN, buff=buff_down)
                gr.to_edge(LEFT, buff=buff_left)
                return vgr

            return func

        frame_1 = self.get_screen_rect()
        self.cases_group_1.add(frame_1)
        self.play(FadeIn(frame_1))
        self.play(
            self.cases_group_1.animate.set_height(1),
            #self.cases_group_1.to_corner, UL, {"buff": 0.1},
            self.cases_group_1.animate.to_corner(UL, buff=0.1),
            run_time=2
        )
        self.play(ApplyFunction(next_proof(), grps[1]))
        self.wait()
        # case 2
        self.cases_group_2 = VGroup(titles[1], case_2)
        self.proof_2(case_2)
        frame_2 = self.get_screen_rect()
        self.cases_group_2.add(frame_2)
        self.play(FadeIn(frame_2))
        self.play(
            #self.cases_group_2.set_height, 1,
            self.cases_group_2.animate.set_height(1),
            #self.cases_group_2.next_to, self.cases_group_1, RIGHT, 0,
            self.cases_group_2.animate.next_to(self.cases_group_1, RIGHT, 0),
            run_time=2
        )
        self.play(ApplyFunction(next_proof(6, 0.2), grps[2]))
        # case 3
        self.cases_group_3 = VGroup(titles[2], case_3)
        self.proof_3(case_3)
        frame_3 = self.get_screen_rect()
        self.cases_group_3.add(frame_3)
        self.play(FadeIn(frame_3))
        all_cases = VGroup(self.cases_group_1, self.cases_group_2, self.cases_group_3)
        '''
        self.play(
            #self.camera_frame.set_width, VGroup(frame_1, frame_2).get_width() * 1,
            #self.camera_frame.move_to, VGroup(frame_1, frame_2).get_center(),
            #self.camera_frame.shift, DOWN * VGroup(frame_1, frame_2).get_height() / 2,
            #self.cases_group_3.set_height, 1,
            #self.cases_group_3.next_to, VGroup(frame_1, frame_2), DOWN, 0,
            self.camera_class.animate.set_width(VGroup(frame_1, frame_2).get_width() * 1),
            self.camera_class.animiate.move_to(VGroup(frame_1, frame_2).get_center()),
            self.camera_class.animate.shift(DOWN * VGroup(frame_1, frame_2).get_height() / 2),
            self.cases_group_3.animate.set_height(1),
            self.cases_group_3.animate.next_to(VGroup(frame_1, frame_2), DOWN, 0),

            run_time=2
        )
        '''
        # self.play(MoveToTarget(all_cases))

        self.wait()
        # self.play(v2.set_value,190,run_time=5,rate_func=linear)


    def proof_1(self, case):
        print("Proof 1")
        dots = case[1]
        d1, d2, d3 = dots
        center = case[0]
        theta = case[-2]
        varphi = case[-1]
        # Radius
        r1 = Line(center.get_center(), d1.get_center(), color=RED_A, stroke_width=8)
        r2 = Line(center.get_center(), d3.get_center(), color=RED_A, stroke_width=8)
        r1_tex = Tex("r").add_background_rectangle()
        r1_tex.move_to(r1)
        r2_tex = r1_tex.copy()
        r2_tex.move_to(r2)
        # self.add(r1,r2,r1_tex,r2_tex)
        self.cases_group_1.add(case, r1, r2, r1_tex, r2_tex, )
        self.play(
            Create(r1),
            Create(r2),
            Write(r1_tex),
            Write(r2_tex),
            Animation(dots),
        )
        self.bring_to_front(dots)
        self.wait()
        # Arc and theta

        #__init__(self, radius, d1, d2, center, invert_angle=False, **kwargs)
        arc_p1 = ArcBetweenVectors(radius=0.6, d1=center, d2=d3, center=d1, invert_angle=True)
        arc_p1.match_color(theta)
        theta_copy = LabelFromArc(arc_p1, theta.get_height(), "$\\theta$", distance_proportion=1.5)
        theta_copy.match_style(theta)
        # psi
        #arc_psi = ArcBetweenVectors(0.4, d3, d1, center, True)
        arc_psi = ArcBetweenVectors(radius=0.4, d1=d3, d2=d1, center=center, invert_angle=True)
        arc_psi.set_color(RED_A)
        psi = LabelFromArc(arc_psi, theta.get_height(), "$\\psi$", distance_proportion=1.3)
        psi.match_color(arc_psi)
        # self.add(arc_p1,theta_copy,arc_psi,psi)
        self.cases_group_1.add(arc_p1, theta_copy, arc_psi, psi)
        self.play(
            TransformFromCopy(theta, theta_copy),
            Create(arc_p1),
            run_time=2
        )
        self.wait(2)
        self.play(
            Create(arc_psi),
            Write(psi),
            run_time=2
        )
        self.wait(2)
        # formulas develop
        t1 = MathTex("\\psi", "+", "2", "\\theta", "=", "180^\\circ",
                        tex_to_color_map={
                            "\\psi": psi.get_color(), "\\theta": theta.get_color(),
                        },
                        )
        t2 = MathTex("\\psi", "+", "\\varphi", "=", "180^\\circ",
                        tex_to_color_map={
                            "\\psi": psi.get_color(), "\\varphi": varphi.get_color(),
                        },
                        )
        t3 = MathTex("\\psi", "+", "2", "\\theta", "=", "\\psi", "+", "\\varphi",
                        tex_to_color_map={
                            "\\psi": psi.get_color(), "\\varphi": varphi.get_color(),
                            "\\theta": theta.get_color()
                        },
                        )
        t4 = MathTex("2", "\\theta", "=", "\\varphi",
                        tex_to_color_map={
                            "\\psi": psi.get_color(), "\\varphi": varphi.get_color(),
                            "\\theta": theta.get_color()
                        },
                        )
        tg = VGroup(t1, t2, t3, t4).arrange(DOWN, buff=0.6)
        self.cases_group_1.add(t1, t2, t3, t4)
        tg.scale(1.35)
        self.align_formulas_with_equal(t2, t1, -2, -2)
        self.align_formulas_with_equal(t3, t1, 4, -2)
        self.align_formulas_with_equal(t4, t1, -2, -2)
        tg.to_edge(RIGHT, buff=0.7)
        # row 1
        tc1 = theta.copy()
        tc2 = theta_copy.copy()
        self.play(
            TransformFromCopy(psi, t1[0]),
            ReplacementTransform(tc1.copy(), t1[3]),
            ReplacementTransform(tc2.copy(), t1[3]),
            # Transform(tc2, t1[3].copy()),
            *[Write(t1[i]) for i in [1, 2, -2, -1]],
            run_time=3
        )
        self.cases_group_1.add(tc1, tc2)
        self.wait()
        self.play(
            TransformFromCopy(t1[0], t2[0]),
            TransformFromCopy(varphi, t2[2], path_arc=-PI / 2),
            *[Write(t2[i]) for i in [1, *range(3, len(t2))]],
            run_time=3
        )
        self.wait()
        self.play(
            TransformFromCopy(t1[:4], t3[:4]),
            TransformFromCopy(t2[:3], t3[-3:]),
            Write(t3[4]),
            run_time=3
        )
        self.wait()
        self.play(
            t3[0].animate.fade(0.5),
            t3[-3].animate.fade(0.5),
        )
        self.wait()
        self.play(
            TransformFromCopy(t3[2:4], t4[:2]),
            TransformFromCopy(t3[-1], t4[-1]),
            Write(t4[2]),
            run_time=3
        )
        self.wait()
        self.play(
            Succession(
                FadeToColor(t4, YELLOW),
                FadeToColor(t4, PURPLE_A),
            ),
            AnimationGroup(
                # ShowCreationThenDestructionAround(t4.copy()),
                # ShowCreationThenDestructionAround(t4.copy()),
                ShowPassingFlash(t4.copy()),
                ShowPassingFlash(t4.copy()),
                lag_ratio=1
            )
        )
        self.wait()

        # n = 0
        # for mob in self.mobjects:
        #     try:
        #         t = Text(f"{n}").next_to(mob,UP,0)
        #         self.add(t)
        #         n += 1
        #     except:
        #         n += 1
        #         pass

    def proof_2(self, case):
        print("Proof 2")
        dots = case[1]
        d1, d2, d3 = dots
        center = case[0]
        theta = case[-2]
        varphi = case[-1]
        # Radius
        r1 = Line(center.get_center(), d1.get_center(), color=RED_A, stroke_width=8)
        r2 = Line(center.get_center(), d2.get_center(), color=RED_A, stroke_width=8)
        r3 = Line(center.get_center(), d3.get_center(), color=RED_A, stroke_width=8)
        r1_tex = Tex("r").add_background_rectangle()
        r1_tex.move_to(r1)
        r2_tex = r1_tex.copy()
        r2_tex.move_to(r2)
        r3_tex = r1_tex.copy()
        r3_tex.move_to(r3)
        arc_p3_2 = ArcBetweenVectors(radius=0.8, d1=center, d2=d2, center=d3).set_color(TEAL)
        arc_p3_1 = ArcBetweenVectors(radius=1, d1=d1, d2=center, center=d3).set_color(TEAL)
        # theta.shift(LEFT*0.2)
        th_1 = LabelFromArc(arc_p3_1, theta.get_height() * 0.8, "$\\theta_1$", color=theta.get_color(),
                            distance_proportion=2)
        th_2 = LabelFromArc(arc_p3_2, theta.get_height() * 0.8, "$\\theta_2$", color=theta.get_color(),
                            distance_proportion=2)
        self.add_foreground_mobjects(dots, case[5])
        self.cases_group_2.add(th_1, th_2)
        self.play(theta.animate.next_to(d3, DOWN, buff=0.2))
        self.wait()
        self.play(
            Create(r1),
            Create(r2),
            Create(r3),
            Write(r1_tex),
            Write(r2_tex),
            Write(r3_tex),
        )
        self.wait()
        self.play(
            ReplacementTransform(theta.copy()[0], th_1[0]),
            ReplacementTransform(theta.copy()[0], th_2[0]),
            Create(arc_p3_1),
            Create(arc_p3_2),
            run_time=3.5
        )
        self.wait()
        # self.remove(theta)
        self.cases_group_2.add(r1, r2, r3, r1_tex, r2_tex, r3_tex, arc_p3_1, arc_p3_2)
        # ---------------- ARC PSI
        arc_psi_1 = ArcBetweenVectors(radius=0.4, d1=d3, d2=d1, center=center, invert_angle=True).set_color(RED_A)
        arc_psi_2 = ArcBetweenVectors(radius=0.4, d1=d3, d2=d2, center=center, invert_angle=True).set_color(RED_A)
        arc_psi_2.rotate(-arc_psi_2.get_angle(), about_point=center.get_center())
        psi_1 = LabelFromArc(arc_psi_1, theta.get_height() * 0.8, "$\\psi_1$", color=RED_A, distance_proportion=1.6)
        psi_2 = LabelFromArc(arc_psi_2, theta.get_height() * 0.8, "$\\psi_2$", color=RED_A, distance_proportion=1.6)
        self.play(
            *list(map(Write, [arc_psi_1, arc_psi_2, psi_1, psi_2])),
            run_time=2
        )
        self.wait()
        self.cases_group_2.add(arc_psi_1, arc_psi_2, psi_1, psi_2)
        # ---------------- FORMUAS transformn
        tex_formulas_kwargs = {
            "tex_to_color_map": {
                "$\\psi_1$": psi_1.get_color(), "$\\psi_2$": psi_2.get_color(), "$\\varphi$": varphi.get_color(),
                "$\\theta_1$": th_1.get_color(), "$\\theta_2$": th_1.get_color(),
            }
        }
        # FORMULAS
        f1 = Tex(
            "$\\psi_1$", "$+$", "$\\psi_2$", "$+$", "$\\varphi$", "$=$", "$360^\\circ$", **tex_formulas_kwargs
        )
        f2 = Tex(
            "$($", "$180^\\circ$", "$-$", "$2$", "$\\theta_1$", "$)$", "$+$", "$($", "$180^\\circ$", "$-$", "$2$", "$\\theta_2$", ")", "+",
            "$\\varphi$", "=", "$360^\\circ$",
            **tex_formulas_kwargs
        )
        f2.add_background_rectangle()
        f3 = Tex(
            "-", "2", "$\\theta_1$", "-", "2", "$\\theta_2$", "+", "$\\varphi$", "=", "0", **tex_formulas_kwargs
        )
        f4 = Tex(
            "$\\varphi$", "=", "2", "$\\theta_1$", "+", "2", "$\\theta_2$", **tex_formulas_kwargs
        )
        f5 = Tex(
            "$\\varphi$", "=", "2", "(", "$\\theta_1$", "+", "$\\theta_2$", ")", **tex_formulas_kwargs
        )
        f6 = Tex(
            "$\\varphi$", "=", "2", "$\\theta$", **tex_formulas_kwargs
        )
        f6[-1].set_color(theta.get_color())
        # f2[0].set_color(RED)
        fg = VGroup(f1, f2, f3, f4, f5, f6).arrange(DOWN, buff=0.6)
        fg.to_edge(RIGHT).to_edge(DOWN)
        self.align_formulas_with_equal(f3, f1, -2, 5)
        self.align_formulas_with_equal(f4, f1, 1, 5)
        self.align_formulas_with_equal(f5, f1, 1, 5)
        self.align_formulas_with_equal(f6, f1, 1, 5)
        # ---------------- FORMUAS transformn
        by_case_1 = Tex("By Case 1").to_edge(RIGHT)
        self.play(
            LaggedStart(
                TransformFromCopy(psi_1[0], f1[0], path_arc=-PI / 2),
                TransformFromCopy(psi_2[0], f1[2], path_arc=-PI / 2),
                TransformFromCopy(varphi, f1[4], path_arc=-PI / 2),
                lag_ratio=0.6
            ),
            LaggedStart(*[Write(f1[i]) for i in [1, 3, 5, 6]]),
            run_time=6
        )
        self.wait()
        self.play(Write(by_case_1))
        self.wait()
        self.play(
            FadeIn(f2[0]),
            *[
                TransformFromCopy(f1[i], f2[j + 1])
                for i, j in zip(
                    [1, 3, 4, 5, 6],
                    [6, 13, 14, 15, 16]
                )
            ],
            TransformFromCopy(f1[0], f2[1:6 + 1]),
            TransformFromCopy(f1[2], f2[7 + 1:13 + 1]),
            # LaggedStart(*[Write(f2[i+1]) for i in [6,13]]),
            run_time=4
        )
        self.wait()
        self.play(Write(by_case_1, rate_func=lambda t: smooth(1 - t)))
        self.wait()
        self.play(
            *[
                ApplyMethod(mob.fade, 0.7)
                for mob in [f2[i + 1] for i in [1, 8, 16]]
            ]
        )
        self.wait(2)
        self.play(
            *[
                TransformFromCopy(f2[i + 1], f3[j])
                for i, j in zip(
                    [2, 3, 4, 9, 10, 11, 13, 14, 15],
                    [*range(len(f3) - 1)]
                )
            ],
            Write(f3[-1]),
            # LaggedStart(*[Write(f2[i+1]) for i in [6,13]]),
            run_time=4
        )
        self.wait()
        self.play(
            *[
                TransformFromCopy(f3[i], f4[j])
                for i, j in zip(
                    [1, 2, 4, 5, 7, 8],
                    [2, 3, 5, 6, 0, 1]
                )
            ],
            Write(f4[4]),
            # LaggedStart(*[Write(f2[i+1]) for i in [6,13]]),
            run_time=4
        )
        self.wait()
        self.play(
            *[
                ReplacementTransform(f4[i].copy(), f5[j])
                for i, j in zip(
                    [0, 1, 2, 3, 4, 5, 6],
                    [0, 1, 2, 4, 5, 2, 6]
                )
            ],
            Write(f5[3]),
            Write(f5[-1]),
            # LaggedStart(*[Write(f2[i+1]) for i in [6,13]]),
            run_time=4
        )
        self.wait()
        self.play(
            *[
                ReplacementTransform(f5[i].copy(), f6[j])
                for i, j in zip(
                    [0, 1, 2],
                    [0, 1, 2]
                )
            ],
            TransformFromCopy(f5[-5:], f6[-1]),
            run_time=4
        )
        self.foreground_mobjects = []
        self.wait()
        self.play(
            Succession(
                FadeToColor(f6, YELLOW),
                FadeToColor(f6, PURPLE_A),
            ),
            AnimationGroup(
                #ShowCreationThenDestructionAround(f6.copy()),
                #ShowCreationThenDestructionAround(f6.copy()),
                ShowPassingFlash(f6.copy()),
                ShowPassingFlash(f6.copy()),
                lag_ratio=1
            )
        )
        # self.play(
        #     *[
        #         TransformFromCopy()
        #     ],
        # )
        # self.add(fg)
        # VGroup(case,*self.mobjects[start_index:]).set_color(TEAL)
        self.cases_group_2.add(fg, by_case_1)
        self.wait()

    def proof_3(self, case):
        print("Proof 3")
        dots = case[1]
        d1, d2, d3 = dots
        center = case[0]
        theta = case[-2]
        varphi = case[-1]
        self.add_foreground_mobject(dots)

        def fade_mobs(fade=0.9):
            def update(mob):
                mob.fade(fade)
                return mob

            return update

        # ---------------- FIGURES DEFINITION
        diameter_vector = Line(d3.get_center(), center.get_center()).get_vector()
        diameter = Line(d3.get_center(), d3.get_center() + diameter_vector * 2, color=RED_A)
        d4 = Dot(diameter.get_end())
        arc_psi_1 = ArcBetweenVectors(radius=0.6, d1=d2, d2=d4, center=d3, color=RED_A)
        arc_psi_2 = ArcBetweenVectors(radius=0.6, d1=d2, d2=d4, center=center, color=RED_A)
        arc_alpha_1 = ArcBetweenVectors(radius=0.7, d1=d1, d2=d4, center=d3, color=YELLOW_B, stroke_width=8)
        arc_alpha_2 = ArcBetweenVectors(radius=0.7, d1=d1, d2=d4, center=center, color=YELLOW_B, stroke_width=8)
        psi_1 = LabelFromArc(arc_psi_1, theta.get_height() * 0.8, "$\\psi_1$", color=RED_A, distance_proportion=2.1)
        psi_2 = LabelFromArc(arc_psi_2, theta.get_height() * 0.8, "$\\psi_2$", color=RED_A, distance_proportion=2.1)
        alpha_1 = LabelFromArc(arc_alpha_1, theta.get_height() * 0.8, "$\\alpha_1$", color=YELLOW_B,
                               distance_proportion=2.5)
        back_1 = BackgroundRectangle(alpha_1)
        alpha_2 = LabelFromArc(arc_alpha_2, theta.get_height() * 0.8, "$\\alpha_2$", color=YELLOW_B,
                               distance_proportion=2.3)
        back_2 = BackgroundRectangle(alpha_2)
        line_1 = Line(center.get_center(), d1.get_center(), color=varphi.get_color())
        line_2 = Line(d3.get_center(), d1.get_center(), color=varphi.get_color())
        # ---------
        psi_g = VGroup(arc_psi_1, arc_psi_2, psi_1, psi_2)
        alpha_g = VGroup(arc_alpha_1, arc_alpha_2, alpha_1, alpha_2)
        theta_g = VGroup(theta, varphi, case[-3], case[-4], case[2], case[3])
        self.wait()
        self.play(
            GrowFromCenter(diameter)
        )
        self.wait()
        self.play(
            LaggedStart(*[
                Write(arc)
                for arc in psi_g
            ]),
        )
        self.wait(2)
        self.play(
            *list(map(FadeIn, [back_1, back_2])),
            LaggedStart(*[
                Write(arc)
                for arc in alpha_g
            ]),
        )
        self.wait(2)
        self.add_foreground_mobjects(back_1, back_2, alpha_g)
        self.cases_group_3.add(
            arc_psi_1, arc_psi_2, arc_alpha_1, arc_alpha_2, diameter,
            psi_1, psi_2, alpha_1, alpha_2,
        )
        self.add(line_1, line_2)
        for i in [psi_g, theta_g]:
            for j in i:
                j.save_state()
        self.play(
            *[ApplyFunction(fade_mobs(), i) for i in psi_g],
            *[ApplyFunction(fade_mobs(), i) for i in theta_g],
        )
        self.wait()
        # self.play(
        #     Restore(psi_g),
        #     Restore(theta_g),
        # )
        # self.wait()
        # self.play(ApplyFunction(show_mobs(),psi_g))
        # ---------------- FORMULAS DEFINITION
        formulas = [
            ["\\alpha_1", "=", "\\psi_1", "+", "\\theta"],
            ["\\alpha_2", "=", "\\psi_2", "+", "\\varphi"],
            ["\\alpha_2", "=", "2", "\\alpha_1"],
            ["\\psi_2", "+", "\\varphi", "=", "2", "(", "\\psi_1", "+", "\\theta", ")"],
            ["\\psi_2", "=", "2", "\\psi_1"],
            ["2", "\\psi_1", "+", "\\varphi", "=", "2", "\\psi_1", "+", "2", "\\theta"],
            ["\\varphi", "=", "2", "\\theta"],
        ]
        tex_formulas_kwargs = {
            "tex_to_color_map": {
                "$\\psi_1$": psi_1.get_color(), "$\\psi_2$": psi_2.get_color(), "$\\varphi$": varphi.get_color(),
                "$\\theta$": theta.get_color(), "$\\alpha_1$": alpha_1.get_color(), "$\\alpha_2$": alpha_2.get_color()
            }
        }
        f = VGroup(*[
            MathTex(*formula, **tex_formulas_kwargs)
            for formula in formulas
        ])
        f.arrange(DOWN)
        f.scale(1.3)
        for fi, i in zip(f[1:], [1, 1, 3, 1, 4, 1]):
            self.align_formulas_with_equal(fi, f[0], i, 1)
        f.to_edge(RIGHT, buff=1.8)
        # --------------------------------------
        by_case_1 = Tex("By case 1")
        by_case_1.next_to(f[2], RIGHT)
        by_case_2 = by_case_1.copy()
        by_case_2.next_to(f[4], RIGHT)
        # ----------- FORMULAS ANIMATIONS
        self.play(
            FadeOut(back_1),
            Restore(theta),
            Restore(psi_1),
            ReplacementTransform(alpha_1[0], f[0][0]),
            run_time=2,
        )
        self.play(
            TransformFromCopy(psi_1[0], f[0][2]),
            TransformFromCopy(theta[0], f[0][-1]),
            *[Write(f[0][i]) for i in [1, 3]],
            run_time=3,
        )
        self.wait()
        self.play(
            FadeOut(back_2),
            Restore(varphi),
            Restore(psi_2),
            ReplacementTransform(alpha_2[0], f[1][0]),
            run_time=2,
        )
        self.play(
            TransformFromCopy(psi_2[0], f[1][2]),
            TransformFromCopy(varphi[0], f[1][-1]),
            *[Write(f[1][i]) for i in [1, 3]],
            run_time=3,
        )
        self.wait()
        # By case 1 - 1
        self.play(
            Write(by_case_1)
        )
        self.wait()
        self.play(
            Write(f[2])
        )
        self.wait()
        # -----------------
        self.play(
            TransformFromCopy(f[0][-3:], f[3][6:9]),
            TransformFromCopy(f[1][-3:], f[3][:3]),
            *[
                TransformFromCopy(f[2][i], f[3][j])
                for i, j in zip(
                    [1, 2],
                    [3, 4]
                )
            ],
            *[Write(f[3][i]) for i in [5, 9]],
            run_time=3
        )
        self.wait()
        # ---------------------------
        self.wait()
        line_3 = Line(d3.get_center(), d2.get_center(), color=TEAL_A)
        line_4 = Line(center.get_center(), d2.get_center(), color=PURPLE_A)
        save_grp = VGroup(arc_alpha_1, arc_alpha_2, varphi, theta)
        for i in save_grp:
            try:
                i.save_state()
            except:
                pass
        self.play(
            FadeOut(line_1),
            FadeOut(line_2),
            # line_1.fade,1,
            # line_2.fade,1,
            FadeIn(line_3),
            FadeIn(line_4),
            *[ApplyMethod(i.fade, 0.92) for i in save_grp],
            *[Restore(i) for i in [arc_psi_1, arc_psi_2]]
        )
        self.wait(3)
        # by case 2
        self.play(
            Write(by_case_2)
        )
        self.wait()
        self.play(
            Write(f[4])
        )
        self.wait(3)
        self.play(
            *[Restore(i) for i in [*save_grp, *case[2:6]]]
        )
        self.wait()
        # ---------------------------
        self.play(
            # TransformFromCopy(f[3][-3:],f[5][6:9]),
            TransformFromCopy(f[3][0], f[5][:2]),
            *[
                TransformFromCopy(f[3][i], f[5][j])
                for i, j in zip(
                    [1, 2, 3, 4, 6, 7, 8, 4],
                    [2, 3, 4, 5, 6, 7, 9, 8]
                )
            ],
            run_time=3
        )
        self.wait()
        self.play(
            *[ApplyMethod(f[5][i].fade, 0.8) for i in [0, 1, 5, 6]],
            run_time=2
        )
        self.play(
            *[
                TransformFromCopy(f[5][i], f[6][j])
                for i, j in zip(
                    [3, 4, 8, 9],
                    [0, 1, 2, 3]
                )
            ],
            run_time=3
        )
        # self.play(
        #     *{Restore(i) for i in [case[2],case[3]]}
        # )

        # self.add(f,by_case_1,by_case_2)

        self.play(
            Succession(
                FadeToColor(f[6], YELLOW),
                FadeToColor(f[6], PURPLE_A),
            ),
            AnimationGroup(
                #ShowCreationThenDestructionAround(f[6].copy()),
                #ShowCreationThenDestructionAround(f[6].copy()),
                ShowPassingFlash(f[6].copy()),
                ShowPassingFlash(f[6].copy()),
                lag_ratio=1
            )
        )
        self.cases_group_3.add(line_1, line_2, line_3, line_4, by_case_1, by_case_2, f)
        self.wait()

    def align_formulas_with_equal(self, f1, f2, i1, i2):
        c1 = f1[i1].get_center()
        c2 = f2[i2].get_center()
        distance = c2 - c1
        f1.shift(RIGHT * distance[0])

    def get_screen_rect(self):
        return Rectangle(width=FRAME_WIDTH, height=FRAME_HEIGHT)



with tempconfig({"quality": "medium_quality"}):
    scene = InscribedAngle()
    scene.render()