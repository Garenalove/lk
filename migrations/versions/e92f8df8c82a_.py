"""empty message

Revision ID: e92f8df8c82a
Revises: 76599f8b7467
Create Date: 2018-04-19 15:45:22.580688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e92f8df8c82a'
down_revision = '76599f8b7467'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_', sa.Column('balance', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_', 'balance')
    # ### end Alembic commands ###