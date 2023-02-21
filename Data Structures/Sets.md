Set
    - store unique values of any type, whether primitive values or object references
    - sets remove duplicate values
    - Sets are an unordered pool of unique values

    const myArray = [1,2,3,4,5,5,5,1];
    const mySet = new Set(myArray);

    console.log(mySet)
        => Set {1,2,3,4,5}

    const uniqueArray = [...mySet]


    - Set Methods

        mySet.add(6)
        mySet.add('hello')
        mySet.add({class: 'Learn JS'})
        mySet.add([6,7,8])

        mySet.delete(3) => Set {1,2,4,5}

        mySet.clear() => Set {}

        mySet.has(1) => true

        mySet.size => 5
