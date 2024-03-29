"""add designer and genre FK to games

Revision ID: 81c78e8e9bca
Revises: 0b04a862ca2b
Create Date: 2023-11-09 11:41:13.752544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81c78e8e9bca'
down_revision = '0b04a862ca2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.add_column(sa.Column('designer_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('genre_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_game_designer_id_designers'), 'designers', ['designer_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_game_genre_id_genres'), 'genres', ['genre_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_game_genre_id_genres'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_game_designer_id_designers'), type_='foreignkey')
        batch_op.drop_column('genre_id')
        batch_op.drop_column('designer_id')

    # ### end Alembic commands ###
