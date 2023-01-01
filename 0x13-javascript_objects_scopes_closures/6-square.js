#!/usr/bin/node
const Square1 = require('./5-square.js');

class Square extends Square1 {
	charPrint(c) {
		if (c === undefined) {
			c = 'X';
		}
		for (let i = 0; i < this.height; i++) {
			let s = '';
			for (let i = 0; i < this.width; i++) {
				s += c;
			}
			console.log(s);
		}
	}
}

module.exports = Square;
