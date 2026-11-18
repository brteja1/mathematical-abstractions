"""Reference scheduler. Public module functions define the evaluated API."""


def new():
    return {'clock': 0, 'jobs': {}}


def _advance(state, now):
    if now < state['clock']:
        raise ValueError('time cannot move backwards')
    state['clock'] = now
    state['jobs'] = {key: row for key, row in state['jobs'].items() if row[2] > now}


def put(state, job_id, priority, expires_at, now):
    _advance(state, now)
    state['jobs'].pop(job_id, None)
    if expires_at > now:
        state['jobs'][job_id] = (job_id, priority, expires_at)


def take(state, now):
    _advance(state, now)
    if not state['jobs']:
        raise KeyError('empty scheduler')
    row = min(state['jobs'].values(), key=lambda item: item[1])
    del state['jobs'][row[0]]
    return row


def snapshot(state, now):
    _advance(state, now)
    return tuple(state['jobs'][key] for key in sorted(state['jobs']))


def clone(state):
    return {'clock': state['clock'], 'jobs': state['jobs'].copy()}
