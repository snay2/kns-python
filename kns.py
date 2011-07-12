import urllib, urllib2, json, string

server = "http://cs.kobj.net/blue/"
event_url = server + "event"

# Raises an event in the given domain to the specified ruleset.
# If dev=True, the event is raised to the dev version of the ruleset.
def raise_event(domain, event, ruleset, params, callback, dev=False):
    is_dev = "%s:kynetx_app_version=dev" % ruleset if dev else ""
    param_str = urllib.urlencode(params);
    url = "%s/%s/%s/%s?%s&%s" % (event_url, domain, event, ruleset, is_dev, param_str)
    handle = urllib2.urlopen(url);
    # Get the content and remove the first line
    str = handle.read()
    just_json = string.split(str, "\n")[1]
    parsed = json.loads(just_json)
    # Call the callback for each of the directives
    for directive in parsed["directives"]:
        callback(directive["name"], directive["options"])
    return str

    
