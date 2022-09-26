- 2 types of sorting algorithms include comparison sort like we've seen in all other examples. The other type takes advantage of some property of the data. Integer sorting is the type of sorting Radix Sort uses.
- Never makes comparisons between to elements. Just sorts lists of numbers-- often non-numerical values are converted to binary to be sorted
- starting from the right most digit in each number of a list, group the numbers into buckets where each number in a bucket has the same right most digit. Then add them all back to the list in order. Repeat this step for the second to last digit and so on. Must repeat this x number of times where x = the length or number of digits of the longest number.


- Use a helper function to find the digit at a given position from the right:

    function getDigit(num, i) {
        return Math.floor(Math.abs(num) / Math.pow(10, i)) % 10;
    }

- Use a helper function to figure out the number of digits in a given number:

    function digitCount(num){
        if (num === 0 ) return 1;
        return Math.floor(Math.log10(Math.abs(num))) + 1;
    }
    
- Use a helper function to figure out how many digits are in the largest number in a list:

    function mostDigits(nums){
        let maxDigits = 0;
        for (let i = 0; i < nums.length; i++){
            maxDigits = Math.max(MaxDigits, digitCount(nums[i]));
        }
        return maxDigits;
    }

- Implementation:

    function radixSort(nums){
        let maxDigitCount = mostDigits(nums);
        for (let k = 0; k < maxDigitCount; k++){
            let digitBuckets = Array.from({length: 10}, () => []);
            for (let i = 0; i < nums.length; i++){
                let digit = getDigit(nums[i], k);
                digitBuckets[digit].push(nums[i]);
            }
            nums = [].concat(...digitBuckets);
        }
        return nums
    }



- Notes:
    use of the spread operator:
    let digitBuckets = [[1], [2], [3]]
    nums = [].concat(...digitBuckets)           => [1, 2, 3]

    nums = [].concat(digitBuckets)              => [[1], [2], [3]]

    