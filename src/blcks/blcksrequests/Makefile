.PHONY: pre-build

pre-build:
	mkdir -p template && \
	ofsm template -l python3_blcks_flask template && \
	faas-cli build --name=blcksrequests --lang=python3_blcks_flask --image=blcksrequests --handler=handler --shrinkwrap && \
	cp *.para build/blcksrequests