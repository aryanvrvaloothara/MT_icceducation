from typing import List, Optional
from pydantic import BaseModel


class Job(BaseModel):
    title: str = None
    experience: str = None
    description: str = None
    no_of_vacancies: int = None

    class Config:
        orm_mode = True


class ReadJob(Job):
    id: int

    class Config:
        orm_mode = True


class ReadApplication(BaseModel):
    id: int
    job_id: int

    class Config:
        orm_mode = True