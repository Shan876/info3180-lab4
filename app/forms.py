  
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

class UploadForm(FlaskForm):
    file_upload = FileField('Image', validators=[FileRequired(), 
    FileAllowed(['jpeg','jpg','png'], 'Images only!')])