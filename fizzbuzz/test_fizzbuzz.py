from fizzbuzz import *
import pytest

def test_mult_3():
    assert FizzBuzz.fizzbuzz(6) == 'Fizz'

def test_mult_5():
    assert FizzBuzz.fizzbuzz(10) == 'Buzz'

def test_mult_3and5():
    assert FizzBuzz.fizzbuzz(15) == 'FizzBuzz'