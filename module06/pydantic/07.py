import requests
from pydantic import BaseModel, IPvAnyAddress, Field, ConfigDict
from pydantic.alias_generators import to_camel, to_pascal, to_snake

v = "years_of_experience"

print(to_camel(v))
print(to_pascal(v))
print(to_camel(v))


class Person(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)
    years_of_experience: int
    first_name: str


person = """
        {   
            "yearsOfExperience": 20, 
            "firstName": "Isaac",
            "lastName": "Newton",
            "age": 44
        }
        """

p = Person.model_validate_json(person)
print(p)
p.first_name
print(p.model_dump_json(by_alias=True))