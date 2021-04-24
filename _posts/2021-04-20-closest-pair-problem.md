---
layout: post
date: 2021-04-20 16:00:00 +08:00
title:  "Closest Pair Problem"
usemath: katex
---

The closest pair of points problem or closest pair problem is a problem of computational geometry: given n points in metric space, find a pair of points with the smallest distance between them. In this post, we only consider 2D points represented by $(x, y)$ with euclidean distance.  

A brute-force algorithm is simple but has complexity $O(n^2)$. However there is an algorithm with complexity $O(n\log n)$ or $O(n\log^2 n)$ by *divide and conquer*. We describe it in detail below.  

First we split the whole point set into two halves by median x-coordinate value. Then in each half, we find minimal distance $d_L$/$d_R$ **recursively**. After that, we need to find minimal distance $d_{LR}$ from two halves(i.e. each pair is composed of one point from left half and the other point from right half), then final distance would $d_0 = \min(d_L, d_R, d_{LR})$. The key part is finding out $d_{LR}$.  

Let $d = \min(d_L, d_R)$. To find $d_0$, we only need to consider points which lie in two $d$ strip (exlusive, dash line in the figure) centered by vertical line of median $x$ value(black line). At first, you may think finding $d_0$ in the strip has complexity $O(n^2)$, but we can show that it only costs linear time.  

In the strip, sort each point by $y$ value. For each point, we construct a rectangle(width $2d$, height $d$) with bottom line passing through that point(e.g. blue rectangle in the figure) since we only consider points which has vertical distance($\mid y_1-y_2 \mid$) with that point less than $d$. Given big rectangle composed of eight small squares with side $\frac{d}{2}$, it is impossible that there are two or more points within small square since maximal distance of points within small square is $\frac{d}{\sqrt{2}}$. Thus there are at most **seven** candidate points for each reference point which may have vertical distance $\mid y_1-y_2 \mid < d$. Therefore, finding $d_0$ in the strip has complexity $O(7n) = O(n)$.  

In order to achieve $O(n\log n)$, we need to presort points by $x$ and by $y$ separately to produce two sorted list$\left(T(n) = 2T(\frac{n}{2}) + O(n)\right)$. However, for the algorithm to [work](https://stackoverflow.com/a/61981008/7390103), the points x-values must be unique. Otherwise, we may resort to algorithm with $O(n\log^2 n)$ which sorts points by $y$ after split$\left(T(n) = 2T(\frac{n}{2}) + O(n\log n)\right)$.  

The [algorithm](https://stackoverflow.com/a/1602328/7390103)$\left(O(n\log^2 n)\right)$ works like:  
- Sort points by $x$
- Split the set of points into two equal-sized subsets by a vertical line $x = \text{xmid}$
- Solve the problem **recursively** in the left and right subsets. This will give the left-side and right-side minimal distances $d_L$ and $d_R$ respectively
- Sort points by $y$, find points in the strip
- Find $d_0$ in strip(check each point in order by ascending $y$)

Full code(including tests) is [here](https://github.com/BruceChen2017/brucechen2017.github.io/tree/main/codes/2021-04-20).  

*Note*: You may get asymptotic bound of complexity of algorithm by [wolfram alpha](https://www.wolframalpha.com/), e.g. [$n\log^2n$](https://www.wolframalpha.com/input/?i=T%28n%29+%3D+2T%28n%2F2%29+%2B+nlogn)


<p align="center">
  <img src="/images/e1.png" />
</p>  

*Figure*: <u>Closest Pair</u>  


**References**:
1. <https://www.geeksforgeeks.org/closest-pair-of-points-onlogn-implementation/>
2. <https://www.youtube.com/watch?v=0W_m46Q4qMc>
3. <https://stackoverflow.com/questions/1602164/shortest-distance-between-points-algorithm/>
