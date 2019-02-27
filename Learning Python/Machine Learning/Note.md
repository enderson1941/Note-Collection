# Notes or anything need to be memorized

* * *

-   代价函数概念：代价函数也被称作平方误差函数，有时也被称为平方误差代价函数。我们之所以要求出误差的平方和，是因为误差平方代价函数，对于大多数问题，特别是回归问题，都是一个合理的选择。还有其他的代价函数也能很好地发挥作用，但是平方误差代价函数可能是解决回归问题最常用的手段了。

$$
Hypothesis:\\
h_\theta(x)=\theta_0+\theta_1x \\
Parameters:\\
\theta_0,\\theta_1\\
Cost Function:\\
J(\\theta_0, \theta_1)=\frac{1}{2m}\sum^m_{i=1}(h_\theta(x^{(i)})-y^{(i)})^2\\
Goal:\mathop{minimize}_{\theta_0,\theta_1}J(\theta_0, \theta_1)
$$
