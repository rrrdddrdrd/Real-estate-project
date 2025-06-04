from sqlalchemy import MetaData, DateTime, func, BIGINT, BigInteger, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, JSON




class Base(DeclarativeBase):
    created: Mapped[MetaData] = mapped_column(DateTime, default=func.now())



class Registration(Base):
    __tablename__ = 'registration_people'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_people: Mapped[int] = mapped_column(BigInteger)
    nick: Mapped[str] = mapped_column(nullable=True)
    fio: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
    like_status: Mapped[dict] = mapped_column(JSON, nullable=True)

class RegistrationHouse(Base):
    __tablename__ = 'registration_house'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[int] = mapped_column(nullable=True)
    address: Mapped[str] = mapped_column(nullable=True)
    repair: Mapped[str] = mapped_column(nullable=True)
    area: Mapped[str] = mapped_column(nullable=True)
    building_type: Mapped[str] = mapped_column(nullable=True)
    gas_supply: Mapped[str] = mapped_column(nullable=True)
    photo: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[str] = mapped_column(nullable=True)
    fio_buy: Mapped[str] = mapped_column(nullable=True)


class Status(Base):
    __tablename__ = 'registration_status'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_house: Mapped[int] = mapped_column(BigInteger)
    like: Mapped[int] = mapped_column(nullable=True)
    like_nick: Mapped[str] = mapped_column(nullable=True)

    watch: Mapped[int] = mapped_column(nullable=True)
