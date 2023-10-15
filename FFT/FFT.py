import numpy as np
def FFT(array,forward=True): #f
    """
    Recursive function for both FFT and IFFT
    """
    #f define recursive function!
    def FFTrecurse(array):
        #f deal with base case!
        if len(array) == 1:
            return array[0]
        #d
        #f deal with recursive case!
        #f split array into segments!
        firstHalf = array[0:len(array)//2]
        secondHalf = array[len(array)//2,len(array)]
        evenSegments = firstHalf + secondHalf
        oddSegments = firstHalf - secondHalf
        #d
        #f modify odd segment
        #f set multiplier according to forward/inverse mode of operation!
        multiplier = np.e**(1.0j/len(array))
        if forward:
            multiplier *= -1
        #d
        #f create modifier
        segmentModifier = np.power(multiplier,np.arange(length/2))
        #d
        #f perform modification!
        oddSegments = np.multiply(oddSegments,segmentModifier)
        #d
        #d
        #f find odd and even results!
        evenResults = FFT_HELPER(evenSegments)
        oddResults = FFT_HELPER(oddSegments)
        #d
        #f interleave the results
        Results = np.array(length)
        Results[0::2] = evenResults
        Results[1::2] = oddResults
        #d
        return Results
        #d
    return FFTrecurse(array)
    #d
    #d

