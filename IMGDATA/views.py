from django.shortcuts import render
from .metaListGenerator import MetaListGenerator
from rest_framework.views import APIView
from rest_framework.response import Response
from .sendAIRequest import SendAIRequest
from .utility import Utility
import time
availableType = ['flowchart','cyclic diagram','component diagram','pyramid chart']
class ImageGenerator(APIView):
    def post(self,request):
        result = []
        clientData =  list(request.data.values())
        ListGenerator = MetaListGenerator()
        SendAIReq = SendAIRequest()
        Util = Utility()
        title = clientData[0]
        scale = clientData[1]
        diagramType = SendAIReq.decideImageType(title)
        curX = 0
        curY = 0
        print(diagramType,'\n\n')
        
        if(diagramType == availableType[0]):
            data = SendAIReq.sendFlowchartAIRequest(title)
            labels= Util.formatFromlistGenerator(data)
            (result,curX,curY) = ListGenerator.constructFlowChartList(labels)
        elif(diagramType == availableType[1]):
            data = SendAIReq.sendFlowchartAIRequest(title)
            labels= Util.formatFromlistGenerator(data)
            (result,curX,curY) = ListGenerator.constructCyclicDiagramList(labels)
        elif(diagramType == availableType[2]):
            data = SendAIReq.sendComponentDiagramAIRequest(title)
            (dispTitle,labels)= Util.formatComponentlist(data)
            (result,curX,curY) = ListGenerator.constructComponentDiagram(dispTitle,labels)
        elif(diagramType == availableType[3]):
            data = SendAIReq.sendPyramidChartAIRequest(title)
            print('data',data)
            labels = Util.formatFromlistGenerator(data)
            (result,curX,curY) = ListGenerator.constructPyramidChart(labels)
        else:
            return Response({'data':'OPPS'})


        time.sleep(5)
        result.append(curX)
        result.append(curY)
        # result.insert(0,{'shape': 'rect', 'x': 0, 'y': 0, 'width': curX, 'height': curY, 'fill': 'white'})
        print('\n\n',result,'\n\n')
        return Response({'data':result})
  