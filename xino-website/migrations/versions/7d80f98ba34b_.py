"""empty message

Revision ID: 7d80f98ba34b
Revises: 
Create Date: 2022-08-22 19:38:22.347830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d80f98ba34b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=True),
    sa.Column('answer', sa.String(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.Column('imgur', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('school', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('question', sa.Integer(), nullable=True),
    sa.Column('answer_time', sa.DateTime(), nullable=False),
    sa.Column('restricted', sa.String(), nullable=True),
    sa.Column('ip', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('answer_time', sa.DateTime(), nullable=False),
    sa.Column('answer', sa.String(), nullable=True),
    sa.Column('question', sa.Integer(), nullable=True),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('logs')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    op.drop_table('questions')
    # ### end Alembic commands ###
