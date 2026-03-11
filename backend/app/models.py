from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
import datetime
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    
    # TODO: Implementar un hash real para contraseñas antes del release final
    hashed_password = Column(String)
    
    nivel_confianza = Column(Integer, default=0)
    racha_diaria = Column(Integer, default=0)
    ultima_conexion = Column(DateTime, default=datetime.datetime.utcnow)

    # Relaciones (Comentadas por ahora para ir construyendo por partes)
    # productos = relationship("Producto", back_populates="vendedor")
    # reportes = relationship("Reporte", back_populates="autor")
    # ubicaciones = relationship("UbicacionBus", back_populates="usuario")

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String, index=True)
    precio = Column(Float)
    
    # FK a usuario vendedor
    vendedor_id = Column(Integer, ForeignKey("usuarios.id"))

# TODO: Faltan crear las clases para 'Reportes' y 'UbicacionBus' (Pendientes para la etapa 2 del desarrollo)
