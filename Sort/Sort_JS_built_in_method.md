- JS built in method can be called with or without a comparator.
    arr = [2, 3, 15, 10]
    arr.sort() => [10, 15, 2, 3]
    - Numbers are sorted based off of their unicode, which is often not what we want. Must pass in a comparison function.


    function numCompare(num1, num2) {
        return num1 - num2;
    }

    If the function above is passed into the JS built in sort method, JS will compare two elements a & b. If the result of the function above is negative, a goes before b (order doesn't change). If positive, b goes before a (switch the position of a and b).

    arr.sort(numCompare) => [2, 3, 10, 15]



    - We could also sort by the length of a string with the following:
    function compareByLength(a, b) {
        return a.length - b.length;
    }

    ["hello", "hi", "goodbye", "yes"].sort(compareByLength) => ["hi", "yes", "hello", "goodbye"]
