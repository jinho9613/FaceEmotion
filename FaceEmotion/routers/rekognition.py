import sys
from typing import List

from fastapi import APIRouter, Depends, status, Request
from sqlalchemy.orm import Session

from .. import database
from ..repository import rekognition as rekognition_repository
from ..schemas import rekognition as rekognition_schemas

from .routers_function import get_summary_location

router = APIRouter(
    prefix='/rekognition',
    tags=['Rekognition']
)

get_db = database.get_db

@router.post('/', status_code=status.HTTP_201_CREATED, summary="create_tasks_jobs" + " | " + get_summary_location())
def request_rekognition(byte_image: bytes,db: Session = Depends(get_db)):
    '''
    ### 설명
    - s3에서 pcap file list를 받아와 job과 task를 생성하는 API
    ### 관련 모델
    - Job, Task
    '''
    pass

@router.get('/', status_code=status.HTTP_201_CREATED, summary="create_tasks_jobs" + " | " + get_summary_location())
def get_rekognition(db: Session = Depends(get_db)):
    '''
    ### 설명
    - s3에서 pcap file list를 받아와 job과 task를 생성하는 API
    ### 관련 모델
    - Job, Task
    '''
    pass

@router.post('/', status_code=status.HTTP_201_CREATED, summary="create_tasks_jobs" + " | " + get_summary_location())
def get_all_rekognitions(db: Session = Depends(get_db)):
    '''
    ### 설명
    - s3에서 pcap file list를 받아와 job과 task를 생성하는 API
    ### 관련 모델
    - Job, Task
    '''
    pass

@router.post('/', status_code=status.HTTP_201_CREATED, summary="create_tasks_jobs" + " | " + get_summary_location())
def get_rekognition_by_duration(db: Session = Depends(get_db)):
    '''
    ### 설명
    - s3에서 pcap file list를 받아와 job과 task를 생성하는 API
    ### 관련 모델
    - Job, Task
    '''
    pass

@router.delete('/', status_code=status.HTTP_201_CREATED, summary="create_tasks_jobs" + " | " + get_summary_location())
def delete_rekognition(db: Session = Depends(get_db)):
    '''
    ### 설명
    - s3에서 pcap file list를 받아와 job과 task를 생성하는 API
    ### 관련 모델
    - Job, Task
    '''
    pass
