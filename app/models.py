from datetime import datetime
from app import db
#
# from werkzeug.security import generate_password_hash, check_password_hash


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    hometown = db.Column(db.String(120), index=True, unique=True)
    songs = db.relationship("Song", backref="artist", lazy="dynamic")

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey("artist.id"))
    name = db.Column(db.String(64), index=True, unique=True)
    song_to_playlists = db.relationship("SongToPlaylist", backref="song", lazy="dynamic")

    def __repr__(self):
        return "<Song {} - {}>".format(self.id, self.name)

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    song_to_playlists = db.relationship("SongToPlaylist", backref="playlist", lazy="dynamic")

class SongToPlaylist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("song.id"))
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlist.id"))