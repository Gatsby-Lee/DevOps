PYPI_OPTIONS = --quiet --no-cache --extra-index-url https://pypi.org/simple
AWS_REGION = us-east-1
help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "release - package and upload a release"
	@echo "dist - package"

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean: clean-build clean-pyc

create-version:
	.venv/bin/python generate_version.py --create-version-file

setup-deploy-venv:
	python3 -m venv .venv
	.venv/bin/pip install pip --upgrade $(PYPI_OPTIONS)
	.venv/bin/pip install awscli bpython twine wheel $(PYPI_OPTIONS)
	.venv/bin/pip list

build: setup-deploy-venv clean create-version
	.venv/bin/python setup.py sdist
	.venv/bin/python setup.py bdist_wheel
	ls -l dist

release-aws:
	.venv/bin/aws codeartifact login --tool twine --domain helloworld --repository pypirepo --region $(AWS_REGION)
	.venv/bin/twine upload --repository codeartifact dist/*.tar.gz


build-release-aws: build release-aws
