def http_label(status):
    match status:
        case 200:                 return "OK"
        case 301 | 302:           return "Redirect"        # OR-pattern
        case code if code >= 500: return "Server error"    # guard + binding
        case _:                   return "Other"     