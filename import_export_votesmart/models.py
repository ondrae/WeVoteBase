
from django.db import models


class State(models.Model):
    """http://api.votesmart.org/docs/State.html
    """
    stateId = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50)
    # senators = None  # example:  0
    # billUrl = None  # example:
    # usCircuit = None  # example:  Ninth
    # ltGov = None  # example:  t
    # rollLower = None  # example:  Roll no.
    # lowerLegis = None  # example:  Assembly
    # voterReg = None  # example:  <p style="orphans: 1;"><strong><span sty
    # flower = None  # example:  Golden Poppy
    # area = None  # example:  158,693 sq mi
    # upperLegis = None  # example:  Legislature
    # termLength = None  # example:  0
    # bicameral = None  # example:  t
    # capital = None  # example:  Sacramento
    # voteUrl = None  # example:
    # nickName = None  # example:  The Golden State
    # bird = None  # example:  California Valley Quail
    # highPoint = None  # example:  Mt. Whitney, 14,491 ft
    # termLimit = None  # example:  0
    # lowPoint = None  # example:  Death Valley, 282 ft below sea level.
    # primaryDate = None  # example:
    # stateType = None  # example:  State
    # statehood = None  # example:  Sept. 9, 1850 (31st state)
    # reps = None  # example:  0
    # motto = None  # example:  Eureka [I Have Found It]
    # population = None  # example:  36,961,664 (2009 est.)
    # tree = None  # example:
    # generalDate = None  # example:
    # rollUpper = None  # example:  Roll no.
    # largestCity = None  # example:


# Methods.
def get_state(stateId):
    """Retrieve State from database."""
    return State.objects.filter(stateId=stateId)


def get_states():
    """"Retrieve all State objects from database."""
    return State.objects.all()
