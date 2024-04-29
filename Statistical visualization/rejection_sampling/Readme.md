We want to simulate the uniform distribution U(D) on the unit disk in two dimensions \( D = \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 \leq 1\} \). To this end, we apply rejection sampling.

a) Implement rejection sampling based on the uniform distribution U[−1, 1]^2 as proposal distribution. The latter can be implemented easily by stochastically independent draws of \( X \sim U[−1, 1] \) and \( Y \sim U[−1, 1] \).

b) Generate \( n = 500 \) samples of the uniform distribution on D via your code and count each time the number of tries until one of the proposal draws is accepted. Then plot the generated 500 samples similar to the figure below.

c) Finally, derive an estimate on the number π based on the stored number of tries of rejection sampling in b). Recall how the success probability of rejection sampling relates to the average number of tries. How large is the success/acceptance probability in this case?
