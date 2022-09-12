- Unlike bubble sort, this approach accumulates sorted data at the beginning of the array
- Find the minimum value in the array and swap it with whatever value is in the 0 index. Then repeat for each additional element in the array.

function selectionSort(arr){
    for (let i = 0; i < arr.length; i++){
        let min = i;
        for (let j = i+1; j < arr.length; j++){
            if(arr[j] < arr[min]) min = j;
        }
        let temp = arr[i];
        arr[i] = arr[min];
        arr[min] = temp;
    }
  return arr
}

- The code above automatically swaps values at the end of every inner loop. We can make the code more efficient by checking to see if a smaller value was found.

function selectionSort(arr){
    for (let i = 0; i < arr.length; i++){
        let min = i;
        for (let j = i+1; j < arr.length; j++){
            if(arr[j] < arr[min]) min = j;
        }
        if(min !== i){
            let temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
  return arr
}

- Time complexity O(n^2)
- The only advantage of selection sort over bubble sort is that there are fewer swaps occurring in each loop (at most 1).
- For nearly sorted data, Selection Sort is much slower than Bubble Sort or Insertion Sort.