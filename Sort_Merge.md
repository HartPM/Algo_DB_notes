- arrays with 0 or 1 element are sorted by nature. To sort a longer array, break each element down into it's own single element array. Then, merging adjacent sorted arrays is easier, and continue the process until you have one sorted array.
- Create a helper function to merge two arrays. This function will have O(n + m) time and space complexity


function merge(arr1, arr2){
  let sortedArr= [];

  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length){
    if(arr1[i] < arr2[j]){
      sortedArr.push(arr1[i])
      i++;
    }else{
      sortedArr.push(arr2[j])
      j++;
    }
  }

  if(arr1.length !== i){
    while(i<arr1.length){
      sortedArr.push(arr1[i])
      i++
    }
  }
    if(arr2.length !== j){
    while(j<arr2.length){
      sortedArr.push(arr2[j])
      j++
    }
  }
  return sortedArr
}

function mergeSort(arr){
    if(arr.length <= 1) return arr;

    let mid = Math.floor(arr.length / 2);
    let left = mergeSort(arr.slice(0, mid));
    let right = mergeSort(arr.slice(mid));

    return merge(left, right);
}



- Time: O(n log(n)) 
    This is the best time complexity possible regardless of data type for a sorting algo. Radix sort can do better but only on collections of numbers.

- Space: O(n)