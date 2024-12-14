# Stage 1: Build the React application
FROM node:14-alpine AS build

# Set working directory inside the container
WORKDIR /app

# Copy dependency files and install dependencies
COPY package.json package-lock.json ./
RUN npm install --production

# Copy the rest of the application code and build it
COPY . .
RUN npm run build

# Stage 2: Serve the application
FROM nginx:alpine

# Copy built files from the build stage to Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Expose default Nginx port
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
