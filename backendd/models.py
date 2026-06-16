from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True) # Corregido: primary_key en minúsculas
    nombre = Column(String)

class Jugador(Base):
    __tablename__ = "jugadores"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

class Pago(Base):
    __tablename__ = "pagos"
    id = Column(Integer, primary_key=True, index=True)
    jugador_id = Column(Integer, ForeignKey("jugadores.id"))
    monto = Column(Float)
    mes = Column(String)
    estado = Column(String)

class Asistencia(Base):
    __tablename__ = "asistencias"
    id = Column(Integer, primary_key=True, index=True)
    jugador_id = Column(Integer, ForeignKey("jugadores.id"))
    fecha = Column(Date)
    estado = Column(String)