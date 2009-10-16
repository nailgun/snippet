import os
import sys

def generate(options, args):
	import jinja2
	jloader = jinja2.FileSystemLoader(os.path.dirname(__file__))
	jenv = jinja2.Environment(loader=jloader)

	type_name = args[0]
	name = args[1]

	context = {
		'type': args[0],
		'name': args[1],
		'setter': options.setter,
		'prefix': options.prefix,
	}
	if options.inline:
		context['inline'] = 'inline '
	else:
		context['inline'] = ''

	template = jenv.get_template('getter.h')
	template.stream(context).dump(sys.stdout)

def main(args):
	from optparse import OptionParser
	parser = OptionParser(usage='Usage: %prog [options] TYPE NAME',
			prog=args[0])
	parser.add_option('-i', action='store_true', dest='inline',
			help='generate functions inline')
	parser.add_option('-s', action='store_true', dest='setter',
			help='generate setter')
	parser.add_option('-p', action='store_true', dest='prefix',
			help='use "get" prefix in getter')
	(options, args) = parser.parse_args(args[1:])
	if len(args) != 2:
		parser.error('missing argument')
	return generate(options, args)

# vim:set ft=python ts=4 sw=4 tw=79 noet: 
