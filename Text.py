
from const import *
from IntroToInfiniteWorld_text_short import tls, annimiations, group_ends
from ZenoParadox import ZenoAnimation
from process_tex_array import process_tex_array

class SquareToCircle(Scene):
    def construct(self):
        #talking_face = ImageMobject(f"{HOME}/talking.gif").set_width(2)
        #talking_face.scale(0.5)
        #talking_face.to_edge(UL, buff=0.5)

        '''
        T1 = ["Well, Calculus might be the most important subject in math.", 0]
        T2 = ["As you might know, Newton is remembered as the most greatest scientist, but some people believe that his most important achievement is on calculus.", 0]
        T3 = ["British people are quite proud for Newton's achievement.", 0]
        T4 = ["But folks in the European Continent are not quite happy with that and they claimed that German mathematician Leibniz should take that credit and argued for a long time with British people in history.", 0]
        T5 = ["I wish I were as enthusiastic like you on calculus.  But can you briefly explain what it is about.", 1]
        T6 = ["Generally speaking, it is hard to summarize in one sentence what a math subject is about, especially for beginners.  Calculus is however special.", 0]
        '''
        temp = None
        #TLines = tls#[L0, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10]

        #group_ends = [0, 3, 5, len(TLines)]

        for num in range(len(group_ends)-1):
            grp_lines = tls[group_ends[num]:group_ends[num+1]]
            grp_texes = process_tex_array(grp_lines, temp)

            grp_of_grp_texes = VGroup(*grp_texes)

            if num not in annimiations.keys():
                g = VGroup(*grp_texes)



            for line in range(len(grp_texes)):
                self.play(FadeIn(grp_texes[line]))
                self.wait(1)

            if num not in annimiations.keys():
                self.play(FadeOut(g))
                self.wait(1)

            if num in annimiations.keys():
                if annimiations[num] == 'zeno_anim_false':
                    temp = self.zeno_anim(False, grp_of_grp_texes).get_zeno_group()
                elif annimiations[num] == 'zeno_anim_true':
                    temp = self.zeno_anim(True, grp_of_grp_texes).get_zeno_group()
                else:
                    print('invalid simulation scen' + annimiations[num])
                    exit(1)

                g = VGroup(*grp_texes, temp)
                self.play(FadeOut(g))
                temp = None
            else:
                if temp != None:
                    self.play(FadeOut(temp))
                temp = None


    def zeno_anim(self, is_explain, location_object):
        print("Here")
        zeno = ZenoAnimation(is_explain)
        zeno.get_zeno_group().scale(0.5)
        zeno.get_zeno_group().next_to(location_object, DOWN)

        self.add(zeno.get_t_line())
        self.add(zeno.get_a_line())

        self.add(zeno.get_d_at(8), zeno.get_d_at(17))
        #self.add_foreground_mobjects(zeno.get_ach(), zeno.get_tort())
        self.add(zeno.get_ach(), zeno.get_tort())

        self.add(zeno.get_t_lines_at(0), zeno.get_a_lines_at(0))
        self.add(zeno.get_t_points_at(0), zeno.get_a_points_at(0))
        for index in range(zeno.get_t_lines_len()):
            self.play(
                Create(zeno.get_t_lines_at(index)),
                Create(zeno.get_a_lines_at(index)),
                MoveAlongPath(zeno.get_tort(), zeno.get_t_lines_at(index)),
                MoveAlongPath(zeno.get_ach(), zeno.get_a_lines_at(index))
            )
            self.add(zeno.get_d_at(zeno.get_dot_index_at(index + 1, 0)), zeno.get_d_at(zeno.get_dot_index_at(index + 1, 1)))
            self.add(zeno.get_t_points_at(index + 1), zeno.get_a_points_at(index + 1))

            if is_explain:
                self.add(zeno.get_a_braces_at(index), zeno.get_t_braces_at(index))
                self.add(zeno.get_a_distances_at(index), zeno.get_t_distances_at(index))
                self.add(zeno.get_a_times_at(index), zeno.get_t_times_at(index))
            self.wait(1)
        #self.play(zeno.get_zeno_group().animate.shift(UP * 2))
        return zeno


