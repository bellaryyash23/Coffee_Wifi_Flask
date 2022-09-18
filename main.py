from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
from csv import writer

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message="This field is required")])
    location = StringField("Location as URL on Google Maps", validators=[URL(message="Enter Proper URL"),
                                                                         DataRequired(
                                                                             message="This field is required")])
    open_time = StringField("Open Time e.g: 8AM", validators=[DataRequired(message="This field is required")])
    close_time = StringField("Close Time e.g:8PM", validators=[DataRequired(message="This field is required")])
    coffee_rating = SelectField("Coffee rating", choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
                                validators=[DataRequired(message="This field is required")])
    wifi_rating = SelectField("Wifi Rating",
                              choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                              validators=[DataRequired(message="This field is required")])
    power_outlet = SelectField("Power Outlet Rating",
                               choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                               validators=[DataRequired(message="This field is required")])
    submit = SubmitField("Submit")


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        new_cafe = [form.cafe.data.title(), form.location.data, form.open_time.data, form.close_time.data,
                    form.coffee_rating.data, form.wifi_rating.data, form.power_outlet.data]
        with open("cafe-data.csv", encoding="utf8", mode="a", newline="") as csv_file:
            writer_obj = writer(csv_file)
            writer_obj.writerow(new_cafe)
        csv_file.close()
        return render_template("index.html")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        csv_file.close()
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
