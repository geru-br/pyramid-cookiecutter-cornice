CURRENT_DIR := $(shell pwd)

.PHONY: build-clients
clients: ## build clients for python, java, and javascript
	mkdir -p ${CURRENT_DIR}/clients/python
	manage development.ini swagger extract > ${CURRENT_DIR}/clients/swagger.json
	docker run -v ${CURRENT_DIR}/clients:/tmp/clients openapitools/openapi-generator-cli:v3.3.0 generate -l python -DpackageName={{cookiecutter.repo_name}}_client -DprojectName={{cookiecutter.repo_name}}-client -i /tmp/clients/swagger.json -o /tmp/clients/python
	docker run -v ${CURRENT_DIR}/clients:/tmp/clients openapitools/openapi-generator-cli:v3.3.0 generate -l java -DpackageName={{cookiecutter.repo_name}}_client -DprojectName={{cookiecutter.repo_name}}-client -i /tmp/clients/swagger.json -o /tmp/clients/java
	docker run -v ${CURRENT_DIR}/clients:/tmp/clients openapitools/openapi-generator-cli:v3.3.0 generate -l javascript -DpackageName={{cookiecutter.repo_name}}_client -DprojectName={{cookiecutter.repo_name}}-client -i /tmp/clients/swagger.json -o /tmp/clients/javascript