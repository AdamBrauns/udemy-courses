'use strict'; // strict mode has to be first line
// forbids us to do certain things
// create visible errors where it would fail 'silently' without it

let hasDriversLicense = false;
const passTest = true;

// Without strict, there is no error mode when the variable is mistyped
// if ( passTest ) hasDriverLicense = true;
if (hasDriversLicense) console.log('I can drive');

// strict mode will error for reserved words
//const interface = 'Audio';
//const private = 534;

// Functions
function logger() {
  console.log('My name is Jonas');
}

// Calling / Running / Invoking function
logger();
logger();
logger();

function fruitProcessor(apples, oranges) {
  const juice = `Juice with ${apples} apples and ${oranges} oranges`;
  return juice;
}

const appleJuice = fruitProcessor(5, 0);
console.log(appleJuice);

const orangeJuice = fruitProcessor(0, 7);
console.log(orangeJuice);

// Function declaration vs expressions
// Function declaration
function calcAge1(birthYear) {
  return 2037 - birthYear;
}
const age1 = calcAge1(1991);

// Function expression
const calcAge2 = function (birthYear) {
  return 2037 - birthYear;
};
const age2 = calcAge2(1991);

console.log(age1, age2);

// Arrow functions
// return value happens automatically if it's a one liner
const calcAge3 = (birthYear) => 2037 - birthYear;
const age3 = calcAge3(1991);
console.log(age3);

const yearsUntilRetirement = (birthYear, firstName) => {
  const age = 2037 - birthYear;
  const retirementAge = 65 - age;
  return `${firstName} retires in ${retirementAge} years`;
};

console.log(yearsUntilRetirement(1991, 'Jonas'));
console.log(yearsUntilRetirement(1995, 'Bob'));

// Functions calling other functions
function cutFruitPieces(fruit) {
  return fruit * 4;
}

function fruitProcessor2(apples, oranges) {
  const applePieces = cutFruitPieces(apples);
  const orangePieces = cutFruitPieces(oranges);
  const juice = `Juice with ${applePieces} pieces of apples and ${orangePieces} pieces of oranges`;
  return juice;
}

console.log(fruitProcessor2(2, 3));

// Function review
const calcAge4 = function (birthYear) {
  return 2037 - birthYear;
};

const yearsUntilRetirement4 = function (birthYear, firstName) {
  const age = calcAge4(birthYear);
  const retirementAge = 65 - age;
  if (retirementAge > 0) {
    console.log(`${firstName} retires in ${retirementAge} years`);
    return retirementAge;
  } else {
    console.log(`${firstName} has already retired.`);
    return -1;
  }
};

console.log(yearsUntilRetirement4(1991, 'Jonas'));
console.log(yearsUntilRetirement4(1950, 'Mike'));
