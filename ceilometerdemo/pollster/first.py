from ceilometer.agent import plugin_base
from ceilometer import sample
from oslo_log import log
from oslo_utils import timeutils

LOG = log.getLogger(__name__)


class MyFirstPollster(plugin_base.PollsterBase):
    @property
    def default_discovery(self):
        return "demo.discoverer"

    def get_samples(self, manager, cache, resources):
        for res in resources:
            LOG.info('Generating sample for resource %s', res)
            yield sample.Sample(name='demo.pollstermeter',
                                type=sample.TYPE_GAUGE,
                                unit='B',
                                volume=0.5,
                                user_id=None,
                                project_id=None,
                                resource_id=str(res),
                                timestamp=timeutils.utcnow().isoformat(),
                                resource_metadata=None,
                                source='demo')


class MyFirstDiscoverer(plugin_base.DiscoveryBase):
    def discover(self, manager, param=None):
        return ['demo://fake_resource']
