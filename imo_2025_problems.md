**Problem 1**

A line in the plane is called *sunny* if it is not parallel to any of the $x$-axis, the $y$-axis, or the line $x+y=0$.

Let $n\ge 3$ be a given integer. Determine all nonnegative integers $k$ such that there exist $n$ distinct lines in the plane satisfying both of the following:

- For all positive integers $a$ and $b$ with $a+b\le n+1$, the point $(a,b)$ lies on at least one of the lines; and
- exactly $k$ of the $n$ lines are sunny.

**Problem 2**

Let $\Omega$ and $\Gamma$ be circles with centres $M$ and $N$, respectively, such that the radius of $\Omega$ is less than the radius of $\Gamma$. Suppose $\Omega$ and $\Gamma$ intersect at two distinct points $A$ and $B$. Line $MN$ intersects $\Omega$ at $C$ and $\Gamma$ at $D$, so that $C,M,N,D$ lie on $MN$ in that order. Let $P$ be the circumcentre of triangle $ACD$. Line $AP$ meets $\Omega$ again at $E\ne A$ and meets $\Gamma$ again at $F\ne A$. Let $H$ be the orthocentre of triangle $PMN$. Prove that the line through $H$ parallel to $AP$ is tangent to the circumcircle of triangle $BEF$.

**Problem 3**

Let $\mathbb{N}$ denote the set of positive integers. A function $f : \mathbb{N} \to \mathbb{N}$ is said to be *bonza* if

$$
f(a)\ \text{divides}\ b^{\,a} - f(b)^{\,f(a)}
$$

for all positive integers $a$ and $b$.

Determine the smallest real constant $c$ such that

$$
f(n) \le cn
$$

for all bonza functions $f$ and all positive integers $n$.

**Problem 4**

A proper divisor of a positive integer $N$ is a positive divisor of $N$ other than $N$ itself.

The infinite sequence $a_1, a_2, \dots$ consists of positive integers, each of which has at least three proper divisors. For each $n \ge 1$, the integer $a_{n+1}$ is the sum of the three largest proper divisors of $a_n$.

Determine all possible values of $a_1$.

**Problem 5**

Alice and Bazza are playing the *inekoalaty* game, a two-player game whose rules depend on a positive real number $\lambda$ known to both players.
On the *n*th turn of the game (starting with $n=1$) the following happens:

- **If $n$ is odd**, Alice chooses a nonnegative real number $x_n$ such that

$$
    x_1 + x_2 + \dots + x_n \le \lambda n.
$$

- **If $n$ is even**, Bazza chooses a nonnegative real number $x_n$ such that

$$
    x_1^{2} + x_2^{2} + \dots + x_n^{2} \le n.
$$

If a player cannot choose a suitable $x_n$, the game ends and the other player wins.
If the game goes on forever, neither player wins. All chosen numbers are known to both players.

Determine all values of $\lambda$ for which Alice has a winning strategy and all those for which Bazza has a winning strategy.

**Problem 6**

Consider a $2025 \times 2025$ grid of unit squares. Matilda wishes to place on the grid some rectangular tiles, possibly of different sizes, such that each side of every tile lies on a grid line and every unit square is covered by at most one tile.

Determine the minimum number of tiles Matilda needs to place so that each row and each column of the grid has exactly one unit square that is not covered by any tile.