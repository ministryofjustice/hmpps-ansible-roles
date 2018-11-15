from ansible import errors


def strip(string, chars):
    """
    :param string: string to remove chars from
    :param chars: characters to remove as string constant
    :return: string
    """
    return string.strip(chars)


def rstrip(string, chars):
    """
    :param string: string to remove chars from
    :param chars: characters to remove as string constant
    :return: string
    """
    return string.rstrip(chars)


def lstrip(string, chars):
    """
    :param string: string to remove chars from
    :param chars: characters to remove as string constant
    :return: string
    """
    return string.lstrip(chars)


def merge_config_dictionaries(*dicts):
    """
    Merges n dictionaries of configuration data
    :param list<dicts>:
    :return dict:
    """
    res_dict = {}

    if isinstance(dicts, list):
        if len(dicts) == 1 and isinstance(dicts[0], dict):
            return dicts[0]
        else:
            for dictionary in dicts:
                if isinstance(dictionary, dict):
                    res_dict.update(dictionary)

    return res_dict


class FilterModule(object):

    def filters(self):
        filter_list = {
            'strip': strip,
            'rstrip': rstrip,
            'lstrip': lstrip,
            'merge_config_dictionaries': merge_config_dictionaries
        }
        return filter_list
