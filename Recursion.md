- A function that calls itself
- different that standard iterative approach
- Call-stack is the order in which Javascript function calls are executed
    -stack overflow occurs when base case is missing or not correct

    function factorial(num) {
        if (num === 1) return 1;
        return num * factorial(num);
    }

- Helper method recursion

    function collectOddValues(arr) {
        let result = [];
        
        function helper(helperInput) {
            if (helperInput.length === 0) return;
            if (helperInput[0] % 2 !== 0) {
                result.push(helperInput[0]);
            helper(helperInput.slice(1));
            }
        }
        helper(arr);
        return result;
    }


- Pure recursion

    function collectOddValues(arr) {
        let newArr = [];

        if (arr.length === 0) {
            return newArr;
        }

        if (arr[0] !== 0) {
            newArr.push(arr[0]);
        }

        newArr = newArr.concat(collectOddValues(arr.slice(1)));
        return newArr;
    }
