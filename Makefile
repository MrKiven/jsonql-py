pep8:
	flake8 jsonql tests

test: pep8
	rm -rf .cache
	mkdir -p .build
	py.test tests -rfExswX --duration=10 --junitxml=.build/unittest.xml --cov jsonql --cov-report xml -n 4

tag:
	@t=`python setup.py  --version`;\
	echo v$$t; git tag v$$t

clear_pyc:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d -delete
