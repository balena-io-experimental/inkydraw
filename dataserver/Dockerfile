FROM balenalib/raspberry-pi-node:14-buster-run
WORKDIR /usr/app
COPY package.json package-lock.json ./
RUN JOBS=MAX npm install --production --unsafe-perm && npm cache verify && rm -rf /tmp/*
COPY . ./
CMD ["node", "index.js"]