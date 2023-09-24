.PHONY: all check clean test fmt help

install:
	pip3 install .

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf src/*.egg-info

ci:
	python3 -m ruff ./src/linux_js --fix
	python3 -m isort src/linux_js
	python3 -m black src/linux_js --safe