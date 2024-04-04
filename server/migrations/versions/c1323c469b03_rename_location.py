"""rename location

Revision ID: c1323c469b03
Revises: 3a7809e0a8b8
Create Date: 2024-04-05 02:22:49.233553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1323c469b03'
down_revision = '3a7809e0a8b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('address', sa.String(), nullable=True))
    op.drop_column('departments', 'location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('location', sa.VARCHAR(), nullable=False))
    op.drop_column('departments', 'address')
    # ### end Alembic commands ###
