
import yaml

data = yaml.safe_load(open("specs/.hippo.yml"))

def get_items(parent="", sub_items={}):
	for key, value in sub_items.items():
		if isinstance(value, dict):
			yield from get_items(key if parent == "" else "{}.{}".format(parent, key), value)
		else:
			yield (key, value) if parent == "" else ("{}.{}".format(parent, key), value)

for v in get_items("", data['data']):
	print("${" + v[0] + "} = ")
	print(v[1])