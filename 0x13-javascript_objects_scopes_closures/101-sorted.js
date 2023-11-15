#!/usr/bin/node

const data = require('./101-data');

const initialDict = data.dict;

// Computing a new dictionary with user ids grouped by occurrence
const newDict = {};

for (const userId in initialDict) {
  const occurrences = initialDict[userId];

  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }

  newDict[occurrences].push(parseInt(userId));
}

// Printing the new dictionary
console.log(newDict);
