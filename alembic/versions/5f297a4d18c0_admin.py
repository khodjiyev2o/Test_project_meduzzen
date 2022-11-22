"""admin

Revision ID: 5f297a4d18c0
Revises: 788860b42f07
Create Date: 2022-11-22 00:01:25.303509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f297a4d18c0'
down_revision = '788860b42f07'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('admin', sa.Boolean(), nullable=True))
    op.drop_index('ix_workers_name', table_name='workers')
    op.drop_column('workers', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('workers', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_workers_name', 'workers', ['name'], unique=False)
    op.drop_column('users', 'admin')
    # ### end Alembic commands ###