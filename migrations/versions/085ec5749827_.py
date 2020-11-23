"""empty message

Revision ID: 085ec5749827
Revises: 
Create Date: 2020-11-19 10:23:57.843046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '085ec5749827'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('hometown', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_artist_hometown'), 'artist', ['hometown'], unique=True)
    op.create_index(op.f('ix_artist_name'), 'artist', ['name'], unique=True)
    op.create_table('playlist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_playlist_name'), 'playlist', ['name'], unique=True)
    op.create_table('song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_song_name'), 'song', ['name'], unique=True)
    op.create_table('song_to_playlist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=True),
    sa.Column('playlist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlist.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['song.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('song_to_playlist')
    op.drop_index(op.f('ix_song_name'), table_name='song')
    op.drop_table('song')
    op.drop_index(op.f('ix_playlist_name'), table_name='playlist')
    op.drop_table('playlist')
    op.drop_index(op.f('ix_artist_name'), table_name='artist')
    op.drop_index(op.f('ix_artist_hometown'), table_name='artist')
    op.drop_table('artist')
    # ### end Alembic commands ###