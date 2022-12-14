- Like an array but without an indexed location. More like a train with cars linked to one another.
- contains a head, tail, and length property.
- consists of nodes. Each node contains a value and a pointer to another node or null.
- each node only points to the next node. Nodes do not point backwards to the previous node.
- cannot randomly access a node. Must traverse from the beginning.
- The benefit is that insertions and deletions are much faster than with an array.


class Node{
    constructor(val){
        this.val = val;
        this.next = null;
    }
}

    - We can create the linked list without a class (for demo, best to use a class)

        const first = new Node("Hi")
        first.next = new Node("There")
        first.next.next = new Node("How")
        first.next.next.next = new Node("Are")
        first.next.next.next.next = new Node("You")
    

- Using a class:

    class SinglyLinkedList{
        constructor(){
            this.head = null;
            this.tail = null;
            this.length = 0;
        }

        push(val){
            let newNode = new Node(val);
            if (!this.head) {
                this.head = newNode;
                this.tail = this.head;
            } else {
                this.tail.next = newNode;
                this.tail = newNode;
            }
            this.length++;
            return this;
        }

        traverse(){
            let current = this.head;
            while(current){
                console.log(current.val);
                current = current.next;
            }
        }

        pop(){
            if(!this.head) return undefined;
            let current = this.head;
            let previous = null;
            while(current.next){
                previous = current.val;
                current = current.next
            }
            this.tail = previous;
            this.tail.next = null;
            this.length--;
            if(this.length === 0){
                this.head = null;
                this.tail = null;
            }
            return current
            }
        }

        shift(){
            if(!this.head) return undefined;
            let currentHead = this.head;
            this.head = currentHead.next;
            this.length --;
            return currentHead;
        }

        unshift(val){
            let newNode = new Node(val);
            if(!this.head){
                this.head = newNode;
                this.tail = this.head;
            } else {
                newNode.next = this.head;
                this.head = newNode;
            }
            this.length++;
            return this;
        }

        get(index){
            if(index < 0 || index >= this.length) return null;
            let counter = 0;
            let current = this.head;
            while(counter !== index){
                current = current.next;
                counter++;
            }
            return current;
        }

        set(index, val){
            let foundNode = this.get(index);
            if(foundNode){
                foundNode.val = val;
                return true;
            }
            return false; 
        }

        insert(index, val){
            if(index < 0 || index > this.length) return false;
            if(index === this.length) return !!this.push(val);
            if(index === 0) return !!this.unshift(val);
            
            let newNode = new Node(val);
            let prev = this.get(index - 1);
            let temp = prev.next;
            prev.next = newNode;
            newNode.next = temp;
            this.length++;
            return true;
        }

        remove(index){
            if(index < 0 || index >= this.length) return undefined;
            if(index === 0) return this.shift();
            if(index === this.length - 1) return this.pop();

            let previousNode = this.get(index -1);
            let removed = previousNode.next;
            previousNode.next = removed.next;
            this.length--;

            return removed;
        }

        //helper function to see how the following reverse method works//
        print(){
            let arr = [];
            let current = this.head;
            while(current){
                arr.push(current.val);
                current = current.next;
            }
            console.log(arr);
        }

        reverse(){
            let node = this.head;
            this.head = this.tail;
            this.tail = node;
            let next;
            let prev = null;
            
            for(let i = 0; i < this.length; i++){
                next = node.next;
                node.next = prev;
                prev = node;
                node = next;
            }
            return this;
        }

    }



    let list = new SinglyLinkedList()
    list.push("hello")
    list.push("goodbye")
    


- Big O
    - Insertion: O(1)
    - Removal: O(1) or O(n)
    - Searching: O(n)
    - Accessing: O(n)

    - If you don't need random access, a linked list excels at insertion and removal where an array would require re-indexing every item for these same tasks.  
