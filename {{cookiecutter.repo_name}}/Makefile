CURRENT_DIR := $(shell pwd)

.PHONY: build-clients
build-clients: ## build clients for python, java, and javascript
    mkdir -p ${CURRENT_DIR}/clients/python
    manage development.ini swagger extract > ${CURRENT_DIR}/clients/swagger.json
    docker run -v ${CURRENT_DIR}/clients:/tmp/clients openapitools/openapi-generator-cli:v3.3.0 generate -l python -DpackageName=cbgb_client -DprojectName=cbgb-client -i /tmp/clients/swagger.json -o /tmp/clients/python