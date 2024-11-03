.PHONY = develop clean

.venv/.venvsetup:
	python3.13 -m venv .venv
	.venv/bin/python3 -m pip install --upgrade pip
	.venv/bin/python3 -m pip install hatch uv
	touch @a


.venv/.devsetup: .venv/.venvsetup
	.venv/bin/python3 -m uv pip install -e .[dev]
	.venv/bin/python3 -m uv pip install -e ../advent_of_code_utils
	touch @a

develop: .venv/.devsetup

clean:
	rm -rf .venv
