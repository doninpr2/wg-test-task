import unittest
from unittest.mock import MagicMock
from domain.usecases.figure_usecase import FigureUseCase
from domain.entities.ColoredRectangle import ColoredRectangle

class TestFigureUseCase(unittest.TestCase):

    def setUp(self):
        self.repository = MagicMock()
        self.figure_use_case = FigureUseCase(self.repository)

    def test_create(self):
        position = (10, 20)
        figure = ColoredRectangle(id="1", position=position)
        self.repository.add.return_value = figure

        created_figure = self.figure_use_case.create(position)

        self.repository.add.assert_called_once_with(position)
        self.assertEqual(created_figure, figure)

    def test_get(self):
        figure = ColoredRectangle(id="1", position=(10, 20))
        self.repository.get.return_value = figure

        retrieved_figure = self.figure_use_case.get("1")

        self.repository.get.assert_called_once_with("1")
        self.assertEqual(retrieved_figure, figure)

    def test_get_all(self):
        figures = [ColoredRectangle(id="1", position=(10, 20)), ColoredRectangle(id="2", position=(30, 40))]
        self.repository.get_all.return_value = figures

        all_figures = self.figure_use_case.get_all()

        self.repository.get_all.assert_called_once()
        self.assertEqual(all_figures, figures)

    def test_move(self):
        figure = ColoredRectangle(id="1", position=(10, 20))
        updated_figure = ColoredRectangle(id="1", position=(30, 40))
        self.repository.get.return_value = figure
        self.repository.update.return_value = updated_figure

        result = self.figure_use_case.move("1", 30, 40)

        self.repository.get.assert_called_once_with("1")
        self.assertEqual(figure.position, (30, 40))
        self.repository.update.assert_called_once_with(figure)
        self.assertEqual(result, updated_figure)

    def test_move_nonexistent(self):
        self.repository.get.return_value = None

        result = self.figure_use_case.move("nonexistent_id", 30, 40)

        self.repository.get.assert_called_once_with("nonexistent_id")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
