Maps

- Allows the usage of primitives and objects as keys and values
- JS objects can only accept one object as a key and stores the last object
    - Maps can store multiple objects as key value pairs

const myMap = new Map([ ['name', 'John'], ['surname', 'Doe'] ])
    => Map { 'name' => 'John', 'surname' => 'Doe' }


const a = {};
const b = {};

const myMap = new Map([ [a, 'a'], [b, 'b'] ])
    => Map { {} => 'a', {} => 'b' }


- Methods

myMap.set(1, 'one');

myMap.delete(1);

myMap.clear();

myMap.has(1)

myMap.size  