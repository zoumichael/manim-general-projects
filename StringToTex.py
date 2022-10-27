#from manim import *
#from const import *
from IntroToInfiniteWorld_text import *
myTemplate = TexTemplate()
myTemplate.add_to_preamble(r"\usepackage{ragged2e}")

def StringToTex(string, my_font_size=standard_font_size, paragraph_width=standard_para_width, my_color=WHITE):
    return Tex(
            "\\justifying \parbox{FILLERin}{STRING}".replace("FILLER", str(paragraph_width)).replace("STRING", string),
            tex_template=myTemplate,
            font_size=my_font_size,
            color=my_color)