- Linear Search
    -Searches one by one for an element in an array
    -Built in JS methods that use linear search:
        .indexOf()
        .includes()

    function linearSearch(arr, search) {
        for (let i = 0; i < arr.length; i++){
            if (arr[i] === search) return i;
        } return -1;
    }


- Binary Search
    - Data has to be sorted
    - Rather than eliminating one element at a time, we throw out half of the data at each step. (Divide and conquer)


    function binarySearch(arr, search){
        let left = 0;
        let right = arr.length - 1;
        let mid = Math.floor((left + right) / 2);
        
        while (arr[mid] !== search && left <= right) {
            if (search < arr[mid]){
                right = arr[mid] -1;
            } else { 
                left = arr[mid] +1;
            }
            mid = Math.floor((left + right) / 2);
        }
        
        return arr[mid] === search ? mid : -1
    }



- Naive string searching algorithm
- KMP string searching algorithm
