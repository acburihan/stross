# STROTSS

See the original code and links to paper at https://github.com/nkolkin13/STROTSS

See the forked version we've based ourselves on at https://github.com/futscdav/strotss

We've created altered versions of the stross.py file with different distances for the content loss.

In strossEuclidianDistance.py we've deleted the original cosine distance and used only the euclidian distance already defined, thus it doesn't the scale invariance needed for self similarity and the results are unsatisfactory.

In stross.py we've used the cosine distance in the content loss, which is the original implementation. This version clearly mantains the scale invariance.

In strossPearsonDistance.py we've used the pearson distance in the content loss. This version mantains the scale invariance and wields very similar results to the original implementation.

<img src="https://latex.codecogs.com/gif.latex?d_{X, Y}=1-\rho_{X, Y}" />
<img src="https://latex.codecogs.com/gif.latex?r_{x y}=\frac{\sum_{i=1}^n\left(x_i-\bar{x}\right)\left(y_i-\bar{y}\right)}{\sqrt{\sum_{i=1}^n\left(x_i-\bar{x}\right)^2} \sqrt{\sum_{i=1}^n\left(y_i-\bar{y}\right)^2}}" />


In strossAngularPearsonDistance.py we've used the analogous angular formulation of the pearson distance in the content loss. This version still mantains the scale invariance and wields unconsistent results depending on the images used.
<img src="https://latex.codecogs.com/gif.latex?d_{X, Y}=1-\rho_{X, Y}" />
<img src="https://latex.codecogs.com/gif.latex?r_{\text {circular }}=\frac{\sum_{i=1}^n \sin \left(x_i-\bar{x}\right) \sin \left(y_i-\bar{y}\right)}{\sqrt{\sum_{i=1}^n \sin \left(x_i-\bar{x}\right)^2} \sqrt{\sum_{i=1}^n \sin \left(y_i-\bar{y}\right)^2}}" />

Usage:
```
python strotss.py <content> <style> [--weight 1.0] [--output strotss.png] [--device "cuda:0"]
```

<p align="center">
  <img src="content.jpg" width="350" title="Content">
  <img src="style.png" width="350" alt="Style">
  <img src="strotss.png" width="350" alt="Result">
</p>
