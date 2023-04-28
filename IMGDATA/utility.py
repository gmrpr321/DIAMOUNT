'''
utility class that contains functions to format data sent by sendAIRequest methods
'''
import math
class Utility():
    def __init__(self):
        None
        '''
        formats the ai list by converting from str to list. returns the list
        '''
    def maxLabelLen(self,labels):
            max = len(labels[0])
            for label in labels:
                if(len(label)) > max:
                    max = len(label)
            return max
    '''
    for a given point, draw a triangle for cyclic diagram that is tilted
    at angle degree while val is the factor of its size
    '''
    def getTrianglePath(self,x, y, degree, val):
            radian = (degree * math.pi) / 180
            x1 = x + val * 3 * math.sin(radian)
            y1 = y - val * 3 * math.cos(radian)
            x2 = x + val * 3 * math.sin(radian + (2 * math.pi) / 3)
            y2 = y - val * 3 * math.cos(radian + (2 * math.pi) / 3)
            x3 = x + val * 3 * math.sin(radian + (4 * math.pi) / 3)
            y3 = y - val * 3 * math.cos(radian + (4 * math.pi) / 3)
            return f'M{x1},{y1} L{x2},{y2} L{x3},{y3} Z'
    '''
    formats the API response as a valid list. returns that list of labels
    '''
    def formatFromlistGenerator(self,data):
        data = data.strip("[]")
        data = data.split(',')
        if(data[0][0] == "'"):
            data[0] = data[1:]
        if(data[-1][-1] == "'"):
            data[-1] = data[-1][:-1]
        labels  = data
        return labels
    '''
    special format fn for component diagrams
    '''
    def formatComponentlist(self,data):
        data = data.strip("[]")
        data = data.split(',')
        if(data[0][0] == "'"):
            data[0] = data[1:]
        if(data[-1][-1] == "'"):
            data[-1] = data[-1][:-1]
        dispTitle = data[0]
        labels = data[1:]
        return (dispTitle,labels)

    '''
    move a point for displacement units from x,y inclined at degree
    '''
    def move_point(self,x, y, degree, displacement):
        radians = math.radians(degree)
        new_x = x + displacement * math.cos(radians)
        new_y = y + displacement * math.sin(radians)
        return (new_x, new_y)
    
    '''
    for a given point , an angle t and a distance h, returns a point that is
    h distance away from a at an angle t
    '''

    def point_at_distance_and_angle(self,x, y, h, t):
        t = math.radians(t)
        new_x = x + h * math.cos(t)
        new_y = y + h * math.sin(t)

        return (new_x, new_y)
    
    '''
    for a given point(x,y) , height h of a triangle and degree t, 
    return the other 2 points of this triangle
    '''
    def get_other_points(x, y, h, t):
        # Find coordinates of point A (tip of the triangle)
        Ax = x
        Ay = y + h
        
        # Find length of base of triangle
        b = 2 * h * math.tan(math.radians(t/2))
        
        # Find x-coordinates of points B and C
        Bx = x - b/2
        Cx = x + b/2
        
        # Find y-coordinates of points B and C (same as y-coordinate of A)
        By = Ay
        Cy = Ay
        
        return [(Bx, By), (Cx, Cy)]
    def points_of_triangle_with_height_and_angle(self,x, y, h, t):
        base_dist = h/(math.tan(math.radians(t)))
        point1_x = x-base_dist
        point1_y = y+h
        point2_x = x+(base_dist)
        point2_y = y+h
        print('base_dist',base_dist,'h',h,'tan(t)',math.degrees(math.tan(t)),'tan :',math.tan(t),t)
        return (point1_x, point1_y), (point2_x, point2_y)
    
    # '''
    # for given two points that forms the shorter side of a equal trapizium, 
    # and height h . return the other two points of the trapezium that forms the larger side
    # '''
    # def points_f_trapezium_with_height(self,x1, y1, x2, y2, h):
    #     length = abs(x2 - x1)
    #     long_length = length + 2 * h
    #     mid_x = (x1 + x2) / 2
    #     left_x = mid_x - long_length / 2
    #     right_x = mid_x + long_length / 2
    #     y3 = y4 = y1 + h
    #     return (left_x, y3), (right_x, y4)
    '''
    given is center point(x,y) radius and degree, returns a point that lies on that circle in that degree
    '''
    def pointOnCircle(self,center, radius, degree):
            x = center[0]
            y = center[1]
            radians = (degree * math.pi) / 180
            x_on_circle = x + radius * math.cos(radians)
            y_on_circle = y + radius * math.sin(radians)
            return {"x": x_on_circle, "y": y_on_circle}
    
    '''
    given are 4 points x1,y1.x2.y2.x3.y3,x4,y4 , return a python function that constructs the d3.js
    'd' path attribute by connecting these points, hence making a quadrilateral
    '''
    def make_quadrilateral_path(self,x1, y1, x2, y2, x3, y3, x4, y4):
        return f'M{x1},{y1} L{x2},{y2} L{x3},{y3} L{x4},{y4} Z'
    
    '''
    given are three points x1,y1,x2,y2,x3,y3. return the d attribute of path variable 
    for d3.js by connecting these points and hence forming a triangle
    '''
    def make_triangle_path(self,x1, y1, x2, y2, x3, y3):
        return f'M{x1},{y1} L{x2},{y2} L{x3},{y3} Z'
    
    def points_of_left_triangle(self,x,y,h,t):
         x1 = x-(h*math.tan(math.radians(t)))
         y1 = y+h
         x2 = x
         y2 = y+h
         result = {
              "left_point" : {
              "x" : x1,
              "y" : y1
              },
              "right_point" :{
              "x" : x2,
              "y" : y2
              }
         }
         return result
    
    def points_of_right_triangle(self,x,y,h,t):
         x1 = x
         y1 = y+h
         x2 = x+(h*math.tan(math.radians(t)))
         y2 = y+h
         result = {
              "left_point" : {
              "x" : x1,
              "y" : y1
              },
              "right_point" :{
              "x" : x2,
              "y" : y2
              }
         }
         return result
    
    def rectangle_path(self,x1, y1, x2, y2, x3, y3, x4, y4):
        width = abs(x2 - x1)
        height = abs(y3 - y1)
        x = min(x1, x2)
        y = min(y1, y3)
        d = "M {} {} L {} {} L {} {} L {} {} Z".format(x, y, x+width, y, x+width, y+height, x, y+height)
        return d