# MIT License
#
# Copyright (c) 2022 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import yaml


class Data():
	"""This class parses repository .hippo.yml file"""

	_items = {}

	def __init__(self, file_path, property_name="data"):
		self._file_path = file_path
		self._property_name = property_name

	def parse(self):
		data = yaml.safe_load(open(self._file_path))

		if "data" not in data.keys():
			return

		for value in self._parse_items("", data[self._property_name]):
			self._items[value[0]] = value[1]

	def _parse_items(self, parent="", sub_items={}):
		for key, value in sub_items.items():
			if isinstance(value, dict):
				yield from self._parse_items(key if parent == "" else "{}.{}".format(parent, key), value)
			else:
				yield (key, value) if parent == "" else ("{}.{}".format(parent, key), value)

	@classmethod
	def from_file(cls, file_path, property_name="data"):
		return Data(file_path, property_name)

	@property
	def items(self):
		return self._items
