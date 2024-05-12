// Data 1
const billAmt = 275;

/* Other test data
const billAmt = 40;
const billAmt = 430;
*/

const tipAmt = billAmt >= 50 && billAmt <= 300 ? billAmt * 0.15 : billAmt * 0.2;
console.log(
  `The bill was $${billAmt}, the tip was $${tipAmt}, and the total value was $${
    billAmt + tipAmt
  }`
);
