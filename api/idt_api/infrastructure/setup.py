from idt_api.infrastructure.db.setup import setup_db

async def setup_infrastructure():
    await setup_db()
