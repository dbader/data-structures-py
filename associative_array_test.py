from associative_array import AssociativeArray


def test_instantiate():
    m = AssociativeArray()
    assert m is not None


def test_set_get():
    aa = AssociativeArray()
    aa.set('foo', 23)
    aa.set('bar', 42)
    assert aa.get('foo') == 23
    assert aa.get('bar') == 42


def test_update():
    aa = AssociativeArray()
    aa.set('foo', 23)
    aa.set('bar', 42)
    aa.set('foo', 'blurb')
    assert aa.get('foo') == 'blurb'
    assert aa.get('bar') == 42


def test_to_string():
    aa = AssociativeArray()
    aa.set('foo', 23)
    aa.set('bar', 42)
    assert "'foo': 23" in str(aa)
    assert "'bar': 42" in str(aa)
