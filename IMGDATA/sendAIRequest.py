import openai
from django.conf import settings
openai.api_key = settings.OPENAI_KEY
aiModel = 'gpt-3.5-turbo'

'''
Used to send request to AI for each diagram type and returns a list of labels
'''
class SendAIRequest():
    def __init__(self):
        None
    def decideImageType(self,title):
        Response = openai.ChatCompletion.create(
            messages = [
                    {
                    'role' : 'system', 'content' : '''You are a helpful assistant that assists in returning a string by following these steps:
                                                        1. Given is a title, choose the most appropriate diagram type to explain the given title
                                                        2. the available diagram types are [flowchart,cyclic diagram,component diagram,pyramid chart].Only choose the most appropriate diagram type from this list.
                                                        3. your output should only contain a string that is the most suitable diagram type from available diagrams list. only give me the diagram type and nothing else       
                                                        4. you should not tell me anything other than the value that is present in the available diagram types list. don't say or expain anything
                                                        5. If 'cycle' is present in the title, then its most probably a cyclic diagram eg(lifecycle)
                                                        6. If multiple diagram types are applicable for a specific title, give me the most appropriate one among the applicable diagram types
                                                        '''},
                                                        
                    {'role' : 'user','content' : 'water cycle'},
                    {'role' : 'assistant','content' : 'cyclic diagram'},
                    {'role' : 'user' , 'content' : f'{title}'}
                    ],
                    temperature = 0.6,
                    max_tokens = 10,
                    model = aiModel
        )
        data = Response['choices'][0]['message']['content']
        return data
    def sendFlowchartAIRequest(self,title):
        Response = openai.ChatCompletion.create(
        messages = [
                    {
                    'role' : 'system', 'content' : '''You are a helpful assistant that assists in returning an array that has following data:
                                                        1. The array elements of the array must contain the labels that will be present in the flowchart diagram to explain the given given title
                                                        2. only give me the list and nothing else.dont say anything else
                                                        3. labels must only be separated by a comma
                                                        4. Prefer maximum number of labels to explain the given title
                                                        5. all labels should be of approximatily in equal length.
                                                        6. dont use connecting words like 'and' to connect with each labels.do not use numbering to specify the order of the labels
                                                        7.do not use numbers to denote the steps. only the value must be present.do not use any type of brackets
                                                        8. Labels should be shorter as possible (< 15 characters)
                                                        '''},
                                                        
                    {'role' : 'user','content' : 'Structure of a Programming language compiler'},
                    {'role' : 'assistant','content' : "[Lexical Analysis,Syntax Analysis,Semantic Analysis,Intermediate Code Generaiton,Optimization,Object Code Generation]"},
                    {'role' : 'user' , 'content' : f'{title}'}
                    ],
                model = aiModel,
                temperature = 0.6,
                max_tokens = 3000
            )
            # data = Response['choices'][0]['text']
        data = Response['choices'][0]['message']['content']
        return data
    def sendComponentDiagramAIRequest(self,title):
        Response = openai.ChatCompletion.create(
        messages = [
                    {
                    'role' : 'system', 'content' : '''You are a helpful assistant that assists in returning an array that has following data:
                                                        1. The array elements of the array must contain the labels that will be present in the component diagram to explain the given given title
                                                        2. only give me the list and nothing else.dont say anything else
                                                        3. labels must only be separated by a comma. 
                                                        4. Prefer maximum number of labels to explain the given title
                                                        5. all labels should be of approximatily in equal length.
                                                        6. dont use connecting words like 'and' to connect with each labels
                                                        7. the first element inside a list must contain the subject from the title. where subject id a word from title
                                                        8. the labels must be the components that comprises the given title.
                                                        9. the subject must be a sliced value from the given title. dont give your own names.it must be all caps
                                                        10.do not use numbers to denote the steps. only the value must be present.do not use any type of brackets
                                                        '''},
                                                        
                    {'role' : 'user','content' : 'components of a car'},
                    {'role' : 'assistant','content' : "[CAR,Engine,Transmission,Suspension,Brakes,Steering system,Exhaust system,Fuel system,Electrical system,Tires,Body]"},
                    {'role' : 'user' , 'content' : f'{title}'}
                    ],
                model = aiModel,
                temperature = 0.5,
                max_tokens = 3000
            )
            # data = Response['choices'][0]['text']
        data = Response['choices'][0]['message']['content']
        print(data)
        return data
    
    def sendPyramidChartAIRequest(self,title):
        Response = openai.ChatCompletion.create(
        messages = [
                    {
                    'role' : 'system', 'content' : '''You are a helpful assistant that assists in returning an array that has following data:
                                                        1. The array elements of the array must contain the labels that will be present in a pyramid chart to explain the given given title
                                                        2. the number of characters present in the first label should not exceed 7
                                                        3. labels must only be separated by a comma. 
                                                        4. The array elements should be listed in the order that they would appear on a nutrition intake pyramid chart, with the top element first and the bottom element last.
                                                        5. only give me the list and nothing else.dont say anything else 
                                                        6. since its a pyramid chart, labels that are present in later part of the list can have more characters than those that are present in first part
                                                        7. dont use connecting words like 'and' to connect with each labels
                                                        8. the labels should be constructed such that they are used to construct a pyramid diagram to explain the given title
                                                        9.do not use numbers to denote the steps. only the value must be present.do not use any type ofbrackets
                                                        '''},
                                                        
                    {'role' : 'user','content' : 'nutrition intake'},
                    {'role' : 'assistant','content' : "[Fats, Dairy, Protein, Fruits, Vegetables, Grains]"},
                    {'role' : 'user' , 'content' : f'{title}'}
                    ],
                model = aiModel,
                temperature = 0.5,
                max_tokens = 3000
            )
            # data = Response['choices'][0]['text']
        data = Response['choices'][0]['message']['content']
        return data