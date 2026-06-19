from django.apps import AppConfig

import logging

logger = logging.getLogger(__name__)


class CalculationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.calculation"

    def ready(self):
        from .cal_config import CalculationConfigManager

        logger.info("Running the initial for calrule")
        CalculationConfigManager().initial()
