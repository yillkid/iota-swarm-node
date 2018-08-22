# check Python version
PY_FAVORED_VER = 3.5
PYTHON := $(shell which "python")
ifndef PYTHON
    PYTHON := $(shell which "python3")
endif

ifndef PYTHON
    PYTHON := $(shell which "python$(PY_FAVORED_VER)")
endif

ifndef PYTHON
    $(error "Python is not executable, try to check the PATH environment variable or \
        install python$(PY_FAVORED_VER) package.")
endif # $(shell which "python")

PY_CHECK_VERSION := $(shell $(PYTHON) -V)

ifeq "$(filter $(PY_FAVORED_VER).%, $(PY_CHECK_VERSION))" ""
    PYTHON := $(shell which "python"$(PY_FAVORED_VER))
    ifdef PYTHON
        $(error "Found python$(PY_FAVORED_VER), but it should be set as \
            default interpreter, try to set $(PYTHON) in PATH environment variable.")
    else
        $(error "$(shell python -V):Unsupported python version, only available for Python$(PY_FAVORED_VER).")
    endif
endif

# check "iota" module in Python installation
PY_CHECK_MOD_IOTA := $(shell python -c "import iota" 2>/dev/null && \
                       echo 1 || echo 0)
ifneq ("$(PY_CHECK_MOD_IOTA)","1")
    $(error "Dependency error $@ because PyOTA is not installed, to install the latest version: pip install pyota")
endif
