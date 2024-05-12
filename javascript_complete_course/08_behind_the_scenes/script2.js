'use strict';

var firstName = 'Matilda';

const jonas = {
  firstName: 'Jonas',
  year: 1991,
  calcAge: function () {
    console.log(this);
    console.log(2037 - this.year);

    // Solution 1
    // const self = this; // Sometimes "that" is also used
    // const isMillennial = function () {
    //   console.log(self);
    //   console.log(self.year >= 1981 && self.year <= 1996);
    // };

    // Solution 2
    // Works because arrow function inherits the "this" from parent
    const isMillennial = () => {
      console.log(this);
      console.log(this.year >= 1981 && this.year <= 1996);
    };
    isMillennial();
  },
  greet: () => {
    console.log(this);
    console.log(`Hey ${this.firstName}`);
  },
};

jonas.greet(); // Prints "Hey Matilda"
console.log(this.firstName); // Prints Matilda
jonas.calcAge();

// Arguments
const addExpr = function (a, b) {
  console.log(arguments);
  return a + b;
};

addExpr(2, 5);
addExpr(2, 5, 6, 12);

// Arguments does not exist in arrow functions
var addArrow = (a, b) => {
  //console.log(arguments);
  return a + b;
};
addArrow(2, 5, 7);

// Primitives vs reference types
let age = 30;
let oldAge = age;
age = 31;

console.log(age);
console.log(oldAge);

const me = {
  name: 'Jonas',
  age: 30,
};

const friend = me;
friend.age = 28;

console.log('Me: ', me);
console.log('Friend: ', friend);
