#!/usr/bin/node
const dict = require('./101-data').dict;
const dicKey = Object.keys(dict);
const dicValues = Object.values(dict);
const result = {};
let match;
for (let i = 0; i < dicValues.length; i++) {
	result[JSON.stringify(dicValues[i])] = [];
	//filter dicKey for if each key in dict[key] is a match with dicValues[i]
	match = dicKey.filter(key => dict[key] === dicValues[i]);
	match.forEach(item => result[JSON.stringify(dicValues[i])].push(item));
}
console.log(result);
