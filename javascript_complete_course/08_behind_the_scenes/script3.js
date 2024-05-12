'use strict';

// Primitive types
let lastName = 'Williams';
let oldLastName = lastName;
lastName = 'Davis';
console.log(lastName, oldLastName);

// Reference Types
const jessica = {
  firstName: 'Jessica',
  lastName: 'Williams',
  age: 27,
};

const marriedJessica = jessica;
marriedJessica.lastName = 'Davis';
console.log('Before marriage: ', jessica);
console.log('After marriage: ', marriedJessica);

// Copying objects
const jessica2 = {
  firstName: 'Jessica',
  lastName: 'Williams',
  age: 27,
  family: ['Alice', 'Bob'],
};

// Creates a "shallow" clone (first level) so any objects are still references
const jessica2Copy = Object.assign({}, jessica2);
jessica2Copy.lastName = 'Davis';
console.log('Before marriage: ', jessica2);
console.log('After marriage: ', jessica2Copy);

jessica2Copy.family.push('Mary');
jessica2Copy.family.push('John');
