#import pymongo
import jsonpatch
from simplejson import dumps
import collections
from copy import deepcopy


class Doc(collections.Mapping):
	"""This represents a single version controlled doc. The class should be
	initalized with the dict that holds the version controlled document in the
	format specified in `./document.schema.json`. Changing the document must
	be done with the provided `commit()` method. You cannot directly modify
	this object because it is made to act as a "FrozenDict" since
	modifications would cause the current state to get out of sync with the
	history"""
	def __init__(self, *args, **kwargs):
		self.doc = dict(*args, **kwargs)
		if 'history' not in self.doc:
			self.doc['history'] = []
		if 'current' not in self.doc:
			self.doc['current'] = {}

		self._hash = None

	def __getitem__(self, key):
		return self.doc[key]

	def __iter__(self):
		return iter(self.doc)

	def __len__(self):
		return len(self.doc)

	def __hash__(self):
		# It would have been simpler and maybe more obvious to use
		# hash(tuple(sorted(self._d.iteritems()))) from this discussion so
		# far, but this solution is O(n). I don't know what kind of n we are
		# going to run into, but sometimes it's hard to resist the urge to
		# optimize when it will gain improved algorithmic performance.
		if self._hash is None:
			self._hash = 0
			for pair in self.iteritems():
				self._hash ^= hash(pair)
		return self._hash

	def __repr__(self):
		"""just output the json representation of the current doc"""
		return dumps(self.doc, separators=(',', ':'))

	def commit(self, new_doc, meta_data={}):
		"""add a revision to the history. the new_doc will replace the current
		doc and a patch will be stored in the history which can be used to
		calculate the previous state of the document"""
		self.doc['history'].append({
			'patch': jsonpatch.make_patch(new_doc, self.doc['current']).patch,
			'meta': meta_data
		})
		self.doc['current'] = new_doc

	def history(self):
		"""return a list of all revisions done to the doc"""
		return self.doc['history']

	def old_doc(self, index):
		"""calculate the state of the document at the given index"""
		patches = []
		for i in range(len(self.doc['history']), index, -1):
			patches += deepcopy(self.doc['history'][i - 1]['patch'])
		return jsonpatch.apply_patch(self.doc['current'], patches)


test_doc = Doc()
test_doc.commit({"blah": 42, "meh": "foo"})
test_doc.commit({"blah": 43, "meh": "foo"})
test_doc.commit({"blah": 43})
test_doc.commit({"blah": 43, 'hoom': [1, 2, 3]})
test_doc.commit({"blah": 43, 'hoom': [3]})
test_doc.commit({})

print test_doc.history()

print test_doc.old_doc(0)
print test_doc.old_doc(1)
print test_doc.old_doc(2)
print test_doc.old_doc(3)
print test_doc.old_doc(4)
print test_doc.old_doc(5)
print test_doc.old_doc(7)
