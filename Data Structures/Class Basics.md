- Class
    - JS uses prototype inheritance. Classes were added in ES2015 as syntactic sugar. JS is not an Object Oriented language.

    class Student{
        constructor(firstName, lastName, year){
            this.firstName = firstName;
            this.lastName = lastName;
            this.grade = year;
        }
    }


- Object instantiation

    let firstStudent = new Student('John', 'Doe', 3)


- Instance methods

        class Student{
        constructor(firstName, lastName, year){
            this.firstName = firstName;
            this.lastName = lastName;
            this.grade = year;
        }
        fullName(){
            return `Your full name is ${this.firstName} ${this.lastName}`;
        }
    }

    firstStudent.fullName()         // 'Your full name is John Doe'

- Class methods

    - use the 'static' keyword in front of a method to make it a class method
    - often used to create utility functions for an application
    
    static enrollStudents(){
        return "Enrolling students!"
    }
    