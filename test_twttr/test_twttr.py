from twttr import shorten


def test_lowercase():
    assert shorten("Lucian is pretty cat") == "Lcn s prtty ct"

def test_special():
    assert shorten("Hey |,./") == "Hy |,./"

def test_uppercase():
    assert shorten("Actually Evidences Are Really Recognizable") == "ctlly vdncs r Rlly Rcgnzbl"

def test_omitting_numbers():
    assert shorten("2 plus 5 is 9") == "2 pls 5 s 9"