from fabric.decorators import task
from fabric.api import run, put, env
from dploi_fabric.supervisor import get_group_name, update_config_file as supervisor_update_config_file
from dploi_fabric.utils import config


@task
def stop():
    for site, site_config in config.sites.items():
        run('supervisorctl --c ~/config/supervisord.conf stop %s:*' %  get_group_name(site, site_config))


@task
def start():
    for site, site_config in config.sites.items():
        run('supervisorctl --c ~/config/supervisord.conf start %s:*' % get_group_name(site, site_config))


@task
def restart():
    for site, site_config in config.sites.items():
        run('supervisorctl  --c ~/config/supervisord.conf restart %s:*' % get_group_name(site, site_config))


@task
def status():
    """
    print status of the supervisor process

    Note: "status" does not yet support the group syntax
    """
    for site, site_config in config.sites.items():
        group_name = get_group_name(site, site_config)
        for process_name, process_cmd in site_config.processes.items():
            run('supervisorctl --c ~/config/supervisord.conf status %s:%s' % (group_name, process_name))


@task
def update():
    for site, site_config in config.sites.items():
        group_name = get_group_name(site, site_config)
        for process_name, process_cmd in site_config.processes.items():
            run('supervisorctl --c ~/config/supervisord.conf update %s:%s' % (group_name, process_name))


@task
def update_config_file(dryrun=False):
    supervisor_update_config_file(dryrun=dryrun, update_command=update)
