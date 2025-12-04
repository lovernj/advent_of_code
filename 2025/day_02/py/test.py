import pytest
import solution
@pytest.mark.parametrize("f", [solution.part1_naive])
def test_part1_internal(f):
    # Test cases from the example inputs
    assert f("11-22") == 11+22
    assert f("95-115") == 99
    assert f("998-1012") == 1010
    assert f("1188511880-1188511890") == 1188511885
    assert f("222220-222224") == 222222
    assert f("1698522-1698528") == 0
    assert f("446443-446449") == 446446
    assert f("38593856-38593862") == 38593859
    assert f("565653-565659") == 0
    assert f("824824821-824824827") == 0
    assert f("2121212118-2121212124") == 0
@pytest.mark.parametrize("f", [solution.part2_naive])
def test_part2_internal(f):
    # Test cases from the example inputs
    assert f("11-22") == 11+22
    assert f("95-115") == 99+111
    assert f("998-1012") == 999+1010
    assert f("1188511880-1188511890") == 1188511885
    assert f("222220-222224") == 222222
    assert f("1698522-1698528") == 0
    assert f("446443-446449") == 446446
    assert f("38593856-38593862") == 38593859
    assert f("565653-565659") == 565656
    assert f("824824821-824824827") == 824824824
    assert f("2121212118-2121212124") == 2121212121


@pytest.mark.parametrize("harness,f,out", [
    (solution.harness,solution.part1_naive,1227775554),
    (solution.harness,solution.part2_naive,4174379265)])
def test_harness(harness, f,out):
    assert harness(f, [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
        "565653-565659",
        "824824821-824824827",
        "2121212118-2121212124",
    ]) == out
