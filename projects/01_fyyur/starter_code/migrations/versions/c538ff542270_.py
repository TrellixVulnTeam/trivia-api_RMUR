"""empty message

Revision ID: c538ff542270
Revises: 8656a1441f2c
Create Date: 2020-10-19 16:28:18.160400

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c538ff542270'
down_revision = '8656a1441f2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('genres', postgresql.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'genres')
    # ### end Alembic commands ###
