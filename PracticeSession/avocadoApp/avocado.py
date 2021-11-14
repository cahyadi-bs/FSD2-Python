"""
This is the people module and supports all the REST actions for the
avocado data
"""

from flask import make_response, abort
from config import db
from models import Avocado, AvocadoSchema

def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    avocado_item = Avocado.query.order_by(Avocado.avocado_id).all()



    # Serialize the data for the response
    avocado_schema = AvocadoSchema(many=True)
    data = avocado_schema.dump(avocado_item)
    return data

def read_one(avocado_id):
    """
    This function responds to a request for /api/people/{person_id}
    with one matching person from people
    :param person_id:   Id of person to find
    :return:            person matching id
    """
    # Get the person requested
    avocado_item = Avocado.query.filter(Avocado.avocado_id == avocado_id).one_or_none()

    # Did we find a person?
    if avocado_item is not None:

        # Serialize the data for the response
        avocado_schema = AvocadoSchema()
        data = avocado_schema.dump(avocado_item)
        return data

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            f"Avocado not found for Region Id: {avocado_id}",
        )

def read_limit(offset, limit):
    # Create the list of people from our data
    avocado_item = Avocado.query.order_by(Avocado.avocado_id).slice(offset,limit)



    # Serialize the data for the response
    avocado_schema = AvocadoSchema(many=True)
    data = avocado_schema.dump(avocado_item)
    return data


def create(avocado):
    """
    This function creates a new person in the people structure
    based on the passed in person data
    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    # Create a person instance using the schema and the passed in person
    schema = AvocadoSchema()
    new_avocado = schema.load(avocado, session=db.session)

    # Add the person to the database
    db.session.add(new_avocado)
    db.session.commit()

    # Serialize and return the newly created person in the response
    data = schema.dump(new_avocado)

    return data, 201

def update(avocado_id, avocado):
    """
    This function updates an existing person in the people structure
    :param person_id:   Id of the person to update in the people structure
    :param person:      person to update
    :return:            updated person structure
    """
    # Get the person requested from the db into session
    update_person = Avocado.query.filter(
        Avocado.avocado_id == avocado_id
    ).one_or_none()

    # Did we find an existing person?
    if update_person is not None:

        # turn the passed in person into a db object
        schema = AvocadoSchema()
        update = schema.load(avocado, session=db.session)

        # Set the id to the person we want to update
        update.avocado_id = update_person.avocado_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_person)

        return data, 200

    # Otherwise, nope, didn't find that person
    else:
        abort(404, f"Region Id: {avocado_id} Not Found")


def delete(avocado_id):
    """
    This function deletes a person from the people structure
    :param person_id:   Id of the person to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the person requested
    avocado = Avocado.query.filter(Avocado.avocado_id == avocado_id).one_or_none()

    # Did we find a person?
    if avocado is not None:
        db.session.delete(avocado)
        db.session.commit()
        return make_response(
            f"Avocado with region id {avocado_id} has been deleted", 200
        )

    # Otherwise, nope, didn't find that person
    else:
        abort(
            404,
            f"Region id : {avocado_id} not found",
        )

