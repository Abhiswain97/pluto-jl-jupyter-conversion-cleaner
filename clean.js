function cleaner(fname) {
	input = File.open(fname, 'r');
	console.log(JSON.parse(input));
}
