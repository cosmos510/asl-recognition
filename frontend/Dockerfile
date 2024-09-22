# Use the official Node.js image.
FROM node:18-alpine

# Set the working directory.
WORKDIR /usr/src/app

# Copy package.json and package-lock.json.
COPY package.json ./
COPY package-lock.json ./

# Install dependencies.
RUN npm install
RUN npm install three

# Copy the rest of the application code.
COPY . ./

# Build the application.
RUN npm run build

# Expose port 3000.
EXPOSE 3000

# Start the application.
CMD ["npm", "start"]