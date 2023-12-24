from itertools import zip_longest

# def generate_diff(first_file, second_file):
#     if first_file is None and second_file is None:
#         return ''
#     keys_list = set(list(first_file.keys()) + list(second_file.keys()))
#     result = ''
#     for key in sorted(keys_list):
#         if first_file.get(key) == second_file.get(key):
#             result += f"   {key}: {first_file.get(key)}\n"
#         elif key in first_file and key not in second_file:
#             result += f"  -{key}: {first_file.get(key)}\n"
#         elif key in second_file and key not in first_file:
#             result += f"  +{key}: {second_file.get(key)}\n"
#         else:
#             result += f"  -{key}: {first_file.get(key)}\n"
#             result += f"  +{key}: {second_file.get(key)}\n"
#     result = '{\n' + result.lower() + '}'
#     return result

f1 = {
    "common": {
      "setting1": "Value 1",
      "setting2": 200,
      "setting3": True,
      "setting6": {
        "key": "value",
        "doge": {
          "wow": ""
        }
      }
    },
    "group1": {
      "baz": "bas",
      "foo": "bar",
      "nest": {
        "key": "value"
      }
    },
    "group2": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  }

f2 = {
    "common": {
      "follow": False,
      "setting1": "Value 1",
      "setting3": None,
      "setting4": "blah blah",
      "setting5": {
        "key5": "value5"
      },
      "setting6": {
        "key": "value",
        "ops": "vops",
        "doge": {
          "wow": "so much"
        }
      }
    },
    "group1": {
      "foo": "bar",
      "baz": "bars",
      "nest": "str"
    },
    "group3": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }

def search_keys(dict1, all_keys = []):
	for k, v in dict1.items():
		all_keys.append(k)
		if isinstance(v, dict):
			return search_keys(v)
	return all_keys


def gendiff(dict1, dict2, depth = 0, result = []):
    all_keys = sorted(set(list(dict1.keys()) + list(dict2.keys())))
    for key in all_keys:
        child_dict_1 = dict1.get(key, 'no such key')
        child_dict_2 = dict2.get(key, 'no such key')
        if key in dict1 and key in dict2:
            if child_dict_1 == child_dict_2:
                result.append(f"{   '  '*depth}  {key}: {child_dict_1}\n")
            elif isinstance(child_dict_1, dict) and isinstance(child_dict_2, dict):
                result.append(' ' + key + ': {\n')
                gendiff(child_dict_1, child_dict_2, depth + 1)
            else:
                result.append(f"{   '  '*depth}- {key}: {child_dict_1}\n")
                result.append(f"{   '  '*depth}+ {key}: {child_dict_2}\n")
        elif key in dict1 and key not in dict2:
            result.append(f"{   '  '*depth}- {key}: {child_dict_2}\n")
        elif key not in dict1 and key in dict2:
             result.append(f"{   '  '*depth}+ {key}: {child_dict_2}\n")
    result = ''.join(result)
    result = '{\n' + result.lower() + '}'
    return result

print(gendiff(f1, f2))