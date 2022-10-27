
from StringToTex import StringToTex
from const import *

def process_tex_array(lines, top=None):
    texes = []
    reference_index = -1

    for index in range(len(lines)):
        if lines[index][2] == NOR or lines[index][2] == TIT or lines[index][2] == TOP or lines[index][2] == EQU:
            if lines[index][1] == 0:
                if lines[index][2] == TIT:
                    texes.append(StringToTex(lines[index][0],my_font_size=title_font_size, my_color=TC))
                else:
                    texes.append(StringToTex(lines[index][0], my_color=TC))
            elif lines[index][1] == 1:
                if lines[index][2] == TIT:
                    texes.append(StringToTex(lines[index][0], my_font_size=title_font_size, my_color=SC))
                else:
                    texes.append(StringToTex(lines[index][0], my_color=SC))
            else:
                print(str(lines[index][1]) + " is not valid.")
                exit(1)

            if reference_index == -1:
                if top == None:
                    texes[index].to_edge(UP, buff=2.0)
                    #texes[index].to_edge(LEFT, buff=0.5)
                else:
                    texes[index].next_to(top,DOWN)

            else:
                texes[index].next_to(texes[reference_index], DOWN)
                #texes[index].to_edge(LEFT, buff=0.5)

            reference_index = index
        else:
            texes.append(StringToTex(lines[index][0], my_color=TC))
            if reference_index != -1:
                texes[index].next_to(texes[reference_index], RIGHT * 2)
            else:
                texes[index].to_edge(UP, buff=2.0)
                texes[index].to_edge(RIGHT, buff=0.5)
    return texes