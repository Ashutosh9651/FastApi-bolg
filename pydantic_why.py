from pydantic import BaseModel,EmailStr,Field
from fastapi import FastAPI
from typing import List,Dict,Optional
from typing_extensions import Annotated

app = FastAPI()

class Patient(BaseModel):
    # name:str = Field(max_lenght=50)
    name:Annotated[str,Field(max_lenght=50,title="Name of the Patient",description="Give the name of patient is less then 50 char",example=['Ram','Shyam'])]
    age:int = Field(gt=0,lt=120)
    email:EmailStr
    weight:float = Field(gt=0)
    married:bool
    allergies:Optional[List[str]] = None
    contact_detail : Dict[str,str]


def insert_patient(patient_info):
    print(patient_info.name)
    print(patient_info.age)
    print(patient_info.email)
    print(patient_info.weight)
    print(patient_info.married)
    print(patient_info.allergies)
    print(patient_info.contact_detail["phone"])
    print('inserted')

patient_info = {'name':"Ram","age":30,"email":"ram@gmail.com","weight":10,"married" : True,"allergies":['Sneze','Dust'],"contact_detail":{"phone":"890909990","email":"ashutosh@gmail.com"}}
patient1 = Patient(**patient_info)
insert_patient(patient1)