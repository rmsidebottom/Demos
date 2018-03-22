# Sessions Demo

## Goal

The goal of this demo is to teach people how to use BurpSuite to change the cookies. Changing the *username* cookie to a different user will change who is signed into the application.

## Setup
Download the whole directory on a Linux system. Once downloaded, ensure all of the scripts have the execute permission set (run *chmod +x script* for each script).
1. Run *./setup.sh* as this will install all of the needed dependencies. It will also run the application itself. You will then be able to connect to the app at http://your_IP_Address:5000.
2. Once you have run the setup script, if you ever need to run the application again, simply run *./runServer.sh* and this will simply run the server.

## Prerequisites
* Python is already installed
* Pip is already installed

## This is currently only available to be run on *nix systems.
