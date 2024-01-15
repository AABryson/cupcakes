"""migrate

Revision ID: 26b7abda1d02
Revises: 
Create Date: 2024-01-07 21:50:24.040183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26b7abda1d02'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cupcakes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('flavor', sa.Text(), nullable=False),
    sa.Column('size', sa.Text(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=False),
    sa.Column('image', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cupcakes')
    # ### end Alembic commands ###
