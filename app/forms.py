from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    image = FileField('image', validators = [FileRequired(), FileAllowed(['jpg', 'png'])])