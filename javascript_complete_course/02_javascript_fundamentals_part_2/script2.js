'use strict';
// Arrays
const friend1 = 'Frank';
const friend2 = 'Larry';
const friend3 = 'Joe';

// More common way
const friends = ['Frank', 'Larry', 'Joe'];
console.log(friends);
// Less common way
const y = new Array(1991, 1984, 2008, 2020);

console.log(friends[0]); // calling the 0th item
console.log(friends[2]);
console.log(friends.length); // number of elements in array
console.log(friends[friends.length - 1]); // getting the last item in the array

// Arrays are not primitive, therefore, you can modify it even though its a const
friends[2] = 'Fred'; // can mutate items directly
console.log(friends);
// friends = ['Bob', 'Alice']; This will fail

const firstName = 'Joe';
const jonas = [firstName, 'Schmoe', 2037 - 1991, 'teacher', friends];
console.log(jonas);
console.log(jonas.length);

const calcAge = function (birthYear) {
  return 2037 - birthYear;
};
const years = [1990, 1967, 2002, 2010, 2018];
const age1 = calcAge(years[0]);
const age2 = calcAge(years[1]);
const age3 = calcAge(years[years.length - 1]);
console.log(age1, age2, age3);

const ages = [
  calcAge(years[0]),
  calcAge(years[1]),
  calcAge(years[years.length - 1]),
];
console.log(ages);

// Array methods
const newLength = friends.push('Aaron'); // push returns the new length
console.log(friends);
console.log(newLength);

friends.unshift('John'); // This prepends an item to the list
console.log(friends);

friends.pop(); // Removes the last element
const popped = friends.pop(); // Returns the elements that was removed
console.log(friends);
console.log(popped);

friends.shift(); // Remove the first element
console.log(friends);

console.log(friends.indexOf('Larry')); // Returns the index of the item
console.log(friends.indexOf('Bob')); // Returns -1 if the item is not found

console.log(friends.includes('Larry')); // Returns true if found
console.log(friends.includes('Bob')); // Returns false if not found
friends.push(23);
console.log(friends.includes('23')); // Uses strict so this returns false

if (friends.includes('Larry')) {
  console.log('You have a friend named Peter');
}

// Introduction to objects
const joe = {
  firstName: 'Joe',
  lastName: 'Schmoe',
  age: 2037 - 1991,
  job: 'teacher',
  friends: ['Frank', 'Larry', 'Joe'],
};

console.log(joe);

// Dot vs Bracket Notation
console.log(joe.lastName); // Dot
console.log(joe['lastName']); // Brackets

// Bracket can do expressions
const nameKey = 'Name';
console.log(joe['first' + nameKey]);
console.log(joe['last' + nameKey]);

const interestedIn = prompt(
  'What do you want to know about Joe? Choose between firstName, lastName, age, job, friends'
);

if (joe[interestedIn]) {
  console.log(joe[interestedIn]);
} else {
  console.log(
    'Wrong request, choose between firstName, lastName, age, job, friends'
  );
}

joe.location = 'Portugal';
joe['eyeColor'] = 'Blue';
console.log(joe);
console.log(
  `${joe.firstName} has ${joe.friends.length} friend(s) and his best friend is named ${joe.friends[0]}`
);
