"""add unique name for designer and genre

Revision ID: 2ac1619a423c
Revises: 6bee64d58278
Create Date: 2023-11-15 16:15:52.625622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ac1619a423c'
down_revision = '6bee64d58278'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('designers', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_designers_name'), ['name'])

    with op.batch_alter_table('genres', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_genres_name'), ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('genres', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_genres_name'), type_='unique')

    with op.batch_alter_table('designers', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_designers_name'), type_='unique')

    # ### end Alembic commands ###
