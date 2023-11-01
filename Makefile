##@ Testing
.PHONY: unit-tests
unit-tests:
	@pytest

.PHONY: unit-tests-cov
unit-tests-cov:
	@pytest --cov=src --cov-report term-missing --cov-report=html

.PHONY: unit-tests-cov-fail
unit-tests-cov-fail:
	@pytest --cov=src --cov-report term-missing --cov-report=html --cov-fail-under=80 --junitxml=pytest.xml | tee pytest-coverage.txt

##@ Formatting

.PHONY: format-black
format-black:
	@black .

.PHONY: format-isort
format-isort:
	@isort .

.PHONY: format
format: format-black format-isort

##@ Linting

.PHONY: lint-black
lint_black:
	@black . --check

.PHONY: lint-isort
lint-isort:
	@isort . --check

.PHONY: lint-flake8
lint-flake8:
	@flake8 .

.PHONY: lint-mypy
lint-mypy:
	@mypy --config-file pyproject.toml ./src

.PHONY: lint-mypy-report
lint-mypy-report:
	@mypy --config-file pyproject.toml ./src --html-report ./mypy_html

lint: lint-black lint-isort lint-flake8 lint-mypy

##@ Clean-up

clean-cov:
	@rm -rf .coverage
	@rm -rf htmlcov
	@rm -rf pytest.xml
	@rm -rf pytest-coverage.txt
