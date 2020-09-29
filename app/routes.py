from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import NewArtistForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gabe'}
    return render_template('index.html', title='Home', user=user)

@app.route('/artists')
def artists():
    artistList = ['Quail', 'RHCP', 'Joji']
    return render_template('artists.html', title='Artists', artistList=artistList)

@app.route('/specArtist')
def specArtist():
    info = {
        "name": "Red Hot Chili Peppers",
        "hometown": "LA",
        "description": "Red Hot Chili Peppers are an American rock band formed in Los Angeles in 1983. Their music incorporates elements of alternative rock, funk, punk rock and psychedelic rock. The band consists of vocalist Anthony Kiedis, guitarist John Frusciante, bassist Flea, and drummer Chad Smith.",
        "events": ["MSG - December 4th", "PNC Arts Center - January 7th"]
    }
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
        info = {
            "name": form.name.data,
            "hometown": form.hometown.data,
            "description": form.description.data
        }
        return render_template("specArtist.html", info=info)
    return render_template('newArtists.html',  title='New Artists', form=form)
