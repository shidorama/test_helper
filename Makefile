wheel: clean
	@python2.7 setup.py bdist_wheel

clean:
	@rm -rf build
	@rm -rf dist
	@rm -rf unittest_helpers.*
