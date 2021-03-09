---
layout: post
date: 2021-03-09 20:00:00 +08:00
usemath: katex
title:  "Katex or Mathjax"
---
If you want to display math formula written by $\LaTeX$ in the web page, you need some display engine for mathematics. The popular choice is [mathjax](https://github.com/mathjax/MathJax) or [katex](https://github.com/KaTeX/KaTeX). In the post, I will show you how to use mathjax or katex in jekyll.  

For mathjax, you just need to include mathjax js file in the `<head>` section and do some configurations by `Mathjax.Hub.Config`(e.g. configuration below enables inline math delimiter `$...$`).    
{% highlight html %}
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [['$','$'], ['\\(','\\)']],
        processEscapes: true
    }
    });
</script>
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
{% endhighlight %}  
For katex, we can do in the similar way.  
{% highlight html %}
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/katex.min.css" integrity="sha384-AfEj0r4/OFrOo5t7NnNe46zW/tFgW6x/bCJG8FqQCEo3+Aro6EYUG4+cU+KJWu/X" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/katex.min.js" integrity="sha384-g7c+Jr9ZivxKLnZTDUhnkOnsh30B4H0rpLUpJ4jAIKs4fnJI+sEnkvrMWph2EDg4" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.12.0/dist/contrib/auto-render.min.js" integrity="sha384-mll67QQFJfxn0IYznZYonOWZ644AWYC+Pt2cHqMaRhXVrursRwvLnLaebdGIlYNa" crossorigin="anonymous"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
            "delimiters":[
              {left: "$$", right: "$$", display: true},
              {left: "$", right: "$", display: false},
              {left: "\\(", right: "\\)", display: false},
              {left: "\\[", right: "\\]", display: true}
            ]
        });
    });
</script>
{% endhighlight %}  

Katex is preferred since it is faster. I will display actual effect of math render below.  
- inline math: `$X \sim N(\mu, \sigma^2$` is displayed as $X \sim N(\mu, \sigma^2)$
- block math: 
    ```
    $$
        \begin{aligned}
            3x + 5y &= 20 \\
            5x + 9y &= 10
        \end{aligned}
    $$
    ```
    is displayed as  

    $$
        \begin{aligned}
            3x + 5y &= 20 \\
            5x + 9y &= 10
        \end{aligned}
    $$
