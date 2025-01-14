# Use an official Node.js image as the base
FROM node:16

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app for production
RUN npm run build

# Install a static server to serve the production build
RUN npm install -g serve

# Use the static server to serve the app
CMD ["serve", "-s", "build", "-l", "3000"]

