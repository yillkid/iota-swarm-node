# check Python version
PYTHON := $(shell which "python")
PYTHON_COMPATIBLE = python3.5

ifndef PYTHON
    $(error "Python is not executable, try to check the PATH environment variable or install $(PYTHON_COMPATIBLE) package.")
endif # PYTHON

ifdef PYTHON
    PY_CHECK_VERSION := $(shell python -c "print(__import__('sys').version_info[0:2])")

ifneq ($(PY_CHECK_VERSION), (3, 5))
    PYTHON_COMPATIBLE_PATH := $(shell which $(PYTHON_COMPATIBLE))

    ifdef PYTHON_COMPATIBLE_PATH
        $(error "Found $(PYTHON_COMPATIBLE) in current environment, but it should be setting as \
            default interpreter, try to create a symbolic link for $(PYTHON_COMPATIBLE_PATH)")
    else
        $(error "$(shell python -V):Invalid Python version, only available for $(PYTHON_COMPATIBLE).")
    endif
endif
endif # PYTHON

ifndef PYTHON

endif # PYTHON

# check "iota" module in Python installation
ifdef PYTHON
PY_CHECK_MOD_IOTA := $(shell $(PYTHON) -c "import iota" 2>/dev/null && \
                       echo 1 || echo 0)
ifneq ("$(PY_CHECK_MOD_IOTA)","1")
    $(error "dependency error $@ because PyOTA is not installed, to install the latest version: pip3 install pyota")
endif
endif # PYTHON
