from const import *

group_ends = [0]
tls = []
annimiations = {}
count = 0

tls = tls + [[r"Now let us back to the real world.", TV, NOR]]
count = count + 1
tls = tls + [[r"For a computer to handle arithmetic operations, numbers need to be expressed "
      r"in decimal expression (or similar like binary format).", TV, NOR]]

count = count + 1
tls = tls + [[r"All irrational numbers, "
      r"simple as $\sqrt 2$, need to be expressed as the summation of a sequence of rational numbers so computer "
      r"can effectively carry out some estimation with desired accuracy.", TV, NOR]]

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
annimiations[len(group_ends)-1]='zeno_anim_true'
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