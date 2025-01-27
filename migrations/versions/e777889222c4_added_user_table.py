"""Added User table

Revision ID: e777889222c4
Revises: b0768990294d
Create Date: 2022-02-06 18:44:33.508231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e777889222c4'
down_revision = 'b0768990294d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('password', sa.String(length=30), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('surname', sa.String(length=30), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
