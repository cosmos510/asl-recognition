# Use the official Node.js image.
FROM node:22-alpine
# Set the working directory.
WORKDIR /usr/src/app

# Copy package.json and package-lock.json.
COPY package.json ./
COPY package-lock.json ./

# Install dependencies.
RUN npm install
RUN npm install three
RUN npm add @honeybadger-io/js --save
RUN npm install --save-dev @babel/plugin-proposal-private-property-in-object


# Copy the rest of the application code.
COPY . ./

# Build the application.
RUN npm run build

# Expose port 3000.
EXPOSE 3000

# Start the application.
CMD ["npm", "start"]