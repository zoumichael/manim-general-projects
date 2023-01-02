from manim import *
#standard_font_size = 32
#standard_para_width = 3

font_teacher="Arial"
font_student="Consolas"
font_statement="Consolas"
font_title = "Arial"
font_remark = "Arial"
font_definition = "Arial"
font_equation = "Arial"
font_proof = "Arial"

color_statement = YELLOW
color_title = PURPLE
color_teacher = BLUE
color_student = YELLOW_A
color_remark = YELLOW_B
color_definition = YELLOW_C
color_equation = LIGHT_PINK
color_emphasize = LIGHT_PINK
color_proof = YELLOW_D
color_default = BLUE
color_animation = PURPLE

standard_font_size = 30
standard_para_width = 5


HOME = "C:/Users/zoumi/Documents/GitHub/manim-general-projects/CalcImage"
#TV = 0 # Teacher
#SV = 1 # Student
att1_normal = 0
att1_question = 1
att1_happy = 2
att1_patience = 3
att1_understand = 4
att1_default = 5
att1_equ = 6
NOT = 1 #notation
TIT = 2  #title
EQU = 3
TOP = 4 # topic
DEF = 5 #definition
THM = 6 #theorm/proposition
REM = 7 #remark
REF = 8 # reference and footnote
PRO = 9 #proof
STA = 10 #statement
EXA = 11 #example
AIM = 12 #animation
TEA = 13 #teacher
STU = 14 #Student

color_map = {TEA: color_teacher, STU:color_student, TIT:color_title, EQU:color_equation, DEF:color_definition,
                 REM:color_remark, STA:color_statement, NOT:color_definition, TOP:color_title,
                 THM:color_definition, REF:color_remark, PRO:color_proof, EXA:color_proof, AIM:color_animation}


title_font_size = 40
statement_font_size = 30
teacher_font_size = 20
student_font_size = 20
remark_font_size = 20
definition_font_size = 25
equation_font_size = 25
proof_font_size = 25
default_large_font_size = 40
default_middle_font_size = 30
default_small_font_size = 20


speaking_speed_per_second = 20

font_size_map = {
                att1_default:default_middle_font_size,
                att1_normal:default_middle_font_size,
                att1_happy:default_large_font_size,
                att1_patience:default_large_font_size,
                att1_understand:default_large_font_size,
                att1_equ:default_large_font_size
                }

line_waiting_time = 1
line_run_time = 3
simulation_step_waiting_time = 3

HOME = "C:/Users/zoumi/Documents/GitHub/manim-general-projects/CalcImage"