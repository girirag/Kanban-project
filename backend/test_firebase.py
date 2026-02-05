#!/usr/bin/env python3
"""
Test script to verify Firebase connection
Run this after setting up firebase-service-account.json
"""

import os
import sys

def test_firebase_connection():
    try:
        # Check if service account file exists
        if not os.path.exists("firebase-service-account.json"):
            print("❌ firebase-service-account.json not found!")
            print("Please download it from Firebase Console > Project Settings > Service Accounts")
            return False
        
        print("✅ Service account file found")
        
        # Try to initialize Firebase
        import firebase_admin
        from firebase_admin import credentials, firestore
        
        cred = credentials.Certificate("firebase-service-account.json")
        app = firebase_admin.initialize_app(cred)
        db = firestore.client()
        
        print("✅ Firebase initialized successfully")
        
        # Test Firestore connection
        test_collection = db.collection('test')
        test_doc = test_collection.document('connection_test')
        test_doc.set({'test': True, 'timestamp': firestore.SERVER_TIMESTAMP})
        
        print("✅ Firestore write test successful")
        
        # Read back the test document
        doc = test_doc.get()
        if doc.exists:
            print("✅ Firestore read test successful")
            print(f"   Data: {doc.to_dict()}")
        
        # Clean up test document
        test_doc.delete()
        print("✅ Test document cleaned up")
        
        # Test the kanbanTasks collection
        tasks_ref = db.collection('kanbanTasks')
        docs = list(tasks_ref.stream())
        print(f"✅ Found {len(docs)} existing tasks in kanbanTasks collection")
        
        print("\n🎉 Firebase connection test PASSED!")
        print("You can now run the FastAPI server with: python main.py")
        
        return True
        
    except ImportError as e:
        print(f"❌ Missing dependencies: {e}")
        print("Run: pip install -r requirements.txt")
        return False
        
    except Exception as e:
        print(f"❌ Firebase connection failed: {e}")
        print("\nTroubleshooting:")
        print("1. Check if firebase-service-account.json has correct credentials")
        print("2. Verify Firestore security rules allow read/write")
        print("3. Make sure the project ID matches in the service account file")
        return False

if __name__ == "__main__":
    print("🔥 Testing Firebase Connection...")
    print("=" * 50)
    
    success = test_firebase_connection()
    
    if not success:
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("✅ All tests passed! Firebase is ready to use.")