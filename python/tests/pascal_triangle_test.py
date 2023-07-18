import pytest

from pascal_triangle.pascal_triangle import draw


class TestPascalTriangle:

    # @pytest.mark.skip(reason="test currently disabled") # Comment or remove this line to enable this test case
    @pytest.mark.skip(reason="test currently disabled")  # Comment or remove this line to enable this test case
    def test_acceptance_test(self) -> None:
        last_line = 7

        expected = "" \
                   "1\n" \
                   "1 1\n" \
                   "1 2 1\n" \
                   "1 3 3 1\n" \
                   "1 4 6 4 1\n" \
                   "1 5 10 10 5 1\n" \
                   "1 6 15 20 15 6 1\n" \
                   "1 7 21 35 35 21 7 1\n"
        assert (expected == draw(last_line))
