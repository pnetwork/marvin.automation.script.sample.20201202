# marvin.automation.script.sample.20201202
Marvin automation script sample: retrieve local IP address via ifconfig.io

## Create a Trek Project from zero
### Steps
1. pip3 install trek==0.0.0a0 blcks -i https://package.pentium.network/repository/pypi-group/simple --trusted-host=package.pentium.network
1. Create a trek project: trek createproject marvin.automation.script.sample.20201202
1. cd marvin.automation.script.sample.20201202
1. Add scripts you need in packages.json: “notification”: “>=0.5.0”
1. Install scripts in package.json:  trek install
1. Create your scripts in project: trek createblcks blcksdescribeinstances
1. Develop your scripts in project: develop blcks in src/blcks/blcksdescribeinstances 
1. Develop your workflow in project: develop workflow in src/graph.yml
1. Setup variables used in workflow: set variables in inputs/data.yml
1. Update JWT:  trek login
1. Run your workflow and scripts: trek run --auto  
1. Pack and deploy project to Marvin: trek deploy -a --autobuildpush --autopack  
1. End of local test:  trek shutdownenv --all

## Setup a Trek Project
### Steps
1. pip3 install trek==0.0.0a0 blcks -i https://package.pentium.network/repository/pypi-group/simple --trusted-host=package.pentium.network
1. chdir to trek project
1. Update marvin_url to yours: .trek/config.json, src/blcks/*/.trek/config. json
1. Update PN_GLOBAL_ROUTER for all Blcks in project: src/blcks/*/tox.ini
1. Update variables used in workflow: set variables in inputs/data.yml
1. Install scripts in package.json:  trek install
1. Update JWT:  trek login
1. Run your workflow and scripts: trek run --auto  
1. Pack and deploy project to Marvin:   trek deploy -a --autobuildpush --autopack  
1. End of local test:  trek shutdownenv --all
