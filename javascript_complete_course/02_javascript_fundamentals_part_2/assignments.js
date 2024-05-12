'use strict';
// Assignment 1: Functions
function describeCountry(country, population, capitalCity) {
  const returnStr = `${country} has ${population} million people and its capital city is ${capitalCity}`;
  return returnStr;
}

const finlandStr = describeCountry('Finland', 6, 'Helsinki');
const unitedStatesStr = describeCountry(
  'United States',
  330,
  'Washington, D.C.'
);
const chinaStr = describeCountry('China', 1400, 'Beijing');

console.log(finlandStr);
console.log(unitedStatesStr);
console.log(chinaStr);

// End Assignment 1: Functions

// Assignment 2: Function declarations vs expressions
function percentageOfWorld1(population) {
  return (population / 7900) * 100;
}

const finlandPercent1 = percentageOfWorld1(6);
const unitedStatesPercent1 = percentageOfWorld1(330);
const chinaPercent1 = percentageOfWorld1(1400);

const percentageOfWorld2 = function (population) {
  return (population / 7900) * 100;
};

const finlandPercent2 = percentageOfWorld2(6);
const unitedStatesPercent2 = percentageOfWorld2(330);
const chinaPercent2 = percentageOfWorld2(1400);

console.log(finlandPercent1, finlandPercent2);
console.log(unitedStatesPercent1, unitedStatesPercent2);
console.log(chinaPercent1, chinaPercent2);
// End Assignment 2: Function declarations vs expressions

// Assignment 3: Arrow functions
const percentageOfWorld3 = (population) => (population / 7900) * 100;
const finlandPercent3 = percentageOfWorld3(6);
const unitedStatesPercent3 = percentageOfWorld3(330);
const chinaPercent3 = percentageOfWorld3(1400);

console.log(finlandPercent3);
console.log(unitedStatesPercent3);
console.log(chinaPercent3);
// End Assignment 3: Arrow functions

// Assignment 4: Functions calling other functions
const describePopulation = (country, population) => {
  const countryPopulationPercent = percentageOfWorld1(population);
  return `${country} has ${population} million people which is about ${countryPopulationPercent}% of the world`;
};
console.log(describePopulation('Finland', 6));
console.log(describePopulation('United States', 330));
console.log(describePopulation('China', 1400));
// End Assignment 4: Functions calling other functions

// Assignment 5: arrays
const populationArray = [6, 330, 1400, 38];
if (populationArray.length === 4) console.log('Array has 4 elements');
const populationArrayPercent = [
  percentageOfWorld1(populationArray[0]),
  percentageOfWorld1(populationArray[1]),
  percentageOfWorld1(populationArray[2]),
  percentageOfWorld1(populationArray[populationArray.length - 1]),
];
console.log(populationArrayPercent);
// End Assignment 5: arrays

// Assignment 6: Basic array operations
const neighbors = ['Canada', 'Mexico'];
neighbors.push('Utopia');
neighbors.pop();
if (neighbors.includes('Germany')) {
  console.log('Probably not a central European country');
}
neighbors[neighbors.indexOf('Mexico')] = 'Republic of Sweden';
console.log(neighbors);
// End Assignment 6: Basic array operations

// Assignment 7: Introduction to Objects
const myCountry = {
  country: 'United States',
  capital: 'Washington, D.C.',
  language: 'English',
  population: 330,
  neighbors: ['Canada', 'Mexico'],
  describe: function () {
    console.log(
      `${this.country} has ${this.population} million ${this.language}-speaking people, ${this.neighbors.length} neighboring countries and a capital called ${this.capital}`
    );
  },
  checkIsland: function () {
    this.isIsland = this.neighbors.length === 0 ? true : false;
  },
};

console.log(myCountry.country);
// End Assignment 7: Introduction to Objects

// Assignment 8: Dot vs Bracket Notation
console.log(
  `${myCountry.country} has ${myCountry.population} million ${myCountry.language}-speaking people, ${myCountry.neighbors.length} neighboring countries and a capital called ${myCountry.capital}`
);
myCountry.population += 2;
myCountry['population'] -= 2;
console.log(myCountry.population);
// End Assignment 8: Dot vs Bracket Notation

// Assignment 9: Object Methods
myCountry.describe();
myCountry.checkIsland();
console.log(myCountry);
// End Assignment 9: Object Methods

// Assignment 10: For loops
for (let voter = 1; voter <= 10; voter++) {
  console.log(`Voter number ${voter} is currently voting...`);
}
// End Assignment 10: For loops

// Assignment 11: Looping arrays, breaking and continuing
const percentages2 = [];
for (let i = 0; i < populationArray.length; i++) {
  percentages2.push(percentageOfWorld1(populationArray[i]));
}
console.log(percentages2);
console.log(populationArrayPercent);
// End Assignment 11: Looping arrays, breaking and continuing

// Assignment 12: Looping backwards and loops in loops
const listOfNeighbors = [
  ['Canada', 'Mexico'],
  ['Spain'],
  ['Norway', 'Sweden', 'Russia'],
];
for (let i = 0; i < listOfNeighbors.length; i++) {
  for (let j = 0; j < listOfNeighbors[i].length; j++) {
    console.log(`Neighbor: ${listOfNeighbors[i][j]}`);
  }
}
// End Assignment 12: Looping backwards and loops in loops

// Assignment 13: The while loop
const percentages3 = [];
let i = 0;
while (i < populationArray.length) {
  percentages3.push(percentageOfWorld1(populationArray[i]));
  i++;
}
console.log(percentages3);
// End Assignment 13: The while loop
