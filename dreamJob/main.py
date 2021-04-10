from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette import status

import crud, models, schemas
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/jobs/", response_model=List[schemas.ReadJob])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_jobs(db, skip=skip, limit=limit)


@app.post("/jobs/", response_model=schemas.ReadJob, status_code=status.HTTP_201_CREATED)
def create_job(job: schemas.Job, db: Session = Depends(get_db)):
    return crud.create_job(db=db, job=job)


@app.put("/jobs/{id}", response_model=schemas.Job)
def update_job(job: schemas.Job, id: int, db: Session = Depends(get_db)):
    return crud.update_job(db=db, job=job, id=id)


@app.delete("/jobs/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(id: int, db: Session = Depends(get_db)):
    return crud.delete_job(db=db, id=id)


@app.get("/jobs/{id}", response_model=schemas.ReadJob, status_code=status.HTTP_200_OK)
def read_job_by_id(id: int, db: Session = Depends(get_db)):
    return crud.get_job(db, id=id)


@app.post("/apply/{id}", response_model=schemas.ReadApplication, status_code=status.HTTP_201_CREATED)
def apply_job(id: int, db: Session = Depends(get_db)):
    return crud.apply_job(db=db, id=id)
