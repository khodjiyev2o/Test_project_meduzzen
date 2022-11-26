"""new

Revision ID: 93cc4067863c
Revises: 06000157e576
Create Date: 2022-11-24 13:18:39.411522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93cc4067863c'
down_revision = '06000157e576'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_appointments_user_id'), 'appointments', ['user_id'], unique=False)
    op.create_foreign_key(None, 'appointments', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'appointments', type_='foreignkey')
    op.drop_index(op.f('ix_appointments_user_id'), table_name='appointments')
    op.drop_column('appointments', 'user_id')
    # ### end Alembic commands ###