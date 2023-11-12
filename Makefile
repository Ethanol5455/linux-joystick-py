.PHONY: all check clean test fmt help

install:
	pip3 install .

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf src/*.egg-info

fmt:
#	Format src
	python3 -m ruff src/linux_joystick --fix
	python3 -m black src/linux_joystick --safe
	python3 -m isort src/linux_joystick
#	Format examples
	python3 -m ruff examples --fix
	python3 -m black examples --safe
	python3 -m isort examples

check_fmt:
#	Check src
	python3 -m ruff src/linux_joystick
	python3 -m black src/linux_joystick --check
	python3 -m isort src/linux_joystick --check
#	Check examples
	python3 -m ruff examples
	python3 -m black examples --check
	python3 -m isort examples --check
