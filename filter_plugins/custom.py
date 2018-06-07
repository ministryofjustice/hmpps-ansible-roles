from ansible import errors


def strip(string, chars):
    return string.strip(chars)


def rstrip(string, chars):
    return string.rstrip(chars)


def lstrip(string, chars):
    return string.lstrip(chars)


class FilterModule(object):

    def filters(self):
        filter_list = {
            'strip': strip,
            'rstrip': rstrip,
            'lstrip': lstrip
        }
        return filter_list