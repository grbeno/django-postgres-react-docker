## Django-Postgres-React-Docker basic-startproject example

#### This repo is based on: [django-postgres-docker](https://github.com/grbeno/django-postgres-docker)

#### :point_right: The steps are similar to the base repository, supplemented with the commands about Node and React, as well as the settings related to the frontend service in the docker-compose.yml and the Dockerfile located in the frontend directory.
---
### Setting up React

__If node is not installed:__
On Windows using [nvm-windows](https://github.com/coreybutler/nvm-windows/releases).

__For nvm-windows:__ After clicking on the link, download the nvm-setup.zip directory (Assets), then unzip it and run the installer!

Install node

```
nvm install <node_version>
```
Check node is installed
```
node -v
```
If more versions are installed, check the list and select newest one.
```
nvm list
```
```
nvm use newest
```
Learn more from the [documentation of nvm-windows](https://github.com/coreybutler/nvm-windows).

```
cd frontend
```
```
npm install
```
```
npm run build
```
