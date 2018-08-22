# check Python version
PYTHON := $(shell which "python")
PYTHON_COMPATIBLE_VERSION = 3.5

ifndef PYTHON
    $(error "Python is not executable, try to check the PATH environment variable or \
        install python$(PYTHON_COMPATIBLE_VERSION) package.")
endif # $(shell which "python")

PY_CHECK_VERSION := $(shell python -c "print(str(__import__('sys').version_info.major) + \
    str('.') + str(__import__('sys').version_info.minor) )")

ifneq ($(PY_CHECK_VERSION), $(PYTHON_COMPATIBLE_VERSION))

    PYTHON_COMPATIBLE_PATH := $(shell which "python"$(PYTHON_COMPATIBLE_VERSION))

    ifdef PYTHON_COMPATIBLE_PATH
        $(error "Found python$(PYTHON_COMPATIBLE_VERSION) in current environment, but it should be setting as \
            default interpreter, try to set $(PYTHON_COMPATIBLE_PATH) in PATH environment variable.")
    else
        $(error "$(shell python -V):Unsupported python version, only available for Python$(PYTHON_COMPATIBLE_VERSION).")
    endif
endif

# check "iota" module in Python installation
PY_CHECK_MOD_IOTA := $(shell python -c "import iota" 2>/dev/null && \
                       echo 1 || echo 0)
ifneq ("$(PY_CHECK_MOD_IOTA)","1")
    $(error "Dependency error $@ because PyOTA is not installed, to install the latest version: pip3 install pyota")
endif
