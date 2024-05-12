'use strict';

// Object Methods
const joe = {
  firstName: 'Joe',
  lastName: 'Schmoe',
  birthYear: 1983,
  job: 'teacher',
  friends: ['Frank', 'Larry', 'Joe'],
  hasDriversLicense: false,

  calcAge: function () {
    this.age = 2037 - this.birthYear;
    return this.age;
  },

  getSummary: function () {
    return `${this.firstName} is a ${this.calcAge()}-year old ${
      this.job
    }, and he has ${this.hasDriversLicense ? 'a' : 'no'} driver's license.`;
  },
};

console.log(joe.calcAge());
// console.log(joe['calcAge']());
console.log(joe.age);
console.log(joe.age);

console.log(joe.getSummary());

// For loop
for (let rep = 1; rep <= 10; rep++) {
  console.log(`Lifting weights, on repetition ${rep}...`);
}

// Looping arrays, breaking and continuing
const fredArray = [
  'Joe',
  'Schmoe',
  1983,
  'teacher',
  ['Frank', 'Larry', 'Joe'],
  true,
];

const types = [];

for (let i = 0; i < fredArray.length; i++) {
  // Reading in from fredArray
  console.log(fredArray[i], typeof fredArray[i]);
  // Filling in types arrya
  types.push(typeof fredArray[i]);
  // types[i] = typeof fredArray[i]; different way to do it
}
console.log(types);

const years = [1991, 2007, 1969, 2020];
const ages = [];
for (let i = 0; i < years.length; i++) {
  ages.push(2037 - years[i]);
}
console.log(ages);

// continue and break
console.log('---ONLY STRINGS---');
for (let i = 0; i < fredArray.length; i++) {
  if (typeof fredArray[i] !== 'string') continue;
  console.log(fredArray[i], typeof fredArray[i]);
}

console.log('---BREAK WITH NUMBER---');
for (let i = 0; i < fredArray.length; i++) {
  if (typeof fredArray[i] === 'number') break;
  console.log(fredArray[i], typeof fredArray[i]);
}

// Looping backwards and loops in loops
const larryArray = [
  'Joe',
  'Schmoe',
  1983,
  'teacher',
  ['Frank', 'Larry', 'Joe'],
  true,
];

for (let i = larryArray.length - 1; i >= 0; i--) {
  console.log(i, larryArray[i]);
}

// for loop within a for loop
for (let exercise = 1; exercise <= 3; exercise++) {
  console.log(`----Starting exercise ${exercise}----`);
  for (let rep = 1; rep <= 5; rep++) {
    console.log(`----Exercise ${exercise}: Starting repetition ${rep}----`);
  }
}

// While loop
let rep = 1;
while (rep <= 10) {
  console.log(`Lifting weights, on repetition ${rep}...`);
  rep++;
}

let dice = 0;
while (dice !== 6) {
  dice = Math.trunc(Math.random() * 6) + 1;
  console.log(`You rolled a ${dice}`);
  if (dice === 6) console.log('You rolled a 6, exiting loop...');
}
