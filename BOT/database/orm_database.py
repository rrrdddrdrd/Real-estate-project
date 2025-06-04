from database.module import Registration, RegistrationHouse, Status
from sqlalchemy import update


from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

async def orm_add_house(session: AsyncSession, data):
    obj = RegistrationHouse(
        title=data['title'],
        price=data['price'],
        address=data['address'],
        repair=data['repair'],
        area=data['area'],
        building_type=data['building_type'],
        gas_supply=data['gas_supply'],
        photo=data['photo'],
        status=data['status'],
        fio_buy=data['fio_buy']
    )
    session.add(obj)
    await session.commit()
    await session.refresh(obj)
    return obj.id

async def orm_get_start(session: AsyncSession):
    query = (
        select(RegistrationHouse)
        .where(RegistrationHouse.status != 'продан')
    )
    result = await session.execute(query)
    return result.scalars().all()


async def orm_get_start_1(session: AsyncSession):
    query = (
        select(RegistrationHouse)
        .where(RegistrationHouse.status != 'продано')
    )
    result = await session.execute(query)
    return result.scalars().all()

async def orm_get_start_12(session: AsyncSession):
    query = select(RegistrationHouse)
    result = await session.execute(query)
    return result.scalars().all()

async def orm_add_status(session: AsyncSession, data):
    obj = Status(
        id_house=data['id_house'],
        like=data['like'],
        like_nick=data['like_nick'],
        watch=data['watch'],
    )
    session.add(obj)
    await session.commit()


async def orm_add_people(session: AsyncSession, data):
    query = select(Registration).where(Registration.id_people == data['id_people'])
    result = await session.execute(query)
    existing = result.scalar_one_or_none()

    if existing:
        return False

    obj = Registration(
        id_people=data['id_people'],
        nick=data['nick'],
        fio=data['fio'],
        phone=data['phone'],
        like_status=data['like_status'],
    )
    session.add(obj)
    await session.commit()
    return True

async def orm_increment_status(session: AsyncSession, product_id: int, field: str):
    if field not in {"like", "watch"}:
        raise ValueError("Можно увеличивать только поля 'like' или 'watch'.")

    query = (
        update(Status)
        .where(Status.id_house == product_id)
        .values({field: getattr(Status, field) + 1})
    )

    await session.execute(query)
    await session.commit()

async def add_to_like_people(session: AsyncSession, id_people: int, key: str, value: any):
    # Загружаем нужный объект
    result = await session.execute(select(Registration).where(Registration.id_people == id_people))
    status = result.scalar_one_or_none()

    if status:
        if status.like_status is None:
            status.like_status = {}

        status.like_status[key] = value  # добавляем переданную пару ключ-значение

        # На всякий случай уведомим SQLAlchemy, что поле изменилось
        from sqlalchemy.orm.attributes import flag_modified
        flag_modified(status, "like_status")

        await session.commit()
        print(f"Добавлено в watch: {key} = {value}")
    else:
        print("Объект не найден.")


async def orm_set_status_sold(session: AsyncSession, product_id: int, text):
    query = (
        update(RegistrationHouse)
        .where(RegistrationHouse.id == product_id)
        .values(status='продан').values(fio_buy=text)
    )
    await session.execute(query)
    await session.commit()


async def orm_append_to_status(session: AsyncSession, product_id: int, append_text: str):
    # Получаем текущее значение поля status
    result = await session.execute(
        select(Status.like_nick).where(Status.id_house == product_id)
    )
    current_status = result.scalar_one_or_none() or ""

    # Добавляем текст к текущему значению
    new_status = f"{current_status.strip()} {append_text}".strip()

    # Обновляем в базе
    query = (
        update(Status)
        .where(Status.id_house == product_id)
        .values(like_nick=new_status)
    )
    await session.execute(query)
    await session.commit()


async def orm_get_start_id_life(session: AsyncSession, id_people):
    query = select(RegistrationHouse).where(RegistrationHouse.id == id_people)
    result = await session.execute(query)
    registration = result.scalar()

    if registration:
        record = {column: getattr(registration, column) for column in registration.__table__.columns.keys()}
        return record

    return None


async def orm_get_start_id_people(session: AsyncSession, id_people):
    query = select(Registration).where(Registration.id_people == id_people)
    result = await session.execute(query)
    registration = result.scalar()

    if registration:
        record = {column: getattr(registration, column) for column in registration.__table__.columns.keys()}
        return record

    return None


async def orm_get_start_id_status(session: AsyncSession, id_house):
    query = select(Status).where(Status.id_house == id_house)
    result = await session.execute(query)
    registration = result.scalar()

    if registration:
        record = {column: getattr(registration, column) for column in registration.__table__.columns.keys()}
        return record

    return None

def categorize_house(title: str) -> str:
    title = title.lower()
    if 'участок' in title:
        return 'Участок'
    elif 'дом' in title:
        return 'Дом'
    elif 'квартира' in title:
        return 'Квартира'
    else:
        return 'Другое'


async def orm_get_filtered(session: AsyncSession, category=None, max_price=None):
    stmt = select(RegistrationHouse)
    if max_price:
        stmt = stmt.where(RegistrationHouse.price <= int(max_price))
    result = await session.execute(stmt)
    all_houses = result.scalars().all()

    if category:
        # Фильтруем вручную по title
        filtered = [h for h in all_houses if categorize_house(h.title) == category]
        return filtered
    return all_houses
