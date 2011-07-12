ruleset a163x36 {
    meta {
        name "EventHandler"
        description <<
        Testing with explicit events
        >>
        author "Steve Nay"
        logging off
    }

    dispatch {
    }

    global {
    }

    rule echo {
        select when test started
        send_directive("echo") with text="No text provided";
    }
    
    rule echo_param {
        select when test started 
        pre {
            text = event:param("text");
            send_text = text => text | "Oops";
        }
        send_directive("echo") with text=send_text;
    }
    
}

