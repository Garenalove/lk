from server import db as Base

session = Base.session
Base.query = session.query_property()

