"""delete user model

Revision ID: 99e75884859e
Revises: 07db183469ec
Create Date: 2023-08-05 13:48:28.019631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99e75884859e'
down_revision = '07db183469ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_id', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_constraint('event_created_by_fkey', 'event', type_='foreignkey')
    op.drop_constraint('location_created_by_fkey', 'location', type_='foreignkey')
    op.drop_constraint('resource_created_by_fkey', 'resource', type_='foreignkey')
    op.drop_table('user')
    op.alter_column('event', 'created_by',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    op.create_index(op.f('ix_event_created_by'), 'event', ['created_by'], unique=False)
    op.alter_column('location', 'created_by',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    op.create_index(op.f('ix_location_created_by'), 'location', ['created_by'], unique=False)
    op.alter_column('resource', 'created_by',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
    op.create_index(op.f('ix_resource_created_by'), 'resource', ['created_by'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('resource_created_by_fkey', 'resource', 'user', ['created_by'], ['id'], ondelete='CASCADE')
    op.drop_index(op.f('ix_resource_created_by'), table_name='resource')
    op.alter_column('resource', 'created_by',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.create_foreign_key('location_created_by_fkey', 'location', 'user', ['created_by'], ['id'], ondelete='CASCADE')
    op.drop_index(op.f('ix_location_created_by'), table_name='location')
    op.alter_column('location', 'created_by',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.create_foreign_key('event_created_by_fkey', 'event', 'user', ['created_by'], ['id'], ondelete='CASCADE')
    op.drop_index(op.f('ix_event_created_by'), table_name='event')
    op.alter_column('event', 'created_by',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=False)
    op.create_index('ix_user_id', 'user', ['id'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    # ### end Alembic commands ###