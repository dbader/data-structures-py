from trie import Trie


def test_put():
    t = Trie()
    t.put("rome", 1)
    t.put("romulus", 2)
    t.put("romanus", 3)
    t.put("romantic", 4)
    assert t.get("rome") == 1
    assert t.get("romulus") == 2
    assert t.get("romanus") == 3
    assert t.get("romantic") == 4
    t.put("romanus", 23)
    assert t.get("romanus") == 23

def test_autocomplete():
    t = Trie()
    t.put("rome", 1)
    t.put("romulus", 2)
    t.put("romani", 3)
    t.put("romantic", 4)
    assert t.matches("rome") == ["rome"]
    assert t.matches("roman") == ["romani", "romantic"]
    assert t.matches("rom") == ["rome", "romani", "romulus", "romantic"]
