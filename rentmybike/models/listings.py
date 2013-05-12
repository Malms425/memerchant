from __future__ import unicode_literals
import logging

from sqlalchemy.orm.exc import NoResultFound

from rentmybike.db import Session
from rentmybike.db.tables import listings, rentals
from rentmybike.models import Base, User


logger = logging.getLogger(__name__)


class Listing(Base):

    __table__ = listings

    def rent_to(self, user, card_uri=None):

        account = user.balanced_account

        if not card_uri:
            if not account.cards.count():
                raise Exception('No card on file')
            if not user.has_password:
                raise Exception('Anonymous users must specify a card')

        # this will throw balanced.exc.HTTPError if it fails
        debit = account.hold(self.price * 100, source_uri=card_uri)

        rental = Rental(buyer_guid=user.guid,
            debit_uri=debit.uri, bike_guid=self.id)

        Session.add(rental)
        return rental

    @property
    def title(self):
        return {
            'cornerstore': 'Corner Store',
            'hybrid': 'Cozmic CX 1.0',
            'road': 'Myata Vintage Road Bike',
            'touring': 'Roberts Cycles Clubman',
            }[self.bike_type]

    @property
    def description(self):
        return {
            'cornerstore': ('The perfect place to showcase your merchandise!'),
            'hybrid': (
                'The Cozmic CX 1.0 features a butted frame (reduces weight) '
                'combined with hydraulic brakes to give amazing stopping power'
                ' with light feel. The forks feature lock out and pre load '
                'adjustment-useful if you are riding along the road to work, '
                'or to the race.'),
            'road': (
                'This 12-speed Miyata 512 is built on a lugged, triple-butted,'
                ' CroMo frame. A solid ride with a tight race geometry to keep'
                ' it quick and easy to handle.'),
            'touring': (
                'The Clubman is tough enough, yet comfortable enough for '
                'regular commuting. The tubing is slightly heavier-duty than '
                'the Audax to take larger panniers. Tubing is Reynolds 853 & '
                '725 with 531 Forks.'),
            }[self.bike_type]

    @property
    def price(self):
        return {
            'cornerstore': 150,
            'hybrid': 18,
            'road': 12,
            'touring': 10,
            }[self.bike_type]


class Rental(Base):
    __table__ = rentals

    @property
    def owner(self):
        return User.query.get(self.owner_guid)

    @property
    def buyer(self):
        try:
            return User.query.get(self.buyer_guid)
        except NoResultFound:
            return None

    @property
    def bike(self):
        return Listing.query.get(self.bike_guid)
