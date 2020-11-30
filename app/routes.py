from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import NewArtistForm, LoginForm, RegistrationForm
from app.models import Artist, SongToPlaylist, Playlist, Song, User


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/artists')
def artists():
    artistList = Artist.query.all()
    return render_template('artists.html', title='Artists', artistList=artistList)

@app.route('/artist/<name>')
def artist(name):
    info = Artist.query.filter_by(name=name).first_or_404()
    print(info.name)
    return render_template("specArtist.html", info=info)

# @app.route('/newArtists')
# def newArtists():
#     return render_template('newArtists.html', title='New Artist', newArtist='newArtist')

@app.route('/newArtists', methods=['GET', 'POST'])
def newArtists():
    form = NewArtistForm()
    if form.validate_on_submit():
        flash('Artist info entered for name {}'.format(
            form.name.data, form.hometown.data, form.description.data))
        a = Artist(name=form.name.data, hometown=form.hometown.data)
        db.session.add(a)
        db.session.commit()
        return redirect(url_for("artists"))
    return render_template('newArtists.html',  title='New Artists', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/populate_db')
def populate_db():
    a1 = Artist(name="Billy Joel", hometown="Long Island, NY")
    a2 = Artist(name="Tash Sultana", hometown="Melbourne, Australia")
    a3 = Artist(name="Mac Miller", hometown="Pittsburgh, PA")
    a4 = Artist(name="Red Hot Chili Peppers", hometown="Los Angeles, CA")

    db.session.add_all([a1, a2, a3, a4])
    db.session.commit()

    s1 = Song(name="Zanzibar", artist=a1)
    s2 = Song(name="Mystik", artist=a2)
    s3 = Song(name="Woods", artist=a3)
    s4 = Song(name="The Longest Wave", artist=a4)

    db.session.add_all([s1, s2, s3, s4])
    db.session.commit()

    print(s1)

    p1 = Playlist(name="Rock")
    p2 = Playlist(name="Slow Jams")

    stp1 = SongToPlaylist(song=s1, playlist=p1)
    stp2 = SongToPlaylist(song=s2, playlist=p1)
    stp3 = SongToPlaylist(song=s3, playlist=p2)
    stp4 = SongToPlaylist(song=s4, playlist=p2)

    db.session.add_all([p1, p2, stp1, stp2, stp3, stp4])
    db.session.commit()

    print("Artist - Woods", s3.artist.name)
    return "Database has been populated."

@app.route('/reset_db')
def reset_db():
    # clear all data from all tables
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print('Clear table {}'.format(table))
        db.session.execute(table.delete())
    db.session.commit()
    populate_db()
    return "Reset Database"