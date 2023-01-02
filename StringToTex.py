from manim import *
#from const import *
#from IntroToInfiniteWorld_text import *
myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{ragged2e}")
myTemplate.add_to_preamble(r"\usepackage{xcolor}")
from const import standard_font_size, standard_para_width, color_teacher
#def StringToTex(string, my_font_size=standard_font_size, paragraph_width=standard_para_width, my_color=WHITE, my_font=font_teacher):
def StringToTex(string, my_color=color_teacher, my_font_size=standard_font_size, paragraph_width=standard_para_width, direction='\\justifying'):
    return Tex(
            "DIRECT\parbox{FILLERin}{STRING}".replace("FILLER", str(paragraph_width)).replace("STRING", string).replace('DIRECT', direction),
            tex_template=myTemplate,
            font_size=my_font_size,
            color=my_color)
            #font=my_font)