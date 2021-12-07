import json
import yaml


class AttrDict(dict):
    """
    Dictionary whose keys can be accessed as attributes.
    Example:
    >>> d = AttrDict(x=1, y=2)
    >>> d.x
    1
    >>> d.y = 3
    """

    def __init__(self, *args, **kwargs):
        self.dict_data = args[0]
        s = args[0]
        s["dict"] = args[0]
        super(AttrDict, self).__init__(s, **kwargs)
        self.__dict__ = self

    def __getattr__(self, item):
        return self.__dict__.get(item)

    def return_dict(self):
        return self.__dict__.get("dict")


def write_array(path, arr):
    with open(path, 'w+') as f:
        for elem in arr:
            f.write(elem + '\n')


def read_json(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(json.loads(line))
    return data


def read_file_line(path):
    res = []
    with open(path) as f:
        for line in f:
            res.append(line.replace('\n', ''))
    return res


def write_string(path, str_):
    with open(path, 'w+') as f:
        f.write(str_)


def read_config(path_yaml):
    with open(path_yaml) as f:
        config_data = AttrDict(yaml.safe_load(f))
        for k, v in config_data.items():
            config_data.setdefault(k, v)
    return config_data


def get_dataset(path):
    data = []
    json_array = read_json(path)
    for elem in json_array:
        if "summary" in elem and "description" in elem:
            data.append(elem)
    return data