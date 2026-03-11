console.log("---- Object Destructuring ----");

// Create Object
var student = {
  name: "Sahana",
  age: 21,
  course: "CSE",
  marks: {
    math: 90,
    science: 85
  }
};

// 1️⃣ Basic Destructuring
var { name, age } = student;
console.log("Basic:", name, age);

// 2️⃣ Renaming Variable
var { course: studentCourse } = student;
console.log("Renamed:", studentCourse);

// 3️⃣ Default Value
var { city = "Bangalore" } = student;
console.log("Default City:", city);

// 4️⃣ Nested Destructuring
var { marks: { math, science } } = student;
console.log("Marks:", math, science);