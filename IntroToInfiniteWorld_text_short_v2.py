from const import *

tls = []
animations = {}
count = 0
pos_start = {}
pos_end ={}

#test 1
tls = tls + [[
                [r"The core concept in calculus:  limit", att1_happy, TIT],
                [r"the bridge to the infinite world", att1_normal, TIT]
            ]]
count = count + 1

tls = tls + [[
                [r"Each time he reaches to the previous position of the tortoise,", att1_normal, TEA],
                [r"the tortoise has moved forward to a new position ahead of him as demonstrated next.", att1_normal, TEA]
            ]]
count = count + 1

anim_name_1 = 'zeno_anim_false'
animations[count] = anim_name_1
pos_start[anim_name_1] = count

tls = tls + [[
                [r"We see that Achilles and the tortoise start at two positions $A_0$ and $T_0$ respectively.", att1_normal, AIM],
                [r"Then the tortoise moves ahead to $T_{1}$ when Achilles catches up to $A_1=T_{0}$;", att1_normal, AIM]
            ]]
count = count + 1

tls = tls + [[
                [r"then the tortoise  moves to $T_{2}$ when Achilles catches up to $A_2=T_{1}$;", att1_normal, AIM]
            ]]
count = count + 1

tls = tls + [[
                [r"then the tortoise moves to $T_{3}$ when Achilles catches up to $A_3=T_{4}$ and so on.", att1_normal, AIM],
                [r"Repeating the process, the tortoise moves to $T_{i}$ when Achilles catches up to $A_i=T_{i-1}$ for each $i=1,2,3,...$.", att1_normal, AIM]
            ]]
count = count + 1

pos_end[anim_name_1] = count

tls = tls + [[
                [r"I see your points.  But I rather directly calculate the total time that $A$ needs to catch up the tortoise by simple algebra.", att1_normal, STU],
                [r" Assu"r"ming $A$ catches $T$ after $t$ seconds. Since $A$ moves extra $100$ meters than $T$, we can get an equation ", att1_normal, STU],
                [r"$t\times v_A = t\times v_T + 100$", att1_equ, STU],
                [r"and solve for $t$", att1_normal, STU],
                [r"$t=100/(v_A-v_T)=100/9$.", att1_equ, STU]
            ]]
count = count + 1

'''
count = count + 1
tls = tls + [[r" Calculus is however special.", TV, NOR]]
count = count + 1
tls = tls + [[r"Calculus is all about {\bf limit}, which bridges a {\em finite} world and an {\em infinite} world.", TV, STA]]
group_ends = group_ends + [count+1]
'''
'''
tls = tls + [[r"Achilles ($A$), the fleet-footed hero of the Trojan War, "
      r"is engaged in a race with a tortoise ($T$), which has been granted a head start. ", TV, TOP]]
count = count + 1
tls = tls + [[r"He shall never catch the tortoise since each time he reaches to the previous position of the tortoise, "
      r"the tortoise has moved forward to a new position ahead of him as demonstrated below,  "
      r"where Achilles and the tortoise start at two positions $A_0$ and $T_0$ respectively and the tortoise moves "
      r"ahead to $T_{i}$ when Achilles catches up to $A_i=T_{i-1}$ for each $i=1,2,3,...$.", TV, TOP]]

group_ends = group_ends + [count+1]
#add animiation of Achilles

count = count + 1
tls = tls + [[r"It is absurd and yet sounds logical.", SV, NOR]]
count = count + 1
tls = tls + [[r"It is a paradox, isn't it? You have to admire ancient Greeks for their passions and curiosities in seeking the knowledge.", TV, NOR]]
count = count + 1
tls = tls + [[r"To get some insights, "
      r"let us be more quantitative and assume that $A$ runs and $T$ moves at speed $v_A=10m/s$ and, "
      r"assuming that the tortoise moves really fast to make calculation easy, $v_T=1m/s$ "
      r"respectively and  $T$ has a head start of $100m$.", TV, NOR]]

group_ends = group_ends + [count+1]
animations[len(group_ends)-1]='zeno_anim_true'
count = count + 1
tls = tls + [[r"Now assume that $A$ spends $t_i$ seconds "
      r"to move from $A_{i}$ to $A_{i+1}$ for $i=0,1,2,3,...$. It is clear $t_0 = \frac{100}{v_A}=10$. "
      r"During the period $[[0, t_0]]$, $T$ moves ahead by the distance $s_1=t_0\times v_T$.", TV, NOR]]

count = count + 1
tls = tls + [[r"To cover the distance $s_1$, $A$ needs $t_1=\frac{s_1}{v_A}=t_0(\frac{v_T}{v_A})$ seconds to reach $A_1$. But in this period ($t_1$ seconds),"
      r"$T$ further moves forward by $t_1\times v_T$ meters.", TV, NOR]]

count = count + 1
tls = tls + [[r" In the next step, $A$ needs $t_2=\frac{t_1\times v_T}{v_A}=t_0 (\frac{v_T}{v_A})^2$ seconds to reach the position $A_2$.", TV, NOR]]

count = count + 1
tls = tls + [[r"In general, $A$ needs $s_i=t_0 (\frac{v_T}{v_A})^{i}$ seconds to reach $A_i$ from $A_{i-1}$.", TV, NOR]]

group_ends = group_ends + [count+1]
count = count + 1
tls = tls + [[r"I see your points.  But I rather directly calculate the total time that $A$ needs to catch up the tortoise by simple algebra."
      r"Say  $A$ catches $T$ after $t$ seconds . Since $A$ moves extra $100$ meters than $T$, we have the equation"
      r"$t\times v_A = t\times v_T + 100$, and solve it for $t$ "
      r"$t=100/(v_A-v_T)=100/9.$", SV, NOR]]
count = count + 1
tls = tls + [[r"Excellent. We know now that $A$ should catch $T$ in exactly $100/9$ second.  But remember that we have paradox to address."
      r"Do you have a way to find the total time following Zeno's argument?", TV, NOR]]
count = count + 1
tls = tls + [[r"By adding $t_1,t_2, ...$?", SV, NOR]]
group_ends = group_ends + [count+1]
'''