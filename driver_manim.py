from const import *
from manim import *

from IntroToInfiniteWorld_text_v2 import tls, animations, pos_start, pos_end
from StringToTex import StringToTex
from ZenoParadox import ZenoAnimation


class Driver(Scene):
    def construct(self):
        #smirk = ImageMobject("img/smirk.png")
        student_figure = ImageMobject("img/po.jpg")
        student_figure.scale(1)
        student_figure.to_edge(UL, buff=0.25)
        #thinking = ImageMobject("img/thinking.png")
        teacher_figure = ImageMobject("img/shifu.jpg")
        teacher_figure.scale(1)
        teacher_figure.to_edge(UR, buff=0.25)

        # 1-D list with VGroups of Tex Objects as each .
        text_array = []
        left_teacher_anchor = StringToTex("left-teacher-anchor-xxxxx-xxxxx-xxxxx-xxxxx-xxxxx")
        left_teacher_anchor.to_edge(LEFT, buff=1.5)
        left_teacher_anchor.to_edge(UP, buff=0.5)

        middle_teacher_anchor = StringToTex("middle-teacher-anchor-xxxxx-xxxxx-xxxxx-xxxxx-xxxxx")
        middle_teacher_anchor.to_edge(LEFT, buff=2.5)
        middle_teacher_anchor.to_edge(UP, buff=0.5)

        right_student_anchor = StringToTex("right student anchor-xxxxx-xxxxx-xxxxx-xxxxx-xxxxx")
        right_student_anchor.to_edge(LEFT, buff=1.5)
        right_student_anchor.to_edge(UP, buff=0.5)

        middle_student_anchor = StringToTex(r"middle student anchor-xxxxx-xxxxx-xxxxx-xxxxx-xxxxx")
        middle_student_anchor.to_edge(LEFT, buff=2.5)
        middle_student_anchor.to_edge(UP, buff=0.5)

        for tls_entry in tls:
            # Create every Tex Object and put them in a VGroup.
            this_group = VGroup(*[
                StringToTex(
                    tls_entry[temp][0],
                    color_map[tls_entry[temp][2]],
                    font_size_map[tls_entry[temp][1]]
                ) for temp in range(len(tls_entry))
            ])

            for vgroup_item in range(len(this_group)):
                # If it is the first item in the group, put it in the appropriate location.
                if vgroup_item == 0:
                    if tls_entry[vgroup_item][2] == TEA:
                        this_group[0].to_edge(UL, buff=1.5)
                    elif tls_entry[vgroup_item][2] == STU:
                        this_group[0].to_edge(UL, buff=1.5)
                    elif tls_entry[vgroup_item][2] == TIT:
                        this_group[0].move_to(ORIGIN)
                    elif tls_entry[vgroup_item][2] == AIM:
                        this_group[0].to_edge(UP, buff=1.5)
                    else:
                        this_group[0].to_edge(UL, buff=1.5)
                # Otherwise, put it under the previous item in the appropriate location.
                else:
                    this_group[vgroup_item].next_to(this_group[vgroup_item - 1], DOWN)
                    if tls_entry[vgroup_item][2] == TEA:
                        if tls_entry[vgroup_item][1] == att1_normal:
                            this_group[vgroup_item].align_to(left_teacher_anchor, LEFT)
                        elif tls_entry[vgroup_item][1] == att1_equ:
                            this_group[vgroup_item].align_to(middle_teacher_anchor, LEFT)
                    elif tls_entry[vgroup_item][2] == STU:
                        if tls_entry[vgroup_item][1] == att1_normal:
                            this_group[vgroup_item].align_to(right_student_anchor, LEFT)
                        elif tls_entry[vgroup_item][1] == att1_equ:
                            this_group[vgroup_item].align_to(middle_student_anchor, LEFT)
                    elif tls_entry[vgroup_item][2] == TIT:
                        pass
                    else:
                        if tls_entry[vgroup_item][1] == att1_normal:
                            this_group[vgroup_item].align_to(left_teacher_anchor, LEFT)
                        elif tls_entry[vgroup_item][1] == att1_equ:
                            this_group[vgroup_item].align_to(middle_teacher_anchor, LEFT)

            text_array.append(this_group)

        index = 0
        while index < len(text_array):
            curr_speaker = "new"
            faces = Group()

            if index in animations.keys():
                labels_anim = text_array[pos_start[animations[index]]: pos_end[animations[index]]]

                if animations[index] == 'zeno_anim_false':
                    temp = self.zeno_anim(labels_anim, False).get_zeno_group()
                elif animations[index] == 'zeno_anim_true':
                    temp = self.zeno_anim(labels_anim, True).get_zeno_group()
                self.wait(simulation_step_waiting_time)
                self.play(FadeOut(temp))
                index = index + (pos_end[animations[index]] - pos_start[animations[index]])
            else:
                for line in range(len(text_array[index])):
                    speaker = tls[index][line][2]
                    if speaker != curr_speaker:
                        if speaker == TEA:
                            temp_face = teacher_figure.copy()
                            temp_face.next_to(text_array[index][line], LEFT)
                            faces.add(temp_face)
                            self.add(temp_face)
                        elif speaker == STU:
                            temp_face = student_figure.copy()
                            temp_face.next_to(text_array[index][line], LEFT)
                            faces.add(temp_face)
                            self.add(temp_face)
                        if speaker == TEA or speaker == STU:
                            curr_speaker = speaker

                    run_time = len(tls[index][line][0])/speaking_speed_per_second
                    self.play(Write(text_array[index][line]), run_time=run_time)
                    self.wait(line_waiting_time)
                self.play(FadeOut(text_array[index]), FadeOut(faces))
                index = index + 1


    def zeno_anim(self, labels_anim, is_explain):
        counter = 0
        zeno = ZenoAnimation(is_explain)
        zeno.get_zeno_group().scale(0.5)
        zeno.get_zeno_group().shift(DOWN*2)
        # zeno.get_zeno_group().next_to(location_object, DOWN)

        self.add(zeno.get_t_line())
        self.add(zeno.get_a_line())

        self.add(zeno.get_d_at(8), zeno.get_d_at(17))
        # self.add_foreground_mobjects(zeno.get_ach(), zeno.get_tort())
        self.add(zeno.get_ach(), zeno.get_tort())

        self.add(zeno.get_t_lines_at(0), zeno.get_a_lines_at(0))

        self.add(zeno.get_t_points_at(0), zeno.get_a_points_at(0))
        for index in range(zeno.get_t_lines_len()):
            for tex_obj in labels_anim[counter]:
                run_time = len(tex_obj[0])/speaking_speed_per_second
                self.play(Write(tex_obj), run_time=run_time)
                self.wait(line_waiting_time)
            self.play(
                Create(zeno.get_t_lines_at(index)),
                Create(zeno.get_a_lines_at(index)),
                MoveAlongPath(zeno.get_tort(), zeno.get_t_lines_at(index), run_time=line_run_time),
                MoveAlongPath(zeno.get_ach(), zeno.get_a_lines_at(index), run_time=line_run_time)
            )
            self.add(zeno.get_d_at(zeno.get_dot_index_at(index + 1, 0)),
                     zeno.get_d_at(zeno.get_dot_index_at(index + 1, 1)))
            self.add(zeno.get_t_points_at(index + 1), zeno.get_a_points_at(index + 1))

            if is_explain:
                self.add(zeno.get_a_braces_at(index), zeno.get_t_braces_at(index), run_time=line_run_time)
                self.add(zeno.get_a_distances_at(index), zeno.get_t_distances_at(index), run_time=line_run_time)
                self.add(zeno.get_a_times_at(index), zeno.get_t_times_at(index), run_time=line_run_time)
            self.wait(line_waiting_time)
            self.play(FadeOut(labels_anim[counter]))
            counter = counter + 1
        # self.play(zeno.get_zeno_group().animate.shift(UP * 2))
        return zeno


with tempconfig({"quality": "medium_quality"}):
    scene = Driver()
    scene.render()