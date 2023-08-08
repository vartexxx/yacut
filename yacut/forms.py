from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp


CUSTOM_ID_REGEX = r'^[a-zA-Z0-9]*$'


class URLForm(FlaskForm):
    original_link = URLField(
        label='Ваша длинная ссылка',
        description="https://example.com",
        validators=[DataRequired(message='Поле обязательно для заполнения')],
    )
    custom_id = URLField(
        label='Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Optional(),
            Regexp(
                CUSTOM_ID_REGEX,
                message='Идентификатор - только латинские буквы и цифры'
            )
        ],
    )
    submit = SubmitField('Создать')
