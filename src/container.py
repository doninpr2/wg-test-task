from dependency_injector import containers, providers

from domain.entities.ColoredRectangle import ColoredRectangle
from frameworks.views.scene_view import SceneView
from domain.usecases.figure_usecase import FigureUseCase
from frameworks.storages.figures_memory_storage import FiguresMemoryStorage

class Container(containers.DeclarativeContainer):
    figures_storage = providers.Singleton(FiguresMemoryStorage)
    figures_use_case = providers.Singleton(FigureUseCase, repository=figures_storage)
    scene_view = providers.Factory(SceneView, figure_usecase=figures_use_case)