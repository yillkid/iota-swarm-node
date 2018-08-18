PYTHON = python3
PYTHON := $(shell which $(PYTHON))
ifndef PYTHON
$(error "python3 is required.")
endif

# check "iota" module in Python installation
PY_CHECK_MOD_IOTA := $(shell $(PYTHON) -c "import iota" 2>/dev/null && \
                       echo 1 || echo 0)
ifneq ("$(PY_CHECK_MOD_IOTA)","1")
    $(error "skip $@ because PyOTA is not installed.")
endif
