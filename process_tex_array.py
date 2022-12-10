
from StringToTex import StringToTex
from const import *

def process_tex_array(lines, top=None):
    texes = []
    reference_index = -1

    for index in range(len(lines)):
        #if lines[index][2] == NOR or lines[index][2] == TIT or lines[index][2] == TOP or lines[index][2] == EQU:
        if lines[index][2] == TIT:
            texes.append(
                StringToTex(lines[index][0], my_font_size=title_font_size, my_color=color_title, my_font=font_title))
        elif lines[index][1] == TV:
            if lines[index][2] == STA:
                texes.append(StringToTex(lines[index][0], my_font_size=statement_font_size, my_color=color_statement, my_font=font_statement))
            elif lines[index][2] == REM:
                texes.append(StringToTex(lines[index][0], my_font_size=remark_font_size, my_color=color_remark, my_font=font_remark))
            elif lines[index][2] == EQU:
                texes.append(StringToTex(lines[index][0], my_font_size=equation_font_size, my_color=color_equation, my_font=font_equation))
            elif lines[index][2] == DEF:
                texes.append(StringToTex(lines[index][0], my_font_size=definition_font_size, my_color=color_definition, my_font=font_definition))
            elif lines[index][2] == PRO:
                texes.append(StringToTex(lines[index][0], my_font_size=proof_font_size, my_color=color_proof, my_font=font_proof))
            else:
                texes.append(StringToTex(lines[index][0], my_font_size=teacher_font_size,my_color=color_teacher, my_font=font_teacher))
        elif lines[index][1] == SV:
            texes.append(StringToTex(lines[index][0], my_font_size=student_font_size, my_color=color_student, my_font=font_student))
        else:
            print(str(lines[index][1]) + " is not valid.")
            exit(1)

        if reference_index == -1:
            if top == None:
                texes[index].to_edge(UP, buff=2.0)
                #texes[index].to_edge(LEFT, buff=0.5)
                if lines[index][2] == NOR:
                    texes[index].to_edge(LEFT, buff=0.5)
                else:
                    texes[index].to_edge(LEFT * 2, buff=0.5)
            else:
                texes[index].next_to(top,DOWN)
                if lines[index][2] == NOR:
                    texes[index].to_edge(LEFT, buff=0.5)
                else:
                    texes[index].to_edge(LEFT * 2, buff=0.5)

        else:
            texes[index].next_to(texes[reference_index], DOWN)
            if lines[index][2] == NOR:
                texes[index].to_edge(LEFT, buff=0.5)
            else:
                texes[index].to_edge(LEFT * 2, buff=0.5)
        reference_index = index
        '''
        else:
            texes.append(StringToTex(lines[index][0], my_color=TC, my_font=font_teacher))
            if reference_index != -1:
                texes[index].next_to(texes[reference_index], RIGHT * 2)
            else:
                texes[index].to_edge(UP, buff=2.0)
                texes[index].to_edge(RIGHT, buff=0.5)
        '''
    return texes