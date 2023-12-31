#f import stuff!
import numpy as np
import logging
#d
def _fft_base(array: np.array, conjugate=True, scale=True ) -> np.array:#f
    #f docstring
    """
    Performs a complex Fast Forier Transform!
    Arrays must be of a size that is a power of two.
    
    array:
        the array we would like to transformed
    conjugate:
        set True if you would like the matrix to effectively be conjugated
    scale:
        set True if the matrix should be downscaled
    
    The default settings: (conjugate=True, scale=False) perform a standard fft transformation
    This may be defined as X_n = sum(start=0,end=N-1,iterator=z,x_n*e^(-2*pi*i*n*z/N))
    
    Where x is a vector of length N representing the value representation at the points a/N for a is 0 to N-1
    Where X is a vector of length N representing the complex frequency representation in frequencies of 0 hz to N-1 hz
    Where N is an integer which has no prime factors besides 2 (The length must be an exponentiation of 2)
    Where X_n is the nth number in X (zero indexed)
    Where x_n is the nth number in x (zero indexed)

    To perform a standard inverse fft transform apply ( conjugate=False , scale=True )
    
    This may be defined as x_n = sum(start=0,end=N-1,iterator=z,X_n*e(2*pi*i*n*z/N)/N)

    On a sidenote. The scale on the inverse makes... less intuitive sense to me. However this will remain here because I have been led to believe that the downscale is standardly placed on the inverse, rather than the forward transformation.
    """
    #d
    logging.debug("FFT called")
    #f copy the array
    array = np.array(array)
    #d
    #f create the modifier
    #f produce the base
    initialModifier = np.e**(
            2j*np.pi
            *
            np.arange(len(array)/2)
            /
            len(array)
            )
    logging.debug("modifiers created")
    #d
    #f scale if needed
    if scale:
        array /= len(array)#d
    #f conjugate if specified
    if conjugate:
        initialModifier = np.conj(initialModifier)
    #d
    #d
    #f define recursive function!
    def FFTRecursiveHelper(array: np.array,oddSegmentModifier) -> None:
        #f docstring
        """
        Helper function which computes the whole thing
        This function uses mutation rather than returns because it felt cleaner here
        array - array to be mutated
        oddSegmentModifier - the modifier, determined by the forward/backwardness of the array
        """
        #d
        logging.debug(f"Helper called {array=} {len(array)=}")
        #f deal with base case!
        if len(array) == 1:
            logging.debug("base case reached, returning")
            return array
        #d
        #f deal with recursive case!
        #f split array into segments!
        firstHalf = array[0:len(array)//2]
        secondHalf = array[len(array)//2:len(array)]
        evenSegments = firstHalf + secondHalf
        oddSegments = firstHalf - secondHalf
        #d
        #f find results for each segment!
        #f find result for even segment!
        #f solve using recursion!
        FFTRecursiveHelper(evenSegments,oddSegmentModifier[0::2])
        #d
        #d
        #f find result for odd segment!
        #f modify odd segment for recursion
        oddSegments = np.multiply(oddSegments,oddSegmentModifier)
        #d
        #f solve using recursion!
        FFTRecursiveHelper(oddSegments,oddSegmentModifier[0::2])
        #d
        #d
        #d
        #f interleave the results!
        #f interleave evens results
        array[0::2] = evenSegments
        #d
        #f interleave odd results
        array[1::2] = oddSegments
        #d
        #d
        #d
    logging.debug("FFT helper function defined")
    #d
    #f call recursive function
    FFTRecursiveHelper(array,initialModifier)
    #d
    return array
    #d
def ffft(array: np.array) -> np.array: #f
    #f docstring
    """
    Performs a FFT operation

    This operation quickly converts a vector representing a time value domain x to a vector representing a frequency value domain X.

    This function requires that all array inputs to it be of the length 2**k where k is some integer.

    This may be defined as X_n = sum(start=0,end=N-1,iterator=z,x_n*e^(-2*pi*i*n*z/N))
    
    Where x is a vector of length N representing the value representation at the points a/N for a is 0 to N-1
    Where X is a vector of length N representing the complex frequency representation in frequencies of 0 hz to N-1 hz
    Where N is an integer which has no prime factors besides 2 (The length must be an exponentiation of 2)
    Where X_n is the nth number in X (zero indexed)
    Where x_n is the nth number in x (zero indexed)
    """
    #d
    return(_fft_base( array , conjugate=True , scale=False ))
#d
def ifft(array: np.array) -> np.array: #f
    #f docstring
    """
    Performs an inverse FFT operation

    This operation quickly converts a vector representing a frequency value domain X to a vector representing a time value domain x.

    This function requires that all array inputs to it be of the length 2**k where k is some integer.

    This may be defined as X_n = sum(start=0,end=N-1,iterator=z,x_n*e^(2*pi*i*n*z/N)/N)
    
    Where x is a vector of length N representing the value representation at the points a/N for a is 0 to N-1
    Where X is a vector of length N representing the complex frequency representation in frequencies of 0 hz to N-1 hz
    Where N is an integer which has no prime factors besides 2 (The length must be an exponentiation of 2)
    Where X_n is the nth number in X (zero indexed)
    Where x_n is the nth number in x (zero indexed)
    """
    #d
    return(_fft_base( array , conjugate=False , scale=True ))
#d
#f testing!
if __name__ == "__main__":
    print('Starting fft Test')
    initialArray = np.array([1,2,3,4,4,3,2,1],dtype='cdouble')
    transformedArray = ffft(initialArray)
    untransformedArray = ifft(transformedArray)
    transformationError = np.linalg.norm(initialArray-untransformedArray)/np.linalg.norm(initialArray)
    if transformationError < 0.01:
        print('test passed!')
    print(f"{initialArray=}\n{transformedArray=}\n{untransformedArray=}\n{transformationError=}")
    print('testing convolution')
    initialArray = np.array([1,1,1,0,0,0,0,0],dtype='cdouble')
    manualArray = np.array([1,2,3,2,1,0,0,0],dtype='cdouble')
    convolvedArray = ifft(np.power(ffft(initialArray),2))
    transformationError = np.linalg.norm(manualArray-convolvedArray)
    if transformationError < 0.01:
        print('test passed!')
    print(f'{initialArray=}\n{np.round(convolvedArray)=}\n{transformationError=}')
#d
