import logging

from ceilometer import publisher
from oslo_log import log
from oslo_utils import timeutils

LOG = log.getLogger(__name__)

class DemoFilePublisher(publisher.PublisherBase):
    def __init__(self, parsed_url):
        super(DemoFilePublisher, self).__init__(parsed_url)
        self.logger = None
        if not parsed_url.path:
            LOG.error("The path for the publisher must be provided")
            return

        rh = logging.FileHandler(parsed_url.path,
                                 mode='a',
                                 encoding='utf8')
        rh.setLevel(logging.INFO)
        self.logger = logging.Logger('publisher.demofile')
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
        self.logger.addHandler(rh)
        self.logger.info("Starting recording at %s" %
                         timeutils.utcnow().isoformat())
        self.logger.info('-' * 80)

    def publish_samples(self, context, samples):
        if self.logger:
            for s in samples:
                self.logger.info(s.as_dict())

    def publish_events(self, context, evetns):
        if self.logger:
            for e in events:
                self.logger.info("%r" % e)

