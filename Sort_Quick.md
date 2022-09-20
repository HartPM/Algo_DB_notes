- Like merge sort, move all elements of an array into their own single element arrays
- Pick a pivot index and move everything that is greater than the pivot to the right and everything that is less than to the left
- Then perform the same moving around of elements about a pivot point on the left and the right side, continuing to subdivide until all elements are sorted together

1. Build helper function to arrange elements on either side of the pivot. Order doesn't matter, just rearrange the array in place
- Ideally the pivot should be the mean value in the array. However, you can just pick the first element but know that the selected first pivot can affect time complexity.
2. Return the pivot index when complete
3. Recursively call quickSort on all elements to the left side and to the right side of the returned pivot index.


function pivot(arr, start=0, end=arr.length+1) {
    function swap(arr, i, j) {
        let temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    let pivot = arr[start];
    let swapIdx = start;
    
    for(let i = start+1; i <arr.length; i++) {
        if(pivot > arr[i]) {
            swapIdx++;
            swap(arr, swapIdx, i);
        }
    }
    swap(arr, start, swapIdx);
    return swapIdx;
}


function quiSort(arr, left = 0, right = arr.length -1){
    if (left < right){
        let pivotIndex = pivot(arr, left, right)
        //left recursive call
        quickSort(arr, left, pivotIndex -1);
        //right recursive call
        quickSort(arr, pivotIndex +1, right);
    }
    return arr;
}


- Time Complexity:
    - Worst Case: O(n^2)
    - Average/ Best: O(n log n)

- Space Complexity: O(log n)