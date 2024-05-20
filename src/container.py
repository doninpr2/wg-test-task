from dependency_injector import containers, providers

from domain.usecases.connections_usecase import ConnectionsUseCase
from frameworks.storages.connections_memory_storage import ConnectionsMemoryStorage
from frameworks.views.scene_view import SceneView
from domain.usecases.figure_usecase import FigureUseCase
from frameworks.storages.figures_memory_storage import FiguresMemoryStorage

class Container(containers.DeclarativeContainer):
    figures_storage = providers.Singleton(FiguresMemoryStorage)
    connections_storage = providers.Singleton(ConnectionsMemoryStorage)

    figures_use_case = providers.Singleton(FigureUseCase, repository=figures_storage)
    connections_use_case = providers.Singleton(ConnectionsUseCase, repository=connections_storage)

    scene_view = providers.Factory(SceneView, figures_usecase=figures_use_case, connections_usecase=connections_use_case)