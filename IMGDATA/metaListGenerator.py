import math
from .utility import Utility
'''
used to generate list of ojects each containing instruction to render each element.
each member gets a list of labels as argument and returns a list  
'''
class MetaListGenerator():
    def __init__(self):
        None

    def constructFlowChartList(self,labels):
            util = Utility()
            curY = 50   #padding top
            longestLabelLen = util.maxLabelLen(labels)
            curX = (longestLabelLen/2)*15
            width = 30 * longestLabelLen
            height = 80
            fill = 'lightBlue'
            result = []
            for x in range(0,len(labels)):
                curdata = {}
                #shape
                curdata['shape'] = 'rect'   
                curdata['x'] = curX
                curdata['y'] = curY
                curdata['width'] = width
                curdata['height'] = height
                curdata['fill'] = fill
                result.append(curdata)
                #text
                curdata = {}
                curdata['shape'] = 'text'
                curdata['font-size'] = '2.5em'
                curdata['text'] = labels[x]
                curdata['x'] = curX + (width - len(labels[x])*17)/2
                curdata['y'] = curY + (height/2)+10
                result.append(curdata)
                if(x != len(labels)-1):
                    #line
                    curdata = {}
                    curdata['shape'] = 'line'
                    curdata['x1'] = curX + (width/2)
                    curdata['y1'] = curY + height
                    curdata['x2'] = curX + (width/2)
                    curdata['y2'] = curY + 2*height
                    curdata['stroke'] = 'black'
                    curdata['strokeWidth'] = '2'
                    result.append(curdata)
                    curdata  = {}
                    #arrow
                    curdata['shape'] = 'path'
                    curdata['d'] = 'M'+str(curX - 10 + (width//2))+' '+str(curY+2*height)+' l20 0l-10 10z'
                    curdata['fill'] = 'black'
                    result.append(curdata)
                curdata = {}
                curY = (curY + 2*height) +10
            print(result)
            return (result,width,curY/2)
    def constructCyclicDiagramList(self,labels):
        util = Utility()
        longestLabelLen = util.maxLabelLen(labels)
        parts = len(labels)
        height = 80
        width = 16 * longestLabelLen
        labellen = len(labels)*70
        if(len(labels) > 15):
             labellen = len(labels) * 150
             
        cyclic = {
        'rectWidth': width,
        'rectHeight': height,
        'circleRadius': labellen * 0.6+ longestLabelLen*17,
        }
        canvas = {
        'width': cyclic['circleRadius']*2.4+200+width/2,
        'height': cyclic['circleRadius']*2.4+200+width/2}
        
        rectPositions = []
        arrowPositions = []
        labelPositions = []
        labelOrArrow = 0
        i=0
        while(i<360):
            points = util.pointOnCircle(
            [canvas['width'] / 2, canvas['height'] / 2],
            cyclic['circleRadius'],
            i - 90)
            arrowPoints = util.pointOnCircle(
            [canvas['width'] / 2, canvas['height'] / 2],
            cyclic['circleRadius'],
            i - 90)
            labelPoints = util.pointOnCircle(
                 [canvas['width']/2,canvas['height']/2],
                 cyclic['circleRadius'],
                 i-90)
            if labelOrArrow % 2 == 0:
                rectPositions.append(points)
                labelPositions.append(labelPoints)
            else:
                arrowPositions.append({
                "shape": "path",
                "d": util.getTrianglePath(arrowPoints["x"], arrowPoints["y"], i + 92, 10),
                "fill": "#0262FF"
            })
            labelOrArrow += 1
            i+=360/(parts*2)
        data = [
            {
             "shape" : "rect",
             "x" : 0,
             "y" : 0,
             'width' : canvas['width'],
             'height' : canvas['height'],
             'fill' : 'white'
            },{
                "shape": "circle",
                "cx": canvas['width'] / 2,
                "cy": canvas['height'] / 2,
                "r": cyclic['circleRadius'],
                "stroke": "black",
                "fill" : 'white',
                "stroke-width": "4"
            }
        ]
        for x in range(parts):
            data.append({
                "shape": "rect",
                "x": rectPositions[x]["x"] - cyclic['rectWidth'] / 2,
                "y": rectPositions[x]["y"]-  cyclic['rectHeight'] / 2,
                "width": cyclic['rectWidth'],
                "height": cyclic['rectHeight'],
                "fill": "lightblue"
            })
        for x in range(len(labels)):
             data.append({
                  "shape" : "text",
                  "text" : labels[x],
                    "x": rectPositions[x]["x"] -  ( cyclic['rectWidth'] / 2)+(cyclic['rectWidth']/2 - len(labels[x])*7) , #was len(labels[x]*7)
                    "y": rectPositions[x]["y"],
                'font-size' :  '1.8em'
             })
        
        data = data + arrowPositions
        return (data,canvas['width']/2 + 50,canvas['height']/2)
    def constructComponentDiagram(self,dispTitle,labels):
        util = Utility()
        longestLabelLen = util.maxLabelLen(labels)
        parts = len(labels)
        height = 80
        width = 24 * longestLabelLen
        component = {
        'rectWidth': width,
        'rectHeight': height,
        'circleRadius': (len(labels)) *3+ longestLabelLen*4 + len(dispTitle)*8,
        'displacement' : longestLabelLen*2 + len(labels)*80
        }
        canvas = {
        'width': component['circleRadius']*2+component['displacement']*3,
        'height': component['circleRadius']*2+component['displacement']*3}
        data = [
             {
             'shape' : 'circle',
             'cx' : canvas['height']/2,
             'cy' : canvas['width']/2,
             'r' : component['circleRadius'],
             "stroke": "black",
             "fill" : 'lightgreen',
             "stroke-width": "0.2rem"
             },
             {'shape' : 'text',
              'text' : dispTitle,
            #   curX + (width - len(labels[x])*10)/2
               'x' : (canvas['width']/2 - component['circleRadius']) + (component['circleRadius'] -len(dispTitle)*8),
               'y' : canvas['height']/2+10,
               'font-size' : '1.9em'
             }
        ]
        rectPositions = []
        arrowPositions = []
        labelPositions = []
        labelOrArrow = 0
        lcount = 0
        x = 0
        while(x<360 and lcount<len(labels)):
             startPoints = util.pointOnCircle([canvas['width']/2,canvas['height']/2],component['circleRadius'],x-90)
             endPoints = util.move_point(startPoints['x'],startPoints['y'],x-90,component['displacement'])
             rectPositions.append({
                  'shape' : 'rect',
                  'x' : endPoints[0]-component['rectWidth']/2,
                  'y' : endPoints[1]-component['rectHeight']/2,
                  'width' : component['rectWidth'],
                  'height': component['rectHeight'],
                  'fill' : 'lightblue'
                }
             )
             arrowPositions.append(
            {'shape' : 'line',
                'x1' : startPoints['x'],
                'y1' : startPoints['y'],
                'x2' : endPoints[0],
                'y2' : endPoints[1],
                'stroke' : 'black',
                'stroke-width' : '4'
            })
             labelPositions.append({
                'shape' : 'text',
                'text' : labels[lcount],
                #   (width - len(labels[x])*10)/2
                'x' : endPoints[0] - component['rectWidth'] + component['rectWidth']-len(labels[lcount]*15)/2,
                'y' : endPoints[1] + 5 ,
                'font-size' : '2em'
            })
             data+=arrowPositions
             data+=rectPositions
             data+=labelPositions
             lcount+=1
             x+=360/parts
        return (data,canvas['height']/2,canvas['height']/2)
    
    def constructPyramidChart(self,labels):
        print('\n\n\n\n','labels[0]',labels[0],'\n\n\n\n')
        metalist = []
        util = Utility()
        maxlabellen = util.maxLabelLen(labels)
        labelnos = len(labels)
        longestLabelLen = util.maxLabelLen(labels),
        calcdeg = 360 - (len(labels[0])*15+longestLabelLen[0]*8+len(labels)*40)
        currentDetails = {
              "segment_height" : len(labels)*8 + maxlabellen*9,
              "triangle_deg" : max(30,min(calcdeg,50))
         }
        canvas = {
              "canvasWidth" : (labelnos*currentDetails['segment_height']) + currentDetails['segment_height'],
              "canvasheight" : labelnos*40 + currentDetails['segment_height'],
              "labelNos" : len(labels),
             
         }
        
        print('calcdeg',calcdeg)
       
        base_triangle_points = {
              "top" : {
              "x" : canvas['canvasWidth'],
              "y" : 50
                    }
         }
        # calculate the other two points 
        triangle_left,triangle_right = util.points_of_triangle_with_height_and_angle(base_triangle_points['top']['x'],
                                                                             base_triangle_points['top']['y'],
                                                                             currentDetails['segment_height'],
                                                                            currentDetails['triangle_deg']
                                                                             )
        base_triangle_points["left"] = {
             "x" : triangle_left[0],
             "y" : triangle_left[1]
        } 
        base_triangle_points["right"] = {
             "x" : triangle_right[0],
             "y" : triangle_right[1]
        }

        # construct base triangle path
        base_triangle_path = util.make_triangle_path(base_triangle_points['top']['x'],base_triangle_points['top']['y'],
                                                           base_triangle_points['left']['x'],base_triangle_points['left']['y'],
                                                           base_triangle_points['right']['x'],base_triangle_points['right']['y'])
        metalist.append({
                "shape": "path",
                "d": base_triangle_path,
                "fill": "#6de3db",
            })
        metalist.append(
        {'shape' : 'text',
              'text' : labels[0],
               'x' : (base_triangle_points['left']['x'] + (base_triangle_points['right']['x'] - base_triangle_points['left']['x'])/2) - 8.5*len(labels[0]) ,
               'y' : base_triangle_points['right']['y'] - (currentDetails['segment_height']/6) ,
               'font-size' : '2.4em'
             })
        # remember the points that make the shortest side of the trapezium
        prev_points = {
            "left" : base_triangle_points['left'],
            "right" : base_triangle_points['right']
        }
        currentDetails['segment_height'] -= currentDetails['segment_height']/2
        for x in range(1,len(labels)):
            fill_color = "#6de3ac"
            if(x%2==0):
                fill_color = "#6de3db"
            current_trapezium_points={
            "left_triangle" : {
            "degree" : 180-(90+currentDetails['triangle_deg']),
            "base_dist" : 0,
            "top_point" : prev_points['left'],
            "left_point" : { "x":0,"y" : 0},
            "right_point" : { "x":0,"y" : 0},
            },
            "rectangle" : {
            "top_left_point" : prev_points['left'],
            "top_right_point" : prev_points['right'],
            "bottom_left_point" : {
            "x" : prev_points['left']['x'],
            "y" : prev_points['left']['y'] + currentDetails['segment_height'],
            },
            "bottom_right_point" : {
            "x" : prev_points['right']['x'],
            "y" : prev_points['right']['y'] + currentDetails['segment_height'],
            },
            },
            "right_triangle" : {
            "top_point" : prev_points['right'],
            "left_point" : { "x":0,"y" : 0},
            "right_point" : { "x":0,"y" : 0},
            "degree" : 180-(90+currentDetails['triangle_deg']),
            "base_dist" : 0,
            },
            "text_position" : {
                "x" : 0,
                "y" : 0
            }
            }
            # calculate the points of both triangles
            left_triangle_points = util.points_of_left_triangle(current_trapezium_points['left_triangle']['top_point']['x'],
                                                       current_trapezium_points['left_triangle']['top_point']['y'],
                                                       currentDetails['segment_height'],
                                                       current_trapezium_points['left_triangle']['degree'])
            
            right_triangle_points = util.points_of_right_triangle(current_trapezium_points['right_triangle']['top_point']['x'],
                                                         current_trapezium_points['right_triangle']['top_point']['y'],
                                                         currentDetails['segment_height'],
                                                         current_trapezium_points['right_triangle']['degree'])
            # update current trapezium points
            current_trapezium_points['left_triangle']['left_point'] = left_triangle_points['left_point']
            current_trapezium_points['left_triangle']['right_point'] = left_triangle_points['right_point']
            current_trapezium_points['right_triangle']['left_point'] = right_triangle_points['left_point']
            current_trapezium_points['right_triangle']['right_point'] = right_triangle_points['right_point']


            current_trapezium_points['text_position']['x'] = ((current_trapezium_points['left_triangle']['right_point']['x']+current_trapezium_points['right_triangle']['left_point']['x'])/2) - 8*len(labels[x])
            current_trapezium_points['text_position']['y'] = current_trapezium_points['right_triangle']['right_point']['y'] - (currentDetails['segment_height']/3)   

            # update the metalist,change prevpoints
            metalist.append({
                "shape": "path",
                "d": util.rectangle_path(current_trapezium_points['rectangle']['top_left_point']['x'],
                                         current_trapezium_points['rectangle']['top_left_point']['y'],
                                         current_trapezium_points['rectangle']['top_right_point']['x'],
                                         current_trapezium_points['rectangle']['top_right_point']['y'],
                                         current_trapezium_points['rectangle']['bottom_left_point']['x'],
                                         current_trapezium_points['rectangle']['bottom_left_point']['y'],
                                         current_trapezium_points['rectangle']['bottom_right_point']['x'],
                                         current_trapezium_points['rectangle']['bottom_right_point']['y'],), 
                "fill": fill_color,
            })
            metalist.append({
                "shape": "path",
                "d": util.make_triangle_path(current_trapezium_points['left_triangle']['top_point']['x'],
                                             current_trapezium_points['left_triangle']['top_point']['y'],
                                             current_trapezium_points['left_triangle']['left_point']['x'],
                                             current_trapezium_points['left_triangle']['left_point']['y'],
                                             current_trapezium_points['left_triangle']['right_point']['x'],
                                             current_trapezium_points['left_triangle']['right_point']['y']), 
                "fill": fill_color,
            })

            metalist.append({
                "shape": "path",
                "d": util.make_triangle_path(current_trapezium_points['right_triangle']['top_point']['x'],
                                             current_trapezium_points['right_triangle']['top_point']['y'],
                                             current_trapezium_points['right_triangle']['left_point']['x'],
                                             current_trapezium_points['right_triangle']['left_point']['y'],
                                             current_trapezium_points['right_triangle']['right_point']['x'],
                                             current_trapezium_points['right_triangle']['right_point']['y']), 
                "fill": fill_color,
            })

            metalist.append(  
            {'shape' : 'text',
              'text' : labels[x],            
               'x' : current_trapezium_points['text_position']['x'],
               'y' : current_trapezium_points['text_position']['y'],
               'font-size' : '2.4em'
             }
            )
            # update prevpoints
            prev_points['left'] = current_trapezium_points['left_triangle']['left_point']
            prev_points['right'] = current_trapezium_points['right_triangle']['right_point']
        # send current x,y values for canvas
        max_x = prev_points['right']['x'] + 50
        max_y = prev_points['right']['y'] + 50
        return (metalist,canvas['canvasWidth'],canvas['canvasheight'])

         
