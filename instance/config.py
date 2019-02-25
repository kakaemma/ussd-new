class MainConfiguration(object):
    """ Parent configuration class"""
    DEBUG = False
    CRSF_ENABLED = True
    LEVEL = DEBUG
    LOGFILE = "logs/ugapay.log"


class DevelopmentEnvironment(MainConfiguration):
    """ Configurations for Development"""
    DEBUG = True

class TestingEnvironment(MainConfiguration):
    """Configurations for Testing"""
    DEBUG = True
    TESTING = True

class StagingEnvironment(MainConfiguration):
    """Configurations for Staging"""
    DEBUG = True

class ProductionEnvironment(MainConfiguration):
    """ Configurations for Production"""
    DEBUG = False
    TESTING = False

application_config = {
    'MainConfig': MainConfiguration,
    'TestingEnv': TestingEnvironment,
    'DevelopmentEnv': DevelopmentEnvironment,
    'ProductionEnv': ProductionEnvironment
}
