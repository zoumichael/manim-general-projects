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
[r"Well, Calculus might be the most important subject in math.", att1_normal,TEA],
[r"As you might know, Newton is remembered as the greatest scientist,", att1_normal,TEA],
[r"yet some people believe that his most important achievement is on calculus,", att1_normal,TEA],
[r"and British people are quite proud for Newton's achievement.", att1_normal,TEA],
[r"Folks in the European Continent are not quite happy with that", att1_normal,TEA],
[r"and they claimed that German mathematician Leibniz should take that credit", att1_normal,TEA],
[r"and argued for a long time with British people in history.", att1_normal,TEA]
]] #use a picture
count = count + 1

tls = tls + [[
[r"I wish I were as enthusiastic like you on calculus.  But could you please briefly explain what it is about.", att1_normal,STU],
[r"Generally speaking, it is hard to summarize in one sentence what a math subject is about, especially for beginners like you.", att1_normal,TEA],
[r" Calculus is however special.", att1_normal,TEA],
[r"Calculus is all about {\bf limit}, which bridges a {\em finite} world and an {\em infinite} world.", att1_normal, STA],
[r"You sound like a philosopher rather than a mathematician. ", att1_normal,STU],
[r"Well, only wish I'd know my own {\em limit} someday.", att1_normal,STU],
[r"But how to define that so called {\bf infinite} world?", att1_normal,STU]
]]
count = count + 1

tls = tls + [[
[r"Well, let's walk in the finite world first, a green world that you should be comfortable to deal with now. Suppose", att1_normal,TEA],
[r"$A_N=(a_1,a_2,...,a_N)$ ", att1_normal, EQU],
[r"denote a list of finite many numbers, We can operate on the elements in $A_N$ in some ways we are familiar with.", att1_normal,TEA],
[r"For examples, we can sum them up ", att1_normal,TEA],
[r" $\sum_{1\le n\le N} a_n = a_1+a_2+\cdots + a_N$", att1_normal, EQU],
[r"we can also identify the maximum value of $A_N$. It might take some time, but we can always get the answer in the end.  can't we?", att1_normal,TEA],
[r"Well, at least I can compare each number with all others to find the answer if I have enough time.", att1_normal,STU],
[r"That is true.  In the finite world, for a task like comparison,  one can naively exhaust all possible scenarios to find the answer.", att1_normal,TEA]
]]

count = count + 1


'''
#test 3
count = count + 1
tls = tls + [[r"Now let us move to the {\bf infinite} world,  and consider a sequence of numbers that never stops, denoted by", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Eq(1.1) $\qquad A:=(a_n)_{n\ge 1}=(a_1,a_2,...,a_n,...).$", att1_normal, EQU]]
count = count + 1
tls = tls + [[r"For example, $A$ stands for the list of all natural numbers with $a_n=n$.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"So what distinguishes the infinite world from the finite world has nothing to do with magnitude of certain quantity?!", att1_normal,STU]]
count = count + 1
tls = tls + [[r"In the infinite world, we need operate on infinite many of animals. ", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Be careful about the difference between two concepts:  ``infinite many'' vs ``infinity''.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"The former should be clear in word itself, i.e. not finitely many.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"It is not easy to explain the latter exactly at this moment.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Intuitively, think about what the following two sequences might represent.", att1_normal,TEA]]

count = count + 1
tls = tls + [[r"$(1,2,\dots, n,\dots), \quad (1^2, 2^2,\dots, n^2,\dots)$.", att1_normal, NOT]]
count = count + 1
tls = tls + [[r"Both sequences 'approaches' to certain kind of infinity, denoted by", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"$\infty$", att1_normal, EQU]]
count = count + 1
tls = tls + [[r"although the second one 'goes' to $\infty$ faster than the first one, "
              r"i.e. there are different kinds of  $\infty$.", att1_normal,TEA]]
group_ends = group_ends + [count+1]

count = count + 1
#test 4
tls = tls + [[r"Does $\infty$ stand for some quality that the sequence ends up?", att1_normal,STU]]
count = count + 1
tls = tls + [[r"In the finite world,  the value of each number is clearly defined.  In another word,  its relation with other numbers are clear.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"In the infinite world, $\infty$ does not refer to a specific quantity, but a characteristic of certain type of sequences that can 'goes' beyond any predefined boundary.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"We shall clarify what it means exactly later.  In the infinite world,  as you said, we often need to deal with infinite many animals or, more accurately, "
              r"end up in an endless process, which distinguish from the finite world we are familiar with.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Let $S$ denote a general set of real numbers, including the case when its elements can not be listed in a sequence such as the open interval $S=(1,2)$."
              r"Here comes the first basic concept in the infinite world.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Def 1.1.1:", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"1. A number $m$ is called as a {\bf lower bound} of $S$ if $m \le x$ for ANY $x\in S$.", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"$S$ is called {\bf lower bounded} if such a lower bound exists;", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"2. A value $M$ is called as a {\bf upper bound} of $S$ if $M \ge x$  for ANY $x\in S$.", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"$S$ is called {\bf upper bounded} if such a upper bound exists;", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"3. $S$ is called {\bf bounded} if it is both lower bounded and upper bounded.", att1_normal, DEF]]
group_ends = group_ends + [count+1]

count = count + 1
tls = tls + [[r"Remark:", att1_normal,REM]]
count = count + 1
tls = tls + [[r"1. Above lower bound $m$ or upper bound $M$  is not required to be in $S$. "
              r"For example, $S=(1,2)$ is bounded with $0$ and $3$ as a lower bound and upper bound respectively.  notice that $0$ and $3$ are not in $S$.", att1_normal,REM]]
count = count + 1
tls = tls + [[r"2. lower bound and upper bound are not unique. $1$ and $2$ are another lower bound and upper bound for above $S$.", att1_normal, REM]]
group_ends = group_ends + [count+1]

#test 5

count = count + 1
tls = tls + [[r"Notice that a finite set is always bounded, the minimum value is a lower bound and the maximum value is a upper bound.",  att1_normal,TEA]]
count = count + 1
tls = tls + [[r"As such,  bound concept is only needed when we deal with a  set $S$ with infinite many elements.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"It is easy to see that both examples listed in Eq(1.2) are lower bounded, but not upper bounded.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Looks like ``any'' in definition 1.1 is the key word to understand lower bound and upper bound.", att1_normal,STU]]
count = count + 1
tls = tls + [[r"The logic of ``any'' need to be emphasized in several key concepts in calculus. Any idea if a number $m$ is not a lower bound of $S$?", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"There should exist at least one number $x\in S$ such that $x<m$, shouldn't there?", att1_normal,STU]]
count = count + 1
tls = tls + [[r"Great! let us write it down", att1_normal,TEA]]
group_ends = group_ends + [count+1]

count = count + 1
tls = tls + [[r"Statement.", att1_normal, STA]]
count = count + 1
tls = tls + [[r"If $m$ is not a lower bound of a set $S$,  there exist $x\in S$ such that $x<m$.", att1_normal, STA]]
count = count + 1
tls = tls + [[r"Similarly, if $M$ is not a upper bound,  there exist $y\in S$ such that $y>M$.", att1_normal, STA]]
count = count + 1
tls = tls + [[r"As another example, let $a_n = (1/2)^n$ in definition (1.1), we get a geometric sequence", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Eq(1.3) $\qquad G(1/2):= (1,1/2,(1/2)^2,\dots, (1/2)^{n-1},...)$", att1_normal, NOT]]
count = count + 1
tls = tls + [[r"Notice that $G(1/2)$ is decreasing and hence the maximum value is $a_1=1$. what can we say about the minimum value of the set $G(1/2)$?", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"$0$ and negative values are not in the sequence. Seems that there is no minimum value for $G(1/2)$, isn't it?", att1_normal,STU]]
count = count + 1
tls = tls + [[r"You got the point! By your analysis, any positive number,  any negative number or zero can not be treated as a minimum, and therefore it does not exist.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Although $0$ is a low bound since all elements in $G(1/2)$ are larger than $0$. Of course, any negative number is a low bound as well.", att1_normal,STU]]
group_ends = group_ends + [count+1]

# test 6
count = count + 1
tls = tls + [[r"What makes $0$ special is that it is {\bf the greatest lower bound} of $G(1/2)$.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"I see.  For any other {\bf larger} number, it is not qualified  as a lower bound of $G(1/2)$, the logic in 'greatest lower bound'?", att1_normal,STU]]
count = count + 1
tls = tls + [[r"Exactly!  we can transform the phrase to a algebraic description that is quite helpful in future analysis:", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Def 1.1.1.", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"Let $S$ be a general set of numbers, A number $m$ is called the greatest lower bound of $S$ if ", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"  a) $ m \le x $  for all $x$ in S;", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"  b) For any positive number $\epsilon$, $m + \epsilon$ is no longer a lower bound, i.e.  there exist $x_0\in S$ such that $x_0 < m + \epsilon$.", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"    The greatest lower bound is denoted by $\inf S$, called the infimum of $S$. We write $\inf S=-\infty$ if it does not exist.", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"A number $M$ is called the least upper bound of $S$ if ", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"  a) $ m \le x $  for all $x$ in S;", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"  b) For any positive number $\epsilon$, $M-\epsilon$ is no longer a upper bound, i.e.  there exist $y_0\in S$ such that $y_0 > M - \epsilon$", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"    The least upper bound is denoted by $\sup S$, called the supremum of $S$. We write $\sup S=\infty$ if it does not exist.", att1_normal, DEF]]
group_ends = group_ends + [count+1]

count = count + 1
tls = tls + [[r"We follow the convention that $x, y, z$ are used to denote ANY element in a set, while  $x_0, y_0, z_0$ are used to denote a selected number.", att1_normal, REF]]
count = count + 1
tls = tls + [[r"The logic sounds right to me. But how can you verify $m+\epsilon$ is not lower bound without knowing the value of $\epsilon$?", att1_normal,STU]]
count = count + 1
tls = tls + [[r"We need some algebra rather than depending on numerical comparison.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Take above $G(1/2)$ as an example, $0$ is clearly a lower bound since each element $a_n=(1/2)^{n-1}$ in $G(1/2)$ is positive.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"To show $0$ is the greatest lower bound, for any given $\epsilon>0$,  we can take a sufficient large $N$ such that", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"$a_N=(1/2)^{N-1}<\epsilon$", att1_normal, EQU]]
count = count + 1
tls = tls + [[r"so that $0+\epsilon=\epsilon$ is no longer a lower bound.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Ex 1.1.1", att1_normal, EXA]]
count = count + 1
tls = tls + [[r"$S=(1,2)$. It is clear that $\inf S = 1$ and $\sup S = 2$", att1_normal, EXA]]
count = count + 1
tls = tls + [[r"$S= (1,2,3,...)$,  the set of all natural numbers.  $S$ is lower bounded with $\inf S=1$ while $\sup S = \infty$ since it is not upper bounded", att1_normal, EXA]]
group_ends = group_ends + [count+1]

# test 7
count = count + 1
tls = tls + [[r"What makes $\sup S$ and $\inf S$ special?", att1_normal,STU]]
count = count + 1
tls = tls + [[r"They are quite helpful for us to understand the fundamental concept {\bf limit}. \\ In fact, "
      r"it turns out that they are exact the mysterious limits for a special type of sequences defined as follows.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r" A sequence $A$ in Eq (1.1) is called increasing (decreasing) if any item in the sequence is always not larger than its following item, i.e. \\"
      r"     $a_n\le a_{n+1}$ ($a_n\ge a_{n+1}$) for any $n\ge 1$.  \\"
              r"$A$ is called monotonic if it is either increasing or decreasing.", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"Ex\\ $A=(1,3, 5, 7, 9, ...)$ is a increasing sequence;\\"
              r"$A=(1, 1/3, 1/5, 1/7, 1/9, ...)$ is a decreasing sequence; \\"
              r"$A=(1, -2, 3, -4, 5, -6,...)$  is not monotonic since it is neither incrasing nor decreasing.", att1_normal, EXA]]
count = count + 1
tls = tls + [[r"We are now in the position to introduce the concept 'limit' of a monotonic sequence.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r" Def 1.1.3:  The limit of a bounded increasing sequence $A$ is defined to be $\sup A$, denoted by", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"$\lim_{n\to \infty}a_n := \sup A;$", att1_normal, EQU]]
count = count + 1
tls = tls + [[r"The limit of a bounded decreasing sequence $A$ is defined to be $\inf A$, denoted by", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"$\lim_{n\to \infty}a_n := \inf A$;", att1_normal, EQU]]
group_ends = group_ends + [count+1]

count = count + 1
tls = tls + [[r"As you can see, for a monotonic sequence, the concept of limit is clear. \\"
              r"One can visualize that 'items in $A$ approaches arbitrarily closely to the limit'.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"The phrase like 'arbitrarily close' sound ambiguous to me.", att1_normal,STU]]
count = count + 1
tls = tls + [[r"You are not alone. Mathematicians in early days also got confused with such description. "
              r"To clarify the ambiguity, let $\epsilon$ be a positive number and \\"
              r" $O(l,\epsilon):=(l-\epsilon, l+\epsilon)$ \\"
              r"denote the neighborhood of $l$ with radius $\epsilon>0$, which contains all numbers "
              r"whose distances to $l$ are less than $\epsilon$", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Denote $l:=\inf A$ for a {\bf bounded decreasing} sequence $A$. For any prescribed $\epsilon>0$, \\"
      r"$l$ is g.l.b,  $\longrightarrow$ $l+\epsilon$ not a l.b. $\longrightarrow$  $\exists a_N\in A$ s.t. $ a_N<l+\epsilon$. \\"
      r"but $l\le a_N$ since $l$ is a l.b., hence\\"
              r" $a_N\in (l, l+\epsilon)\subset O(l,\epsilon)$. \\ "
      r"Since $A\downarrow $, all terms after $a_N$ is more closer to $l$ than $a_N$ "
      r"and fall in the $(l, l+\epsilon)$ as shown below, and we have ", att1_normal,TEA]]
count = count + 1
# insert figure 1.2 here
tls = tls + [[r"Eq(1.6) $\qquad |a_n-l|<\epsilon, \quad \quad  \mbox{for ALL $n\ge N$}$", att1_normal, EQU]]
group_ends = group_ends + [count+1]

# test 8
count = count + 1
tls = tls + [[r"Got it.  Items in $A$ approach {\bf arbitrarily close} to $l$  simply because $\epsilon$ can be a arbitrarily small.", att1_normal,STU]]
count = count + 1
tls = tls + [[r"Exactly. let me emphasize that $\epsilon$ caps the distances to $l$ for {\bf all} terms following $a_N$.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Pay attention to the key word 'all'.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"In another word, the distance threshold $\epsilon$ is applied to all items "
      r"in the sequence except for some {\bf finite} many items in the sequence.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Let me confirm my understanding.", att1_normal,STU]]
count = count + 1
tls = tls + [[r"By saying ``items in $A$ approach arbitrarily close to $l$'' ", att1_normal,STU]]
count = count + 1
tls = tls + [[r"it doesn't mean that certain {\bf fixed} terms in the sequence are arbitrarily close to $l$. ", att1_normal,STU]]
count = count + 1
tls = tls + [[r"It actually means that, for any given threshold $\epsilon>0$, all items except for some finite many are close "
      r"to $l$ within the threshold $\epsilon$. ", att1_normal,STU]]
count = count + 1
tls = tls + [[r"Exactly.  Notice that as $\epsilon>0$ becomes smaller, we need exclude more terms in $A$ to make the rest close "
      r"to $l$ within the threshold $\epsilon$. ", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"But it does not matter how many items need to be removed as long as they are finite many "
      r"to meet the requirement 'items in $A$ approach arbitrarily close to $l$'.", att1_normal,TEA]]
group_ends = group_ends + [count+1]
# start with definition of limit
count = count + 1
tls = tls + [[r"The idea discussed before can be used to describe the limit of a general sequence!", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Def 1.1.4: A sequence $A$ is called to "
              r"{\bf converge} to $l$ if for any given $\epsilon>0$, there exists $N$ such that ", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"$|a_n-l|<\epsilon, \quad \quad  \forall n\ge N$.", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"In this case, we write", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"$\lim_{n\to \infty} a_n = l \qquad or \qquad a_n\to l$,", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"and $l$ is called the {\bf limit} of the sequence.", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"Remark 1.1.2: The concept of the limit of a sequence is one of two fundamental concepts in calculus!", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"We shall touch the other type of limit about function late. ", att1_normal,TEA]]
group_ends = group_ends + [count+1]
# test 9
tls = tls + [[r"Let us look some examples. ", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"$\lim_{n\to \infty} \frac{n^2}{n^2+1} = 1$.", att1_normal, EXA]]
count = count + 1
tls = tls + [[r"It is increasing with $\sup A =1$.", att1_normal, PRO]]
count = count + 1
tls = tls + [[r"$\lim_{n\to \infty} \frac{1}{n^{2+(-1)^n}} = 0$.", att1_normal, EXA]]
count = count + 1
tls = tls + [[r"It is neither increasing nor decreasing. Let us prove it by definition. ", att1_normal, PRO]]
count = count + 1
tls = tls + [[r"  For any $\epsilon>0$, we need find required $a_N$.", att1_normal, PRO]]
count = count + 1
tls = tls + [[r"  Since $0<a_n\le \frac1n$, "
      r"to make $|a_n-0|<\epsilon$, we only need $\frac1n<\epsilon$.", att1_normal, PRO]]
count = count + 1
tls = tls + [[r"  If we choose $N$ be any integer that is larger than $\frac1\epsilon$, then"
      r"$$|a_n-l|=a_n\le \frac1n<\frac1N<\epsilon, \quad  \forall n\ge N.$$ ", att1_normal, PRO]]
count = count + 1
tls = tls + [[r"  Since $0<a_n\le \frac1n$,  "
      r"to make $|a_n-0|<\epsilon$, we only need $\frac1n<\epsilon$. If we choose $N$ be any integer that is larger than $\frac1\epsilon$, then"
      r"$$|a_n-l|=a_n\le \frac1n<\frac1N<\epsilon, \quad  \forall n\ge N.$$ ", att1_normal, PRO]]
count = count + 1
tls = tls + [[r"$\lim_{n\to \infty} (1+(-1)^n)$ does not exist.", att1_normal, EXA]]

count = count + 1
tls = tls + [[r"Intuitively, the sequence does not approach to a given value since $a_n$ is alternating between $0$ and $2$.  "
      r"one can also argue vigorously that the sequence can not converge to any given number $l$.  In fact, for any $l$,  we have "
      r"$$2=|a_n-a_{n+1}| = |(a_n-l) + (l- a_{n+1})| \le  |a_n-l|+|a_{n+1}-l|$$"
      r"as such,  $|a_n-l|$ and $|a_{n+1}-l|$ can not be smaller than $\frac12$ simultaneously for any $n$. So for $\epsilon=\frac12$, "
      r"there is no $N$ that meets Inequlity (1.7). ", att1_normal, PRO]]
group_ends = group_ends + [count+1]

count = count + 1
tls = tls + [[r"What can we do with limit? how does it bridge the finite world to the infinite world? ", att1_normal,STU]]
count = count + 1
tls = tls + [[r"Let us start with the task to add all terms in $A$.  It becomes actually quite trivial once we have the limit as a tool", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Defintition of adding infinite many numbers.", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"Let $S_n = \sum_{1\le i\le n}a_i$ be the sum of the first $n$ terms in $A$.", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"If $S_n$ converges to certain value $S$, then the sequence is called summable and $S$ is defined as the sum of the sequence $A$. We write", att1_normal, DEF]]
count = count + 1
tls = tls + [[r" Eq(1.9) $\qquad \sum_{1\le i< \infty}a_i := S = \lim_{n\to \infty} S_n$", att1_normal, DEF]]
count = count + 1
tls = tls + [[r"Basically, we use the partial sum $S_n$ as an estimation and", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"the limit of the estimation process is equal to the exact value of the summation if the limit does exit. ", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"As an example, consider a general geometric sequence on the right", att1_normal,TEA]]
count = count + 1
tls = tls + [[r" Eq(1.10)  $\qquad G(x):= (1,x,x^2,\dots, x^{n-1},...).$", att1_normal, EQU]]
count = count + 1
tls = tls + [[r"we can add first n terms and get the partial sum:", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"$S_n:=(1+x+x^2+\dots+x^{n-1})=\frac{1-x^n}{1-x}.$", att1_normal, EQU]]
count = count + 1
tls = tls + [[r"For $0\le x<1$, it is not hard to show $S_n$ is increasing and converges to its supreme $\frac1{1-x}$, i.e.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Eq(1.11) $\qquad \sum_{1\le n <\infty}x^{n-1}=\frac1{1-x}, \quad 0\le x<1$", att1_normal, EQU]]
group_ends = group_ends + [count+1]
#here
count = count + 1
tls = tls + [[r"To add infinite many items, we start working in the finite world by adding finite terms to get $S_n$, ", att1_normal,STU]]
count = count + 1
tls = tls + [[r"then take the limit of the sequence $(S_1,S_2,\cdots, S_n,\cdots)$ to get the sum of the sequence.", att1_normal,STU]]
count = count + 1
tls = tls + [[r" Looks that limit indeed plays a bridge rule here.", att1_normal,STU]]
count = count + 1
tls = tls + [[r"Indeed! In general,", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"If a direct solution for a task is not available, "
              r"we often start with certain estimation process to estimate the target value and "
              r"expect that the limit of the estimation process is the target value.", att1_normal, STA]]
count = count + 1
tls = tls + [[r"But why bother to add infinite many terms? ", att1_normal,STU]]
count = count + 1
tls = tls + [[r"It is one of basic operations for us to explore in the infinite world and ", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"is essential for both theoretic development and real world applications.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"But let us roam in the ancient Greek imaginary world for a while ", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"and think about the following famous paradox by the Greek philosopher Zeno nearly $2500$ thousand years ago.", att1_normal,TEA]]


group_ends = group_ends + [count+1]
animations[len(group_ends) - 1]= 'zeno_anim_false'
count = count + 1
tls = tls + [[r"Achilles ($A$), the fleet-footed hero of the Trojan War, is engaged in a race with a tortoise ($T$), which has been granted a head start. ", att1_normal, TOP]]
count = count + 1
tls = tls + [[r"He shall never catch the tortoise!", att1_normal, TOP]]
count = count + 1
tls = tls + [[r"Each time he reaches to the previous position of the tortoise, ", att1_normal, TOP]]
count = count + 1
tls = tls + [[r"the tortoise has moved forward to a new position ahead of him as demonstrated below.", att1_normal, TOP]]
count = count + 1
tls = tls + [[r"We see that Achilles and the tortoise start at two positions $A_0$ and $T_0$ respectively and ",  att1_normal, TOP]]

count = count + 1
tls = tls + [[r"the tortoise moves ahead to $T_{i}$ when Achilles catches up to $A_i=T_{i-1}$ for each $i=1,2,3,...$.", att1_normal, TOP]]


group_ends = group_ends + [count+1]
#add animiation of Achilles

count = count + 1
tls = tls + [[r"It is absurd and yet sounds logical.", att1_normal,STU]]
count = count + 1
tls = tls + [[r"It is a paradox, isn't it? You have to admire ancient Greeks for their passions and curiosities in seeking the knowledge.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"To get some insights, "
      r"let us be more quantitative and assume that $A$ runs and $T$ moves at speed $v_A=10m/s$ and, "
      r"assuming that the tortoise moves really fast to make calculation easy, $v_T=1m/s$ "
      r"respectively and  $T$ has a head start of $100m$.", att1_normal,TEA]]

group_ends = group_ends + [count+1]
animations[len(group_ends) - 1]= 'zeno_anim_true'

count = count + 1
tls = tls + [[r"Now assume that $A$ spends $t_i$ seconds "
      r"to move from $A_{i}$ to $A_{i+1}$ for $i=0,1,2,3,...$. It is clear $t_0 = \frac{100}{v_A}=10$. "
      r"During the period $[[0, t_0]]$, $T$ moves ahead by the distance $s_1=t_0\times v_T$.", att1_normal,TEA]]

count = count + 1
tls = tls + [[r"To cover the distance $s_1$, $A$ needs $t_1=\frac{s_1}{v_A}=t_0(\frac{v_T}{v_A})$ seconds to reach $A_1$. But in this period ($t_1$ seconds),"
      r"$T$ further moves forward by $t_1\times v_T$ meters.", att1_normal,TEA]]

count = count + 1
tls = tls + [[r" In the next step, $A$ needs $t_2=\frac{t_1\times v_T}{v_A}=t_0 (\frac{v_T}{v_A})^2$ seconds to reach the position $A_2$.", att1_normal,TEA]]

count = count + 1
tls = tls + [[r"In general, $A$ needs $s_i=t_0 (\frac{v_T}{v_A})^{i}$ seconds to reach $A_i$ from $A_{i-1}$.", att1_normal,TEA]]

group_ends = group_ends + [count+1]
count = count + 1
tls = tls + [[r"I see your points.  But I rather directly calculate the total time that $A$ needs to catch up the tortoise by simple algebra."
      r"Say  $A$ catches $T$ after $t$ seconds . Since $A$ moves extra $100$ meters than $T$, we have the equation"
      r"$t\times v_A = t\times v_T + 100$, and solve it for $t$ "
      r"$t=100/(v_A-v_T)=100/9.$", att1_normal,STU]]
count = count + 1
tls = tls + [[r"Excellent. We know now that $A$ should catch $T$ in exactly $100/9$ second.  But remember that we have paradox to address."
      r"Do you have a way to find the total time following Zeno's argument?", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"By adding $t_1,t_2, ...$?", att1_normal,STU]]

group_ends = group_ends + [count+1]

count = count + 1
tls = tls + [[r"Right. We need add all those $t_i$ to get the total time.  Zeno's argument implicitly implies that adding "
      r"infinite many of numbers should {\bf always} lead to some sort of infinity. We now know how to add a geometric sequence in "
      r"Eq(1.11) and find the total time $T$ ", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"$\lim_{n\to \infty}T_n=\lim_{n\to \infty} 10(1+\frac{v_T}{v_A} +\cdots + (\frac{v_T}{v_A})^{n-1}) = 10 \times \frac1{1-\frac1{10}}=\frac{100}{9}$", att1_normal, EQU]]
count = count + 1
tls = tls + [[r"which is consistent to what you just covered using simple algebra.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Woo! The phase 'never catch' in the paradox is misleading because the total time $A$ spends in the process is "
      r"not infinity although Achilles's catch-up process goes on forever.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Right.  Ancient Greeks did not know how to add infinite many numbers in general.  "
      r"Had adding infinite many numbers always ended up with 'infinity', Achilles would never have caught the tortoise. "
      r"But we know now that the result can be a finite value as demonstrated above.", att1_normal,TEA]]
group_ends = group_ends + [count+1]
#here
count = count + 1
tls = tls + [[r"Now let us back to the real world.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"For a computer to handle arithmetic operations, numbers need to be expressed "
      r"in decimal expression (or similar like binary format).", att1_normal,TEA]]

count = count + 1
tls = tls + [[r"All irrational numbers, "
      r"simple as $\sqrt 2$, need to be expressed as the summation of a sequence of rational numbers so computer "
      r"can effectively carry out some estimation with desired accuracy.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"As a typical example, the well-known $\pi$ can be expressed in following ways, discovered by Leibniz,", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"$\frac{\pi}{4} = 1-\frac13 + \frac15 -\frac17 +\frac19 + \cdots=\sum_{n=0}^{\infty}(-1)^{n}\frac1{2n+1}$.", att1_normal, EQU]]
count = count + 1
tls = tls + [[r"If we use the sum $S_n$ of the first $n$ term as approximation of $\pi/4$, one can show", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"$|\frac{\pi}4 -S_n|< \frac1{2n+1}.$", att1_normal, EQU]]
count = count + 1
tls = tls + [[r"As such, we can not only estimate ${\pi}$ by $4S_n$, but also know that the error is not bigger than $\frac4{2n+1}$. ", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"If you want to estimate $\pi$ with tolerate error $10^{-3}$, we need  ", att1_normal,TEA]]
count = count + 1
tls = tls + [[r" $\frac4{2n+1}<\frac1{10^{3}}$, or roughly $n>2\times 10^3=2000$.", att1_normal, EQU]]
count = count + 1
tls = tls + [[r"You are encouraged to search the latest development online to find some amazing "
      r"algorithm to estimate $\pi$.", att1_normal,TEA]]

count = count + 1
tls = tls + [[r"The idea is the same: express $\pi$ in term of a summation of series and use the partial summation of first $n$ terms as approximation.", att1_normal,TEA]]

group_ends = group_ends + [count+1]
count = count + 1
tls = tls + [[r"So we end with an irrational number by adding infinite many rational numbers.", att1_normal,STU]]
count = count + 1
tls = tls + [[r"I remember that we can only get a rational number by adding finite many rational numbers.", att1_normal,STU]]
count = count + 1
tls = tls + [[r"The above expression of $\pi$ shows that you might get an apple by adding infinite many of oranges.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"But what really surprises us is that sophisticated functions can be expressed as the summation of simple power functions as we did before. ", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"We are going to show that, under certain conditions, this can be done for a general function $f(x)$, i.e. there exists $a_0,a_1,..$ such that", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"Eq(1.13) $\qquad f(x) = a_0 + a_1 x + a_2x^2 + \dots +a_n x^n + \dots$", att1_normal, EQU]]
count = count + 1
tls = tls + [[r"For examples, ", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"$\sin(x) = \frac{1}{1!}x  - \frac{1}{3!} x^3 + \frac{1}{5!} x^5 -\frac{1}{7!} x^7 \dots , \quad x\in R $", att1_normal, EQU]]
count = count + 1
tls = tls + [[r"$\cos(x) = 1- \frac{1}{2!}x^2  + \frac{1}{4!} x^4 - \frac{1}{6!} x^6  \dots , \quad x\in R$", att1_normal, EQU]]
group_ends = group_ends + [count+1]
count = count + 1
tls = tls + [[r"Interesting.  I do not know much about the two trigonometric functions except they are periodic and bounded by $1$.  "
      r"It is hard for me to associate them with power functions.", att1_normal,STU]]
count = count + 1
tls = tls + [[r"It is hard for me to associate them with power functions.", att1_normal,STU]]
count = count + 1
tls = tls + [[r"It is actually quite easy to derive them once we develop certain tools.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"We will see more magics in our future exploration in the infinite world. ", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"We have made a great achievement with a solid first step into the new world. ", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"We have introduced the core concept, the limit of a sequence, and use it to sum infinite many numbers.", att1_normal,TEA]]
count = count + 1
tls = tls + [[r"OK, let us take a break before we introduce the next fundamental important concept: derivative. ", att1_normal,TEA]]
group_ends = group_ends + [count+1]


'''