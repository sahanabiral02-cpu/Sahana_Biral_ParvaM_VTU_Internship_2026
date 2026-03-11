console.log("===== STUDENT RESULT MANAGEMENT SYSTEM =====");

// Initial Data
const students = [
  { id: 1, name: "Rahul", marks: [80, 75, 90] },
  { id: 2, name: "Sneha", marks: [60, 70, 65] },
  { id: 3, name: "Arjun", marks: [95, 92, 88] }
];

// ===============================
// Task 1: Calculate Total (reduce)
// ===============================
function calculateTotal(marks) {
  return marks.reduce((sum, mark) => sum + mark, 0);
}

// ===============================
// Task 2: Arrow Function - Average & Grade
// A >=90 | B >=75 | C >=60 | Fail <60
// ===============================
const calculateGrade = (total, count) => {
  const average = total / count;
  let grade;

  if (average >= 90) grade = "A";
  else if (average >= 75) grade = "B";
  else if (average >= 60) grade = "C";
  else grade = "Fail";

  return { average, grade };
};

// ===============================
// Task 3: map()
// Create new array with name, total, average, grade
// ===============================
const resultData = students.map(student => {
  const total = calculateTotal(student.marks);
  const { average, grade } = calculateGrade(total, student.marks.length);

  return {
    name: student.name,
    total,
    average,
    grade
  };
});

console.log("\n--- Mapped Result Data ---");
console.log(resultData);

// ===============================
// Task 4: filter()
// Students with average > 75
// ===============================
const above75 = resultData.filter(student => student.average > 75);

console.log("\n--- Students with Average > 75 ---");
console.log(above75);

// ===============================
// Task 5: forEach()
// Print formatted output
// ===============================
console.log("\n--- All Student Details ---");
resultData.forEach(student => {
  console.log(
    `Name: ${student.name}, Total: ${student.total}, Average: ${student.average.toFixed(2)}, Grade: ${student.grade}`
  );
});

// ===============================
// Task 6: Scope Example
// ===============================
function scopeExample() {
  var a = 10;     // Function scoped
  let b = 20;     // Block scoped
  const c = 30;   // Block scoped

  console.log("\nInside Function:", a, b, c);

  if (true) {
    var a = 100;      // Affects outside (var is function scoped)
    let b = 200;      // Block scoped
    const c = 300;    // Block scoped

    console.log("Inside Block:", a, b, c);
  }

  console.log("After Block:", a, b, c);
}

console.log("\n--- Scope Example ---");
scopeExample();

/*
Explanation:
var is function scoped, so value changes outside block.
let and const are block scoped, so they stay unchanged outside.
*/

// ===============================
// Task 7: Primitive vs Reference
// ===============================

console.log("\n--- Primitive vs Reference ---");

// Primitive
let num1 = 10;
let num2 = num1; // Copy value
num2 = 50;

console.log("Primitive Example:");
console.log("num1:", num1); // 10
console.log("num2:", num2); // 50

/*
Primitive copies value.
Changing num2 does NOT affect num1.
*/

// Reference
let arr1 = [1, 2, 3];
let arr2 = arr1; // Copy reference
arr2.push(4);

console.log("\nReference Example:");
console.log("arr1:", arr1); // [1,2,3,4]
console.log("arr2:", arr2); // [1,2,3,4]

/*
Reference copies memory address.
Changing arr2 also changes arr1.
*/

console.log("\n===== PROGRAM COMPLETED SUCCESSFULLY =====");