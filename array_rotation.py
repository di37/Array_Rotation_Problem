def arr_rotation(arr, d):
    '''Performs left rotation by d units to the left. 

    Parameters:
        arr - Array of integers.
        d - Number of rotations.

    Returns:
        Resulting array after rotation operation is performed.    
    '''
    return arr[d:] + arr[:d]

# Testing
print(arr_rotation([1,2,3,4,5], 2))