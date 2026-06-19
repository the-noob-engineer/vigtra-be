import pathlib
from dataclasses import dataclass
from modules.core import PROJECT_ROOT
from modules.core.config_manager import BASE_DIR
import yaml
import os
import logging

logger = logging.getLogger(__name__)

CALCULATION_RULE_CONFIG_FILE = pathlib.Path(BASE_DIR).joinpath(
    "calculation_rule.config.yaml"
)

DEFAULT_CALC_RULES_DIR = os.path.join(PROJECT_ROOT, "default_calculation_rules")


@dataclass
class CalculationConfigModelDef:
    name: str
    description: str
    dsl_file_path: str
    models: list[str]
    enable: bool = True

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "dls_file_path": self.dsl_file_path,
            "models": [model for model in self.models],
            "enable": self.enable,
        }


DEFAULT_CONFIG = [
    CalculationConfigModelDef(
        name="Income",
        description="Just testing based on income",
        dsl_file_path=os.path.join(DEFAULT_CALC_RULES_DIR, "income_calc_rule.cel"),
        models=["claim", "insuree"],
    )
]


class CalculationConfigManager:
    """This is not to be stored in the database"""

    @classmethod
    def initial(cls):
        if not CALCULATION_RULE_CONFIG_FILE.exists():
            cls.load_configuration()

    @classmethod
    def load_configuration(cls):
        with open(CALCULATION_RULE_CONFIG_FILE, "w") as file:
            yaml.safe_dump([entry.to_dict() for entry in DEFAULT_CONFIG], file)
