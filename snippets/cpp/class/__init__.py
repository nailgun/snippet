import os
import sys

def generate(options, args):
	import jinja2
	jloader = jinja2.FileSystemLoader(os.path.dirname(__file__))
	jenv = jinja2.Environment(loader=jloader)

	class_name = args[0]
	if options.inline:
		header = jenv.get_template('inline.h')
	else:
		header = jenv.get_template('class.h')
	if options.files:
		header_out = class_name + '.h'
	else:
		header_out = sys.stdout
	header.stream(class_name=class_name).dump(header_out)
	if not options.inline:
		source = jenv.get_template('class.cpp')
		if options.files:
			source_out = class_name + '.cpp'
		else:
			source_out = sys.stdout
		source.stream(class_name=class_name).dump(source_out)

def main(args):
	from optparse import OptionParser
	parser = OptionParser(usage='Usage: %prog [options] CLASSNAME',
			prog=args[0])
	parser.add_option('-i', action='store_true', dest='inline',
			help='make inline constructor and destructor')
	parser.add_option('-f', action='store_true', dest='files',
			help='generate files instead of writing to stdout')
	(options, args) = parser.parse_args(args[1:])
	if len(args) != 1:
		parser.error('missing CLASSNAME')
	return generate(options, args)

# vim:set ft=python ts=4 sw=4 tw=79 noet: 
