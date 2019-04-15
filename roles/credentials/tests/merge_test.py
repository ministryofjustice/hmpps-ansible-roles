import yaml


with open("left.yml", "r") as left_stream:
    left_dict = yaml.load(left_stream, Loader=yaml.SafeLoader)

with open("right.yml", "r") as right_stream:
    right_dict = yaml.load(right_stream, Loader=yaml.SafeLoader)

with open("expected.yml", "r") as expected_stream:
    expected_dict = yaml.load(expected_stream, Loader=yaml.SafeLoader)

print(left_dict)
print(right_dict)
print(expected_dict)

test = {}
test.update(left_dict)
print(test)
test.update(right_dict)
print(test)

context = dict(list(left_dict.items()) + list(right_dict.items()))
print(context)

foo = left_dict.copy()
