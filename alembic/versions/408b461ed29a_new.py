"""new

Revision ID: 408b461ed29a
Revises: d29ac16eb013
Create Date: 2022-11-23 15:16:48.091687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '408b461ed29a'
down_revision = 'd29ac16eb013'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_procedures_name', table_name='procedures')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_procedures_name', 'procedures', ['name'], unique=False)
    # ### end Alembic commands ###
