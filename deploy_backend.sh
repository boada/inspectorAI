#!/bin/bash

function initialize_worker() {
    printf "*********\n\t\tSetting up host \n*********\n"
    # Update packages
    echo ======= Updating packages ========
    sudo apt-get update

    # Export language locale settings
    echo ======= Exporting language locale settings =======
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8

    # Install pip3
    echo ======= Installing pip3 =======
    sudo apt-get install -y python3-pip
}

function setup_python_venv() {
    printf "*********\n\t\tSetting up Venv \n*********\n"
    # Install virtualenv
    echo ======= Installing virtualenv =======
    pip3 install virtualenv --user

    source ~/.profile
    # Create virtual environment and activate it
    echo ======== Creating and activating virtual env =======
    virtualenv venv
    source ./venv/bin/activate
}

function clone_app_repository() {
    printf "*********\n\t\tFetching App \n*********\n"
    # Clone and access project directory
    echo ======== Cloning and accessing project directory ========
    if [[ -d ~/insight ]]; then
        #sudo rm -rf ~/insight
        #git clone https://github.com/boada/insight.git ~/insight
        cd ~/insight/demo
    else
        git clone https://github.com/boada/insight.git ~/insight
        cd ~/insight/demo
    fi
}

function setup_app() {
    printf "*********\n\t\tInstalling App dependencies and Env Variables \n*********\n"
    setup_env
    # Install required packages
    echo ======= Installing required packages ========
    pip3 install -r requirements.txt
    pip3 install gunicorn
}

# Create and Export required environment variable
function setup_env() {
    echo ======= Exporting the necessary environment variables ========
    sudo cat > ~/.env << EOF
    export APP_CONFIG="production"
    export SECRET_KEY="mYd3rTyL!tTl#sEcR3t"
    export FLASK_APP=app.py
EOF
    echo ======= Exporting the necessary environment variables ========
    source ~/.env
}

# Install and configure nginx
function setup_nginx() {
    printf "*********\n\t\tSetting up nginx \n*********\n"
    echo ======= Installing nginx =======
    sudo apt-get install -y nginx

    # Configure nginx routing
    echo ======= Configuring nginx =======
    echo ======= Removing default config =======
    sudo rm -rf /etc/nginx/sites-available/default
    sudo rm -rf /etc/nginx/sites-enabled/default
    echo ======= Replace config file =======
    sudo bash -c 'cat <<EOF > /etc/nginx/sites-available/default
    server {
            listen 80 default_server;
            listen [::]:80 default_server;

            server_name _;

            location / {
                    # reverse proxy and serve the app
                    # running on the localhost:8000
                    proxy_pass http://127.0.0.1:8000/;
                    proxy_set_header HOST \$host;
                    proxy_set_header X-Forwarded-Proto \$scheme;
                    proxy_set_header X-Real-IP \$remote_addr;
                    proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
            }
    }
EOF'

    echo ======= Create a symbolic link of the file to sites-enabled =======
    sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

    # Ensure nginx server is running
    echo ====== Checking nginx server status ========
    sudo systemctl restart nginx
    sudo nginx -t
}

# Add a launch script
function create_launch_script () {
    printf "*********\n\t\tCreating a Launch script \n*********\n"

    sudo cat > /home/ubuntu/launch.sh <<EOF
    #!/bin/bash
    cd ~/insight/demo
    source ~/.env
    source ~/venv/bin/activate
    gunicorn app:flask_app -D
EOF
    sudo chmod 744 /home/ubuntu/launch.sh
    echo ====== Ensuring script is executable =======
    ls -la ~/launch.sh
}

function create_term_script () {
    printf "*********\n\t\tCreating a Term script \n*********\n"

    sudo cat > /home/ubuntu/terminate.sh <<EOF
    pkill gunicorn
EOF
    sudo chmod 744 /home/ubuntu/terminate.sh
    echo ====== Ensuring script is executable =======
    ls -la ~/terminate.sh
}

function configure_startup_service () {
    printf "*********\n\t\tConfiguring startup service \n*********\n"

    sudo bash -c 'cat > /etc/systemd/system/insight-demo.service <<EOF
    [Unit]
    Description=insight-demo startup service
    After=network.target

    [Service]
    User=ubuntu
    ExecStart=/bin/bash /home/ubuntu/launch.sh

    [Install]
    WantedBy=multi-user.target
EOF'

    sudo chmod 664 /etc/systemd/system/insight-demo.service
    sudo systemctl daemon-reload
    sudo systemctl enable insight-demo.service
    sudo systemctl start insight-demo.service
    sudo service insight-demo status
}

Serve the web app through gunicorn
function launch_app() {
    printf "*********\n\t\tServing the App \n*********\n"
    sudo bash /home/ubuntu/launch.sh
}

######################################################################
########################      RUNTIME       ##########################
######################################################################

initialize_worker
setup_python_venv
clone_app_repository
setup_app
setup_nginx
create_launch_script
create_term_script
# configure_startup_service
launch_app
