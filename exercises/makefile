.DEFAULT_GOAL := test

FILES :=           \
    IsPrime1T      \
    IsPrime2T      \
    FactorialT     \
    ReduceT        \
    MapT           \
    RangeIteratorT \
    RangeT         \
    DecoratorsT    \
    ComplexT       \
    SelectT        \
    ProjectT

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint3.5
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.4
    AUTOPEP8 := autopep8
endif

.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@

RMSET.pyx: RMSE.py RMSET.py .pylintrc
	-$(PYLINT) $<
	-$(PYLINT) $(@:.pyx=.py)
	$(PYTHON) $<

%T.pyx: %.py %T.py .pylintrc
	-$(PYLINT) $<
	-$(PYLINT) $(@:.pyx=.py)
	$(COVERAGE) run --branch $(@:.pyx=.py)
	$(COVERAGE) report -m

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -rf __pycache__

test: $(FILES:=.pyx)
