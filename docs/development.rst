Development
==================================================

Development Structure
****************************************

The skeleton is broken down into an MVC paradigm. Views, Controllers and Models. Unfortunetly due to Flask-Classy's class name, it would be unconventional to rename the upper levels into folders ``Views``, ``Controllers``, and ``Models``. Instead the following structure is used:

:models: The models folder stores all the models for the application.
:templates: The templates folder stores all the view controllers. These are where the HTML templates that flask uses to render are stored.
:views: These are the view controllers. They are responsible for serving content to the client and using the templates to generate these responses.


Adding a Model
****************************************

To add a new model, make a new file in models named the same as the name of the class for the model. 

Use parts of the following sample to create your new model:

.. code-block:: python

    from Application import db

    many_to_many_helper = db.Table('many_to_many_helper',
        db.Column('class1_id', db.Integer, db.ForeignKey('class1.id')),
        db.Column('class2_id', db.Integer, db.ForeignKey('class2.id'))
    )

    class Class1(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        text = db.Column(db.Text())
        float = db.Column(db.Float())
        string = db.Column(db.String(255), unique=True)
        _hidden_string = db.Column(db.String(255))
        boolean = db.Column(db.Boolean())
        date = db.Column(db.DateTime())
        
        # Many to One relationship
        related_item_id = db.Column(db.Integer, db.ForeignKey('class2.id'))
        related_item = db.relationship('Class2')

        # Many to Many relationship
        related_items = db.relationship('Class2', secondary=many_to_many_helper, lazy='dynamic')

        @property
        def hidden_string(self):
            return self.hidden_string + 'Appended'


.. code-block:: python

    from Application import db
    from .Class1 import many_to_many_helper

    class Class2(db.Model):
        id = db.Column(db.Integer, primary_key=True)

        # One to Many relationship
        related_items = db.relationship('Class1',lazy='dynamic')

        # Many to Many relationship
        related_items = db.relationship('Class1', secondary=many_to_many_helper, lazy='dynamic')

        @property
        def hidden_string(self):
            return self.hidden_string + 'Appended'

Adding a View
****************************************

To add a new view, make a new file in views named the same as the name of the class for the view. 

Use parts of the following sample to create the view.

.. code-block:: python

    from Application import app
    from flask import render_template, url_for, redirect
    from flask.ext.classy import FlaskView, route


    class ClassyViewExample(FlaskView):
        route_base = '/classy-view/'

        def index(self):
            return redirect(url_for('ClassViewExample:get', url_data='Hello World'))

        # Go to /classy-view/blah/
        def get(self, url_data):
            return render_template('index.html', content=url_data)

        # Go to /classy-view/custom-route/
        # Route will also take parameters similar to how flask does it
        # ie you can do <int:urlthing>
        @route('/custom-route/')
        def custom_route(self):
            return render_template('index.html', content="Custom Route!")


    ClassyViewExample.register(app)


Adding a Template
****************************************

To add a template that the ``render_template`` function from flask can render, simply make a new file in the ``templates`` folder. `The existing templates make use of Jinja's subtemplates/subclass system. <http://flask.pocoo.org/docs/0.10/templating/>`_

