class Room
    attr_reader :num
    attr_reader :visitors
    
    def initialize(roomNum)
        @num = roomNum
        @visitors = 0
        @totalTime = 0
        @currOccupants = {}
    end
    
    def startVisit(id, startTime)
        if !@currOccupants.has_key?(id) || @currOccupants[id] == nil
            @currOccupants[id] = startTime
        end
    end
    
    def endVisit(id, endTime)
        if(@currOccupants.has_key?(id) && @currOccupants[id] <= endTime)
            elapsedTime = endTime - @currOccupants[id]
            @visitors += 1
            @totalTime += elapsedTime
        end
    end
    
    def to_s
        return "Room " + num.to_s + ", " + calcAvg.floor.to_s + " minute average visit, " + visitors.to_s + " visitor(s) total"
    end
    
    private
    
    def calcAvg()
        average = 0
        if @visitors != 0
            average = @totalTime / @visitors
        end
        return average
    end
end

in_events = []
out_events = []
rooms = []

num_in = Integer(ARGF.readline.chomp)

(0...num_in).each do |i|
    currEvent = ARGF.readline.chomp.split(" ")
    if currEvent[2] == "I"
        rooms << Room.new(Integer(currEvent[1]))
        in_events << [Integer(currEvent[0]), Integer(currEvent[1]), Integer(currEvent[3])]
    elsif currEvent[2] == "O"
        rooms << Room.new(Integer(currEvent[1]))
        out_events << [Integer(currEvent[0]), Integer(currEvent[1]), Integer(currEvent[3])]
    end
end

rooms.uniq! { |a| a.num }
rooms = rooms.sort_by { |a| a.num }
in_events = in_events.sort_by { |a| a[2] }
out_events = out_events.sort_by { |a| a[2] }
in_events.reverse!
out_events.reverse!

rooms.each do |i|
    puts i.num
end

while !out_events.empty? || !in_events.empty?
    inE = false
    outE = false
    if in_events.empty?
        curr = out_events.pop
        outE = true
    elsif out_events.empty?
        curr = in_events.pop
        inE = true
    else
        if in_events.last[2] <= out_events.last[2]
            curr = in_events.pop
            inE = true
        else
            curr = out_events.pop
            outE = true
        end
    end
    theRoom = rooms.bsearch { |x| x.num >= curr[1]}
    if theRoom != nil
        if inE == true
            theRoom.startVisit(curr[0], curr[2])
        elsif outE == true
            theRoom.endVisit(curr[0], curr[2])
        end
    end
end

rooms.each do |i|
    puts i.to_s
end
