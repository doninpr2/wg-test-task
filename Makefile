activate:
	@echo "Activating virtual environment..."
	source venv/bin/activate

deactivate:
	@echo "Deactivating virtual environment..."
	deactivate

install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

run:
	@echo "Running the application..."
	python src/main.py