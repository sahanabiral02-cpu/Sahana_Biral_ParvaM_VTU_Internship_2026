console.log("---- Cloning Array Methods ----");

// Original Array
var originalArray = [10, 20, 30, 40];


// 1️⃣ Clone using Spread Operator
var clone1 = [...originalArray];
console.log("Spread Clone:", clone1);


// 2️⃣ Clone using slice()
var clone2 = originalArray.slice();
console.log("Slice Clone:", clone2);


// 3️⃣ Clone using concat()
var clone3 = [].concat(originalArray);
console.log("Concat Clone:", clone3);


// Proving they are separate copies
clone1.push(50);

console.log("After modifying clone1:");
console.log("Original:", originalArray);
console.log("Clone1:", clone1);