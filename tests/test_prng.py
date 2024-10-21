import pytest
from lib.prng import PRNG
from statistics import mean, median


def test_no_collisions():
    num_or_rands = 10_000
    generator = PRNG()

    rands = []
    for i in range(num_or_rands):
        rands.append(generator.get_random())

    assert (len(set(rands)) == len(rands))

def test_adequate_mean():
    epsilon = 0.01
    num_or_rands = 100_000
    generator = PRNG()

    rands = []
    for i in range(num_or_rands):
        rands.append(generator.get_random())

    expected_mean = generator.upper_bound / 2

    assert (abs(mean(rands) - expected_mean) < expected_mean * epsilon)

