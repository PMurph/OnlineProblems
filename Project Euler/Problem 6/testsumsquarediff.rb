require "./sumsquarediff"
require "test/unit"

class TestSumSquareDiff < Test::Unit::TestCase
    def testSumOfNums
        assert_equal(1, sumOfNums(1), 'sumOfNums(1) should have returned 1 but returned ' + sumOfNums(1).to_s)
        assert_equal(3, sumOfNums(2), 'sumOfNums(2) should have returned 3 but returned ' + sumOfNums(2).to_s)
        assert_equal(6, sumOfNums(3), 'sumOfNums(3) should have returned 6 but returned ' + sumOfNums(3).to_s)
        assert_equal(55, sumOfNums(10), 'sumOfNums(10) should have returned 55 but returned ' + sumOfNums(10).to_s)
        assert_equal(210, sumOfNums(20), 'sumOfNums(20) should have returned 210 but returned ' + sumOfNums(20).to_s)
    end
    
    def testSumOfSquares
        assert_equal(1, sumOfSquares(1), 'sumOfSquares(1) should have returned 1 but returned ' + sumOfSquares(1).to_s)
        assert_equal(5, sumOfSquares(2), 'sumOfSquares(2) should have returned 5 but returned ' + sumOfSquares(2).to_s)
        assert_equal(14, sumOfSquares(3), 'sumOfSquares(3) should have returned 14 but returned ' + sumOfSquares(3).to_s)
        assert_equal(55, sumOfSquares(5), 'sumOfSquares(5) should have returned 55 but returned ' + sumOfSquares(5).to_s)
        assert_equal(385, sumOfSquares(10), 'sumOfSquares(10) should have returned 385 but returned ' + sumOfSquares(10).to_s)
    end
    
    def testDiffSumSquares
        assert_equal(0, diffSumSquares(1), 'diffSumSquares(1) should have returned 0 but returned ' + diffSumSquares(1).to_s)
        assert_equal(4, diffSumSquares(2), 'diffSumSquares(2) should have returned 4 but returned ' + diffSumSquares(2).to_s)
        assert_equal(22, diffSumSquares(3), 'diffSumSquares(3) should have returned 22 but returned ' + diffSumSquares(3).to_s)
        assert_equal(2640, diffSumSquares(10), 'diffSumSquares(10) should have returned 2640 but returned ' + diffSumSquares(10).to_s)
    end
end