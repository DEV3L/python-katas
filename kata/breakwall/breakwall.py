from typing import List


def elf_report(numbers: List) -> List:
    if not numbers or len(numbers) < 2:
        return []

    for index, number in enumerate(numbers):
        for next in range(index + 1, len(numbers)):
            next_number = numbers[next]

            if number + next_number == 2020:
                return [number, next_number]

    return []


def elf_multiply(result: List) -> int:
    return result[0] * result[1]


def elf_report_three(numbers: List) -> List:
    if not numbers or len(numbers) < 3:
        return []

    for first, first_number in enumerate(numbers):
        for second in range(first + 1, len(numbers)):
            second_number = numbers[second]
            for third in range(second + 1, len(numbers)):
                third_number = numbers[third]

                if first_number + second_number + third_number == 2020:
                    return [first_number, second_number, third_number]

    return []


def elf_multiply_three(result: List) -> int:
    return result[0] * result[1] * result[2]


if __name__ == "__main__":
    numbers_list = [
        2000,
        50,
        1984,
        1600,
        1736,
        1572,
        2010,
        1559,
        1999,
        1764,
        1808,
        1745,
        1343,
        1495,
        1860,
        1977,
        1981,
        1640,
        1966,
        1961,
        1978,
        1719,
        1930,
        535,
        1804,
        1535,
        1507,
        1284,
        1618,
        1991,
        1589,
        1593,
        1960,
        1953,
        1963,
        1697,
        1741,
        1823,
        1932,
        1789,
        1822,
        1972,
        1570,
        1651,
        1800,
        1514,
        726,
        1567,
        72,
        1987,
        1791,
        1842,
        1020,
        1541,
        1383,
        1505,
        2009,
        1925,
        13,
        1973,
        1599,
        1632,
        1905,
        1626,
        1554,
        1913,
        1890,
        1583,
        1513,
        1828,
        187,
        1616,
        1508,
        1524,
        1613,
        1648,
        32,
        1612,
        1992,
        1671,
        1955,
        1943,
        1936,
        1870,
        1629,
        1493,
        1770,
        1699,
        1990,
        1658,
        1592,
        1596,
        1888,
        1540,
        239,
        1677,
        1602,
        1877,
        1481,
        2004,
        1985,
        1829,
        1980,
        2008,
        1964,
        897,
        1843,
        1750,
        1969,
        1790,
        1989,
        1606,
        1484,
        1983,
        1986,
        1501,
        1511,
        1543,
        1869,
        1051,
        1810,
        1716,
        1633,
        1850,
        1500,
        1120,
        1849,
        1941,
        1403,
        1515,
        1915,
        1862,
        2002,
        1952,
        1893,
        1494,
        1610,
        1797,
        1908,
        1534,
        1979,
        2006,
        1971,
        1993,
        1432,
        1547,
        1488,
        1642,
        1982,
        1666,
        1856,
        1889,
        1691,
        1976,
        1962,
        2005,
        1611,
        1665,
        1816,
        1880,
        1896,
        1552,
        1809,
        1844,
        1553,
        1841,
        1785,
        1968,
        1491,
        1498,
        1995,
        1748,
        1533,
        1988,
        2001,
        1917,
        1788,
        1537,
        1659,
        1574,
        1724,
        1997,
        923,
        1476,
        1763,
        1817,
        1998,
        1848,
        1974,
        1830,
        1672,
        1861,
        1652,
        1551,
        1363,
        1645,
        1996,
        1965,
        1967,
        1778,
    ]

    result = elf_report(numbers_list)
    value = elf_multiply(result)
    print(value)

    result = elf_report_three(numbers_list)
    value = elf_multiply_three(result)
    print(value)
