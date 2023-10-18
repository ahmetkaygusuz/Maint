from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from database import get_session
from models.workCenter_models import WorkCenter
from models.workCenter_schema import WorkCenterCreate, WorkCenterDTO


router = APIRouter()


# get
@router.get("/api/workcenter/{id}", response_model=WorkCenterDTO)
async def get(*, session: Session = Depends(get_session), id: int):
    rec = session.get(WorkCenter, id)
    if not rec:
        raise HTTPException(404)
    return rec


@router.get("/api/workcenter/", response_model=List[WorkCenterDTO])
async def getAll(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    return session.exec(select(WorkCenter).offset(offset).limit(limit)).all()


# yeni kayıt
@router.post("/api/workcenter/", response_model=WorkCenterDTO)
async def create(*, session: Session = Depends(get_session), model: WorkCenterCreate):
    rec = WorkCenter().from_orm(model)
    session.add(rec)
    session.commit()
    session.refresh(rec)
    return rec


# update kayıt
@router.patch("/api/workcenter/{id}", response_model=WorkCenterDTO)
async def update(
    *, session: Session = Depends(get_session), id: int, model: WorkCenterCreate
):
    rec = session.get(WorkCenter, id)
    if not rec:
        raise HTTPException(404)
    rec.name = model.name
    rec.code = model.code
    session.add(rec)
    session.commit()
    session.refresh(rec)
    return rec


# delete kayıt
@router.delete("/api/workcenter/{id}")
async def delete(*, session: Session = Depends(get_session), id: int):
    rec = session.get(WorkCenter, id)
    if not rec:
        raise HTTPException(404)
    session.delete(rec)
    session.commit()
    session.refresh(rec)
    return {"ok": True}
