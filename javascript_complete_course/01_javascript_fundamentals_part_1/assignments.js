// Assignment 1: Values and Variables
let country = 'United States';
let continent = 'North America';
let population = 328.2;

console.log(country);
console.log(continent);
console.log(population);
// End Assignment 1: Values and Variables

// Assignment 2: Values and Variables
let isIsland = false;
let language1;

console.log(isIsland);
console.log(population);
console.log(country);
console.log(language1);
// End Assignment 2: Values and Variables

// Assignment 3: let, const and var
const language2 = 'English';
console.log(language2);
// language2 = 'French'; => this fails

// End Assignment 3: let, const and var

// Assignment 4: Basic Operators
let halfPopulation = population / 2;
halfPopulation++;
console.log(halfPopulation);

const finlandPopulation = 6;
console.log(population > finlandPopulation);

const avgPopulation = 33;
console.log(population > avgPopulation);
let description =
  'Portugal is in Europe, and its 11 million people speak portuguese';
console.log(description);
// End Assignment 4: Basic Operators

// Assignment 5 Strings and Template Literals
country = 'Portugal';
population = 11;
let language = 'portuguese';
// Old way:
//const description = country + ' is in Europe, and its ' + population + ' million people speak ' + language;
//console.log(description);

// New way:
description = `${country} is in Europe, and its ${population} million people speak ${language}`;
console.log(description);
// End Assignment 5 Strings and Template Literals

// Assignment 6: Taking decisions if else statements
// Other data:
// population = 13;
population = 130;
if (population > avgPopulation) {
  console.log(`${country}'s population is above average'`);
} else {
  console.log(
    `${country}'s population is ${avgPopulation - population} below average.`
  );
}
// End Assignment 6: Taking decisions if else statements

// Assignment 7: Type Conversion and Coercion
let n;

n = '9' - '5'; // Results in 4
console.log(n);

n = '19' - '13' + '17'; // Results in 617
console.log(n);

n = '19' - '13' + 17; // Results in 23
console.log(n);

n = '123' < 57; // Results in false
console.log(n);

n = 5 + 6 + '4' + 9 - 4 - 2; // Results in 1143
console.log(n);
// End Assignment 7: Type Conversion and Coercion

// Assignment 8: Equality Operators: == vs ===
const numNeighbors = Number(
  prompt('How many neighbor countries does your country have?')
);
if (numNeighbors === 1) {
  console.log('Only 1 border!');
} else if (numNeighbors >> 1) {
  console.log('More than 1 border!');
} else {
  console.log('No borders!');
}

// End Assignment 8: Equality Operators: == vs ===

// Assignment 9: Logical Operators
language = 'English';
population = 20;
isIsland = false;
if (language === 'English' && population < 50 && !isIsland) {
  console.log('You should live in Jonasville');
} else {
  console.log('Jonasville does not meet your criteria :(');
}
// End Assignment 9: Logical Operators

// Assignment 10: switch statement
language = 'mandarin';
switch (language) {
  case 'mandarin':
    console.log('Most number of native speakers');
    break;
  case 'spanish':
    console.log('2nd place in number of native speakers');
    break;
  case 'english':
    console.log('3rd place');
    break;
  case 'hindi':
    console.log('4th place');
    break;
  case 'arabic':
    console.log('5th most spoken language');
    break;
  default:
    console.log('Great language too');
}
// End Assignment 10: switch statement

// Assignment 11: ternary operator
const ternaryStr = population > 33 ? 'above' : 'below';
console.log(`Portugal's population is ${ternaryStr} average`);

// End Assignment 11: ternary operator
