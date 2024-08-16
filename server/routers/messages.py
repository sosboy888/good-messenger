from fastapi import APIRouter
from .types import message
import uuid
from fastapi import Request, Depends
from dependencies import get_current_user

router = APIRouter()

insert_query = "INSERT INTO public.messages(uuid, user_id, to_id, text) VALUES($1, $2, $3, $4);"

fetch_query = """
SELECT * from public.messages where user_id = $1;
"""

fetch_query_received = """
SELECT * from public.messages where (to_id = $2 and user_id = $1) or (user_id = $2 and to_id = $1);
"""


@router.post("/messages/", tags=["messages"])
async def write(message: message.Message, request: Request, current_user : dict = Depends(get_current_user)):
    message_uuid = uuid.uuid4()
    result = await request.app.state.db.save_row(
        insert_query,
        message_uuid,
        message.user_id,
        message.to_id,
        message.text
    )
    
    return {"message":"create successful"}

@router.post("/messages/fetch/", tags=["messages"])
async def get_message(fetchRequest: message.FetchRequest, request: Request, current_user : dict = Depends(get_current_user)):
    from_id = fetchRequest.from_id
    to = fetchRequest.to
    result = await request.app.state.db.fetch_rows(
        fetch_query_received,
        from_id,
        to
    )
    return {"messages": result}