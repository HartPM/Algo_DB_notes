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
    function naiveSearch(long, short){
        let count = 0;
        for (let i = 0; i < long.length; i++){
            for (let j = 0; j < short.length; j++){
                if(short[j] !== long[i+j]){
                    break;
                }
                if (j === short.length - 1) {
                    count++;
                }
            }
        }
        return count;
    }

    naiveSearch("lorie loled", "lol") ==> should return 1




- KMP string searching algorithm
