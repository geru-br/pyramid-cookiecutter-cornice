CURRENT_DIR := $(shell pwd)

.PHONY: clean
clean: ## clean clients for python, java, and javascript
	rm -rf ${CURRENT_DIR}/clients/python
	rm -rf ${CURRENT_DIR}/clients/java
	rm -rf ${CURRENT_DIR}/clients/javascripts


.PHONY: clients
clients: clean ## clients for python, java, and javascript
	mkdir -p ${CURRENT_DIR}/clients/python
	manage development.ini swagger extract > ${CURRENT_DIR}/clients/swagger.json
	{{ cookiecutter.docker_command }} run -v ${CURRENT_DIR}/clients:/tmp/clients openapitools/openapi-generator-cli:v3.3.0 generate -l python -DpackageName={{cookiecutter.repo_name}}_client -DprojectName={{cookiecutter.repo_name}}-client -i /tmp/clients/swagger.json -o /tmp/clients/python
	{{ cookiecutter.docker_command }} run -v ${CURRENT_DIR}/clients:/tmp/clients openapitools/openapi-generator-cli:v3.3.0 generate -l java -DpackageName={{cookiecutter.repo_name}}_client -DprojectName={{cookiecutter.repo_name}}-client -i /tmp/clients/swagger.json -o /tmp/clients/java
	{{ cookiecutter.docker_command }} run -v ${CURRENT_DIR}/clients:/tmp/clients openapitools/openapi-generator-cli:v3.3.0 generate -l javascript -DpackageName={{cookiecutter.repo_name}}_client -DprojectName={{cookiecutter.repo_name}}-client -i /tmp/clients/swagger.json -o /tmp/clients/javascript