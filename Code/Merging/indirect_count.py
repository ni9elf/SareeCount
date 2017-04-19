import math


def length ( line ):
    #returns length of line segment
    x1 = float(line[0])
    x2 = float(line[2])
    y1 = float(line[1])
    y2 = float(line[3])
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    
   
def angle ( line ): 
    #returns angle of line in degrees
    #calculation does not consider shifted top left origin as shift is
    #applicable to all lines
    x1 = float(line[0])
    x2 = float(line[2])
    y1 = float(line[1])
    y2 = float(line[3])
    if(x2 == x1):
        if (y2 > y1):
            return 90
        else:
            return 270                
    #range is [0, 360] degrees
    slope = 180 + math.degrees(math.atan2((y2 - y1), (x2 - x1)))    
    #normalize slope values to lie between -45 to 135 degrees (180 degree range)
    if(slope >= 135 and slope <= 315):
        slope -= 180
    if(slope >= 315 and slope <= 360):            
        slope -=360
    return slope    


if __name__ == '__main__':
    with open('merged_lines.txt', 'r') as f:
        line_segments = f.readlines()
    ls = [x.strip().split(' ') for x in line_segments]     
    ls.sort(cmp = lambda x, y: 1 if length(x) < length(y) else -1)
   
    #count no of lines in two groups
    group1 = []
    group2 = []
    for line in ls[0:20]:
        slope = angle(line)
        if(slope >= -45 and slope <= 45):
            group1.append(slope)
        else:
            group2.append(slope)
            
    #keep majority group
    if(len(group1) > len(group2)):
        group = group1
    else:
        group = group2
    
    #find length of small lines
    sum_ = 0
    for line in ls:
        l = length(line)
        sum_ += l
    l_avg = sum_/len(ls)
    
    count = 0
    #count small lines with same slope as saree shelf
    for line in ls:
        slope = angle(line)
        l = length(line)
        if(l >= l_avg-10 and l <= l_avg+10):
            for m in group:
                if (slope >= m-5 and slope <= m+5):
                    count += 1
                    break
    print "Number of sarees:", count
