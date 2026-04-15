# JU251.4 Applied Stochastic Calculus I
## Motivating Example
Define $R_i$ to be a random variable for a coin flip, fair coin that pays out either $\pm 1$.
Then;
$$
    E[R_i] = 0\\
    E[R_i^2] = 1\\
    E[R_iR_j] = 0\\
$$

Define;
$$
    S_i = \sum_{j=1}^i R_j
$$

Then;
$$
    E[S_i] = \sum_{j=1}^i E[R_j] = 0\\
    E[S_i^2] = \sum_{j=1}^i E[R_j^2] = \sum_{j=1}^i 1 = i\\
$$

additionally;
$$
    E[S_i|R_1, R_2, \dots, R_{i-1}] = R_{i-1}
$$
_i.e._ the Martingale property.


## Variations
An _n-th variation_ is defined as;
$$
    \sum_{j=1}^i (S_j - S_{j-1})^n
$$

So, the variation is always 0, and the quadratic variation is always $i$.

## Brownian Motion
The issue with a bet size of 1, is that the variance explodes linearly. So let's instead define the bet size to
be $\sqrt{\frac{t}{n}}$.

Then the _quadratic variation_ is;
$$
    Q = \sum_{j=1}^n (S_j - S_{j-1})^2 = \sum_{j=1}^n \sqrt{\frac{t}{n}}^2 = n \cdot \sqrt{\frac{t}{n}}^2 = t
$$

### Taking the limit
Let's now move to sending $n -> \infty$. We note, the mean and the variance don't change. 
Thus we end up with a _Weiner Process_:
$$
    E[X(t)] = 0\\
    E[X(t)^2] = t
    X(t) ~ N(0,t)
$$

There are the below properties of _Brownian Motion_:
 - $X(0) = 0$ almost surely.
 - $t -> X(t)$ is continuous everywhere and differentiable nowhere.
 - $dX(t) = X(t + dt) - X(t) ~ N(0,dt)$, and that Brownian motion increments are independant, and Gaussian.
 - Brownian motion is a stochastic process, _i.e._, $\{X(t):t\in \mathcal{R}^+\}$

Thus, giving $t>s$, we get $X(t) - X(s) ~ N(0,|t-s|)$

## Rules of Stochastic Calculus
We don't work with the usual rules of caluclus, instead we work with _stochastic differential equations_.
These take the form:
$$
    dF = \square dt + \square dX
$$

### Itô's Formulas
#### Itô I
This comes from a Taylor expansion, ignoring all of the higher order terms.
$$
    dF = \frac{dF}{dX}dX + \frac{d^2F}{2dX^2} dt
$$
Since we can replace $dX^2$ with $dt$ as our timesteps get smaller.

#### Itô II
Now we do the same Taylor expansion, but this time in two variables, $t$ and $X_t$.
$$
dF = \left(\frac{\partial F}{\partial t} + \frac{\partial^2 F}{2\partial X_t^2}\right) dt + \frac{\partial F}{\partial X_t} dX
$$
