.PHONY: init

init:
	${INFO} "Creating draco folder if it does not exist"
	@ mkdir -p $(PROJECT_FOLDER)/draco
	${INFO} "Creating initial files for pipeline structure"
	@ cp -r $(SOURCE_FOLDER)/dracopip_templates/* $(PROJECT_FOLDER)/draco

# Cosmetics
YELLOW := "\e[1;33m"
NC := "\e[0m"

#Shell Functions
INFO := @bash -c '\
    printf $(YELLOW); \
    echo "=> $$1"; \
    printf $(NC)' SOME_VALUE
