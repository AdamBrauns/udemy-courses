'use strict';

const airline = 'TAP Air Portugal';
const plane = 'A320';

console.log(plane[0]);
console.log(plane[1]);
console.log(plane[2]);
console.log(plane[3]);
console.log('B737'[0]);

console.log(airline.length);
console.log('B737'.length);

console.log(airline.indexOf('r'));
console.log(airline.lastIndexOf('r'));
console.log(airline.indexOf('Portugal')); // Case sensitive

console.log(airline.slice(4));
console.log(airline.slice(4, 7));

console.log(airline.slice(0, airline.indexOf(' ')));
console.log(airline.slice(airline.lastIndexOf(' ') + 1));

console.log(airline.slice(-2));
console.log(airline.slice(1, -1));

const checkMiddleSeat = function (seat) {
  // B and E are middle seats
  const seatPosition = seat.slice(-1);
  if (seatPosition === 'B' || seatPosition === 'E') console.log('You got the middle seat :(');
  else console.log('You got lucky :)');
};
checkMiddleSeat('11B');
checkMiddleSeat('23C');
checkMiddleSeat('3E');

// JavaScript uses a term called boxing to convert string to object to call methods on
console.log(new String('jonas'));
console.log(typeof new String('jonas'));
console.log(typeof new String('jonas').slice(1));

console.log(airline.toLocaleLowerCase());
console.log(airline.toLocaleUpperCase());

// Fix capitalization in name
const passenger = 'jOnAS';
const passengerLower = passenger.toLocaleLowerCase();
const passengerCorrect = passengerLower[0].toUpperCase() + passengerLower.slice(1);
console.log(passengerCorrect);

const caseCorrectName = function (name) {
  const nameLower = name.toLocaleLowerCase();
  return nameLower[0].toLocaleUpperCase() + nameLower.slice(1);
};

console.log(caseCorrectName('RaNdY'));

// Compare emails
const email = 'hello@jonas.io';
const loginEmail = '  HelLo@JoNas.Io \n';

const normalizedEmail = loginEmail.toLowerCase().trim();
console.log(normalizedEmail);
console.log(email === normalizedEmail);

// Replacing
const priceGB = '£288,97';
const priceUS = priceGB.replace('£', '$').replace(',', '.');
console.log(priceUS);

const announcement = 'All passengers come to boarding door 23, Boarding door 23!';
console.log(announcement.replaceAll('door', 'gate'));

// Regex method
console.log(announcement.replace(/door/g, 'gate'));

// Booleans
const anotherPlane = 'Airbus A320neo';
console.log(anotherPlane.includes('A320'));
console.log(anotherPlane.includes('Boeing'));
console.log(anotherPlane.startsWith('Air'));
console.log(anotherPlane.startsWith('Boeing'));

if (anotherPlane.startsWith('Airbus') && anotherPlane.endsWith('neo')) console.log('Part of the NEW airbus family');

// Practice exercise
const checkBaggage = function (items) {
  const baggage = items.toLocaleLowerCase();
  if (baggage.includes('knife') || baggage.includes('weapon')) {
    console.log('You are NOT allowed on board');
  } else {
    console.log('Welcome aboard');
  }
};
checkBaggage('I have a laptop, some Food and a pocket knife');
checkBaggage('Socks and a camera');
checkBaggage('Got some snacks and a weapon for protection');

// Split and join
console.log('a+very+nice+string'.split('+'));
console.log('Jonas Schmedtmann'.split(' '));

const [firstName, lastName] = 'Jonas Schmedtmann'.split(' ');
const newName = ['Mr.', firstName, lastName.toUpperCase()].join(' ');
console.log(newName);

const capitalizeName = function (name) {
  const names = name.split(' ');
  const namesUpper = [];
  for (const n of names) {
    // namesUpper.push(n[0].toUpperCase() + n.slice(1));
    namesUpper.push(n.replace(n[0], n[0].toUpperCase()));
  }
  console.log(namesUpper.join(' '));
};

capitalizeName('jessica ann smith davis');
capitalizeName('jonas schmedtmann');
capitalizeName('greta van fleet');

// Padding
const message = 'Go to gate 23';
console.log(message.padStart(25, '+').padEnd(30, '+'));
console.log('Jonas'.padStart(25, '+').padEnd(30, '+'));

const maskCreditCard = function (number) {
  const str = number + ''; // works the same as String() method
  const lastFour = str.slice(-4);
  return lastFour.padStart(str.length, '*');
};

console.log(maskCreditCard('12345678'));
console.log(maskCreditCard('84759238494837443'));
console.log(maskCreditCard('8475923849483744234234113'));

// Repeat
const message2 = 'Bad weather.. All Departures Delayed... ';
console.log(message2.repeat(5));

const planesInLine = function (n) {
  console.log(`There are ${n} planes in line ${'⚽'.repeat(n)}`);
};
planesInLine(5);
planesInLine(3);
planesInLine(12);
