#!/usr/bin/env python3
import subprocess
import sys
import os

def install_requirements():
    """Install Python requirements"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False
    return True

def check_firebase_config():
    """Check if Firebase configuration exists"""
    if not os.path.exists("firebase-service-account.json"):
        print("⚠️  Firebase service account file not found!")
        print("Please create 'firebase-service-account.json' based on the example file.")
        print("You can download this from your Firebase Console > Project Settings > Service Accounts")
        return False
    
    if not os.path.exists(".env"):
        print("⚠️  .env file not found!")
        print("Please create '.env' file based on '.env.example'")
        return False
    
    return True

def main():
    print("🚀 Setting up FastAPI Backend for Kanban Board...")
    
    if not install_requirements():
        sys.exit(1)
    
    if not check_firebase_config():
        print("\n📝 Next steps:")
        print("1. Copy firebase-service-account.json.example to firebase-service-account.json")
        print("2. Add your Firebase service account credentials")
        print("3. Copy .env.example to .env and configure if needed")
        print("4. Run: python main.py")
    else:
        print("✅ Setup complete! You can now run: python main.py")

if __name__ == "__main__":
    main()