## Installation
 This site uses python Flask. To avoid setting up backend enviroment, the site uses Docker Container it wraps the Python dependencies into an isolate container. Follow the instructions below:

 - ### Install via git clone.
 1. In your terminal, run the  ``` git clone https://github.com/cent-ivan/hotel-booking-site.git```
 2. Download npm, and run the ``` npm install```, to generate your own node_modules directory
 3. Run this command,``` npm dev run```, to generate a tailwind file
 4. `Ctrl + C` to exit tailwind logs and Run ` uv add -r requirements.txt`, to install required python libraries.
 5. Set up the backend container by running, `docker compose up -d backend` (Make sure you have Docker installed).
 6. To turn off contianer, run `docker compose down`

## Usage
 - ### How to Develop with Python Flask (Containerized) with Tailwind (via Host)?
 1. Run `docker compose up -d backend`
 2. Run this command,``` npm dev run```
 3. Code some changes, save it and tailwind cli will automatically regenerate.

 ## Contributing
The developer welcome contributions from the community! To get started:

1. **Clone** your fork locally:
   ```bash git clone https://github.com/cent-ivan/ojt-time-tracker.git ```
2. **Create a new branch** for your feature or fix:
   ```bash git checkout -b your-branch-name```
3. **Add and commit** your code:
   ```bash 
      git add filename
      git commit -m "short and meaningful message"
   ```
4. **Push** to your branch:
   ```bash git push origin your-branch-name```
5. **Open a Pull** Request from the main repository