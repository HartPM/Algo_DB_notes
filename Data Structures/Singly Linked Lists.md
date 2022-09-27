- Like an array but without an indexed location. More like a train with cars linked to one another.
- contains a head, tail, and length property.
- consist of nodes. Each node contains a value and a pointer to another node or null.
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
    }

    let list = new SinglyLinkedList()
    list.push("hello")
    list.push("goodbye")
    