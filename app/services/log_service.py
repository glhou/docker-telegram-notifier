from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Log
from app.repositories import log_repository

ListLogsQuery = log_repository.ListLogsQuery


async def list_logs(session: AsyncSession, query: log_repository.ListLogsQuery):
    return await log_repository.list_logs(session, query)


async def list_available_services(session: AsyncSession):
    return await log_repository.list_services(session)


async def save_logs(session: AsyncSession, logs: list[Log]):
    for log in logs:
        session.add(log)
        await session.flush()
        await session.refresh(log)
    await session.commit()
    return logs
