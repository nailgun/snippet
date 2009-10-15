import jinja2
import os

jloader = jinja2.FileSystemLoader(os.path.dirname(__file__))
jenv = jinja2.Environment(loader=jloader)

def usage(call_name):
	print 'USAGE: %s CLASS-NAME' % call_name

def generate(args):
	if len(args) != 2:
		usage(args[0])
		return 1
	class_name = args[1]
	header = jenv.get_template('class.h')
	header.stream(class_name=class_name).dump(class_name + '.h')
	source = jenv.get_template('class.cpp')
	source.stream(class_name=class_name).dump(class_name + '.cpp')
