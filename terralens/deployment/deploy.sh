#!/usr/bin/env bash

set -e

APP_NAME="terralens"
PROJECT_DIR="$HOME/Terralens/terralens"
VENV_DIR="$PROJECT_DIR/venv"

echo "===================================="
echo " Deploying TerraLens"
echo "===================================="

echo "[1/6] Creating virtual environment..."

if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
fi

echo "[2/6] Activating virtual environment..."

source "$VENV_DIR/bin/activate"

echo "[3/6] Installing Python dependencies..."

pip install --upgrade pip
pip install -r requirements.txt

echo "[4/6] Restarting systemd service..."

sudo systemctl daemon-reload

if systemctl list-unit-files | grep -q terralens.service; then
    sudo systemctl restart terralens
else
    echo "WARNING:"
    echo "terralens.service not installed yet."
    echo "Install it first."
fi

echo "[5/6] Checking service..."

sudo systemctl --no-pager status terralens

echo "[6/6] Deployment complete."

echo
echo "Local test:"
echo "curl http://127.0.0.1"
