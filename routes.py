from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db
from models import VLE, Consumer
from forms import LoginForm, ConsumerForm

# Create initial VLE user if none exists
def create_initial_vle():
    if not VLE.query.first():
        vle = VLE(username="admin", email="admin@suryaghar.com")
        vle.set_password("admin123")
        db.session.add(vle)
        db.session.commit()

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('consumer_form'))

    # Create initial VLE user
    create_initial_vle()

    form = LoginForm()
    if form.validate_on_submit():
        user = VLE.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('consumer_form'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/consumer-form', methods=['GET', 'POST'])
@login_required
def consumer_form():
    form = ConsumerForm()

    # Set choices for state and district from the form submission
    if request.method == 'POST':
        form.state.choices = [(request.form.get('state'), request.form.get('state'))]
        form.district.choices = [(request.form.get('district'), request.form.get('district'))]

    if form.validate_on_submit():
        consumer = Consumer(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            mobile=form.mobile.data,
            email=form.email.data,
            address=form.address.data,
            block=form.block.data,
            state=form.state.data,
            district=form.district.data,
            pin_code=form.pin_code.data,
            ca_number=form.ca_number.data,
            vle_id=current_user.id
        )
        db.session.add(consumer)
        db.session.commit()
        flash('Consumer data saved successfully!')
        return redirect(url_for('consumer_form'))

    return render_template('consumer_form.html', form=form)