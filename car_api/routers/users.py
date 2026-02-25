from fastapi import APIRouter, status

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
async def list_users():
    return {
        "users": [
           {
            "id": 1,
            "email": "john.doe@example.com"
           },
           {
            "id": 2,
            "email": "jane.smith@example.com"
           },
           {
            "id": 3,
            "email": "bob.johnson@example.com"
           },
        ]
    }