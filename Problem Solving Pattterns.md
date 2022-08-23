- Frequency Counter
    - Uses objects or sets to collect values/ frequencies of values
    - O(N) time 
    - Ex_1: 
        Write a function called same, which accepts two arrays. The function should return true if every value in the array has it's corresponding value squared in the second array. The frequency of values must be the same.

    -Solution:
        function same(arr1, arr2){
            if(arr1.length !== arr2.length){
                return false;
            }
            let frequencyCounter1 = {}
            let frequencyCounter2 = {}
            for(let val of arr1){
                frequencyCounter1[val] = (frequencyCounter1[val] || 0) + 1
            }
            for(let val of arr2){
                frequencyCounter2[val] = (frequencyCounter2[val] || 0) + 1        
            }
            console.log(frequencyCounter1);
            console.log(frequencyCounter2);
            for(let key in frequencyCounter1){
                if(!(key ** 2 in frequencyCounter2)){
                    return false
                }
                if(frequencyCounter2[key ** 2] !== frequencyCounter1[key]){
                    return false
                }
            }
            return true
        }

        same([1,2,3,2,5], [9,1,4,4,11])


    - Ex_2: 
        Given two strings, write a function to determine if the second string is an anagram of the first. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

    - Solution:
        function validAnagram(str1, str2){
            if (str1.length !== str2.length){
                return false
            }
            
            let lookup = {}
            for (let i=0; i < str1.length; i++) {
                str1[i] in lookup ? lookup[str1[i]] +=1 : lookup[str1[i]] = 1
            }
            
            for (let i=0; i < str2.length; i++) {
                if (!lookup[str2[i]]) {
                    return false
                } else {
                    lookup[str2[i]] -= 1
                }
            }
            return true
        }



- Multiple Pointers
    -Ex:
        Implement a function called countUniqueValues, which accepts a sorted array, and counts the unique values in the array. There can be negative numbers in the array, but it will always be sorted.

    - Solution:
        function countUniqueValues(arr){
            if (arr.length === 0) {
                return 0
            }
            let i = 0
            for (let j=1; j < arr.length; j++){
                if (arr[i] !== arr[j]){
                    i += 1
                    arr[i] = arr[j]
                } 
            }
            return i + 1
        }


- Sliding Window
- Divide and Conquer
- Dynamic Programming
- Greedy Algorithms
- Backtracking