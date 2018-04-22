from sqlalchemy.orm import subqueryload, Query
from typing import Optional, List
from datetime import datetime
from ..database import session
from ..models.computer import Computer
from ..models.user import User
from ..models.license import License
from ..models.product import Product
from ..models.role import Role

def query_computers(mask: Optional[str] = None, deleted: bool = False) -> Query:
    query = session.query(Computer).filter_by(deleted=deleted)
    if mask:
        query = query.filter_by(mask=mask)
    return query.order_by(Computer.mask.asc())


def query_users(email: Optional[str] = None,
                password: Optional[str] = None,
                computers: Optional[List[Computer]] = None,
                licenses: Optional[List[License]] = None,
                computers_limit: Optional[int] = None,
                deleted: bool = False) -> Query:
    query = session.query(User).filter_by(deleted=deleted)
    if email:
        query.filter_by(email=email)
    if password:
        query.filter_by(password=password)
    if computers:
        query.filter_by(computers=computers)
    if licenses:
        query.filter_by(licenses=licenses)
    if computers_limit:
        query.filter_by(computers_limit=computers_limit)
    return query.options(
        subqueryload(User.roles),
        subqueryload(User.computers),
        subqueryload(User.licenses)
    ).order_by(User.email.asc())


def query_addons(name: Optional[str] = None,
                 description: Optional[str] = None,
                 cost: Optional[float] = None,
                 period: Optional[int] = None,
                 slug: Optional[str] = None,
                 deleted: bool = False) -> Query:
    query = session.query(Product).filter_by(deleted=deleted)
    if name:
        query.filter_by(name=name)
    if description:
        query.filter_by(description=description)
    if cost:
        query.filter_by(cost=cost)
    if period:
        query.filter_by(period=period)
    if slug:
        query.filter_by(slug=slug)
    return query.order_by(Product.name.asc())


def query_license(addon: Optional[Product] = None,
                  end_time: Optional[datetime] = None,
                  deleted: bool = False) -> Query:
    query = session.query(License).filter_by(deleted=deleted)
    if addon:
        query.filter_by(addon=addon)
    if end_time:
        query.filter_by(end_time=end_time)
    return query.options(subqueryload(License.addon)).order_by(License.end_time.asc())


def computer(mask: Optional[str] = None, deleted: bool = False) -> Optional[Computer]:
    return query_computers(
        mask=mask,
        deleted=deleted
    ).first()


def computers(deleted: bool = False) -> List[Computer]:
    return query_computers(
        deleted=deleted
    ).all()


def user(email: Optional[str] = None,
         password: Optional[str] = None,
         computers: Optional[List[Computer]] = None,
         licenses: Optional[List[License]] = None,
         computers_limit: Optional[int] = None,
         deleted: bool = False) -> User:
    return query_users(
        email=email,
        password=password,
        computers=computers,
        licenses=licenses,
        computers_limit=computers_limit,
        deleted=deleted
    ).first()


def users(computers_limit: Optional[int] = None,
          deleted: bool = False) -> List[User]:
    return query_users(
        computers_limit=computers_limit,
        deleted=deleted
    ).all()


def addon(name: Optional[str] = None,
          description: Optional[str] = None,
          cost: Optional[float] = None,
          period: Optional[int] = None,
          slug: Optional[str] = None,
          deleted: bool = False) -> Product:
    return query_addons(
        name=name,
        description=description,
        cost=cost,
        period=period,
        slug=slug,
        deleted=deleted
    ).first()


def addons(description: Optional[str] = None,
           cost: Optional[float] = None,
           period: Optional[int] = None,
           deleted: bool = False) -> List[Product]:
    return query_addons(
        description=description,
        cost=cost,
        period=period,
        deleted=deleted
    ).all()


def license(addon: Optional[Product] = None, end_time: Optional[datetime] = None, deleted: bool = False) -> License:
    return query_license(
        addon=addon,
        end_time=end_time,
        deleted=deleted
    ).first()


def licenses(addon: Optional[Product] = None,
             end_time: Optional[datetime] = None,
             deleted: bool = False) -> List[License]:
    return query_license(
        addon=addon,
        end_time=end_time,
        deleted=deleted
    ).all()

