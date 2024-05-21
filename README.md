# wargaming-test-task
 
Объяснение структуры:
- `domain` - Слой доменной области
- `domain/entities` - Бизнес сущности
- `domain/usecases` - Бизнес логика
- `domain/utils` - Вспомогательные классы и инструменты

- `frameworks` - Внешний слой (Библиотеки, фреймворки, базы данных и т.д.)
- `frameworks/storages` - Реализация хранилищ данных
- `frameworks/views` - Реализация представлений (UI)

- `main.py` - Главный файл
- `constants.py` - Константы
- `container.py` - Реализация Dependency Injection (DI) контейнера
- `run_tests.py` - Запуск тестов

Запуск приложения:
1. Создать виртуальное окружение `python -m venv venv`
2. Активировать виртуальное окружение `source venv/bin/activate`
3. Установить зависимости `pip install -r requirements.txt`
4. Запустить приложение `python src/main.py`

Запуск тестов: `python src/run_tests.py`

Для удобства был создан файл Makefile, который содержит команды для запуска приложения и тестов.

Версия Python: 3.9.9

За основу архитектуры был взят Clean Architecture, однако в целях упрощения был убран промещуточный слой адаптеров между слоями домена и фреймворков.

Подробнее о Clean Architecture:
- https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html

Подробнее о Dependency Injection:
- https://en.wikipedia.org/wiki/Dependency_injection

Подробнее о SOLID:
- https://en.wikipedia.org/wiki/SOLID
