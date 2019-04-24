# -*- coding: utf-8 -*-
from fabric import task


@task
def restart(c):
    c.run('~/bin/gunicorn restart')
    c.run('~/bin/celeryd restart')
    c.run('~/bin/celerycam restart')


@task
def start(c):
    c.run('~/bin/gunicorn start')
    c.run('~/bin/celeryd start')
    c.run('~/bin/celerycam start')


@task
def stop(c):
    c.run('~/bin/gunicorn stop')
    c.run('~/bin/celeryd stop')
    c.run('~/bin/celerycam stop')


@task
def update_config_file(c):
    # no config
    pass


@task
def update(c):
    # no config
    pass