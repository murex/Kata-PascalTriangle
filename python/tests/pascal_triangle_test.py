import pytest

from pascal_triangle.pascal_triangle import do_something


class TestPascalTriangle:

    @pytest.mark.skip(reason="test currently disabled") # Comment or remove this line to enable this test case
    def test_acceptance_test(self) -> None:
        assert(42 == do_something())
