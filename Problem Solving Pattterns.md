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
    - Used on array, string, or linked list. 
    - Usually looking for a pair of values that match each other
    - Uses two pointers or variables (i, j) that correspond to indices, working across an array in a direction to compare the two pointers.
    - Often useful with sorted arrays or strings.

    -Ex_1:
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

    -Ex_2:
        Write a function called isSubsequence which takes in two strings and checks whether the characters in the first string form a subsequence of the characters in the second string. In other words, the function should check whether the characters in the first string appear somewhere in the second string, without their order changing.

        Examples:

        isSubsequence('hello', 'hello world'); // true
        isSubsequence('sing', 'sting'); // true
        isSubsequence('abc', 'abracadabra'); // true
        isSubsequence('abc', 'acb'); // false (order matters)
        Your solution MUST have AT LEAST the following complexities:

        Time Complexity - O(N + M)

        Space Complexity - O(1)

    - Solution:
        function isSubsequence(str1, str2) {
            let i = 0;
            let j = 0;
            if (!str1) return true;
            while (j < str2.length) {
                if (str2[j] === str1[i]) i++;
                if (i === str1.length) return true;
                j++;
            }
            return false;
        }


- Sliding Window
    - Used to keep track of subsets within an array or string.
    - Array doesn't have to be sorted.
    - Time: O(n)

    - Ex_1:
        - Write a function called maxSubArraySum which accepts an array of integers and a number called n. The function should calculate the maximum sum of n consecutive elements in the array.

    - Solution:
        function maxSubArraySum(arr, n) {
            let maxSum = 0;
            let tempSum = 0;
            if (arr.length < n) return null;
            for (let i= 0; i < n; i++){
                maxSum += arr[i]
            }
            tempSum = maxSum;
            for (let i = n; i < arr.length; i++){
                tempSum = tempSum - arr[i - n] + arr[i];
                maxSum = Math.max(maxSum, tempSum);
            }
            return maxSum;
        }

    - Ex_2:
        Write a function called minSubArrayLen which accepts two parameters - an array of positive integers and a positive integer.

        This function should return the minimal length of a contiguous subarray of which the sum is greater than or equal to the integer passed to the function. If there isn't one, return 0 instead.
        
        Examples:

        minSubArrayLen([2,3,1,2,4,3], 7) // 2 -> because [4,3] is the smallest 

    - Solution:
        function minSubArrayLen(nums, sum) {
            let total = 0;
            let minLength = nums.length + 10; 
            let start = 0;
            let end = 0;

            while (start < nums.length) {
                if (total < sum && end < nums.length) {
                total += nums[end]
                end ++
                }
                else if (total >= sum) {
                minLength = minLength < (end - start) ? minLength : end - start;
                total -= nums[start]
                start ++
                } 
                else {
                break;
                }
            }
            return minLength > nums.length ? 0 : minLength
        }


- Divide and Conquer
    -Ex:
        Given a sorted array, return the index where a given element is found.

        arr = [1, 2, 3, 4, 5], n = 4 | returns 3

    - Naive solution (linear search):
        Loop over each element and check to see if element at that index is the same as n.
        O(n) time complexity

    - Solution (binary search):
        - pick a middle point in the given array. If this value is less than n, throw out the latter half of the array and search just the first half (or vice versa). Continue on this pattern until n is found or return -1 if n is not in the array.
        - Time: O(Log(n))

        function search(arr, val) {
            let min = 0;
            let max = arr.length - 1;

            while (min <= max) {
                let middle = Math.floor((min + max) / 2);
                let currentElement = arr[middle];

                if (arr[middle] < val) {
                    min = middle + 1;
                } 
                else if (arr[middle] > val) {
                    min = middle - 1;
                }
                else {
                    return middle;
                }
            }
            return -1;
        }




- Dynamic Programming
- Greedy Algorithms
- Backtracking