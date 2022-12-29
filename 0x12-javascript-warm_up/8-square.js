#!/usr/bin/node
let arg1 = process.argv[2];
if (isNaN(arg1) || arg1 === undefined) {
	console.log("MIssing size");
} else {
	let x = Number(arg1);
	const y = x;
	while (x > 0) {
		console.log('X'.repeat(y));
		x--;
	}
}
