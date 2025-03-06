from fastapi.responses import JSONResponse
from idt_api.domain.errors.influencer_not_found import InfluencerNotFound


async def influencer_not_found_handler(_, exc: InfluencerNotFound):
    return JSONResponse(
        status_code=404,
        content={
            "message": str(exc),
            "code": exc.code
        }
    )