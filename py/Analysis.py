from robotlibcore import DynamicCore, keyword
from robot.api import logger

class Analysis(DynamicCore):
    ROBOT_LIBRARY_VERSION = "1.0.0"
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LISTENER_API_VERSION = 2
    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        DynamicCore.__init__(self, [])

    @keyword
    def analyze(self):
        logger.info("Analysis.analyze")


    def _endKeyword(self, name, attrs):
        # WORKS
        logger.info("Analysis._end_keyword({}, {})".format(name, attrs), also_console=True)

    def _startSuite(self, name, attrs):
        # Doesnt accumulate to output.xml log
        logger.info("Analysis._start_suite({})".format(name), also_console=True)

    def _endSuite(self, name, attrs):
        # Doesnt accumulate to output.xml log
        logger.info("Analysis._end_suite({})".format(name), also_console=True)

    def _startTest(self, name, attrs):
        # Doesnt accumulate to output.xml log
        logger.info("Analysis._start_test({})".format(name), also_console=True)

    def _endTest(self, name, attrs):
        # Doesnt accumulate to output.xml log
        logger.info("Analysis._end_test({})".format(name), also_console=True)

    def _startKeyword(self, name, attrs):
        # WORKS
        logger.info("Analysis._start_keyword({}, {})".format(name, attrs), also_console=True)
