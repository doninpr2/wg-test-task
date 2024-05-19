import unittest
from frameworks.storages.figures_memory_storage import FiguresMemoryStorage

class TestFiguresMemoryStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FiguresMemoryStorage()

    def test_add_figure(self):
        position = (10, 20)
        figure = self.storage.add(position)
        self.assertIsNotNone(figure.id)
        self.assertEqual(figure.position, position)
        self.assertIn(figure.id, self.storage.figures)

    def test_get_figure(self):
        position = (10, 20)
        added_figure = self.storage.add(position)
        retrieved_figure = self.storage.get(added_figure.id)
        self.assertEqual(added_figure, retrieved_figure)

    def test_get_all_figures(self):
        position1 = (10, 20)
        position2 = (30, 40)
        self.storage.add(position1)
        self.storage.add(position2)
        all_figures = self.storage.get_all()
        self.assertEqual(len(all_figures), 2)
        self.assertEqual(all_figures[0].position, position1)
        self.assertEqual(all_figures[1].position, position2)

    def test_update_figure(self):
        position = (10, 20)
        added_figure = self.storage.add(position)
        new_position = (30, 40)
        added_figure.position = new_position
        self.storage.update(added_figure)
        updated_figure = self.storage.get(added_figure.id)
        self.assertEqual(updated_figure.position, new_position)

if __name__ == "__main__":
    unittest.main()
