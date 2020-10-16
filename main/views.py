from flask import request, render_template, redirect, url_for
from main.database import Urls
from hashlib import blake2b
from . import app, session
from main.forms import NameForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if request.method == 'POST':
        long_url = form.link.data
        res = session.query(Urls.hash_url).filter(Urls.real_url == long_url).first()

        if res:
            return redirect(url_for('short_link', long_url=long_url))

        hash_url = blake2b(long_url.encode()).hexdigest()[:5]
        session.add(Urls(long_url, hash_url, 0))
        session.commit()

        return redirect(url_for('short_link', long_url=long_url))

    return render_template('index.html', form=form)


@app.route('/short_link')
def short_link():
    long_url = request.args.get('long_url')
    res = session.query(Urls.hash_url, Urls.count).filter(Urls.real_url == long_url).first()
    hash_url = res.hash_url
    count = res.count
    return render_template('short_link.html', hash_url=hash_url, count=count)


@app.route('/<hash_url>')
def redirect_url(hash_url):
    res = session.query(Urls.real_url).filter(Urls.hash_url == hash_url)
    line = res.first()
    if line:
        res.update({Urls.count: Urls.count + 1})
        session.commit()
        return redirect(line.real_url)
    return render_template('error.html')
