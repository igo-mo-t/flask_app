"""empty message

Revision ID: e78fe2abf0dc
Revises: d6dd3294f53b
Create Date: 2022-10-28 00:31:31.723008

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e78fe2abf0dc'
down_revision = 'd6dd3294f53b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password_hash',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=1000),
               nullable=False)
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100), nullable=True))
    op.alter_column('users', 'password_hash',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=1000),
               nullable=True)
    # ### end Alembic commands ###
