#!/bin/bash

# Script to upload Battery Health App to GitHub
# Run this after installing Xcode Command Line Tools

echo "🚀 Setting up GitHub repository for coolbambook01..."

# Initialize git repository
echo "📦 Initializing git repository..."
git init

# Add all files
echo "➕ Adding files..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Battery Health Predictor app

- Streamlit web app for predicting phone battery health
- XGBoost model pipeline for predictions
- Recommends: Keep Using, Replace Battery, or Change Phone"

# Set main branch
git branch -M main

# Add remote repository
echo "🔗 Setting up remote repository..."
git remote add origin https://github.com/coolbambook01/BatteryHealthApp.git

echo ""
echo "✅ Repository setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Go to https://github.com/new"
echo "2. Repository name: BatteryHealthApp"
echo "3. Make it Public (or Private if you prefer)"
echo "4. DO NOT check 'Add a README file' (we already have one)"
echo "5. Click 'Create repository'"
echo ""
echo "6. Then run this command to push:"
echo "   git push -u origin main"
echo ""
echo "💡 Tip: If you get 2FA prompts, consider setting up SSH keys:"
echo "   https://docs.github.com/en/authentication/connecting-to-github-with-ssh"
