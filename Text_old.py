from manim import *

myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
standard_font_size = 20
standard_para_width = 4

HOME = "C:/Users/zoumi/Documents/GitHub/manim-general-projects/CalcImage"


def StringToTex(string, my_font_size=standard_font_size, paragraph_width=standard_para_width, my_color=WHITE):
    return Tex(
            "\\justifying \parbox{FILLERin}{STRING}".replace("FILLER", str(paragraph_width)).replace("STRING", string),
            tex_template=myTemplate,
            font_size=my_font_size,
            color=my_color)

class SquareToCircle(Scene):



    def construct(self):
        #talking_face = ImageMobject(f"{HOME}/talking.gif").set_width(2)
        #talking_face.scale(0.5)
        #talking_face.to_edge(UL, buff=0.5)

        T1 = ["Well, Calculus might be the most important subject in math.", 0]
        T2 = ["As you might know, Newton is remembered as the most greatest scientist, but some people believe that his most important achievement is on calculus.", 0]
        T3 = ["British people are quite proud for Newton's achievement.", 0]
        T4 = ["But folks in the European Continent are not quite happy with that and they claimed that German mathematician Leibniz should take that credit and argued for a long time with British people in history.", 0]
        T5 = ["I wish I were as enthusiastic like you on calculus.  But can you briefly explain what it is about.", 1]
        T6 = ["Generally speaking, it is hard to summarize in one sentence what a math subject is about, especially for beginners.  Calculus is however special.", 0]

        TLines = [T1, T2, T3, T4, T5, T6]

        TTex = []
        for i in range(len(TLines)):
            if TLines[i][1] == 0:
                TTex.append(StringToTex(TLines[i][0], my_color=BLUE))
            else:
                TTex.append(StringToTex(TLines[i][0], my_color=RED))

            if i == 0:

                TTex[i].to_edge(UP, buff=2.0)
                if TLines[i][1] == 0:
                    TTex[i].to_edge(LEFT, buff=0.5)
                else:
                    TTex[i].to_edge(RIGHT, buff=0.5)
            else:
                TTex[i].next_to(TTex[i-1], DOWN)
                if TLines[i][1] == 0:
                    TTex[i].to_edge(LEFT, buff=0.5)
                else:
                    TTex[i].to_edge(RIGHT, buff=0.5)

        g = VGroup(*TTex)

        #self.add(talking_face)
        for i in range(len(TTex)):
            self.play(FadeIn(TTex[i]))
            self.wait(1)

        self.wait(2)

        #self.play(FadeOut(g))
        self.wait(2)
