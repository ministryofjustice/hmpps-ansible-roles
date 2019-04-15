from ansible import errors


def merge_config_dictionaries(*dictionary_list):
    """
    Merges n dictionaries of configuration data
    :param dictionary_list: list
    :return dict:
    example usage set_fact: my_dictionary=>"{{ my_dictionary| merge_config_dictionaries([config_1, config_n) }}"
    """
    res_dict = {}

    if isinstance(dictionary_list, list):
        if len(dictionary_list) == 1 and isinstance(dictionary_list[0], dict):
            return dictionary_list[0]
        else:
            for dictionary in dictionary_list:
                if isinstance(dictionary, dict):
                    res_dict.update(dictionary)
    else:
        raise TypeError("We expect a list of dictionaries")
    return res_dict


def merge_dictionaries(*dicts):
    """
    Merges n dictionaries of configuration data
    :param list<dicts>:
    :return dict:
    Merges n dictionaries passed in as arguments, dictionaries will be overwritten in FIFO order
    """
    try:
        return {k: v for d in dicts for k, v in d.items()}
    except AttributeError as exep:
        print("Only dictionaries are supported as an argument list")
        print(exep)


class FilterModule(object):
    def filters(self):
        filter_list = {
            'merge_config_dictionaries': merge_config_dictionaries,
            'merge_dictionaries': merge_dictionaries
        }
        return filter_list
