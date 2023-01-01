#!/usr/bin/node
let logM = 0;

exports.logMe = function (item) {
	console.log(`${logM}: ${item}`);
	logM++;
}
