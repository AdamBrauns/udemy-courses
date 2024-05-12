// Data 1
scoreDolphins = (96 + 108 + 89) / 3;
scoreKoalas = (88 + 91 + 110) / 3;

/*
// Data 2
scoreDolphins = ( 97 + 112 + 101 ) / 3;
scoreKoalas = ( 109 + 95 + 123 ) / 3;

// Data 3
scoreDolphins = ( 97 + 112 + 101 ) / 3;
scoreKoalas = ( 109 + 95 + 106 ) / 3;
*/

console.log(scoreDolphins, scoreKoalas);

if (scoreDolphins > scoreKoalas && scoreDolphins >= 100) {
  console.log("Dolphin's win");
} else if (scoreDolphins < scoreKoalas && scoreKoalas >= 100) {
  console.log("Koala's win");
} else if (scoreDolphins === scoreKoalas && scoreDolphins >= 100) {
  console.log('There was a draw');
} else {
  console.log('Nobody wins');
}
