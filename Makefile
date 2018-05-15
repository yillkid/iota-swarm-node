DCURL_DIR := deps/dcurl

DCURL_LIB := $(DCURL_DIR)/deps/dcurl/build/libdcurl.so
DEPS += $(DCURL_LIB)

all: $(DEPS)

$(DCURL_DIR):
	git submodule init $@
	git submodule update $@

$(DCURL_LIB): $(DCURL_DIR)
	$(MAKE) -C $^ config
	@echo
	$(info Modify $(DCURL_DIR)/build/local.mk for your environments.)
	$(MAKE) -C $^ all

clean:
	find . -name '*.pyc' | xargs $(RM)
	$(MAKE) -C $(DCURL_DIR) clean
distclean: clean
	$(RM) -r $(DCURL_DIR)
