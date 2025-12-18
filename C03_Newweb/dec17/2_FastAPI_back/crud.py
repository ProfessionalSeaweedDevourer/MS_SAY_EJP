from sqlalchemy.orm import Session
import models, schemas

def get_menus(db: Session):
    return db.query(models.Menu).all()

def create_menu(db: Session, menu: schemas.MenuCreate):
    db_menu = models.Menu(
        m_name=menu.m_name,
        m_price=menu.m_price,
        m_desc=menu.m_desc
    )
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu

def delete_menu(db: Session, m_name: str):
    db_menu = db.query(models.Menu).filter(models.Menu.m_name == m_name).first()
    if db_menu:
        db.delete(db_menu)
        db.commit()
        return True
    return False