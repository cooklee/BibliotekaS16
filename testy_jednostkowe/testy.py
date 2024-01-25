from datetime import datetime

import pytest


def suma(a, b):
    return a + b


def analyze_pesel(pesel):
    weights = [1, 3, 7, 9,
               1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0
    for digit in pesel[: -1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0
    gender = "male" if int(pesel[-2]) % 2 == 1 else "female"
    month = int(pesel[2:4])
    years = {
        0: '19',
        1: '20',
        2: '21',
        3: '22',
        4: '18'
    }
    year_begging = years[month // 20]
    year = int(year_begging + pesel[0: 2])
    birth_date = datetime(year, month % 20, int(pesel[4:6]))
    result = {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": birth_date
    }
    return result


kobiety = """
70111427229
06293014742
68031676544
98121032521
75052933242
88062234368
94042641648
06280357245
97032069787
57020754745
""".split()
x = analyze_pesel("74041584984")


@pytest.mark.parametrize("pesel, result",
                         [('74041584984', True),
                          ('70111427229', True),
                          ('68031676544', True),
                          ('74041584983', False),
                          ('70111427228', False),
                          ('68031676543', False)
                          ]
                         )
def test_valid_param(pesel, result):
    ret_val = analyze_pesel(pesel)
    assert ret_val['valid'] == result


@pytest.mark.parametrize("pesel",
                         [('74041584984'),
                          ('70111427229'),
                          ('68031676544'),
                          ('74041584983'),
                          ('70111427228'),
                          ('68031676543')
                          ]
                         )
def test_valid_param(pesel):
    ret_val = analyze_pesel(pesel)
    assert ret_val['pesel'] == pesel


@pytest.mark.parametrize("pesel, result",
                         [('74041584984', 'female'),
                          ('70111427229', 'female'),
                          ('68031676544', 'female'),
                          ('85101441154', 'male'),
                          ('76010892292', 'male'),
                          ('55020559551', 'male'),
                          ('67121464113', 'male')
                          ]
                         )
def test_valid_param(pesel, result):
    ret_val = analyze_pesel(pesel)
    assert ret_val['gender'] == result


@pytest.mark.parametrize("pesel, result",
                         [('74041584984', datetime(1974, 4, 15)),
                          ('70111427229', datetime(1970, 11, 14)),
                          ('68031676544', datetime(1968, 3, 16)),
                          ('85101441154', datetime(1985, 10, 14)),
                          ('76010892292', datetime(1976, 1, 8)),
                          ('42262765996', datetime(2042, 6, 27)),
                          ('58220564662', datetime(2058, 2, 5)),
                          ('14431629323', datetime(2114, 3, 16)),
                          ('88692048629', datetime(2288, 9, 20)),
                          ('54892618399', datetime(1854, 9, 26)),

                          ]
                         )
def test_valid_param(pesel, result):
    ret_val = analyze_pesel(pesel)
    assert ret_val['birth_date'] == result
