# hltpro
Repository of HLT Online Test Stand (Hilton) software used on online validation machines. More details on the [Hilton Twiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/HLTOnlineTestStand), including the prerequisites described on the [HLT DOC Twiki](https://twiki.cern.ch/twiki/bin/viewauth/CMS/HLTOnCallGuide).

## Development

Each push to GitLab that introduces new commits will start a CI pipeline.
The source for that is the `.gitlab-ci.yml` file.

Each pipeline contains a build of an RPM package for the Hilton software.

## Deployment

GitLab CI can deploy to P5. To do this, perform the following steps:

- [Create a new tag](https://gitlab.cern.ch/cms-tsg-fog/hltpro/-/tags/new)
- [Create a new pipeline](https://gitlab.cern.ch/cms-tsg-fog/hltpro/-/pipelines/new)
  - `Run for` must be set to your newly created tag instead of master
  - Set variables `P5_USER` and `P5_PASS` to your P5 username and password.
- In this newly created pipeline, press the `deploy:P5` play button
