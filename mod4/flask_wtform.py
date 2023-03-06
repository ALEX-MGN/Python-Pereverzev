from dataclasses import Field
from typing import Optional
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, ValidationError, Email

app = Flask(__name__)

def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        if len(str(field.data)) > max or len(str(field.data)) < min:
            raise ValidationError(message = message)
    return _number_length

class NumberLength:
    def __init__(self, min, max, message):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        if len(str(field.data)) > self.max or len(str(field.data)) < self.min:
            raise ValidationError(message = self.message)

class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberLength(10, 10,"Неверный формат номера телефона")])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone, name, address, index, comment = form.email.data, form.phone.data, form.name.data, form.address.data, form.index.data, form.comment.data
        return f"Successfully registered user {email} with phone +7{phone} for name {name} wtih address {address}({index}). Comment: {comment}"

    return f"Invalid input, {form.errors}" , 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)