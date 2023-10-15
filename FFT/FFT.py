### 
import numpy as np
import logging
#logging.basicConfig(level=logging.DEBUG)
###
def FFT(array: np.array, forward=True) -> np.array:#f
    #f docstring
    """
    performs a complex Fast Forier Transform!
    CURRENTLY ONLY WORKS IF THE ARRAY IS 2**n IN SIZE!
    array
        the array we would like to transformed
    forward:
        True - converting from a time domain to a frequency domain
        False   - converting from a frequency domain to a time domain
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
    #f scale if forward
    if forward:
        array /= len(array)#d
    #f conjugate if reverse
    else:
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
###
initialArray = np.array([1.1,2.5,3.1,4.9],dtype='cdouble')
transformedArray = FFT(initialArray)
untransformedArray = FFT(transformedArray, forward=False)
print(f"{initialArray=}\n{transformedArray=}\n{untransformedArray=}")
###
