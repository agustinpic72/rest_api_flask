from first_part import word_counter
import pytest

@pytest.mark.parametrize(
    "frase , expected",
    [
        ('Hi, hi, hI, HI',{'hi':4}),
        ("Hi i'm im IM Agustin agustin aguSTIN Piccoli picCOLI and aN??D thi!!s i,,,s my test! Test teSt",{'hi': 1, 'im': 3, 'agustin': 3, 'piccoli': 2, 'and': 2, 'this': 1, 'is': 1, 'my': 1, 'test': 3})
    ]
)
def test_word_counter(frase,expected):
    assert word_counter(frase) == expected