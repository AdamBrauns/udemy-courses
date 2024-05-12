// Truthy vs Falsy values
// 5 falsy values (0, '', undefined, null, NaN)
// falsy values will be converted to false when we convert to boolean
// everything else is considered truthy and will be converted to true

console.log(Boolean(0)); // false
console.log(Boolean(undefined)); // false
console.log(Boolean('')); // false
console.log(Boolean('Jonas')); // true
console.log(Boolean({})); // true

// const money = 0;
const money = 100;

if (money) {
  console.log("Don't spend it all");
} else {
  console.log('You should get a job');
}

let height = 0;
if (height) {
  console.log('height is defined');
} else {
  console.log('height is undefined');
}

// Equality Operators == vs ===
// === strict comparison
let age = 18;
if (age === 18) console.log('You just became an adult');

// == loose comparison
if (age == '18') console.log('You just became an adult');
// This will not be true
// if ( age === '18') console.log('You just became an adult');
// Avoid using == when you can as it produces unintended bugs

// Prompt for user input
const favorite_num = Number(prompt("What's your favorite number?"));
console.log(favorite_num);
console.log(typeof favorite_num); // returns string

if (favorite_num === 23) {
  console.log('23 is your favorite number');
} else if (favorite_num === 7) {
  console.log('7 is your favorite number');
} else if (favorite_num === 9) {
  console.log('7 is your favorite number');
} else {
  console.log("You're favorite number is not 23, 7 or 9");
}

// !== is strict, != is loose
if (favorite_num !== 23) console.log('Why not 23?');

// Logical operators
let hasDriversLicense = true; // A
let hasGoodVision = true; // B

console.log(hasDriversLicense && hasGoodVision); // returns true

hasGoodVision = false;
console.log(hasDriversLicense && hasGoodVision); // returns false
console.log(hasDriversLicense || hasGoodVision); // returns true
console.log(!hasDriversLicense); // returns false

hasGoodVision = true;
if (hasDriversLicense && hasGoodVision) {
  console.log('Sarah is able to drive!');
} else {
  console.log('Someone else should drive...');
}

const isTired = false; // C
console.log(hasDriversLicense && hasGoodVision && isTired); // returns true

if (hasDriversLicense && hasGoodVision && !isTired) {
  console.log('Sarah is able to drive!');
} else {
  console.log('Someone else should drive...');
}

// The Switch Statement
const day = 'sunday';

switch (day) {
  case 'monday': // day === 'monday'
    console.log('Play some golf');
    break;
  case 'tuesday':
    console.log('Go for a walk');
    break;
  case 'wednesday':
  case 'thursday':
    console.log('Write code examples'); // matches both wednesday and thursday
    break;
  case 'friday':
    console.log('Record video');
    break;
  case 'saturday':
  case 'sunday':
    console.log('Enjoy weekend');
    break;
  default:
    console.log('Not a valid day');
}

// If else equivalent
if (day === 'monday') {
  console.log('Play some golf');
} else if (day === 'tuesday') {
  console.log('Go for a walk');
} else if (day === 'wednesday' || day === 'thursday') {
  console.log('Write code examples');
} else if (day === 'friday') {
  console.log('Record video');
} else if (day === 'saturday' || day === 'sunday') {
  console.log('Enjoy weekend');
} else {
  console.log('Not a valid day');
}

// Conditional (ternary) operator
age = 23;
// If ? then : else
age >= 18
  ? console.log('I like to play golf')
  : console.log('I like to play basketball');

let sport = age >= 18 ? 'golf' : 'basketball';
console.log(sport);

// If else standard comparison
if (age >= 18) {
  sport = 'golf';
} else {
  sport = 'basketball';
}
console.log(sport);

// ternary used in template literal
console.log(`I like to play ${age >= 18 ? 'golf' : 'basketball'}`);
// ternary is only used for quick comparison
