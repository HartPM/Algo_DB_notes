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



- Fibonacci
    Write a recursive function called fib which accepts a number and returns the nth number in the Fibonacci sequence. Recall that the Fibonacci sequence is the sequence of whole numbers 1, 1, 2, 3, 5, 8, ... which starts with 1 and 1, and where every number thereafter is equal to the sum of the previous two numbers.

        // fib(4) // 3
        // fib(10) // 55
        // fib(28) // 317811
        // fib(35) // 9227465

    function fib(n){
        if (n <= 2) return 1;
        return fib(n-1) + fib(n-2)
    }

//4 
//3     + 2
//2 + 1 + 1
//1 + 1 + 1 = 3


- Reverse String
    Write a recursive function called reverse which accepts a string and returns a new string in reverse.

    function reverse(str){
        if (str.length <= 1) return str;
        return reverse(str.slice(1)) + str[0];
    }
