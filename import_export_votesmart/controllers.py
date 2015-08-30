
from models import State
from votesmart import votesmart
from wevotebase.base import get_environment_variable


votesmart.apikey = get_environment_variable(VOTESMART_API_KEY)


def _get_state_by_id_as_dict(stateId):
    """Access Votesmart API and return dictionary representing state."""
    return votesmart.state.getState(stateId).__dict__


def _get_state_names():
    """Access Votesmart API and return generator of all stateIds."""
    return (state.stateId for state in votesmart.state.getStateIDs())


def load_states():
    """Load/Update all states into database."""
    for stateId in _get_state_names:
        state, created = State.objects.get_or_create(**_get_state_by_id_as_dict(stateId))
        state.save()
