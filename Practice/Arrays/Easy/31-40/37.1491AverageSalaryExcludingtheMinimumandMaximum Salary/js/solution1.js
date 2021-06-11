/**
 * @param {number[]} salary
 * @return {number}
 */
var average = function(salary) {
    salary.sort((a, b) => a - b);

    // Remove first and last salary
    salary.shift();
    salary.pop();

    // Get average by summing salaries and dividing by number
    return salary.reduce((a, b) => a + b) / salary.length;
};