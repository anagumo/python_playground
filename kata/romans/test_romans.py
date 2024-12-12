import romans

def test_number_to_list():
    assert romans.to_number_list("") == []
    assert romans.to_number_list("zsh") == []
    assert romans.to_number_list(1939) == [1,9,3,9]

def test_to_base_10():
    assert romans.to_base_10([]) == []
    assert romans.to_base_10([1,8]) == [10,8]
    assert romans.to_base_10([1,9,3,9]) == [1000,900,30,9]

def test_to_roman():
    assert romans.to_roman([]) == ""
    assert romans.to_roman([10,8]) == "XVIII"
    assert romans.to_roman([1000,900,30,9]) == "MCMXXXIX"