import pytest
import solution
@pytest.mark.parametrize("f", [solution.part1])
def test_part1(f):
    # Right nonoverflow move
    assert f(10, 50, 0) == (60, 0)
    # Right overflow move
    assert f(60, 50, 0) == (10, 0)
    # Right exact overflow move
    assert f(50, 50, 0) == (0, 1)
    # Left nonoverflow move
    assert f(-10, 50, 0) == (40, 0)
    # Left overflow move
    assert f(-60, 50, 0) == (90, 0)
    # Left exact overflow move
    assert f(-50, 50, 0) == (0, 1)

@pytest.mark.parametrize("f", [solution.part2_naive, solution.part2_optimized])
def test_part2(f):
    # Right nonoverflow move
    assert f(10, 50, 0) == (60, 0)
    # Right overflow move
    assert f(60, 50, 0) == (10, 1)
    # Right exact overflow move
    assert f(50, 50, 0) == (0, 1)
    # Left nonoverflow move
    assert f(-10, 50, 0) == (40, 0)
    # Left overflow move
    assert f(-60, 50, 0) == (90, 1)
    # Left exact overflow move
    assert f(-50, 50, 0) == (0, 1)
    
    # Right double overflow move
    assert f(160, 50, 0) == (10, 2)
    # Left double overflow move
    assert f(-160, 50, 0) == (90, 2)
    # Right double exact overflow move
    assert f(150, 50, 0) == (0, 2)
    # Left double exact overflow move
    assert f(-150, 50, 0) == (0, 2)