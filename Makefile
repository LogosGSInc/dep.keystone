install:
	python -m pip install -e .

test:
	pytest -q

verify-example:
	dep-keystone verify --input ./examples/sample_requirements.txt --type requirements.txt --out ./out
