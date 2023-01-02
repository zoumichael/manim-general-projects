from const import *
from IntroToInfiniteWorld_text_short_v2 import tls, animations, pos_start, pos_end
from ZenoParadox import ZenoAnimation
from StringToTex import StringToTex
from manim import *

#myTemplate = TexTemplate()
#myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
#myTemplate.add_to_preamble(r"\usepackage{xcolor}")


class template(Scene):
    def construct(self):
        text_array = []
        for tls_entry in tls:
            temp_group = VGroup(*[
                            StringToTex(tls_entry[0][i], color_map[tls_entry[2]], font_size_map[tls_entry[2]]) for i in range(len(tls_entry[0]))
                         ])

            for i in range(len(temp_group)):
                if i == 0:
                    if tls_entry[2] == TEA:
                        temp_group[i].to_edge(UL, buff=0.5)
                    elif tls_entry[2] == STU:
                        temp_group[i].to_edge(UR, buff=0.5)
                    elif tls_entry[2] == TIT:
                        temp_group[i].move_to(ORIGIN)
                    elif tls_entry[2] == AIM:
                        temp_group[i].to_edge(UP, buff=0.5)
                elif i != 0:
                    temp_group[i].next_to(temp_group[i-1], DOWN)
            text_array.append(temp_group)

        '''
        labels = VGroup(*[
            StringToTex(label[0], color_map[label[2]], font_size_map[label[2]]) for label in tls
        ])
        current_student = []
        previous_student = []
        current_teacher = []
        previous_teacher = []
        current_bottom = []
        previous_bottom = []
        buff_size = 0.5
        for i in range(len(labels)):
            if tls[i][2] == TEA:
                labels[i].to_edge(UL, buff=0.5)
            elif tls[i][2] == STU:
                labels[i].to_edge(UR, buff=0.5)
            elif tls[i][2] == TIT:
                labels[i].move_to(ORIGIN)
        '''
        ''''''

        label_anchor = []
        group_this = []
        index = 0
        while index < len(text_array):
            if index in animations.keys():
                labels_anim = text_array[pos_start[animations[index]]: pos_end[animations[index]]]

                if animations[index] == 'zeno_anim_false':
                    temp = self.zeno_anim(labels_anim, False).get_zeno_group()
                elif animations[index] == 'zeno_anim_true':
                    temp = self.zeno_anim(labels_anim, True).get_zeno_group()
                self.wait(1)
                self.play(FadeOut(temp))
                index = index + (pos_end[animations[index]] - pos_start[animations[index]])
            else:
                for line in text_array[index]:
                    self.play(Write(line))
                self.play(FadeOut(text_array[index]))
                index = index + 1
        '''
        for i in range(len(text_array)):
            if i in animations.keys():
                animation_pos_this = pos_end[animations[i]]
                labels_anim = text_array[pos_start[animations[i]]: pos_end[animations[i]]]

                if animations[i] == 'zeno_anim_false':
                    temp = self.zeno_anim(labels_anim, False).get_zeno_group()
                elif animations[i] == 'zeno_anim_true':
                    temp = self.zeno_anim(labels_anim, True).get_zeno_group()
                self.wait(1)
                self.play(FadeOut(temp))
                if i>=
                i = pos_end[animations[i]]
            else:
                for line in text_array[i]:
                    self.play(Write(line, run_time=4))
                self.play(FadeOut(text_array[i]))
'''
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
                self.play(Write(tex_obj))
                self.wait(1)
            self.play(
                Create(zeno.get_t_lines_at(index)),
                Create(zeno.get_a_lines_at(index)),
                MoveAlongPath(zeno.get_tort(), zeno.get_t_lines_at(index)),
                MoveAlongPath(zeno.get_ach(), zeno.get_a_lines_at(index))
            )
            self.add(zeno.get_d_at(zeno.get_dot_index_at(index + 1, 0)),
                     zeno.get_d_at(zeno.get_dot_index_at(index + 1, 1)))
            self.add(zeno.get_t_points_at(index + 1), zeno.get_a_points_at(index + 1))

            if is_explain:
                self.add(zeno.get_a_braces_at(index), zeno.get_t_braces_at(index))
                self.add(zeno.get_a_distances_at(index), zeno.get_t_distances_at(index))
                self.add(zeno.get_a_times_at(index), zeno.get_t_times_at(index))
            self.wait(2)
            self.play(FadeOut(labels_anim[counter]))
            counter = counter + 1
        # self.play(zeno.get_zeno_group().animate.shift(UP * 2))
        return zeno



with tempconfig({"quality": "medium_quality"}):
    scene = template()
    scene.render()

