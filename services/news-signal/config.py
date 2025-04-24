from typing import Literal, Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file='settings.env')

    kafka_broker_address: str
    kafka_input_topic: str
    kafka_output_topic: str
    kafka_consumer_group: str

    model_provider: Literal['anthropic', 'ollama', 'dummy']
    data_source: Literal['live', 'historical']


class FineTuningConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='fine_tuning_settings.env', env_file_encoding='utf-8'
    )

    comet_api_key: Optional[str] = None
    comet_ml_workspace: Optional[str] = None
    comet_ml_project_name: Optional[str] = None
    comet_log_assets: Optional[str] = None
    comet_mode: Optional[str] = None
    comet_auto_log_graph: Optional[bool] = None
    comet_auto_log_metrics: Optional[bool] = None
    comet_auto_log_parameters: Optional[bool] = None
    comet_auto_log_cli_arguments: Optional[bool] = None
    hf_token: Optional[str] = None


config = Config()
fine_tuning_config = FineTuningConfig()
