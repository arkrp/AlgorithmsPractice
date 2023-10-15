### 
import numpy as np
import logging
logging.basicConfig(level=logging.DEBUG)
###
def FFT(array: np.array, forward=True, dtype='cdouble') -> None:#f
    logging.debug("FFT called")
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
    #f convert to more precise datatype
    array = np.array(array,dtype=dtype)
    #d
    #f create initial modifier
    initialModifier = np.e**(
            2j*np.pi
            *
            np.arange(len(array)/2,dtype=dtype)
            /
            len(array)
            )
    logging.debug("modifiers created")
    #d
    #f scale if forward
    if forward:
        array /= len(array)#d
    else:
        initialModifier = np.conj(initialModifier)
    #f define recursive function!
    def FFTRecursiveHelper(array: np.array,oddSegmentModifier) -> np.array:
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
        evenResults = FFTRecursiveHelper(evenSegments,oddSegmentModifier[0::2])
        #d
        #d
        #f find result for odd segment!
        #f modify odd segment for recursion
        oddSegments = np.multiply(oddSegments,oddSegmentModifier)
        #d
        #f solve using recursion!
        oddResults = FFTRecursiveHelper(oddSegments,oddSegmentModifier[0::2])
        #d
        #d
        #d
        #f interleave the results!
        #f interleave evens results
        array[0::2] = evenResults
        #d
        #f interleave odd results
        array[1::2] = oddResults
        #d
        #d
        return array
        #d
    logging.debug("FFT helper function defined")
    #d
    return FFTRecursiveHelper(array, initialModifier)
    #d
###
initialArray = np.array([1,2,3,4])
transformedArray = FFT(initialArray)
untransformedArray = FFT(transformedArray, forward=False)
print(f"{initialArray=}\n{transformedArray=}\n{untransformedArray=}")
###
