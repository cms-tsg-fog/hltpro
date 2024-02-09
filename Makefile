SHELL:=/bin/bash
.DEFAULT_GOAL := rpm

CI_COMMIT_TAG ?= 0.0.0
VERSION = ${CI_COMMIT_TAG}
RELEASE = 1
ARCH = amd64
# Get the git branch name and the short commit hash
CI_COMMIT_BRANCH ?= $(shell git rev-parse --abbrev-ref HEAD)
BRANCH = ${CI_COMMIT_BRANCH}
HASH = $(shell git rev-parse --short HEAD)

# e.g. 'python36'
PYTHON_VERSION = $(shell python --version 2>&1| sed -E 's|^Python ([0-9])\.([0-9])\..*$$|python\1\2|')
$(info Python version '${PYTHON_VERSION}')

#.PHONY: build
#build: rpm
#	make -C hilton

RPM_NAME = hilton-${VERSION}.${ARCH}.${BRANCH}.${HASH}

.PHONY: rpm
rpm: ${RPM_NAME}
${RPM_NAME}:
	# Clean up the rpmroot directory
	rm -rf rpmroot
	# Create /opt
	mkdir -p rpmroot/opt
	# Copy the hilton folder
	cp -r hilton rpmroot/opt

	mkdir -p rpms/${PYTHON_VERSION}

	# Launch fpm to package the prepared folder	
	fpm \
	-p ${RPM_NAME}-${PYTHON_VERSION}.rpm \
	-n hilton \
	-s dir \
	-t rpm \
	-v ${VERSION} \
	-a ${ARCH} \
	-d root -d ${PYTHON_VERSION}-root \
	--iteration ${RELEASE} \
	--description "HLT Online Test Stand (Hilton) software, for testing High Level Trigger (HLT) menus and reconstruction in a manner as close as possible to the online environment at P5." \
	--url "https://gitlab.cern.ch/cms-tsg/fog/hilton" \
	--vendor "CERN" \
	rpmroot/=/

	mv *-${PYTHON_VERSION}.rpm rpms/${PYTHON_VERSION}
