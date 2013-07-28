import random
import string
import unittest
from associative_array import AssociativeArray, HashMap


class DictionaryTests:
    def test_instantiate(self):
        aa = self.instance()
        assert aa is not None


    def test_set_get(self):
        aa = self.instance()
        aa.put('foo', 23)
        aa.put('bar', 42)
        assert aa.get('foo') == 23
        assert aa.get('bar') == 42


    def test_update(self):
        aa = self.instance()
        aa.put('foo', 23)
        aa.put('bar', 42)
        aa.put('foo', 'blurb')
        assert aa.get('foo') == 'blurb'
        assert aa.get('bar') == 42


    def test_to_string(self):
        aa = self.instance()
        aa.put('foo', 23)
        aa.put('bar', 42)
        assert "'foo': 23" in str(aa)
        assert "'bar': 42" in str(aa)


    def test_monkey_put_get(self):
        def random_key():
            return ''.join(random.choice(string.ascii_letters) for x in range(8))

        aa = self.instance()
        ref = dict()

        for v in range(100):
            k = random_key()
            aa.put(k, v)
            ref[k] = v

        for k, v in ref.items():
            assert aa.get(k) == v

class AssociativeListTests(DictionaryTests, unittest.TestCase):
    def instance(self):
        return AssociativeArray()

class HashMapTests(DictionaryTests, unittest.TestCase):
    def instance(self):
        return HashMap()
