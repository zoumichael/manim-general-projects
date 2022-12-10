
from const import *
from IntroToInfiniteWorld_text_short import tls, annimiations, group_ends
#from IntroToInfiniteWorld_text import tls, annimiations, group_ends
from ZenoParadox import ZenoAnimation
from process_tex_array import process_tex_array
from StringToTex import StringToTex

class Intro_Limit(Scene):
    def construct(self):
        #talking_face = ImageMobject(f"{HOME}/talking.gif").set_width(2)
        #talking_face.scale(0.5)
        #talking_face.to_edge(UL, buff=0.5)

        temp = None
        #TLines = tls#[L0, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10]

        #group_ends = [0, 3, 5, len(TLines)]
        for i in range(len(tls)):
            if tls[i][2] == TIT:
                [font_size_this, color_this, font_this] = [title_font_size, color_title, font_title]
            elif tls[i][2] == STA:
                [font_size_this, color_this, font_this] = [statement_font_size, color_statement, font_statement]
            elif tls[i][2] == REM:
                [font_size_this, color_this, font_this] = [remark_font_size, color_remark, font_remark]
            elif tls[i][2] == EQU:
                [font_size_this, color_this, font_this] = [equation_font_size, color_equation, font_equation]
            elif tls[i][2] == DEF:
                [font_size_this, color_this, font_this] = [definition_font_size, color_definition, font_definition]
            elif tls[i][2] == PRO:
                [font_size_this, color_this, font_this] = [proof_font_size, color_proof, font_proof]
            else:
                [font_size_this, color_this, font_this] = [teacher_font_size, color_teacher, font_teacher]
            line_current = StringToTex(tls[i][0], my_font_size=font_size_this, my_color=color_this, my_font=font_this)
            if tls[i][2] == TIT:
                line_current.to_edge(UP, buff=2.0)
            elif tls[i][2] == NOR and tls[i][1] == TV:
                line_current.to_corner(DOWN + LEFT, buff=0.5)
            elif tls[i][2] == NOR and tls[i][1] == SV:
                line_current.to_corner(DOWN + RIGHT, buff=0.5)
            elif tls[i][2] == DEF:
                line_current.to_edge(LEFT, buff=0.5)
            elif tls[i][2] == EQU:
                line_current.to_edge(RIGHT, buff=0.5)
            self.play(
                Write(line_current),
                #FadeIn(basel, shift=DOWN),
            )
            self.wait()
            if i<len(tls)-1:
                if tls[i+1][2] == TIT:
                    [font_size_this, color_this, font_this] = [title_font_size, color_title, font_title]
                elif tls[i+1][2] == STA:
                    [font_size_this, color_this, font_this] = [statement_font_size, color_statement, font_statement]
                elif tls[i+1][2] == REM:
                    [font_size_this, color_this, font_this] = [remark_font_size, color_remark, font_remark]
                elif tls[i+1][2] == EQU:
                    [font_size_this, color_this, font_this] = [equation_font_size, color_equation, font_equation]
                elif tls[i+1][2] == DEF:
                    [font_size_this, color_this, font_this] = [definition_font_size, color_definition, font_definition]
                elif tls[i+1][2] == PRO:
                    [font_size_this, color_this, font_this] = [proof_font_size, color_proof, font_proof]
                else:
                    [font_size_this, color_this, font_this] = [teacher_font_size, color_teacher, font_teacher]
                line_next = StringToTex(tls[i+1][0], my_font_size=font_size_this, my_color=color_this, my_font=font_this)
                if tls[i+1][2] == TIT:
                    line_next.to_edge(UP, buff=2.0)
                elif tls[i+1][2] == NOR and tls[i][1] == TV:
                    line_next.to_corner(DOWN + LEFT, buff=0.5)
                elif tls[i+1][2] == NOR and tls[i][1] == SV:
                    line_next.to_corner(DOWN + RIGHT, buff=0.5)
                elif tls[i+1][2] == DEF:
                    line_next.to_edge(LEFT, buff=0.5)
                elif tls[i+1][2] == EQU:
                    line_next.to_edge(RIGHT, buff=0.5)
                self.play(
                    Transform(line_current, line_next),
                )
                self.wait()



with tempconfig({"quality": "medium_quality"}):
    #scene = UsingBraces()
    scene = Intro_Limit()
    scene.render()



