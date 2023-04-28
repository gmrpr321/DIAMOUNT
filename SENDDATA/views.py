from django.shortcuts import render
from MAINAPP.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import openai
url = "https://api.openai.com/v1/completions"


class Textview(APIView):
    def post(self,request):
            print("\nreqsent\n")
            openai.api_key = settings.OPENAI_KEY
            aiModel = "text-davinci-003"
            HeadingInstructions =    '''1.prompt should not contain any special characters like comma to separate two titles
                                    2.prompt should separate each heading with a '\n' '''
            paraForHeadingInstructions = '''1.prompt can gererate multiple para for a heading but should contain a newline between two paras
                                            2.prompt should not start with a title
                                            4.prompt should not contain trailing spaces in the beginning or end
                                            5.the entire prompt should be a string
                                            6.do not start with an introduction line about the title, jump right into the contents of subheading'''
            def generateHeadings(title,nos,instructions):
                response =openai.Completion.create(
                    model = aiModel,
                    prompt = f'''give me {nos} headings for an article about {title} 
                            strictly follow these instructions {instructions}''',
                    max_tokens = 200,
                    temperature = 0.6,
                )
                headings = response['choices'][0]['text'].split('\n')
                while("" in headings):
                    headings.remove("")
                for x in range(0,len(headings)):
                    if((headings[x][0]).isdigit()):
                        headings[x] = headings[x][2:]
                        headings[x] = headings[x].strip()
                    if(headings[x][-1] == "'"):
                        headings[x] = headings[:-1]
                return headings

            def generateParaforHeadings(title,headings,nos,instructions):
                result = []
                for heading in headings:
                    response = openai.Completion.create(
                        model = aiModel,        
                        prompt = f'''give me a paragraph for about {nos} words for an article{title} for the sub heading{heading}
                                    while strictly following these instructions {instructions}''',
                        max_tokens= 500,
                        temperature = 0.6,
                    )  
                    result.append(response['choices'][0]['text'])
                while("" in result):
                    result.remove("")
                return result
            title = "Structure of a programming Language Compiler"
            titleNos = 10
            paraLength = 150
            headings = generateHeadings(title,titleNos,HeadingInstructions)
            paragraphs =  generateParaforHeadings(title,headings,paraLength,paraForHeadingInstructions)
            result = {'headings' : headings,'paragraphs' : paragraphs}
            return Response({'data' :result})


# def get(self,request):
#         openai.api_key = settings.OPENAI_KEY
#         response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt="explain about swarm technology",
#         temperature=1,
#         max_tokens=500,
#         )
#         print('\n\n\n\n',response,'\n\n\n\n')
#         return Response({"data" : response["choices"][0]["text"]})
