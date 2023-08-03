from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLForm(FlaskForm):
    original_link = URLField(
        label='Ваша длинная ссылка',
        validators=[DataRequired(message='Поле обязательно для заполнения'), Length(1, 256)],
    )
    custom_id = URLField(
        label='Ваш вариант короткой ссылки',
        validators=[Length(1, 16), Optional()],
    )
    submit = SubmitField('Создать')
