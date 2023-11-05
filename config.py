from pydantic import BaseModel, field_validator


class Config(BaseModel):
    scroll_rpc_url: str
    eth_rpc_url: str
    scroll_explorer_url: str
    max_gwei: float
    min_length: int
    max_length: int
    min_sleep_time: float
    max_sleep_time: float

    @classmethod
    def load(cls):
        with open('config.json') as file:
            return cls.model_validate_json(file.read())

    @field_validator('max_gwei')
    def check_max_gwei(cls, v: float):
        if v <= 0:
            raise ValueError('Max gwei must be positive')

        return v

    @field_validator('min_length')
    def check_min_length(cls, v: int):
        if v <= 0:
            raise ValueError('Min length must be positive')

        return v

    @field_validator('max_length')
    def check_max_length(cls, v: int, values):
        if v <= 0:
            raise ValueError('Max length must be positive')
        elif v < values.data['min_length']:
            raise ValueError('Max length must be greater than min length')

        return v

    @field_validator('min_sleep_time')
    def check_min_sleep_time(cls, v: float):
        if v <= 0:
            raise ValueError('Min sleep time must be positive')

        return v

    @field_validator('max_sleep_time')
    def check_max_sleep_time(cls, v: float, values):
        if v <= 0:
            raise ValueError('Max sleep time must be positive')
        elif v < values.data['min_sleep_time']:
            raise ValueError('Max sleep time must be greater than min sleep time')

        return v
