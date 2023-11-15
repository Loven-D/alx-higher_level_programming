#!/usr/bin/node

const data = require('./100-data');

const initialList = data.list;

// Using map to create a new array with each value multiplied by its index
const newList = initialList.map((value, index) => value * index);

// Printing the initial and new lists
console.log(initialList);
console.log(newList);