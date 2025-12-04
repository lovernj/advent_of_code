import pytest
import solution
@pytest.mark.parametrize("f", [solution.exhaustive,solution.smart])
def test_part1(f):
    # defaut test cases from the prompt
    assert f("987654321111111",2) == '98'
    assert f("811111111111119",2) == '89'
    assert f("234234234234278",2) == '78'
    assert f("818181911112111",2) == '92'  

@pytest.mark.parametrize("f,l,out", [
    (solution.smart,2,357),
    (solution.exhaustive,2,357),
    (solution.smart,12,3121910778619),
    (solution.exhaustive,12,3121910778619)])
def test_harness(f,l,out):
    data = ["987654321111111","811111111111119","234234234234278","818181911112111"]
    assert solution.harness(f,l,data) == out

@pytest.mark.parametrize("f", [solution.exhaustive,solution.smart])
def test_part2(f):
    assert f("987654321111111",12) == '987654321111'
    assert f("811111111111119",12) == '811111111119'
    assert f("234234234234278",12) == '434234234278'
    assert f("818181911112111",12) == '888911112111'