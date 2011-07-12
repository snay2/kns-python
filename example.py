import kns

def callback(directive, options):
    print "This is the callback."
    print "\tDirective: " + directive
    print "\tText: " + options["text"]

params = {'text': 'Hello, there!'}
result = kns.raise_event("test", "started", "a163x36", params, callback, True)

print "\nThe raw directives were the following: \n%s" % result

