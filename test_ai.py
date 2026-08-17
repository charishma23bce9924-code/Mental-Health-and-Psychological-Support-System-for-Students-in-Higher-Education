#!/usr/bin/env python3
"""
Test script for the integrated AI engine
"""

import sys
import asyncio
from backend.integrated_ai_engine import create_mental_health_ai

async def test_ai_engine():
    print("🧠 Testing Mental Health AI Engine...")
    print("=" * 50)
    
    try:
        # Initialize AI engine
        ai = create_mental_health_ai()
        print("✅ AI Engine initialized successfully")
        
        # Check provider status
        status = ai.get_provider_status()
        print("\n📊 AI Provider Status:")
        
        available_providers = []
        for name, info in status.items():
            status_icon = "✅" if info["available"] else "❌"
            print(f"  {status_icon} {name}")
            print(f"     Description: {info['description']}")
            if info["available"]:
                available_providers.append(name)
        
        print(f"\n🔢 Total available providers: {len(available_providers)}")
        
        if available_providers:
            print(f"✅ Active providers: {', '.join(available_providers)}")
            
            # Test basic response generation
            print("\n🧪 Testing response generation...")
            
            test_message = "I'm feeling stressed about my upcoming exams."
            response = await ai.generate_response(
                message=test_message,
                user_profile=None,
                context={},
                crisis_detected=False
            )
            
            print(f"Test message: '{test_message}'")
            print(f"AI Response: {response.text[:200]}...")
            print(f"Risk Level: {response.risk_level}")
            print(f"Therapeutic Technique: {response.therapeutic_technique}")
            print("✅ Response generation test passed")
            
        else:
            print("⚠️  No AI providers available - system will use rule-based responses")
            
    except Exception as e:
        print(f"❌ Error testing AI engine: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_ai_engine())