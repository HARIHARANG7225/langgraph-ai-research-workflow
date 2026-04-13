from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage
from langgraph.graph import StateGraph,END
from typing import TypedDict
from dotenv import load_dotenv

import os 


#LLm 
load_dotenv()
Api_key= os.getenv("Google_api_key")
if not Api_key:
     raise ValueError("Api Key Not found in environment variable")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
       google_api_key=Api_key,
       temperature=0.2)
class mystate(TypedDict , total=False):
     input:str
     research_state:str
     summary_state:str
     error:str

#Agent/Node

def Research_agent(state:mystate):
     try:
          input_content=state.get('input',"").strip()
          if not input_content:
               return{"error":'Input content is empty '}
          else:
               
               res_response=llm.invoke([SystemMessage(content="""You are an professional Researcher 
                                                      Who always prefer factual Informayion 
                                                      Analyse topic and Give it 4 Bullet Points"""),
                                                      HumanMessage(content=f"""Research The Following Content {input_content}""")])
               return{'research_state':res_response.content}
     except Exception as e:
          return{"error":f" Research Agent Failed {e}"}
     
def Summary_agent(state:mystate):
     try: 
         if state.get("error"):
              print("The process is failed Due to Previouse Error")
         else :    
              
              Summary_input=state.get("research_state","").strip
              sum_res=llm.invoke([SystemMessage(content="""You are an professional Gen AI Teacher With 5 years of experience
                                                Answer All Question wich can be understandabel to 9 year old kids
                                                Explain it with an simple example """),
                                                HumanMessage(content=f"""You have been Asked by {state['input']}
                                                this are the four factual Points for the respective question {Summary_input}""")])
              return{'summary_state':sum_res.content}
     except Exception as e:
         print(f"Sorry The Summary Agent  is failed due to {e}")

#Graph
Builder=StateGraph(mystate)

Builder.add_node('Research',Research_agent)
Builder.add_node("Summary",Summary_agent)

Builder.set_entry_point('Research')
Builder.add_edge('Research','Summary')
Builder.add_edge('Summary',END)


graph=Builder.compile()

result=graph.invoke({'input':'About Rest Api'})
print(result['summary_state'])
        
