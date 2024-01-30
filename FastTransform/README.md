# Fast Transforms

Author: Hannah Nelson
Date: January 30, 2024

This module contains standard Fast Fourier Transform algorithms.

Specifically this module contains:
FFT.ffft - The standard Fast Fourier Transform algorithm
FFT.ifft - The standard Inverse Fast Fourier Transform algorithm

## Usage

To make use of the transform import the module with the desired transform and then call the subroutine from that module. Transforms of the module are designed to use NumPy arrays
Example usage:
```
import AlgorithmsPractice.FastTransform.FFT as FFT
import numpy as np
print(FFT.ffft(np.Array([1,2,3,4])))
```

## Principle of operation
### What is the Discreet Fourier Transform?
The fundemental idea of the Fourier Transform is that a signal can be represented as a sum of waves of multiple frequencies. By treating our signal as a vector we can project it onto the basis which is our waves of frequencies!

The following vector is the discreet representation of a wave with frequency of n cycles per signal on a signal of N samples in length. 
```math
\textbf{v}_n=\begin{bmatrix}v_{k}\end{bmatrix}_{N{\times}1}
```
where
```math
v_{k} = e^{\frac{-2{\pi}ik}{n}}
```
It can be shown that the vectors $v_n$ for $n=1,2,3{\ldots}$ are orthagonal to each other. Due to this orthagonality it is trivially easy to create a orthonormal matrix $A$ which can simply convert from representation as sum of time measurements to representation as sum of waves.
The matrix A is as follows:
```math
A=\begin{bmatrix}a_{k,j}\end{bmatrix}_{N{\times}N}
```
where
```math
a_{k,j} = \frac{1}{\sqrt{N}}e^{\frac{-2{\pi}ikj}{n}}
```
Because of $A$ is orthonormal it is trivial to create its inverse $A^{-1}$ by transposing it and conjugating it!
```math
A^{-1}=\begin{bmatrix}a_{k,j}\end{bmatrix}_{N{\times}N}
```
where
```math
a_{k,j} = \frac{1}{\sqrt{N}}e^{\frac{2{\pi}ikj}{n}}
```
This allows for easy conversion of a sum of waves representation back into the original signal format.

TODO Note that the standard convention is to move the multiplication to the inverse

The Discreet Fourier Transform is the use of this matrix to convert signals into wave representations and back. The ability to convert something to frequency representation is immensely useful for any application which neccesitates the use of frequency and any application which is dependent on the measurement of frequency.

### The Fast Fourier Transformation
How to multiply faster?
TODO Explain how the FFT algorithm makes the multiplication by this matrix faster
