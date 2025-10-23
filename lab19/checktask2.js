function checkNumber(num) {
    if (num > 0) {
        console.log("The number is positive");
    } else if (num < 0) {
        console.log("The number is negative");
    } else {
        console.log("The number is zero");
    }
}

// Call the function with test inputs
checkNumber(-5);
checkNumber(0);
checkNumber(7);