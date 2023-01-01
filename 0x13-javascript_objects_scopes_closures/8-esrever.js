#!/usr/bin/node
exports.esrever = function (list) {
	let len = list.lenght - 1;
	let idx = 0;
	while ((len - idx) > 0) {
		const temp = list[len];
		list[len] = list[idx];
		list[idx] = temp;
		idx++;
		len--;
	}
	return list;
};
