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