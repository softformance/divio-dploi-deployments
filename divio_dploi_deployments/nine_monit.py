# -*- coding: utf-8 -*-
from fabric.api import env
from fabric.decorators import task
from fabric.operations import run


@task
def restart():
    run('~/bin/gunicorn restart')
    run('~/bin/celeryd restart')
    run('~/bin/celerycam restart')


@task
def start():
    run('~/bin/gunicorn start')
    run('~/bin/celeryd start')
    run('~/bin/celerycam start')


@task
def stop():
    run('~/bin/gunicorn stop')
    run('~/bin/celeryd stop')
    run('~/bin/celerycam stop')


@task
def update_config_file():
    # no config
    pass


@task
def update():
    # no config
    pass