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