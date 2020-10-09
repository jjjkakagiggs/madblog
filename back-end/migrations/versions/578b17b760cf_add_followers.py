"""add followers

Revision ID: 578b17b760cf
Revises: bff64a27bc9b
Create Date: 2020-09-30 15:10:25.842578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '578b17b760cf'
down_revision = 'bff64a27bc9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###