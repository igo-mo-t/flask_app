"""empty message

Revision ID: d6dd3294f53b
Revises: 4784ca95c567
Create Date: 2022-10-27 21:50:50.294519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6dd3294f53b'
down_revision = '4784ca95c567'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('users', 'password_hash',
                    existing_type=sa.VARCHAR(length=100),
                    type_=sa.String(length=1000),
                    )


def downgrade():
    op.alter_column('users', 'password_hash',
                    existing_type=sa.String(length=1000),
                    type_=sa.VARCHAR(length=100),
                    )
