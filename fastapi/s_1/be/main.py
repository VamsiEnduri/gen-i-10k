from fastapi import FastAPI
# pydantic fastapi data validation
from pydantic import BaseModel ,EmailStr,Field ,field_validator# class ,Filed


# creating my own class 
class regUser(BaseModel):
    name: str = Field(min_length=3,max_length=10)
    email: EmailStr
    age: int = Field(ge=18,le=35)
    ph_number: str= Field(min_length=10,max_length=15)
    skills: str
    password: str =Field(min_length=8,max_length=15)
    c_password: str=Field(min_length=8,max_length=15)



    @field_validator("name")
    @classmethod
    def validate_name(cls,value):
        if not value.isalpha() :
            raise ValueError("enter only chars")

        return   value  




    @field_validator("password")
    @classmethod 
    def validate_password(cls,p_str):
        if not any(char.isupper() for char in p_str):
            raise ValueError("password must be containg ateast 1 upper char")

        if not any(char.islower() for char in p_str):
            raise ValueError("password must be containg ateast 1 lower char")

        if not any(char.isdigit() for char in p_str):
            raise ValueError("password must be containg ateast 1 digit char")

        if not any(not char.isalnum() for char in p_str):
            raise ValueError("password must be containg ateast 1 special char")            
       

obj=FastAPI()

@obj.post("/register") #decorator
def reg_student(p:regUser): # type annotation
    print(p) 
    return {
        "msg":"stu reg successfully...."
    }
    # pass 
    # if new_stud["name"] != isalpha():
    #     raise "pass only str in name not nums r symbols"