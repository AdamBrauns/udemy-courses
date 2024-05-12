// Operator Precedence
const currentYear = 2037;
const ageJonas = currentYear - 1991;
const ageSara = currentYear - 2018;
console.log(currentYear - 1991 > currentYear - 2018);

console.log(25 - 10 - 5); // left to right operation
let x, y;
x = y = 25 - 10 - 5; // right to left operation
console.log(x, y);

const avgAge = (ageJonas + ageSara) / 2;
console.log(ageJonas, ageSara, avgAge);

// Strings and Template Literals
const firstName = 'Jonas';
const job = 'Teacher';
const birthYear = 1991;

const jonas =
  "I'm " +
  firstName +
  ', a ' +
  (currentYear - birthYear) +
  ' year old ' +
  job +
  '!';
console.log(jonas);

// String literal
const jonasNew = `I'm ${firstName}, a ${
  currentYear - birthYear
} year old ${job}!`;
console.log(jonasNew);

// You can also use it without variables (some devs are going this route)
console.log(`Normal string`);

// For multi-lines, string literal is much cleaner
console.log('String with \n\
multiple\n\
lines');

console.log(`String with
multiple
lines`);

// Taking Decisions: if / else statements
const age = 15;
const drivingAge = 16;

if (age >= drivingAge) {
  console.log(`Sarah can start driving`);
} else {
  const yearsLeft = drivingAge - age;
  console.log(`Sarah is too young, wait another ${yearsLeft} year(s).`);
}

let century;
const birthYear2 = 2012;

if (birthYear2 <= 2000) {
  century = 20;
} else {
  century = 21;
}
console.log(century);

// Type Conversion and Coercion
// Conversion is when we manually convert from one type to another
// Coersion is when JS automatically converts it for us

// Type Conversion
const inputYear = '1991';
console.log(Number(inputYear), inputYear);
console.log(Number(inputYear) + 18);

console.log(Number('Jonas')); // Returns NaN (not a number)
console.log(typeof NaN); // NaN is a number, but an invalid one
console.log(String(23), 23);

// Type Coercion
console.log('I am ' + 100 + ' years old.');
console.log('23' + '10' + 3); // Numbers converted to strings
console.log('23' - '10' - 3); // Strings converted to numbers
console.log('23' * '2');
console.log('23' / '2');
console.log('23' > '18');

let n = '1' + 1;
n -= 1;
console.log(n); // Results in 10

n = 2 + 3 + 4 + '5';
console.log(n); // Results in 95

n = '10' - '4' - '3' - 2 + '5';
console.log(n); // Results in 15
