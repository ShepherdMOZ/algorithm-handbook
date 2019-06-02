### Anlysis

Before start, let's have a look at Monte Carlo Method.

This method uses random generated numbers to estimate the result within a certain mathmatical constrains or model. What it does is basically using large amount of random generated "points" to fill a constrained target area (used to represent the demanded result) as much as possible (Actually this is the integration in math). As for its name, Monte Carlo, is a place in America that is famous for gambling. You guessed it, the way that Monte Carlo method works is just like gambling. 

It is certainly difficult to actually calculate $\pi$. But just using Monte Carlo, we can estimate $\pi$ just using this two formulars:

x^2 + y^2 = r^2

S = $\pi$r ^2


Now imaging that everything is sitted inside a 2D coordinate system. Firstly, we can randomly generate points (x,y) x,y $\in$ [-1.000,1.000] with 3 demical places. And than put these numbers into the first equation to find out which points actually fit. If so then we know that these points are in the circle. Once we get enough accumulation of points, we can use the count of points as an estimate of area size of circle, and then calculate (it is indeed estimate) the Pi using S = $\pi$r^2

A thing to notice, since we are actually 'filling' things, the more points we can generate, the higher accuracy we can get. To get a satisfied result in this case, we need at least 1000 estimation