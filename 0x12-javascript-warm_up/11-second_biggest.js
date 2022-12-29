#!/usr/bin/node
if (process.argv.length < 4) {
	console.log('0');
} else {
	let arr = process.argv.splice(2).map(Number);
	arr = arr.sort((a,b) => b - a);
	console.log(arr[1]);
}
