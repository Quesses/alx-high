#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
	let nbOcc = 0;
	let len = list.length;
	for (let i = 0; i < len; i++) {
		if (searchElement === list[i]) {
			nbOcc++;
		}
	}
	return nbOcc;
}
