from flask import flash, redirect, render_template

from . import BASE_URL, app, db
from .error_handlers import check_inique_short_url
from .forms import URLForm
from .models import URLMap
from .utils import check_symbols, get_unique_short_url


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data

        if check_inique_short_url(custom_id):
            flash(f'Имя {custom_id} уже занято!')
            return render_template('yacut/main.html', form=form)
        if custom_id and not check_symbols(custom_id):
            flash('Допустимые символы: A-z, 0-9')
            return render_template('yacut/main.html', form=form)

        if custom_id is None:
            custom_id = get_unique_short_url()

        url = URLMap(
            original=original_link,
            short=custom_id,
        )
        db.session.add(url)
        db.session.commit()
        return render_template(
            'yacut/main.html',
            form=form,
            short_link=BASE_URL + url.short,
            original_link=url.original
        )
    return render_template('yacut/main.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def redirect_to_url_view(short):
    url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url.original)