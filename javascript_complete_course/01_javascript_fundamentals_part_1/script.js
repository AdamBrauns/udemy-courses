// Assign variable and use it in an if statement
let js = 'amazing';
if (js === 'amazing') console.log('JavaScript is amazing!');

// console.log examples
console.log(40 + 8 + 23 - 10);
console.log('Jonas');
console.log(23);

// Naming Convention is camelCase
let firstName = 'Matt';
console.log(firstName);
console.log(firstName);
console.log(firstName);

/*
   Can only use numbers, letters, underscores, and $
   Invalid Examples:
     let 3years = 3;
     let janas&matilda = 'JM'
*/

/*
  Other Rules:
  - Do not start variable with uppercase letter.
  - Constant variables are capitalized
  - Make variable names descriptive:
      myFirstJob vs job1
      myCurrentJob vs job2
*/

// Data Type Section
// Dynamic typing is possible with variables
let javaScriptIsFun = true;
console.log(typeof javaScriptIsFun);
javaScriptIsFun = 'Yes!';
console.log(typeof javaScriptIsFun);

// Undefined Variable
let year;
console.log(year);
console.log(typeof year);

year = 2021;
console.log(year);
console.log(typeof year);

// null returns as an object and is considered a bug but is kept for legacy reasons
console.log(typeof null);

// let, const and var
// let is good for mutable and unassigned
let height;
let age = 30;
age = 31;

// const is immutable
const birthYear = 1970;
// birthYear = 1920; => this will error
// const job; => this will also error

/*
  const is best unless you are sure the variable will change
  var should be avoided
  It is possible to declare a variable without keyword, but should be avoided
*/

// Basic operators
const currentYear = 2037;
const ageJonas = currentYear - 1991;
const ageSara = currentYear - 2018;
console.log(ageJonas, ageSara);
console.log(ageJonas * 2, 2 ** 3); // 2 ** 3 is 2 to the power of 3

// Concat strings
const firstName2 = 'Joe';
const lastName2 = 'Schmoe';
console.log(firstName2 + ' ' + lastName2);

// Assignment operators
let x = 10 + 5;
x += 10; // x = x + 10
x *= 4; // x = x * 4
x++; // x = x + 1
x--; // x = x -1
console.log(x);

// Comparison operators
console.log(ageJonas > ageSara); // >, <, <=, >=
const isFullAge = ageSara >= 18;
console.log(isFullAge);
