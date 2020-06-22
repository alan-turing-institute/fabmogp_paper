IMAGE = fabmogp
docker_out = /home/root/fabmogp/output/

.PHONY: fabmogp_build
fabmogp_build: Dockerfile
	docker build --no-cache -t ${IMAGE} - < Dockerfile

.PHONY: fabmogp_docker
fabmogp_docker: Dockerfile
	mkdir -p output
	docker run --rm -v `pwd`/output/:${docker_out} -ti ${IMAGE}
