# Use the official Golang image as the base image
FROM golang:1.20

# Set the working directory inside the container
WORKDIR /app

# Copy the main.go file to the working directory
COPY main.go .

# Expose the port that the API listens on
EXPOSE 8080

# Run the code when the container starts
CMD [ "go", "run", "main.go" ]