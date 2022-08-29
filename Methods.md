Character codes
.charCodeAt(0) 
- 48 to 57: (0 - 9)
- 65 to 90: (A - Z)
- 97 to 122 (a - z)

Reduce
-iterates over each element of an array and stores the results of each previous iteration in the "previous" variable and then does something with the "current" element.
-Ex:
    let sum = arr.reduce((previous, current)=> previous + current)