- Not the most efficient or often used but it is a good starting point to understanding how sorting algorithms work.

- Basic implementation would run through a nested loop arr.length number of times and compare adjacent elements and swapping the two elements currently in view if they are out of order. This takes the largest element and moves it to the end of the array. However, at each subsequent iteration, the algorithm checks back over the end of the array, which is already sorted at this point. To better optimize our algorithm, we can prevent the loop from scanning over the elements at the end of the array that we know are already sorted. Here's the optimized solution:

function bubbleSort(arr){
    for (let i = arr.length; i > 0; i--) {
        for (let j = 0; j < i-1; j++){
            if(arr[j] > arr[j+1]){
                let temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    return arr;
}

- The inner loop compares two adjacent elements at a time and swaps them if they are out of order until it reaches the end of the array. At this point the largest value bubbles to the top (the largest value moves to the end of the array). 
- Now we know the last element in the array is sorted, so we can look at all of the remaining elements (arr.length - 1). We repeat the previous steps and now the last 2 elements in the array are sorted so we reduce the number of elements again.
- repeat until the last two elements of the array are sorted and return the sorted array.


- The solution above is horribly inefficient when dealing with arrays that just have a few elements out of order because it will continue looping until it reaches the end even if the array is correctly ordered after just one or two steps through the loop. To further optimize the algorithm, we can break out of the loop if no swaps were made on a given pass-- this indicates the array is in order!

function bubbleSort(arr){
    let noSwaps;
    for (let i = arr.length; i > 0; i--) {
        noSwaps = true;
        for (let j = 0; j < i-1; j++){
            if(arr[j] > arr[j+1]){
                let temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                noSwaps = false;
            }
        }
        if (noSwaps) break;
    }
    return arr;
}

- Time Complexity: O(n^2) unless you know the data is nearly sorted, then potentially Bubble Sort could be a good algorithm to use with a time complexity of O(n)