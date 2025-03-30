from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def read_events():
    return {
        "results": [1,2,3]
    }