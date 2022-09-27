- More often used that bubble or selection sort but only good in certain scenarios
- Builds up a sorted portion of the array and inserts additional elements into the sorted side where they belong
- Works well when data is coming in live and you need to insert it in order

function insertionSort(arr){
    for(let i = 1; i < arr.length; i++){
        let currentVal = arr[i];
        let j = i -1;

        while(j >= 0 && arr[j] > currentVal){
            arr[j+1] = arr[j];
            j--;
        }

        arr[j+1] = currentVal;
    }
    return arr
}

- Time Complexity: O(n^2)
- Space Complexity: O(1)