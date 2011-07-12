import kns

def callback(directive, options):
    print "This is the callback."
    print "\tDirective: " + directive
    print "\tText: " + options["text"]

print kns.raise_event("test", "started", "a163x36", callback, True)

