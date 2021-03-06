#!/usr/bin/python3
"""Base Model Module"""

import json
import csv


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Me!
        Args:
            id - int value greater than 0
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string repr"""

        if list_dictionaries is None or not len(list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string repr to a file"""

        with open(cls.__name__ + '.json', "w", encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string(
                    [o.to_dictionary() for o in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of jSON string repr"""

        if not isinstance(json_string, str) or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances read from a file"""

        obj_list = []
        try:
            with open(cls.__name__ + ".json", "r", encoding='utf-8') as f:
                text = f.read()
            for d in cls.from_json_string(text):
                obj_list.append(cls.create(**d))
        except:
            pass
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves objects to CSV file"""

        res = [o.to_dictionary() for o in list_objs]
        with open(cls.__name__ + '.csv', "w", encoding='utf-8') as f:
            dwriter = csv.DictWriter(f, res[0].keys())
            dwriter.writeheader()
            dwriter.writerows(res)

    @classmethod
    def load_from_file_csv(cls):
        """Reads from csv file to object list"""

        obj_list = []
        with open(cls.__name__ + ".csv", "r", encoding='utf-8') as f:
            dreader = csv.DictReader(f)
            for row in dreader:
                tmp = {}
                for k, v in dict(row).items():
                    tmp[k] = int(v)
                obj_list.append(cls.create(**tmp))
        return obj_list
