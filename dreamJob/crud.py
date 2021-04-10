from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

import models, schemas


def create_job(db: Session, job: schemas.Job):
    try:
        db_job = models.Job(title=job.title, experience=job.experience,
                             description=job.description, no_of_vacancies=job.no_of_vacancies)
        db.add(db_job)
        db.commit()
        db.refresh(db_job)
        print(db_job)
        return db_job

    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unexpected Error Occurred")



def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(models.Job).offset(skip).limit(limit).all()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unexpected Error Occurred")


def update_job(db: Session, job: schemas.Job, id: int):
    try:
        db_job = db.query(models.Job).filter(models.Job.id ==id).first()

        db_job.title = job.title
        db_job.experience = job.experience
        db_job.description = job.description
        db_job.no_of_vacancies = job.no_of_vacancies

        db.commit()
        db.refresh(db_job)
        return db_job

    except Exception as e:
        print(e)
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unexpected Error Occurred")


def delete_job(db: Session, id: int):
    try:
        db.query(models.Job).filter(models.Job.id == id).delete(synchronize_session=False)
        db.commit()
        return None

    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unexpected Error Occurred")


def get_job(db: Session, id: int):
    status_code = 0
    detail = ""
    try:
        db_job = db.query(models.Job).filter(models.Job.id == id).first()
        if db_job is None:
            status_code=status.HTTP_404_NOT_FOUND
            detail="Job not found"
        else:
            return db_job

    except Exception as e:
        print(e)
        status_code=status.HTTP_400_BAD_REQUEST
        detail="Unexpected Error Occurred"

    raise HTTPException(status_code=status_code, detail=detail)


def apply_job(db: Session, id: int):
    try:
        db_job = models.Application(job_id=id)
        db.add(db_job)
        db.commit()
        db.refresh(db_job)
        return db_job

    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Unexpected Error Occurred")
