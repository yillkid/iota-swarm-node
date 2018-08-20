PYTHON = python3.5
PYTHON := $(shell which $(PYTHON))
ifndef PYTHON
$(error "python3.5 is required.")
endif

# check "iota" module in Python installation
PY_CHECK_MOD_IOTA := $(shell $(PYTHON) -c "import iota" 2>/dev/null && \
                       echo 1 || echo 0)
ifneq ("$(PY_CHECK_MOD_IOTA)","1")
    $(error "dependency error $@ because PyOTA is not installed, to install the latest version: pip3 install pyota")
endif
