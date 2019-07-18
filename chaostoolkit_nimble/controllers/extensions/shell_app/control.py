import time
from typing import List

from chaoslib.types import Configuration, \
    Experiment, Run, Secrets, Activity


def after_activity_control(context: Activity, state: Run,
                           configuration: Configuration = None,
                           secrets: Secrets = None, **kwargs):
    """
    after-control of the activity's execution

    Called by the Chaos Toolkit before the activity is applied. The result of
    the execution is passed as `state`. See
    https://docs.chaostoolkit.org/reference/api/journal/#run for more
    information.
    """
    print("----------------STATE AFTER ACTIVITY:  %s" %state)
    
def after_method_control(context: Experiment, state: List[Run],
                         configuration: Configuration = None,
                         secrets: Secrets = None, **kwargs):
    """
    after-control of the method's execution

    Called by the Chaos Toolkit after the activities of the method have been
    applied. The `state` is the list of activity results. See
    https://docs.chaostoolkit.org/reference/api/journal/#run for more
    information.
    """
    print("----------------STATE AFTER METHOD:  %s" % state)