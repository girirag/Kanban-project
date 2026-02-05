#!/usr/bin/env python3
"""
Quick setup script for Firebase + FastAPI integration
"""

import os
import json
import webbrowser

def main():
    print("🚀 Firebase + FastAPI Quick Setup")
    print("=" * 50)
    
    # Check if service account exists
    if os.path.exists("firebase-service-account.json"):
        print("✅ firebase-service-account.json found")
        
        # Test the connection
        print("\n🔥 Testing Firebase connection...")
        os.system("python test_firebase.py")
        
    else:
        print("❌ firebase-service-account.json not found")
        print("\n📋 Follow these steps:")
        print("1. The Firebase Console should be open in your browser")
        print("2. Go to Project Settings (gear icon)")
        print("3. Click 'Service Accounts' tab")
        print("4. Click 'Generate new private key'")
        print("5. Download and save as 'firebase-service-account.json' in this folder")
        
        # Open Firebase console
        firebase_url = "https://console.firebase.google.com/project/firstapp-ddec4/settings/serviceaccounts/adminsdk"
        print(f"\n🌐 Opening Firebase Console...")
        webbrowser.open(firebase_url)
        
        input("\nPress Enter after you've downloaded the service account file...")
        
        if os.path.exists("firebase-service-account.json"):
            print("✅ Service account file detected!")
            print("\n🔥 Testing Firebase connection...")
            os.system("python test_firebase.py")
        else:
            print("❌ Service account file still not found")
            print("Please make sure you saved it as 'firebase-service-account.json'")
            return
    
    print("\n🚀 Starting FastAPI server...")
    print("The server will be available at: http://localhost:8000")
    print("API docs will be at: http://localhost:8000/docs")
    print("\nPress Ctrl+C to stop the server")
    
    # Start the FastAPI server
    os.system("python main.py")

if __name__ == "__main__":
    main()