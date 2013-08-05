require "./foottraffic"
require "test/unit"

class TestFootTraffic < Test::Unit::TestCase
    def testVisitorToS
        err_msg = "Room to_s method did not return the correct string."
        testRoom = Room.new(0)
        assert_equal("Room 0, 0 minute average visit, 0 visitor(s) total", testRoom.to_s, err_msg) 
        
        testRoom.startVisit(0, 540)
        assert_equal("Room 0, 0 minute average visit, 0 visitor(s) total", testRoom.to_s, err_msg)
        
        testRoom.endVisit(0, 560)
        assert_equal("Room 0, 20 minute average visit, 1 visitor(s) total", testRoom.to_s, err_msg)
        
        testRoom.startVisit(1, 240)
        testRoom.startVisit(2, 480)
        testRoom.endVisit(1, 340)
        assert_equal("Room 0, 60 minute average visit, 2 visitor(s) total", testRoom.to_s, err_msg)
        testRoom.endVisit(2, 529)
        assert_equal("Room 0, 56 minute average visit, 3 visitor(s) total", testRoom.to_s, err_msg)
        
        testRoom = Room.new(5)
        
        testRoom.startVisit(3, 450)
        testRoom.endVisit(3, 479)
        assert_equal("Room 5, 29 minute average visit, 1 visitor(s) total", testRoom.to_s, err_msg)
        
        testRoom.startVisit(5, 470)
        testRoom.endVisit(5, 524)
        assert_equal("Room 5, 41 minute average visit, 2 visitor(s) total", testRoom.to_s, err_msg)
    end
end