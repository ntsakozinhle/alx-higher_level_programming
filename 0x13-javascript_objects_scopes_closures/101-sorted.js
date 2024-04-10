#!/usr/bin/node

const { dict } = require('./101-data');

const sortedDict = {};

for (const userId in dict) {
  const occurrence = dict[userId];
  if (!(occurrence in sortedDict)) {
    sortedDict[occurrence] = [];
  }
  sortedDict[occurrence].push(userId);
}

console.log(sortedDict);
