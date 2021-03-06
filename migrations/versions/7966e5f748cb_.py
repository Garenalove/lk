"""empty message

Revision ID: 7966e5f748cb
Revises: 5ce54342eab4
Create Date: 2018-04-27 14:09:32.626267

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7966e5f748cb'
down_revision = '5ce54342eab4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('release',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=False),
    sa.Column('version', sa.String(length=255), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(length=255), nullable=False),
    sa.Column('can_be_sell', sa.Boolean(), nullable=False),
    sa.Column('product_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('path')
    )
    op.drop_column('product', 'release')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('release', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False))
    op.drop_table('release')
    # ### end Alembic commands ###
