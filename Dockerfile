ARG CI_COMMIT_REF_NAME=master
ARG CI_COMMIT_SHORT_SHA=latest
FROM gitlab-registry.cern.ch/cms-tsg/fog/hilton/builder:${CI_COMMIT_REF_NAME}-${CI_COMMIT_SHORT_SHA}

COPY hilton /hilton
#WORKDIR /hilton
#RUN make
