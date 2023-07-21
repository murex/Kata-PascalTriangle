import { draw } from '../src/PascalTriangle';

describe('pascal_triangle', () => {
  // Remove the ".skip" below to enable this test case
  test.skip('acceptance test', () => {
    let lastLine: number = 7;
    let expected: string
      = '1\n'
      + '1 1\n'
      + '1 2 1\n'
      + '1 3 3 1\n'
      + '1 4 6 4 1\n'
      + '1 5 10 10 5 1\n'
      + '1 6 15 20 15 6 1\n'
      + '1 7 21 35 35 21 7 1\n';

    expect(draw(lastLine)).toEqual(expected);
  });
});
