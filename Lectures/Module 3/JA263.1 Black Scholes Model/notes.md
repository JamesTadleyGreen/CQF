# JA263.1 Black Scholes Model
## Options
The price (value) of an option is as follows
$$
    V(S,t;\sigma,\mu;E,T;r)
$$
Where;

 - $S$ is the stock price
 - $t$ is the time
 - $\sigma$ is the volatility
 - $\mu$ is the drift
 - $E$ is the strike price
 - $T$ is the time of expiry
 - $r$ is the rfr

The assumptions of the B-S-M model are;

 - The underlying $S$ follows a lognormal random walk, with a known $\sigma$.
 - The rfr is a known function of time.
 - There are no dividends on the underlying $S$.
 - Delta hedging is done continuously.
 - There are no transaction costs.
 - There are no arbitrage opportunities.

We denote the folowing;
$$
    \Pi = V(S,t) - \Delta S
$$
This is the value of a position that is long the option, and short $\Delta$ lots of the underlying.


Now, let's consider movements in this portfolio;
$$
    d\Pi = dV - \Delta dS
$$

 > Note: We fix delta within each timestep, but recalculate across each timestep
 > Note: When we move to continuous time, we have continuous delta hedging

Since $V$ is a function of both $S$ and $t$ we can apply Ito IV:
GRIM MATHS FORMULA

We factor out the 'randomness' i.e. $dX$, and want to set this to 0, so we have $\Delta = \frac{dV}{dS}$.
Thus with this $\Delta$ value we have the change in the portfolio that is completely riskless.
We know that our rfr is $r$, and due to no arbitrage we know that both values must be the same.

## Properties of B-S-M
### Linearity

 - *Scalar Multiplication*: If one option is worth $V$; $k$ options are worth $kV$.
 - *Vector Addition*: If we have have two options $V_1$ and $V_2$; the value of the portfolio is $V_1 + V_2$.

### Elimination of $\mu$
By setting our $\Delta$ we have removed $\mu$ from the equation. So if two people agree on the volatility of an asset, 
they necessarily must agree on the price of the option, even if they have differing estimates for the drift.

### Final Condition
The B-S-M has no concept of put vs call, so we define the payoff for $V$:

 - $V(S,E) = max(S-E,0)$ for a call
 - $V(S,E) = max(E-S,0)$ for a put

## Solving B-S-M
To solve this equation we do three steps:
 - Reduce the B-S equation to a 1D heat equation
 - Solve this diffusion using similarly reduction (Lecture 1.3)
 - Unwind the reduction above


### Present to future values
First we have to move the time to $t$ rather than time 0. Let's write the value of the option as the PV of
some unknown function $U$, then;
$$
\begin{align*}
    V &= e^{-r(T-t)}U\\
    \implies \frac{\partial V}{\partial t} &= re^{-r(T-t)}U + e^{-r(T-t)}\frac{\partial U}{\partial t}\\
    \implies \frac{\partial V}{\partial S} &= e^{-r(T-t)}\frac{\partial U}{\partial S}\\
    \implies \frac{\partial^2 V}{\partial S^2} &= e^{-r(T-t)}\frac{\partial^2 U}{\partial S^2}\\
\end{align*}
$$

We can sub this into our equation to get a new equation.

 > Note: This removes the $rV$ term.

### Similarity reduction
We set $\tau = T - t$, 

