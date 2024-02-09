# Hilton

Repository of the HLT Online Test Stand (Hilton) software used on online validation machines, used for testing High Level Trigger (HLT) menus and reconstruction in a manner as close as possible to the online environment at CMS P5.


A complete set of instructions can be found on the
[CMS HLT Operations Documentation](https://cms-hlt-operations.docs.cern.ch/Hilton/quickTest), including the prerequisites for the technical [setup](https://cms-hlt-operations.docs.cern.ch/GeneralHLTDOC/setup).

## CI/CD Pipelines

Each push to GitLab that introduces new commits will start a CI pipeline. The source for that is the `.gitlab-ci.yml` file.

Each pipeline contains a build of an RPM package for the Hilton software, which could be deployed to P5.
