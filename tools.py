def mock_lead_capture(name: str, email: str, platform: str):
    """
    Mock function to simulate lead capture API.
    Only triggers after all required fields are collected.
    """

    # Basic validation
    if not name or not email or not platform:
        return "❌ Missing required details. Lead not captured."

    # Simulate backend processing
    print("\n=== TOOL EXECUTION STARTED ===")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Platform: {platform}")
    print("=== TOOL EXECUTION COMPLETED ===\n")

    return f"✅ Lead captured successfully for {name} 🚀"