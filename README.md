velocity = 20  
distance = time * velocity / 10 (cm)  
width = 11cm  


a = width  
b = distance  

r구하기
$f(x)=r\cdot cos^{-1}(\frac{r-a}{r})-b$
$f'(x) = cos^{-1}(1 - \frac{a}{r}) - \frac{(\frac{1}{r}-\frac{r-a}{r^2})r}{\sqrt{1-\frac{(r-a)^2}{r^2}}}$
$r_2 = r_1  -  \frac{f(r_1)}{f'(r_1)}$

cameraPointDistance = 16  

$반지름 = \sqrt{r^2-cameraPointDistance ^2}$  

차세로길이  = 21  
$(\frac{180}{\pi})*tan^{-1}(\frac{차세로길이}{반지름})$
