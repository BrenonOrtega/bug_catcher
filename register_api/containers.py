from dependency_injector import providers, containers
from .models import Error, Register

class Configs(containers.DeclarativeContainer):
    config = provider.Configuration('config')

class IError(containers.DeclarativeContainer):
    Register = providers.Singleton(Error, Configs.config)
