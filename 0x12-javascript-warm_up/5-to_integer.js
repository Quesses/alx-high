#!/usr/bin/node
let arg1 = process.argv[2];
if (isNaN(arg1) || arg1 === undefined) {
	console.log("Not a number");
} else {
	console.log('My number: ' + parseInt(arg1));
}
