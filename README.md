# TerraLens 🌍
## Scalable Flask Application Deployment using Nginx Load Balancer

TerraLens is a Flask-based web application designed to help users evaluate land conditions before making investment decisions. This project demonstrates the deployment of a scalable web application architecture using multiple servers, Gunicorn, Nginx, and automated deployment scripts.

## Deployment Architecture

The application was deployed using a three-server architecture:

                User
                  |
                  |
          Nginx Load Balancer
                LB01
          10.227.47.81:80
                  |
    --------------------------------
    |                              |
    |                              |
 WEB-01                         WEB-02

Flask + Gunicorn               Flask + Gunicorn
10.227.126.54:8000             10.227.67.249:8000


The load balancer receives incoming HTTP requests and distributes them between the two backend web servers. Each web server runs an independent instance of the TerraLens Flask application.

---

# Deployment Process

## 1. Preparing the Web Servers

Two Ubuntu servers were created:

- `5867-web-01`
- `5867-web-02`

Each server was configured with:

- Ubuntu Linux
- Python virtual environment
- Flask application
- Gunicorn WSGI server
- Systemd service management


The application source code was stored in GitHub and deployed by cloning the repository:


git clone https://github.com/EKporon/Terralens.git

The repository contains automated deployment scripts:

deployment/
│
├── deploy.sh
├── install.sh
└── terralens.service
2. Automated Application Deployment

The deployment scripts automate the setup process across servers.

Creating the virtual environment

A Python virtual environment was created:

python3 -m venv venv

The environment was activated:

source venv/bin/activate

Dependencies were installed:

pip install -r requirements.txt

The required packages include:

Flask
Requests
Python-dotenv
Gunicorn
3. Configuring Gunicorn

Gunicorn was used as the production WSGI server.

The application was launched using the Flask application factory:

gunicorn --workers 3 \
--bind 127.0.0.1:8000 \
"app:create_app()"

This allowed multiple worker processes to handle incoming requests.

4. Creating a Systemd Service

To ensure the application starts automatically and restarts after failure, a systemd service was created.

Location:

/etc/systemd/system/terralens.service

Configuration:

[Unit]
Description=TerraLens Flask Application
After=network.target

[Service]
User=ubuntu
Group=ubuntu

WorkingDirectory=/home/ubuntu/Terralens/terralens

Environment="PATH=/home/ubuntu/Terralens/terralens/venv/bin"

ExecStart=/home/ubuntu/Terralens/terralens/venv/bin/gunicorn \
          --workers 3 \
          --bind 127.0.0.1:8000 \
          "app:create_app()"

Restart=always

[Install]
WantedBy=multi-user.target

The service was enabled and started:

sudo systemctl enable terralens
sudo systemctl start terralens

The deployment was verified using:

sudo systemctl status terralens

Both web servers successfully showed:

Active: active (running)
5. Configuring the Nginx Load Balancer

A third server was configured as the load balancer:

5867-lb-01

Nginx was installed:

sudo apt update
sudo apt install nginx

The Nginx configuration was updated:

File:

/etc/nginx/sites-available/default

Configuration:

upstream terralens_backend 
{

    server 10.227.126.54:8000;
    server 10.227.67.249:8000;

}


server 
{

    listen 80;

    server_name _;


    location / {

        proxy_pass http://terralens_backend;


        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

    }

}

This configuration defines both web servers as backend nodes.

Nginx uses the upstream group:

terralens_backend

to distribute incoming traffic between:

WEB-01
10.227.126.54:8000

WEB-02
10.227.67.249:8000

The configuration was tested:

sudo nginx -t

Successful output:

syntax is ok
test is successful

Nginx was restarted:

sudo systemctl restart nginx
Testing and Verification

Testing was performed at multiple levels.

Testing individual web servers

WEB-01:

curl http://10.227.126.54:8000

WEB-02:

curl http://10.227.67.249:8000

Both servers successfully returned the TerraLens HTML page.

Testing the Load Balancer

The load balancer was tested:

curl http://localhost

The response returned the TerraLens homepage HTML, confirming that:

Nginx was running
The backend servers were reachable
Traffic was successfully forwarded

The complete request flow was:

Client Request
      |
      |
Nginx Load Balancer
      |
      |
-------------------------
|                       |
WEB-01               WEB-02
Flask                Flask
Gunicorn             Gunicorn
Deployment          Automation

To support future scaling, deployment scripts were created.

A new server can be prepared by:

Cloning the repository
Running the installation script
Starting the application service

This approach allows additional web servers to be added without manually repeating every configuration step.

AWS Configuration Note

The application deployment and internal load balancing were completed successfully.

The remaining external accessibility step requires AWS console access to update the Load Balancer security group rules.

The required rule:

Inbound Rule:

Type: HTTP
Port: 80
Source: 0.0.0.0/0

This allows users outside the AWS VPC to access the TerraLens application through the load balancer.

Demo Video

The deployment demonstration video can be found here:

YouTube Link:

[INSERT YOUTUBE LINK HERE]

Technologies Used:
Python
Flask
Gunicorn
Nginx
Ubuntu Linux
Git/GitHub
AWS EC2
Systemd
Shell scripting
Author

Kporon Ejiroghene Solomon
African Leadership University
Software Engineering
