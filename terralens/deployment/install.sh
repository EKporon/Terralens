#!/usr/bin/env bash

set -e

echo "===================================="
echo " Installing TerraLens Server"
echo "===================================="


echo "[1/5] Updating system packages..."

sudo apt update
sudo apt upgrade -y


echo "[2/5] Installing dependencies..."

sudo apt install -y \
    git \
    nginx \
    python3 \
    python3-pip \
    python3-venv


echo "[3/5] Setting up systemd service..."

sudo cp deployment/terralens.service \
/etc/systemd/system/terralens.service


echo "[4/5] Reloading systemd..."

sudo systemctl daemon-reload


echo "[5/5] Enabling services..."

sudo systemctl enable terralens
sudo systemctl enable nginx


echo "===================================="
echo " Installation Complete"
echo "===================================="
